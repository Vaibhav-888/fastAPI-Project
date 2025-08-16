# from fastapi import FastAPI
# import uvicorn
# # from logger import logger
# # from middleware import log_middleware
# # from starlette.middleware.base import BaseHTTPMiddleware
#
# app = FastAPI()
# # app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)
# # logger.info("Started APP...")
#
# @app.get("/")
# async def root() -> dict:
#     # logger.info("Requested to index page...")
#     return {"message": "Hello"}
#
# @app.get("/upload_video")
# async def upload_video():
#     # logger.info("Requested to upload video...")
#     return {"message": "video uploaded"}
#
# if __name__ == "__main__":
#     uvicorn.run(app)
from idlelib.debugobj import dispatch

from fastapi import FastAPI
import uvicorn
from logger import get_logger
from middleware import log_middleware
from starlette.middleware.base import BaseHTTPMiddleware
import logging
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()
app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)
get_logger.info("Application started...")

@app.get("/")
async def root():
    get_logger.info(f"get method: '/' endpoint invoked: root method return some message")
    return {"message": "this is root endpoint"}

@app.get("/upload_video")
async def upload_vd():
    get_logger.info(f"get method: '/upload video' endpoint invoked: video uploaded.")
    return {"message": "video uploaded!"}


if __name__ == "__main__":
    uvicorn.run(app)