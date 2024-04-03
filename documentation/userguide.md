# User guide

## Instructions for starting the app:

Clone the repository to your computer.

Navigate to the root directory of the project.

Install the application dependencies with the following command:

```bash
poetry install
```

Start the application with the following command:

```bash
poetry run invoke start
```

## Other command line functions

Run tests with the following command:

```bash
poetry run invoke test
```

Create coverage report with the following command:

```bash
poetry run invoke coverage-report
```

Run pylint with the following command:

```bash
poetry run invoke lint
```