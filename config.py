import os
from dotenv import load_dotenv
load_dotenv()

CONFIG = {
    "N": int(os.getenv("TOP_N", "20")),
    "platforms": os.getenv("PLATFORMS", "google").split(","),
    "google_api_key": os.getenv("GOOGLE_API_KEY"),
    "google_cse_id": os.getenv("GOOGLE_CSE_ID"),
}
