from textsummarizer.logging import logger
from textsummarizer.pipeline.stage_1_data_ingestion import DataIngestionTrainingpipeline
from textsummarizer.pipeline.stage_2_data_validation import DataValidationTrainingpipeline
from textsummarizer.pipeline.stage_3_data_transformation import DataTransformationTrainingpipeline



stage_name = "Data Ingestion Training"
try:
    logger.info(f"============ {stage_name} started ============")
    data_ingestion = DataIngestionTrainingpipeline()
    data_ingestion.main()
    logger.info(f"============ {stage_name} completed ============")

except Exception as e:
    logger.error(f"============ {stage_name} failed ============")
    logger.exception(e)
    raise e



stage_name = "Data Validation Training"
try:
    logger.info(f"============ {stage_name} started ============")
    data_validation = DataValidationTrainingpipeline()
    data_validation.main()
    logger.info(f"============ {stage_name} completed ============")

except Exception as e:
    logger.error(f"============ {stage_name} failed ============")
    logger.exception(e)
    raise e



stage_name = "Data Transformation Training"
try:
    logger.info(f"============ {stage_name} started ============")
    data_transformation = DataTransformationTrainingpipeline()
    data_transformation.main()
    logger.info(f"============ {stage_name} completed ============")

except Exception as e:
    logger.error(f"============ {stage_name} failed ============")
    logger.exception(e)
    raise e
