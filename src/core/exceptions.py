class AppError(Exception):
    """Base class for all custom errors in the app."""

    pass


class ExternalServiceError(AppError):
    """Raised when an external API like OpenAI or Arxiv fails."""

    def __init__(self, service: str, detail: str):
        self.service = service
        self.detail = detail
        super().__init__(f"{service} failed: {detail}")


#  inhirits from AppError which inhirits from Exception
class NotFoundError(AppError):
    """Raised when a paper, review, or result is missing."""

    pass


class ValidationError(AppError):
    """Raised when input data is incorrect or missing."""

    pass
