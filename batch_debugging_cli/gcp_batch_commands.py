import typer
from typing_extensions import Annotated
from rich import print
from google.cloud import batch_v1
from core.gcp_batch import GCPBatch


class GCPBatchCommandsInterface():
    
    def create_test_job(self, job_name: str) -> None:
        pass
    
gcp = typer.Typer()

class GCPBatchCommands():
    
    @gcp.command("test-job")
    @staticmethod
    def create_test_job(job_name: Annotated[str, typer.Option(prompt="Please insert a name for the batch job:")]) -> None:
        gcp_batch = GCPBatch()
        test_job = gcp_batch.create_test_job(job_name)
        print(test_job)
         