import subprocess
import threading
import time
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

from dotenv import load_dotenv

load_dotenv()

logger = get_logger(__name__)

def run_backend():
    try:
        logger.info("Starting backend service...")
        subprocess.run(["uvicorn", "app.backend.api:app", "--host", "127.0.0.1", "--port", "9999"], check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Backend failed to start: {e}")
        raise CustomException("Backend service failed to start", error_detail=e)

def run_frontend():
    try:
        logger.info("Starting frontend service...")
        subprocess.run(["streamlit", "run", "app/frontend/ui.py"], check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Frontend failed to start: {e}")
        raise CustomException("Frontend service failed to start", error_detail=e)

if __name__ == "__main__":
    try:
        threading.Thread(target=run_backend).start()
        time.sleep(2) 
        run_frontend()

    except CustomException as e:
        logger.exception(f"CustomException occurred: {str(e)}")
    except Exception as e:
        logger.exception(f"An unexpected error occurred: {str(e)}")
