# Line API Utils

A Python utility for managing LINE Messaging API features.

## Overview

line_api_utils

 is a versatile tool designed to simplify the management of various features in the LINE Messaging API. Currently, it provides functionalities such as deleting all existing rich menus, with plans to add more capabilities in the future to enhance menu and user management.

## Installation

Ensure you have [Poetry](https://python-poetry.org/) installed. Then, clone the repository and install the dependencies:

```sh
poetry install
```

## Usage

### Delete All Rich Menus

To delete all rich menus, run the 

delete_all_rich_menus.py

 script:

```sh
poetry run python line_api_utils/delete_all_rich_menus.py
```

### Future Features

Additional functionalities will be available as the project evolves, such as creating rich menus, managing user profiles, and handling messaging events. Stay tuned for updates.

## Configuration

Create a 

.env

 file in the root directory with the necessary environment variables:

```
LINE_CHANNEL_ACCESS_TOKEN=your_channel_access_token
```

## Testing

Run the tests using Poetry:

```sh
poetry run pytest
```

## License

This project is licensed under the MIT License.
