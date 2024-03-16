from textsummarizer.logging import logger
from textsummarizer.pipeline.stage_1_data_ingestion import DataIngestionTrainingpipeline

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
