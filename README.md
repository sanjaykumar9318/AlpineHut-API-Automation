# AlpineHut – Python API Automation Testing Framework

## Project Overview

A Python-based automation testing framework built using Pytest and Requests to test the deployed AlpineHut hotel listing application.

The framework automates HTTP workflows, authentication, session management, CRUD operations and negative testing.

## Tech Stack

- Python
- Requests
- Pytest
- Requests Session
- JSON Schema
- python-dotenv

## Framework Architecture

```text
AlpineHut-API-Automation/
│
├── clients/
│   └── api_client.py
├── config/
│   └── config.py
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_listings.py
│   ├── test_reviews.py
│   ├── test_authorization.py
│   └── test_schema.py
├── schemas/
│   └── listing_schema.json
├── utils/
├── .env
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md

## Features

- Reusable API client
- HTTP request handling
- Session and cookie management
- Authentication testing
- Positive and negative testing
- CRUD test scenarios
- Pytest fixtures
- Parametrized testing
- JSON Schema validation

## Installation

```bash
git clone YOUR_REPOSITORY_URL
cd AlpineHut-API-Automation
python -m venv venv
```

Activate the virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file:

```env
BASE_URL=https://alphinehut.onrender.com
TEST_USERNAME=your_test_username
TEST_PASSWORD=your_test_password
```

## Execute Tests

Run all tests:

```bash
python -m pytest -v
```

Run authentication tests:

```bash
python -m pytest tests/test_auth.py -v
```

Run listing tests:

```bash
python -m pytest tests/test_listings.py -v
```

## Application Under Test

AlpineHut is a hotel listing application built using Node.js, Express.js, MongoDB, Mongoose and Passport.js.

The current application primarily uses server-rendered HTML responses and session-based authentication. JSON Schema validation is demonstrated separately using a representative listing object; it is not yet validating live JSON API responses.

## Future Improvements

- Dedicated JSON REST API endpoints
- Live JSON response schema validation
- OpenAPI specification
- CI/CD integration