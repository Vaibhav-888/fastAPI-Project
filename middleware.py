# from fastapi import Request
# from logger import logger
#
# async def log_middleware(request: Request, call_next):
#     try:
#         log_dict = {
#             "url": request.url.path,
#             "method": request.method
#         }
#         logger.info(f"request method info: {log_dict}")
#
#         logger.info(f"Incoming request: {request.method} {request.url.path}")
#         response = await call_next(request)
#         logger.info(f"Response status: {response.status_code}")
#         return response
#     except Exception as e:
#         logger.error(f"Middleware error: {e}")
#         raise e


from fastapi import Request
from logger import get_logger

async def log_middleware(request: Request, call_next):
    try:
        dict = {
            "url": request.url.path,
            "method": request.method,
        }

        get_logger.info(f"request method info: {dict}")
        response = await call_next(request)

    except Exception as e:
        get_logger.error(f"Middleware error: {e}")