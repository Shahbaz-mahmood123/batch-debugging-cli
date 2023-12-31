from infrastructure.pulumi import PulumiExecution
from infrastructure.gcp_compute_engine import PulumiGCP
from infrastructure.pulumi_config import PulumiGCPConfig

class PulumiCommandsInterface():
    def pulumi_up(self) -> None:
        pass 
    def pulumi_destroy(self) -> None:
        pass
    
class PulumiCommands(PulumiCommandsInterface):
    
    def __init__(self, config_file: str) -> None:
        self.config_file = config_file
        self.config = PulumiGCPConfig(self.config_file) 
        self.infra_config = PulumiGCP(project_id=self.config.project_id, 
                                 location=self.config.location, name=self.config.resource_name, region=self.config.region, 
                                 zone=self.config.zone, instance_name=self.config.instance_name)

        self.execution = PulumiExecution(project_id=self.config.project_id,
                                    stack_name=self.config.stack_name,pulumi_gcp=self.infra_config, work_dir=".")
    
    def pulumi_up(self) -> None:
        result = self.execution.execute()
    
    def pulumi_destroy(self):
        destroy = self.execution.destroy()
    
    def pulumi_preview(self):
        preview = self.execution.preview()
    
    def pulumi_cancel(self):
        cancel = self.execution.cancel()
    
    def pulumi_refresh(self):
        refresh = self.execution.refresh()
        
    