import os
from textsummarizer.logging import logger
from textsummarizer.entity import DataValidationConfig


class DataValidation:
    def __init__(self, config : DataValidationConfig):
        self.config = config
    
    def validate_all_files_exists(self) -> bool:
        try:
            validation_status = None

            all_files = os.listdir(os.path.join('artifacts','data_ingestion','samsum_dataset'))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'Validation status : {validation_status} \nFile {file} not found in {self.config.ALL_REQUIRED_FILES}')
                    logger.info(f'File {file} not found')

                else :
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'Validation status : {validation_status}')
                    logger.info(f'File {file} found')

            return validation_status
                
        except Exception as e:
            logger.error(e)
            raise e
