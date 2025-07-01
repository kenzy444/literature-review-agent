from src.core.exceptions import ExternalServiceError

try:
    raise ExternalServiceError("HuggingFace", "timeout")
except ExternalServiceError as e:
    print("Caught error:", str(e))
