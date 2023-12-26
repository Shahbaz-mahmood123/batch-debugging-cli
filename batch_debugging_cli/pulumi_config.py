import yaml

class PulumiConfigInterface():
    def validate_yaml(self):
        pass

class PulumiConfig(PulumiConfigInterface):
    
    def __init__(self, file_path: str) -> None:
        
        with open(file_path, 'r') as file:
            configs = yaml.safe_load(file) 
            
        self.project_id = configs['project_id']
        self.stack_name = configs['stack']
        self.location = configs['location']
        self.resource_name = configs['name']
        
    def validate_yaml(self):
        pass
        
         
    