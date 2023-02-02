import uvicorn
import loguru
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from features import converter_router

app = FastAPI()

# app.mount('/asset', StaticFiles(directory='../asset'), name='asset')
app.include_router(converter_router)


uvicorn.Config(app, host='0.0.0.0', port=8000)