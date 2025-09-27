"""
Lime IoT ML Platform Configuration
Settings and environment variables for the project
"""

import os
from pathlib import Path

# Project structure
PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# API Configuration
LIME_BASE_URL = "https://data.lime.bike/api/partners/v1/gbfs"
DEFAULT_CITY = "seattle"

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://localhost/lime_iot")

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

print("🚀 Lime IoT ML Platform - Configuration loaded!")
