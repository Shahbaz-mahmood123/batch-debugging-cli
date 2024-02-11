from typing import Optional
import typer

from rich import print
from core.debug_aws_batch import DebugAWSBatch

from batch_debugging_cli.gcp_batch_commands import GCPBatchCommands, gcp
from batch_debugging_cli.aws_batch_commands import aws
from batch_debugging_cli.seqera_commands import seqera 
from batch_debugging_cli.pulumi_commands import pulumi


## TODO: Check if I need add to the below pretty_exceptions_enable=False, add_completion=True
app = typer.Typer()
azure = typer.Typer()


@app.command("version")
def version():
    __cli_version__ = '0.0.9'
    print(f"CLI version: {__cli_version__}")
            
app.add_typer(gcp, name="gcp")
app.add_typer(aws, name="aws")
app.add_typer(azure, name="azure")
app.add_typer(seqera, name="seqera")
app.add_typer(pulumi,name = "pulumi" )
 
if __name__ == "__main__":
    app()