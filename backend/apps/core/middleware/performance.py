import logging
import time

logger = logging.getLogger(
    __name__,
)


class PerformanceLoggingMiddleware:
    """
    Log request execution time.
    """

    def __init__(
        self,
        get_response,
    ):
        self.get_response = get_response

    def __call__(
        self,
        request,
    ):
        start_time = time.time()

        response = self.get_response(
            request,
        )

        duration = time.time() - start_time

        logger.info(
            ("Request completed | method=%s path=%s duration=%.2fs"),
            request.method,
            request.path,
            duration,
        )

        return response
