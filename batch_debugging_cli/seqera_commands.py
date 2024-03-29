import typer
from typing_extensions import Annotated
from rich import print

from core.compute_envs import SeqeraComputeEnvsWrapper

class SeqeraInterface():

    def optimize_compute_enviornment(self, compute_env_id: str):
        pass
    
seqera = typer.Typer()

class SeqeraCommands():
    
    @staticmethod
    @seqera.command("optimize-compute")
    def optimize_compute_enviornment(compute_env_id: Annotated[str, typer.Option(prompt="Please enter the compute enviornment id:")]):
        seqera = Seqera()
        response = seqera.optimize_compute_enviornment(compute_env_id=compute_env_id)

class Seqera(SeqeraInterface):
    
    def __init__(self, seqera_compute_env_wrapper = None) -> None:
        self.seqera_compute_env_wrapper = SeqeraComputeEnvsWrapper()
    
    def debug_compute_enviornment(self, compute_env_id: str):
        pass
    
    def optimize_compute_enviornment(self, compute_env_id: str):
        
        if compute_env_id:
            compute_env_response = self.seqera_compute_env_wrapper.get_compute_env(compute_env_id)
            recommendations = self.seqera_compute_env_wrapper.optimize_compute_env(compute_env_response)
            print(recommendations)
        else:
            print("Please provide a valid compute enviornment ID")
            