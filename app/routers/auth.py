from fastapi import APIRouter, HTTPException
from datetime import datetime
from uptime_kuma_api import UptimeKumaException, UptimeKumaApi

from models.user import Users
from config import settings
from config import logger as logging

router = APIRouter(redirect_slashes=True)

@router.post("/access-token")
async def login_access_token():
    try:
        user = await Users.get_or_none(username="admin")
        if not user:
            logging.info("Admin user not found")
            raise HTTPException(400, {"message": "Admin user not found"})

        user.last_visit = datetime.now()
        await user.save(update_fields=["last_visit"])

        logging.fatal(f"hello from {settings.KUMA_SERVER}")
        api = UptimeKumaApi(settings.KUMA_SERVER)
        resp = api.login(settings.KUMA_USERNAME, settings.KUMA_PASSWORD)

        logging.info("Logged in to UptimeKuma")

        response = {"message": "Logged in successfully"}

    except UptimeKumaException as e:
        logging.info(e)
        raise HTTPException(400, {"message": "Incorrect Kuma credentials"})
    except Exception as e:
        logging.fatal(e)
        raise HTTPException(400, str(e))

    return response