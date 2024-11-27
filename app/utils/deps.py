from fastapi import Depends, HTTPException, Header
from config import settings, logger as logging

async def get_api_key(x_api_key: str = Header(...)):
    if x_api_key != settings.API_KEY:
        logging.info("Invalid API Key")
        raise HTTPException(status_code=403, detail="Invalid API Key")
