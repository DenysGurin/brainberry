import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.flaskenv'))


class Config(object):
    APP_NAME = "app"
    LOGGER_NAME = "app"
    DB_NAME = "api_db"
    DB_HOST = 'localhost'
    DB_PORT = 27017
    PROJECT_PATH = basedir
    # set PROJECT_PATH as current working directory
    os.chdir(PROJECT_PATH)

    API_PREFIX = "/api{}"

