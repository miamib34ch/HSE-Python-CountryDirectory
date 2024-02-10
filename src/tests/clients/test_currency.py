"""
Тестирование функций клиента для получения информации о курсах валют.
"""


import pytest
from clients.currency import CurrencyClient


@pytest.mark.asyncio
class TestClientCurrency:
    """
    Тестирование клиента для получения информации о валютах.
    """

    base_url = "https://api.apilayer.com/fixer/latest"

    @pytest.fixture
    def client(self):
        return CurrencyClient()

    async def test_get_base_url(self, client):
        assert await client.get_base_url() == self.base_url

    async def test_get_currency(self, mocker, client):
        mocker.patch("clients.currency.CurrencyClient._request")
        await client.get_rates()
        client._request.assert_called_once_with(f"{self.base_url}?base=rub")

        await client.get_rates("test")
        client._request.assert_called_with(f"{self.base_url}?base=test")
