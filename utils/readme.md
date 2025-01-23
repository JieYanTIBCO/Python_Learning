# Python Utils Module

Common utility modules for logging and function decorators.

## Overview

This module provides reusable utilities for:
- Configurable logging setup with JSON support
- Function decoration with retry logic and type checking

## Modules

### setup_logging.py

Flexible logging configuration with JSON support and rotation capabilities.

#### Features
- JSON and plain text log formats
- Log file rotation with size limits
- Console output options
- Customizable formatting
- Type-safe configuration
- Timezone awareness

#### Usage

```python
from utils.setup_logging import get_logger

# Basic logging
logger = get_logger()
logger.info("Basic log message")

# JSON logging with indentation
logger = get_logger(json_format=True, indent=2)
logger.info("Structured logging")

# Custom file and rotation
logger = get_logger(
    log_file="app.log",
    max_bytes=10*1024*1024,  # 10MB
    backup_count=5
)
```

### log_decoration.py

A Python decorator module that provides function retry logic, type checking, and logging capabilities.

#### Features
- Automatic retry mechanism for failed function calls
- Configurable retry attempts and delay intervals
- Runtime type checking for function arguments and return values
- Detailed logging of function execution and failures
- Exception handling and custom error reporting

#### Installation

1. Copy `log_decoration.py` to your project:
```bash
cp log_decoration.py your-project/utils/
```

## Features
- Automatic retry on failures
- Configurable retry attempts and delays
- Optional type checking
- Detailed logging of function calls

## Usage

## Installation
Clone the repository
Copy required modules to your project

## Requirements
Python 3.7+
No external dependencies

## License
MIT License

## Contributing
Pull requests welcome. Please ensure tests pass and add documentation.