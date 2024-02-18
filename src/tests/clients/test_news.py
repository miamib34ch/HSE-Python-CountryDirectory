"""
Тестирование клиента для получения информации о новостях.
"""


import pytest
from clients.news import NewsClient
from settings import API_KEY_NEWSAPI, NEWS_COUNT


@pytest.mark.asyncio
class TestClientNews:
    """
    Тестирование клиента для получения информации о новостях.
    """

    base_url = "https://newsapi.org/v2/everything"

    @pytest.fixture
    def client(self):
        return NewsClient()

    async def test_get_base_url(self, client):
        assert await client.get_base_url() == self.base_url

    async def test_get_news(self, mocker, client):
        mocker.patch("clients.news.NewsClient._request")
        await client.get_news("test")
        client._request.assert_called_once_with(
            f"{self.base_url}?q=test&apiKey={API_KEY_NEWSAPI}&pageSize={NEWS_COUNT}"
        )
