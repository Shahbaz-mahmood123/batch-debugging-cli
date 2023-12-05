import typer
from typing_extensions import Annotated
from rich import print
from google.cloud import batch_v1
from core.gcp_batch import GCPBatch


class GCPBatchCommandsInterface():
    
    def create_test_job(project_id: str, region: str, job_name: str) -> batch_v1.Job:
        pass
    

class GCPBatchCommands():
             
    def create_test_job(job_name: str) -> batch_v1.Job:
        gcp_batch = GCPBatch()
        test_job = gcp_batch.create_test_job(job_name)
        return test_job
         