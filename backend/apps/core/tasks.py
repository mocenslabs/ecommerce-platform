from celery import Task


class BaseTaskWithRetry(
    Task,
):
    """
    Base Celery task with automatic retry.

    Future improvements:
    - dead letter queues
    - SQS integration
    - monitoring hooks
    - tracing support
    """

    autoretry_for = (Exception,)

    retry_kwargs = {
        "max_retries": 3,
        "countdown": 10,
    }

    retry_backoff = True

    retry_backoff_max = 60

    retry_jitter = True
