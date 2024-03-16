from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.components.data_validation import DataValidation



class DataValidationTrainingpipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation = DataValidation(config=config.get_data_validation_config())
        data_validation.validate_all_files_exists()