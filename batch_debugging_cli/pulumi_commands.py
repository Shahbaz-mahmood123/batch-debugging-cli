from infrastructure.pulumi import PulumiExecution
from infrastructure.gcp_compute_engine import PulumiGCP
from batch_debugging_cli.pulumi_config import PulumiConfig
import typer



class PulumiCommandsInterface():
    def pulumi_up(self) -> None:
        pass 
    def pulumi_destroy(self) -> None:
        pass
    
class PulumiCommands(PulumiCommandsInterface):
    
    def __init__(self, config_file: str) -> None:
        self.config_file = config_file
        self.config = PulumiConfig(self.config_file) 
        self.infra_config = PulumiGCP(project_id=self.config.project_id, 
                                 location=self.config.location, name=self.config.resource_name)
        self.execution = PulumiExecution(project_id=self.config.project_id,
                                    stack_name=self.config.stack_name,pulumi_gcp=self.infra_config)
    
    def pulumi_up(self) -> None:
        result = self.execution.execute_gcp()
        return    
    
    def pulumi_destroy(self):
        destroy = self.execution.destroy()
    
    
if __name__ == "__main__":
    app()
