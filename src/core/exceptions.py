class AppException(Exception):
    def __init__(
        self,
        message: str,
        *,
        code: str = "APP_ERROR",
        status_code: int = 500,
        details: dict | None = None,
    ):
        self.message = message
        self.code = code
        self.status_code = status_code
        self.details = details or {}


class ResourceNotFound(AppException):
    def __init__(
        self,
        message: str = "Resource not found",
        code: str = "RESOURCE_NOT_FOUND",
        details: dict | None = None,
    ):
        super().__init__(message=message, code=code, status_code=400, details=details or {})


class UserNotFound(ResourceNotFound):
    def __init__(self, user_id: str):
        super().__init__(
            message=f"User {user_id} not found",
            code="USER_NOT_FOUND",
        )


class GroupNotFound(ResourceNotFound):
    def __init__(self, group_id: str):
        super().__init__(
            message=f"group {group_id} not found",
            code="GROUP_NOT_FOUND",
        )


class InsufficientBalance(AppException):
    def __init__(self, balance: float):
        super().__init__(
            message="Insufficient balance",
            code="INSUFFICIENT_BALANCE",
            status_code=409,
            details={"balance": balance},
        )


class BadRequest(AppException):
    def __init__(self, field_name: str, field_value: str):
        super().__init__(
            message=f"Invalid value for {field_name} = {field_value}",
            code="INVALID_REQUEST",
            status_code=400,
            details={"field": field_name},
        )
