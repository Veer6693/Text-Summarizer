from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.components.data_transformation import DataTransformation



class DataTransformationTrainingpipeline:
    def __init__(self):
        pass

    def main(self):
        config_manager = ConfigurationManager()
        data_transformation = DataTransformation(config_manager.get_data_transformation_config())
        data_transformation.convert()