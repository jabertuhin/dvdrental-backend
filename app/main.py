from fastapi import FastAPI

from app.routes import health


app = FastAPI()


# including router in the app
app.include_router(health.router)
