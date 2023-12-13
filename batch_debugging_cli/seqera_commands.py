import typer
from typing_extensions import Annotated
from rich import print

from core.compute_envs import SeqeraComputeEnvsWrapper

class SeqeraCommandsInterface():

    def optimize_compute_enviornment(self, compute_env_id: str):
        pass


class SeqeraCommands(SeqeraCommandsInterface):
    
    def __init__(self, seqera_compute_env_wrapper = None) -> None:
        self.seqera_compute_env_wrapper = SeqeraComputeEnvsWrapper()
    
    def optimize_compute_enviornment(self, compute_env_id: str):
        
        if compute_env_id:
            compute_env_response = self.seqera_compute_env_wrapper.get_compute_env(compute_env_id)
            recommendations = self.seqera_compute_env_wrapper.optimize_compute_env(compute_env_response)
            print(recommendations)


# test = seqera.get_compute_env("5tQSF2ahyA19GNS5b8rzNS")
# recommendations = seqera.optimize_compute_env(test)