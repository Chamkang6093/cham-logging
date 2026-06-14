# cham-logging

A small stdlib-only helper for configuring Python logging.

## Usage

Call `init_logger()` once near the start of your process.

```python
import logging

from cham_logging.bootstrap import init_logger


init_logger()

logger = logging.getLogger(__name__)
logger.info("service started")
```

## Environment variables

`LOG_LEVEL` controls the root logger and handler level.

```bash
LOG_LEVEL=DEBUG python -m your_app
```

If `LOG_LEVEL` is not set, `INFO` is used.

`LOG_FILE` enables an additional UTF-8 file handler.

```bash
LOG_FILE=app.log python -m your_app
```

Both variables can be used together.

```bash
LOG_LEVEL=DEBUG LOG_FILE=app.log python -m your_app
```

## Format

Logs use UTC with microsecond precision:

```text
2026-06-14T13:30:00.123456+00:00 - INFO - service started
```

The timezone is fixed to UTC for now and cannot be configured.
