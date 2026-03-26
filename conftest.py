import os
import pytest
from dotenv import load_dotenv  

load_dotenv()  # Load environment variables from .env file  

@pytest.fixture
def api_config():
    return {
        "key": os.getenv("API_KEY"),
        "url": os.getenv("BASE_URL")
    }
