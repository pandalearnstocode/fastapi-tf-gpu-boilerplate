from fastapi import FastAPI, HTTPException
from loguru import logger
import tensorflow as tf
from utils import get_available_devices


app = FastAPI()


@app.get("/tic")
def get_toc():
    logger.info("App is up.")
    try:
        logger.info("Able to call internal modules from pymmm.")
        return {"tic": "toc"}
    except Exception as e:
        logger.critical(f"Check detailed error here: {e}.")
        raise HTTPException(status_code=404, detail="pymmm module not found")

@app.get("/version")
def get_tf_version():
    try:
        return {"tv_version": tf.__version__}
    except Exception as e:
        logger.critical(f"Check detailed error here: {e}.")
        raise HTTPException(status_code=404, detail="pymmm module not found")

@app.get("/device_list")
def get_device_list():
    logger.info("Looking for hardware resources for TF.")
    try:
        available_devices = get_available_devices()
        return {"available_devices": available_devices}
    except Exception as e:
        logger.critical(
            "Unable to access pymmm library internal function : get_available_devices."
        )
        logger.critical(f"Check detailed error here: {e}.")
        raise HTTPException(
            status_code=404, detail="Unable to access hard resource details."
        )