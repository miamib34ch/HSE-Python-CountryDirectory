"""
Тестирование функций генерации выходных данных.
"""


import pytest
from collectors.models import (
    CountryDTO,
    CurrencyInfoDTO,
    LanguagesInfoDTO,
    LocationInfoDTO,
    NewsInfoDTO,
    WeatherInfoDTO,
)
from renderer import Renderer


@pytest.mark.asyncio
class TestRenderer:
    location = LocationInfoDTO(
        location=CountryDTO(
            alpha2code="RU",
            capital="Moscow",
            currencies={CurrencyInfoDTO(code="USD")},
            languages={LanguagesInfoDTO(name="Russian", native_name="Русский")},
            flag="test",
            subregion="test",
            name="Russia",
            population=3,
            area=3,
            longitude=3,
            latitude=3,
            alt_spellings=["test"],
            timezones=[3],
        ),
        weather=WeatherInfoDTO(
            timezone=3,
            temp=3,
            pressure=3,
            humidity=3,
            wind_speed=3,
            visibility=3,
            dt=1,
            description="test",
        ),
        currency_rates={"USD": 1.0},
        news=[
            NewsInfoDTO(
                source="test",
                published_at=0,
                title="test",
                content="test",
                description="test",
                url="test",
                url_to_image="test",
            )
        ],
    )

    async def test_format_languages(self):
        renderer = Renderer(self.location)
        result = await renderer._format_languages()
        assert result == "Russian (Русский)"

    async def test_format_currencies_rates(self):
        renderer = Renderer(self.location)
        result = await renderer._format_currency_rates()
        assert result == "USD = 1.00 руб."

    async def test_format_news(self):
        renderer = Renderer(self.location)
        results = await renderer._format_news(self.location.news, 10, 20)
        assert len(results) == 7
        first_column = [
            "Источник",
            "Новость",
            "Ссылка",
            "Дата",
            "Описание",
            "Текст",
            "",
        ]
        second_column = [
            "test",
            "test",
            "test",
            "01.01.197000:00",
            "test",
            "test",
            None,
        ]
        for result, first_col, second_col in zip(results, first_column, second_column):
            if result[0] == "-":
                continue
            result = result.replace(" ", "").split("|")
            assert result[1] == first_col, f"{result[1]} != {first_col}"
            assert result[2] == second_col, f"{result[2]} != {second_col}"

    async def test_format_population(self):
        renderer = Renderer(self.location)
        result = await renderer._format_population()
        assert result == "3"

    async def test_format_news_line(self):
        renderer = Renderer(self.location)
        result = await renderer._format_news_line("test", "test", 10, 10)
        assert result == ["|test      |      test|"]

    async def test_format_news_line_long(self):
        renderer = Renderer(self.location)
        result = await renderer._format_news_line("test", "test" * 10, 10, 10)
        assert len(result) == 4
        assert result == [
            "|test      |testtestte|",
            "|          |sttesttest|",
            "|          |testtestte|",
            "|          |sttesttest|",
        ]
