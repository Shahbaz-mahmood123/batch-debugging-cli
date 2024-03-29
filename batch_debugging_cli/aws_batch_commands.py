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
from datetime import datetime
import tempfile
import typer
from typing_extensions import Annotated
from rich import print


from core.debug_aws_batch import DebugAWSBatch

class AWSBatchCommandsInterface():
    
    def debug_compute_env(self, compte_env: str) -> None:
        pass


aws = typer.Typer()   

class AWSCommands():

    def __init__(self) -> None:
        pass
        
    @staticmethod
    @aws.command("debug-batch")
    def debugCE(compute_env_id: Annotated[str, typer.Option(prompt="Please insert a valid compute environment name")]):
        aws_batch_commands = AWSBatch(compute_env_id=compute_env_id, debug_aws_batch=DebugAWSBatch())
        aws_batch_commands.debug_compute_env(compute_env_id)
        
    # @aws.command("get-lt")
    # def getLaunchTemplate(compute_env_id: str):
    #     launch_template_id = debug_aws_batch.get_aws_batch_compute_env_launch_template_id(compute_env_id)
    #     launch_template_object = debug_aws_batch.get_user_data_from_launch_template(launch_template_id)            
    #     launch_template_userdata = debug_aws_batch.extract_and_decode_user_data(launch_template_object)
    #     print(launch_template_userdata)

class AWSBatch(AWSBatchCommandsInterface):

    def __init__(self, compute_env_id: str, debug_aws_batch: DebugAWSBatch):
        self.compute_env_id = compute_env_id
        self.debug_aws_batch = debug_aws_batch
        self.temp_file = None
        
        
    def create_temp_file(self):
        # Create a temporary file
        self.temp_file = tempfile.NamedTemporaryFile(mode="w+", delete=False)
        self.temp_file.write(self.variable_content)
    
 
    def debug_compute_env(self, compute_env_id: Annotated[str, typer.Option(prompt="Please insert a valid compute environment name")]) -> None:
        
        """This function will debug a given compute enviornment for a given compute enviornment ID
        Args:
            compte_env (str): The ID of your current compute enviornment. 
        Returns:
            dict: returns the status of a compute enviornment and any issues. 
        """
         
        #TODO: add better error handling
        if self.compute_env_id:
            # 1. Check the status of the job queue
            job_queue_status = self.debug_aws_batch.get_job_queue_status(job_queue_id=compute_env_id)
            print("The current status of the job queue:")
            print(job_queue_status)
            
            #2. Check the current status of the compute enviornment 
            compute_env_status = self.debug_aws_batch.get_compute_env_status(compute_env_id=compute_env_id)
            print("The current status of the compute enviornment:")
            print(compute_env_status)
            
            #3. Check for SUCEEDED, FAILED and Running jobs
            running_jobs = self.debug_aws_batch.get_running_jobs(compute_env_id)
            succeeded_jobs = self.debug_aws_batch.get_succeeded_jobs(compute_env_id)
            failed_jobs = self.debug_aws_batch.get_failed_jobs(compute_env_id)
            
            print("RUNNING Jobs:")
            print(running_jobs)
            print("FAILED Jobs:")
            print(failed_jobs)
            print("SUCCEEDED Jobs:")
            print(succeeded_jobs)
            
            #4. Check auto scaling group and check activity for that group for any errors and EC2 instance ID. 
            autoscaling_group = self.debug_aws_batch.get_autoscaling_group(compute_env_id)
            autoscaling_activity = self.debug_aws_batch.get_scaling_activities(autoscaling_group)
            print("The activitiy within the autoscaling group:")
            print(autoscaling_activity)
            
            #TODO: check the state of the ECS Cluster.
            print("ECS Cluster details:")
            ecs_cluster = self.debug_aws_batch.get_ecs_cluster(compute_env_id)
            print(ecs_cluster)
            #5. TODO: Check ec2 instance state
            
            #6 Return the launch template for inspection
            launch_template_id = self.debug_aws_batch.get_aws_batch_compute_env_launch_template_id(compute_env_id)
            launch_template_object = self.debug_aws_batch.get_user_data_from_launch_template(launch_template_id)            
            launch_template_userdata = self.debug_aws_batch.extract_and_decode_user_data(launch_template_object)
            print("This is the current Launch Template:")
            print(launch_template_userdata)
            
            #7 Cloudwatch
            cloud_watch_logs = self.debug_aws_batch.get_recent_forge_cloudwatch_logs(autoscaling_group_activity=autoscaling_activity)
            if cloud_watch_logs is None:
                print("No logs found in Cloudwatch. Your log retention policy may have cleaned the logs up")
            for events in cloud_watch_logs.events:
                print(f"Time {datetime.fromtimestamp(events.timestamp / 1000.0)}, Log event: {events.message}")
                
        else: 
            return(f"Missing a valid Compute enviornment ID.  {compute_env_id} ")

    
        
        
     
    

    
    