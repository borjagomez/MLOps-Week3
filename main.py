from fastapi import FastAPI, status

import logging
from logging.config import dictConfig
from log_config import log_config # this is your local file

from pydantic import BaseModel
class PredictionRequest(BaseModel):
  query_string: str

from transformers import pipeline
sentiment_model = pipeline("sentiment-analysis")  

dictConfig(log_config)
logger = logging.getLogger("reddit-broker-bot") # should be this name unless you change it in log_config.py

app = FastAPI()

@app.get('/healthcheck', status_code=status.HTTP_200_OK)
def perform_healthcheck():
    logger.info('Healthcheck ok')
    return {'healthcheck': 'Ok'}

@app.post("/predict")
def predict(request: PredictionRequest):
  # YOUR CODE GOES HERE
  sentiment_query_sentence = request.query_string
  sentiment = sentiment_model(sentiment_query_sentence)
  return {'sentiment': sentiment}