import os

from infrastructure.pulumi import PulumiExecution
from infrastructure.gcp_compute_engine import PulumiGCP
from infrastructure.pulumi_config import PulumiGCPConfig, PulumiConfig

class PulumiCommandsInterface():
    def pulumi_up(self) -> None:
        pass
    
    def pulumi_destroy(self):
        pass
    
    def pulumi_preview(self):
        pass
    
    def pulumi_cancel(self):
        pass
    
    def pulumi_refresh(self):
        pass
    
    def select_gcp_type(self):
        pass
    
class PulumiCommands(PulumiCommandsInterface):
    
    def __init__(self, config_file: str) -> None:
        self.config_file = config_file
        
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"File not found: {self.config_file}")
        
        #self.select_gcp_type()
        #TODO Dynamically select which type of deployment it will be, GKE, GCP compute, azure, aks etc
        
        self.config = PulumiGCPConfig(self.config_file) 
        
        current_working_directory = os.getcwd()
        
        self.infra_config = PulumiGCP(project_id=self.config.project_id, 
                                 location=self.config.location, name=self.config.resource_name, region=self.config.region, 
                                 zone=self.config.zone, instance_name=self.config.instance_name,tower_env_secret=self.config.tower_env_secret,
                                 tower_yaml_secret=self.config.tower_yaml_secret, harbor_creds=self.config.harbor_creds,
                                groundswell_secret=self.config.groundswell_secret, source_ranges=self.config.source_ranges, 
                                tags=self.config.tags, source_tags=self.config.source_tags)
                       
        self.execution = PulumiExecution(project_id=self.config.project_id,
                                    stack_name=self.config.stack_name,pulumi_program=self.infra_config, work_dir=current_working_directory)
    
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
        
    def destroy_stack(self):
        refresh = self.execution.destroy_stack()
        
    def select_gcp_type(self):
        
        if self.config.provider == 'minimal':
            PulumiGCPConfig(self.config_file) 
            self.infra_config = PulumiGCP(project_id=self.config.project_id, 
                                 location=self.config.location, name=self.config.resource_name, region=self.config.region, 
                                 zone=self.config.zone, instance_name=self.config.instance_name)
        
        if self.config.provider == 'standard':
            pass
        
        if self.config.provider == 'private':
            pass
    
    def select_gke_type(self):
        
        if self.config.provider == 'minimal':
            pass 
        
        if self.config.provider == 'standard':
            pass
        
        if self.config.provider == 'private':
            pass
    