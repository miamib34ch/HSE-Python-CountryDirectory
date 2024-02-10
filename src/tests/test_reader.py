"""
Тестирование функций поиска (чтения) собранной информации в файлах.
"""


import pytest
from collectors.models import (
    CountryDTO,
    LocationDTO,
    LocationInfoDTO,
    NewsInfoDTO,
    WeatherInfoDTO,
)
from reader import Reader


@pytest.mark.asyncio
class TestReader:
    location = LocationDTO(
        alpha2code="RU",
        capital="Moscow",
    )

    @pytest.fixture
    def reader(self):
        return Reader()

    async def test_find(self, reader):
        location = await reader.find("Russia")
        assert type(location) == LocationInfoDTO
        assert location.location.name == "Russian Federation"
        assert location.location.capital == "Moscow"
        assert location.location.alpha2code == "RU"
        assert len(location.location.currencies) == 1
        assert len(location.location.languages) == 1
        assert len(location.location.timezones) == 9
        assert location.location.population > 145934462
        assert location.location.area == 17124442
        assert location.location.longitude == 100.0
        assert location.location.latitude == 60.0
        assert len(location.location.alt_spellings) == 5
        assert location.location.subregion == "Eastern Europe"
        assert type(location.weather) == WeatherInfoDTO
        assert location.weather.timezone == 3
        assert len(location.news) == 3
        assert len(location.currency_rates) == 1

    async def test_get_weather(self, mocker, reader):
        weather = await reader.get_weather(self.location)
        assert type(weather) == WeatherInfoDTO
        assert weather.timezone == 3

    async def test_get_news(self, mocker, reader):
        news = await reader.get_news(self.location)
        assert len(news) == 3
        assert type(news[0]) == NewsInfoDTO

    async def test_find_country(self, mocker, reader):
        country = await reader.find_country("Russia")
        assert type(country) == CountryDTO
        assert country.name == "Russian Federation"
        assert country.capital == "Moscow"

    async def test_find_country_none(self, mocker, reader):
        country = await reader.find_country("test")
        assert country is None