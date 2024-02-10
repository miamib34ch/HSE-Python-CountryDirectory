"""
Тестирование функций сбора информации о погоде.
"""


import pytest
from collectors.collector import WeatherCollector
from collectors.models import LocationDTO


@pytest.mark.asyncio
class TestWeatherCollector:
    """
    Тестирование функций сбора информации о погоде.
    """

    location = LocationDTO(
        capital="Moscow",
        alpha2code="RU",
    )

    @pytest.fixture(autouse=True)
    def setup(self):
        self.collector = WeatherCollector()

    async def test_collect_weather_success(self):
        """
        Тестирование получения информации о погоде.
        """
        await self.collector.collect(frozenset([self.location]))

    async def test_read_weather_success(self):
        """
        Тестирование чтения информации о погоде.
        """
        weather = await self.collector.read(self.location)
        assert weather is not None
        assert weather.timezone == 3
