# K-LAGAN Challenge

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

1. A Linux based OS. MacOS was used to develop this
2. Python 3.8.2 or higher
3. Poetry https://python-poetry.org/docs/
4. Selenium remote server installed and running. https://www.npmjs.com/package/selenium-standalone was used to develop/run the UI tests
5. Google Chrome
6. Appium server running for mobile tests

### Installing

Clone repo

```
git clone https://github.com/ggiunta/k-lagan-challenge-python.git
```

Install using Poetry

```
poetry install
```

## Start Selenium server
```
selenium-standalone start
```
## Start Appium server
```
appium
```

## Running the tests using Behave

1. Pokemon

```
poetry run behave --no-capture --no-color --include PokeAPI
```

2. Renfe 

```
poetry run behave --no-capture --no-color --include Renfe
```