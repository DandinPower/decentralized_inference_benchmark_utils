from pathlib import Path
from typing import Callable, Any


def validate_fields(d: dict, *fields: str, expected_type: Any, extra_validator: Callable[[Any], tuple[bool, str]] = None):
    """
    A generic function to validate fields in a dictionary.

    Args:
        d: The dictionary to check.
        fields: The field names to validate.
        expected_type: The expected type for the field's value (e.g., int, str).
        extra_validator: An optional function for custom validation logic.
                         It should accept the value and return a tuple:
                         (is_valid: bool, error_message: str).
    """
    for f in fields:
        value = d.get(f)

        # 1. Check for presence and correct type
        assert value is not None, f"Missing required field: {f}"
        assert isinstance(
            value, expected_type), f"Field '{f}' must be type {expected_type.__name__}, but got {type(value).__name__}"

        # 2. Perform extra validation if a validator is provided
        if extra_validator:
            is_valid, error_message = extra_validator(value)
            assert is_valid, error_message


def check_path_exists(path_str: str) -> tuple[bool, str]:
    """Validator to check if a path exists."""
    if not Path(path_str).exists():
        return (False, f"File path not found: {path_str}")
    return (True, "")
