from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.components.model_evaluation import ModelEvaluation



class ModelEvaluationTrainingpipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation = ModelEvaluation(config=config.get_model_evaluation_config())
        model_evaluation.evaluate()