"""
Тестирование функций сбора информации о странах.
"""


import pytest
from collectors.collector import CountryCollector


@pytest.mark.asyncio
class TestCountryCollector:
    """
    Тестирование функций сбора информации о странах.
    """

    @pytest.fixture(autouse=True)
    def setup(self):
        self.collector = CountryCollector()

    async def test_collect_country_success(self):
        """
        Тестирование получения информации о стране.
        """
        countries = await self.collector.collect()
        assert len(countries) == 49

    async def test_read_country_success(self):
        """
        Тестирование чтения информации о стране.
        """
        countries = await self.collector.read()
        assert len(countries) == 49