class UserNotFoundError(Exception):
    external_id_reference = "external_id"
    email_reference = "email"

    def __init__(self, reference: str, value: str) -> None:
        super().__init__(f"User not found, {reference}: {value}")


class DuplicateUserError(Exception):
    def __init__(self, email: str) -> None:
        super().__init__(f"User email already exists, email: {email}")
