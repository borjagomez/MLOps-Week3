from fastapi import FastAPI, status

import logging
from logging.config import dictConfig
from log_config import log_config # this is your local file

dictConfig(log_config)
logger = logging.getLogger("my-project-logger") # should be this name unless you change it in log_config.py

app = FastAPI()

@app.get('/healthcheck', status_code=status.HTTP_200_OK)
def perform_healthcheck():
    logging.info('Healthcheck ok')
    return {'healthcheck': 'Ok'}
    