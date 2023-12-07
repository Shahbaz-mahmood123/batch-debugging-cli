import typer
from typing_extensions import Annotated
from rich import print
from core.debug_aws_batch import DebugAWSBatch

from batch_debugging_cli.gcp_batch_commands import GCPBatchCommands
from batch_debugging_cli.aws_batch_commands import AWSBatchCommands

app = typer.Typer()
aws = typer.Typer()
gcp = typer.Typer()
azure = typer.Typer()

app.add_typer(gcp, name="gcp")
app.add_typer(aws, name="aws")
app.add_typer(azure, name="azure")
debug_aws_batch = DebugAWSBatch()

@aws.command("debug-batch")
def debugCE(compute_env_id: Annotated[str, typer.Option(prompt="Please insert a valid compute environment name")]):
    aws_batch_commands = AWSBatchCommands(compute_env_id=compute_env_id, debug_aws_batch=debug_aws_batch)
    aws_batch_commands.debug_compute_env(compute_env_id)


@aws.command("get-lt")
def getLaunchTemplate(compute_env_id: str):
    launch_template_id = debug_aws_batch.get_aws_batch_compute_env_launch_template_id(compute_env_id)
    launch_template_object = debug_aws_batch.get_user_data_from_launch_template(launch_template_id)            
    launch_template_userdata = debug_aws_batch.extract_and_decode_user_data(launch_template_object)
    print(launch_template_userdata)

 
@gcp.command("test-job")
def gcp_create_job(job_name: Annotated[str, typer.Option(prompt="Please insert a name for the batch job")]):
    gcp_batch_commands = GCPBatchCommands()
    batch_job = gcp_batch_commands.create_test_job(job_name)
    
 
if __name__ == "__main__":
    app()