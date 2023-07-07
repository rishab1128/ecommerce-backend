from fastapi import FastAPI
from routes.ecommerce_routes import route

app = FastAPI()
app.include_router(route)