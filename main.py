from textsummarizer.logging import logger
from textsummarizer.pipeline.stage_1_data_ingestion import DataIngestionTrainingpipeline
from textsummarizer.pipeline.stage_2_data_validation import DataValidationTrainingpipeline
from textsummarizer.pipeline.stage_3_data_transformation import DataTransformationTrainingpipeline
from textsummarizer.pipeline.stage_4_model_trainer import ModelTrainerTrainingpipeline
from textsummarizer.pipeline.step_5_model_evaluation import ModelEvaluationTrainingpipeline




stage_name = "Data Ingestion Stage"
try:
    logger.info(f"============ {stage_name} started ============")
    data_ingestion = DataIngestionTrainingpipeline()
    data_ingestion.main()
    logger.info(f"============ {stage_name} completed ============")

except Exception as e:
    logger.error(f"============ {stage_name} failed ============")
    logger.exception(e)
    raise e



stage_name = "Data Validation Stage"
try:
    logger.info(f"============ {stage_name} started ============")
    data_validation = DataValidationTrainingpipeline()
    data_validation.main()
    logger.info(f"============ {stage_name} completed ============")

except Exception as e:
    logger.error(f"============ {stage_name} failed ============")
    logger.exception(e)
    raise e



stage_name = "Data Transformation Stage"
try:
    logger.info(f"============ {stage_name} started ============")
    data_transformation = DataTransformationTrainingpipeline()
    data_transformation.main()
    logger.info(f"============ {stage_name} completed ============")

except Exception as e:
    logger.error(f"============ {stage_name} failed ============")
    logger.exception(e)
    raise e



stage_name = "Model Trainer Stage"
try:
    logger.info(f"============ {stage_name} started ============")
    model_trainer = ModelTrainerTrainingpipeline()
    model_trainer.main()
    logger.info(f"============ {stage_name} completed ============")

except Exception as e:
    logger.error(f"============ {stage_name} failed ============")
    logger.exception(e)
    raise e


stage_name = "Model Evaluation Stage"
try:
    logger.info(f"============ {stage_name} started ============")
    model_evaluation = ModelEvaluationTrainingpipeline()
    model_evaluation.main()
    logger.info(f"============ {stage_name} completed ============")

except Exception as e:
    logger.error(f"============ {stage_name} failed ============")
    logger.exception(e)
    raise e


