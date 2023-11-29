"""
Steps to debug batch env in AWS Batch:

1. Check job queue status
2. Check CE status 
3. Check auto scaling group and check activity for that group for any errors and EC2 instance ID. 
4. Check ec2 instance state
6. Check tower/forge log group in cloud watch
7. Check cloud trail
8. Check ECS cluster.
"""
import typer
from typing_extensions import Annotated
from rich import print

from core.debug_aws_batch import DebugAWSBatch


class AWSBatchCommandsInterface():
    
    def debug_compute_env(self, compte_env: str) -> None:
        pass
    
class AWSBatchCommands(AWSBatchCommandsInterface):

    def __init__(self, compute_env_id: str, debug_aws_batch: DebugAWSBatch):
        self.compute_env_id = compute_env_id
        self.debug_aws_batch = debug_aws_batch
        
    def debug_compute_env(self, compute_env_id: str) -> None:
        """This function will debug a given compute enviornment for a given compute enviornment ID
        Args:
            compte_env (str): The ID of your current compute enviornment. 
        Returns:
            dict: returns the status of a compute enviornment and any issues. 
        """
    
        self.compute_env_id = compute_env_id
        
        #TODO: add better error handling
        if self.compute_env_id:
            # 1. Check the status of the job queue
            job_queue_status = self.debug_aws_batch.get_job_queue_status(job_queue_id=self.compute_env_id)
            print("The current status of the job queue is")
            print(job_queue_status)
            
            #2. Check the current status of the compute enviornment 
            compute_env_status = self.debug_aws_batch.get_compute_env_status(compute_env_id=self.compute_env_id)
            print("The current status of the compute enviornment is:")
            print(compute_env_status)
            
            #3. Check auto scaling group and check activity for that group for any errors and EC2 instance ID. 
            autoscaling_group = self.debug_aws_batch.get_autoscaling_group(compute_env_id)
            autoscaling_activity = self.debug_aws_batch.get_scaling_activities(autoscaling_group)
            print("The activitiy within the autoscaling group")
            print(autoscaling_activity)
            
            #TODO: check the state of the ECS Cluster.
            print("ECS Cluster details")
            ecs_cluster = self.debug_aws_batch.get_ecs_cluster(compute_env_id)
            print(ecs_cluster)
            #5. TODO: Check ec2 instance state
            
            #6 Return the launch template for inspection
            launch_template_id = self.debug_aws_batch.get_aws_batch_compute_env_launch_template_id(compute_env_id)
            launch_template_object = self.debug_aws_batch.get_user_data_from_launch_template(launch_template_id)            
            launch_template_userdata = self.debug_aws_batch.extract_and_decode_user_data(launch_template_object)
            print("This is the current Launch Template")
            print(launch_template_userdata)
            
        else: 
            return(f"Missing a valid Compute enviornment ID.  {self.compute_env_id} ")

    
        
        
     
    

    
    