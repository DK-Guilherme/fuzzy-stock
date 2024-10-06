from fastapi import FastAPI

from server.routes.company_router import router as company_router

app = FastAPI()

app.include_router(company_router, prefix="/company")