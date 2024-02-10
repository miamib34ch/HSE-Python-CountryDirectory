"""
Тестирование функций сбора информации о курсах валют.
"""


import pytest
from collectors.collector import CurrencyRatesCollector


@pytest.mark.asyncio
class TestCurrencyCollector:
    """
    Тестирование функций сбора информации о курсах валют.
    """

    @pytest.fixture(autouse=True)
    def setup(self):
        self.collector = CurrencyRatesCollector()

    async def test_collect_currency_success(self):
        """
        Тестирование получения информации о курсе валют.
        """
        await self.collector.collect()

    async def test_read_currency_success(self):
        """
        Тестирование чтения информации о курсе валют.
        """
        currencies = await self.collector.read()
        assert currencies is not None
        assert currencies.base == "RUB"
        assert len(currencies.rates) == 169
