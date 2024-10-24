from src.datascience.constants import *
from src.datascience.utils.common import read_yaml, create_directories
from src.datascience.entity.config_entity import (DataIngestionConfig)

class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH,
                 schema_filepath=SCHEMA_FILE_PATH):
        # Convert paths to absolute paths based on the current working directory
        self.config_filepath = Path(config_filepath).absolute()
        print(f"Config file absolute path: {self.config_filepath}")
        self.params_filepath = Path(params_filepath).absolute()
        self.schema_filepath = Path(schema_filepath).absolute()
        
        # Log the absolute paths to confirm
        print(f"Config file absolute path: {self.config_filepath}")
        print(f"Params file absolute path: {self.params_filepath}")
        print(f"Schema file absolute path: {self.schema_filepath}")
        
        # Read YAML files
        self.config = read_yaml(self.config_filepath)
        self.params = read_yaml(self.params_filepath)
        self.schema = read_yaml(self.schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> 'DataIngestionConfig':
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir).absolute(),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file).absolute(),
            unzip_dir=Path(config.unzip_dir).absolute()
        )
        return data_ingestion_config