from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.components.model_trainer import ModelTrainer



class ModelTrainerTrainingpipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer = ModelTrainer(config.get_model_trainer_config())
        model_trainer.train()