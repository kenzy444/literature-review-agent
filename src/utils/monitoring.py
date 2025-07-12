import time
from functools import wraps
from src.core import exceptions, log
# wraps preserves metadata, should be with decorators


def timed(fn):
    """Decorator that measure execution time"""

    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            elapsed = (time.perf_counter() - start) * 1000
            log.info(f"{fn.__name__} took {elapsed:.1f} ms")

    return wrapper


def retry(times: int = 3, delay: float = 1.0):
    """Retry decorator for flaky external calls."""

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            last_err = None
            for i in range(times):
                try:
                    return fn(*args, **kwargs)
                except exceptions.ExternalServiceError as e:
                    last_err = e
                    log.warning(f"{fn.__name__} failed ({i+1}/{times})")
                    time.sleep(delay)
            raise last_err
        return wrapper

    return decorator
