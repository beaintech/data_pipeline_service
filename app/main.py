from fastapi import FastAPI
from app.database import Base, engine
from app.api.pipeline import router as pipeline_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Data Pipeline Side Service")

app.include_router(pipeline_router)

@app.get("/")
def root():
    return {"status": "ok"}
