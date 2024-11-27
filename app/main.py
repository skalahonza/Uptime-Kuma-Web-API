# main.py
from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse

from routers import (
    statuspage,
    monitor,
    auth,
    tags,
    cert,
    info,
    uptime,
    ping,
    database,
    user,
    settings,
    maintenance,
)
from config import settings as app_settings, logger
from app_setup import initialize_app
from utils.deps import get_api_key

app = FastAPI(title=app_settings.PROJECT_NAME)
app.router.redirect_slashes = True

app.include_router(user.router, prefix="/users", tags=["Users"], dependencies=[Depends(get_api_key)])
app.include_router(settings.router, prefix="/settings", tags=["Settings"], dependencies=[Depends(get_api_key)])
app.include_router(database.router, prefix="/database", tags=["DataBase"], dependencies=[Depends(get_api_key)])
app.include_router(monitor.router, prefix="/monitors", tags=["Monitor"], dependencies=[Depends(get_api_key)])
app.include_router(statuspage.router, prefix="/statuspages", tags=["Status Page"], dependencies=[Depends(get_api_key)])
app.include_router(maintenance.router, prefix="/maintenance", tags=["Maintenance"], dependencies=[Depends(get_api_key)])
app.include_router(tags.router, prefix="/tags", tags=["Tags"], dependencies=[Depends(get_api_key)])
app.include_router(cert.router, prefix="/cert_info", tags=["Certification Info"], dependencies=[Depends(get_api_key)])
app.include_router(info.router, prefix="/info", tags=["Informations"], dependencies=[Depends(get_api_key)])
app.include_router(ping.router, prefix="/ping", tags=["Ping Average"], dependencies=[Depends(get_api_key)])
app.include_router(uptime.router, prefix="/uptime", tags=["Uptime"], dependencies=[Depends(get_api_key)])
app.include_router(auth.router, prefix="/login", tags=["Authentication"], dependencies=[Depends(get_api_key)])


@app.on_event("startup")
async def startup_event():
    await initialize_app(app)
    logger.info("KumaAPI started...")


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")
