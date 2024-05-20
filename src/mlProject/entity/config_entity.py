from pydantic import BaseModel
from pathlib import Path

class DataIngestionConfig(BaseModel):
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

    model_config = {
        "frozen": True  # This makes the model immutable
    }

class DataValidationConfig(BaseModel):
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict

    model_config = {
        "frozen": True
    }


class DataTransformationConfig(BaseModel):
    root_dir: Path
    data_path: Path

    model_config = {
        "frozen": True
    }

class ModelTrainerConfig(BaseModel):
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    modelName: str
    alpha: float
    l1_ratio: float
    target_column: str

    model_config = {
        "frozen": True
    }