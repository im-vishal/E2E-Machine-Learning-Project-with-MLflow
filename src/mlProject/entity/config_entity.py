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