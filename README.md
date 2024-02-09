# Country Directory 

Console application for getting up-to-date information about countries.

The application allows you to receive from open sources and save to the files information about countries and provide it to the user.

## Installation

Clone the repository to your computer:
```bash
git clone https://github.com/mnv/python-course-country-directory.git
```

### Requirements:

Install the appropriate software:

1. [Docker Desktop](https://www.docker.com).
2. [Git](https://github.com/git-guides/install-git).
3. [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/download) (optional).

## Usage

1. To configure the application copy `.env.sample` into `.env` file:
    ```shell
    cp .env.sample .env
    ```
   
    This file contains environment variables that will share their values across the application.
    The sample file (`.env.sample`) contains a set of variables with default values. 
    So it can be configured depending on the environment.

    To access the API, visit the appropriate resources and obtain an access token:
    - APILayer – Geography API (https://apilayer.com/marketplace/geo-api)
    - OpenWeather – Weather Free Plan (https://openweathermap.org/price#weather)
   
    Set received access tokens as environment variable values (in `.env` file):
    - `API_KEY_APILAYER` – for APILayer access token
    - `API_KEY_OPENWEATHER` – for OpenWeather access token

2. Build the container using Docker Compose:
    ```shell
    docker compose build
    ```
    This command should be run from the root directory where `Dockerfile` is located.
    You also need to build the docker container again in case if you have updated `requirements.txt`.

3. To see the documentation for the console command run:
    ```shell
    docker compose run app python main.py --help
    ```
   
4. To start the application run:
    ```shell
    docker compose up cron
    ```
   
    A background program will start that will collect information about countries from various sources and save
    it to files in the `media` directory. The data collection process runs once per minute.
    The frequency of data updates depends on the settings in the variables (in `.env` file):

    - `CACHE_TTL_COUNTRY` (country data up-to-date time in seconds)
    - `CACHE_TTL_CURRENCY_RATES` (currency rates data up-to-date time in seconds)
    - `CACHE_TTL_WEATHER` (weather data up-to-date time in seconds)
   
5. After collecting all the data, you can query the country information by executing the command:
    ```shell
    docker compose run app
    ```
   
    This command will use its default parameters. 

    You can also specify needed parameters:
    ```shell
    docker compose run app python main.py --location London
    ```

### Automation commands

The project contains a special `Makefile` that provides shortcuts for a set of commands:
1. Build the Docker container:
    ```shell
    make build
    ```

2. Generate Sphinx documentation run:
    ```shell
    make docs-html
    ```

3. Autoformat source code:
    ```shell
    make format
    ```

4. Static analysis (linters):
    ```shell
    make lint
    ```

5. Autotests:
    ```shell
    make test
    ```

    The test coverage report will be located at `src/htmlcov/index.html`. 
    So you can estimate the quality of automated test coverage.

6. Run autoformat, linters and tests in one command:
    ```shell
    make all
    ```

Run these commands from the source directory where `Makefile` is located.

## Documentation

The project integrated with the [Sphinx](https://www.sphinx-doc.org/en/master/) documentation engine. 
It allows the creation of documentation from source code. 
So the source code should contain docstrings in [reStructuredText](https://docutils.sourceforge.io/rst.html) format.

To create HTML documentation run this command from the source directory where `Makefile` is located:
```shell
make docs-html
```

After generation documentation can be opened from a file `docs/build/html/index.html`.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
