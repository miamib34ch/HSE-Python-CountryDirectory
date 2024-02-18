"""
Настройки проекта.
"""

import os
from typing import Optional

# путь к директории для сохранения файлов
MEDIA_PATH: str = os.getenv("MEDIA_PATH", "../media")

# путь к директории для логирования
LOGGING_PATH: str = os.getenv("LOGGING_PATH", "../logs")
# формат для записей логов
LOGGING_FORMAT: str = os.getenv(
    "LOGGING_FORMAT", "%(name)s %(asctime)s %(levelname)s %(message)s"
)
# уровень логирования
LOGGING_LEVEL: str = os.getenv("LOGGING_LEVEL", "INFO")

# ключи для доступа к API
API_KEY_APILAYER: Optional[str] = os.getenv("API_KEY_APILAYER")
API_KEY_OPENWEATHER: Optional[str] = os.getenv("API_KEY_OPENWEATHER")
API_KEY_NEWSAPI: Optional[str] = os.getenv("API_KEY_NEWSAPI")

# время актуальности данных о странах (в секундах), по умолчанию – один год
CACHE_TTL_COUNTRY: int = int(os.getenv("CACHE_TTL_COUNTRY", "31_536_000"))
# время актуальности данных о курсах валют (в секундах), по умолчанию – сутки
CACHE_TTL_CURRENCY_RATES: int = int(os.getenv("CACHE_TTL_CURRENCY_RATES", "86_400"))
# время актуальности данных о погоде (в секундах), по умолчанию ~ три часа
CACHE_TTL_WEATHER: int = int(os.getenv("CACHE_TTL_WEATHER", "10_700"))
# время актуальности данных о новостях (в секундах), по умолчанию – один час
CACHE_TTL_NEWS: int = int(os.getenv("CACHE_TTL_NEWS", "3_600"))
# количество новостей для показа
NEWS_COUNT: int = int(os.getenv("NEWS_COUNT", "3"))
