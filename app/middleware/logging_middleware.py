from starlette.middleware.base import BaseHTTPMiddleware
from app.utils.logger import logger
import time

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.time()
        response = await call_next(request)
        duration = round((time.time() - start) * 1000, 2)

        logger.info(f"{request.method} {request.url.path} - {duration}ms")

        return response
