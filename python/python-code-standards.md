# Docstrings

Should use 'google' convention, they should look something like this:

def my_function(param1: str, param2: int = 0) -> bool:
    """One-line summary sentence.

    Optional extended description that can span multiple lines and goes into
    more detail about what the function does.

    Args:
        param1: Description of param1. No need to repeat the type since it's
            in the signature. Continuation lines are indented by 4 spaces.
        param2: Description of param2. Defaults to 0.

    Returns:
        Description of the return value.

    Raises:
        ValueError: When and why this is raised.
        KeyError: When and why this is raised.

    Example (optional):
        >>> my_function("hello", 5)
        True
    """


# .ignore

*# Python
__pycache__/
.pytest_cache/
.ruff_cache/
modules/__pycache__/
scripts/__pycache__/
sqs/__pycache__/
tests/unit/__pycache__/

*# Environment
.env
.venv/
venv/

*# Distribution / packaging
*.egg-info/
dist/
build/

*# IDEs and editors
.vscode/


# loggin() not print()




# lazy loggin(%) not f-strings

f-string logging
====================
- example : logger.debug(f"Processing order {order_id}")
- The string is formatted immediately, even if the log is never emitted
- Since function still runs even if DEBUG logs are turned off, compute and loggin costs increases e.g for Lambdas.
- If deploying Lambdas you want to minimize execution time and CloudWatch ingestion costs.

✅ Lazy logging (recommended)
===============================
- example : logger.debug("Processing order %s", order_id)
- Formatting happens only if the log level is enabled
- Helps cut unnecessary processing and unnecessary log generation hence reducing cloud or storage costs.

for truly expensive work, always guard:

if logger.isEnabledFor(logging.DEBUG):
    result = expensive_function()
    logger.debug("Result: %s", result)
