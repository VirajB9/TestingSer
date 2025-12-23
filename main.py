from routes.brand_route import brand_router
from routes.item_route import item_router
from fastapi import FastAPI
from sql.database import Base, engine


app=FastAPI(title="Brand and Item Management API", version="1.0.0")

Base.metadata.create_all(bind=engine)

app.include_router(brand_router)
app.include_router(item_router)