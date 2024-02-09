"""
Функции для формирования выходной информации.
"""

from decimal import ROUND_HALF_UP, Decimal

from collectors.models import LocationInfoDTO


class Renderer:
    """
    Генерация результата преобразования прочитанных данных.
    """

    def __init__(self, location_info: LocationInfoDTO) -> None:
        """
        Конструктор.

        :param location_info: Данные о географическом месте.
        """

        self.location_info = location_info

    async def render(self) -> tuple[str, ...]:
        """
        Форматирование прочитанных данных.

        :return: Результат форматирования
        """

        values = {
            "Страна": self.location_info.location.name,
            "Столица": self.location_info.location.capital,
            "Регион": self.location_info.location.subregion,
            "Языки": await self._format_languages(),
            "Население страны": await self._format_population(),
            "Курсы валют": await self._format_currency_rates(),

            "Площадь страны": self.location_info.location.area,
            "Широта": self.location_info.location.latitude,
            "Долгота": self.location_info.location.longitude,

            "Погода": self.location_info.weather.temp,
            "Время": self.location_info.weather.dt.strftime("%d.%m.%Y %H:%M"),
            "Часовой пояс": self.location_info.weather.timezone,
            "Описание погоды": self.location_info.weather.description,
            "Видимость": self.location_info.weather.visibility,
            "Влажность": self.location_info.weather.humidity,
            "Скорость ветра": self.location_info.weather.wind_speed,
            "Давление": self.location_info.weather.pressure,
        }

        first_column_width = max(len(key) for key in values) + 1
        second_column_width = max(len(str(value)) for value in values.values()) + 1
        formatted_values = [("-" * (first_column_width + second_column_width + 3))]
        formatted_values.extend(
            [
                f"|{key:<{first_column_width}}|{value:>{second_column_width}}|"
                for key, value in values.items()
            ]
        )
        formatted_values.append("-" * (first_column_width + second_column_width + 3))

        return tuple(formatted_values)

    async def _format_languages(self) -> str:
        """
        Форматирование информации о языках.

        :return:
        """

        return ", ".join(
            f"{item.name} ({item.native_name})"
            for item in self.location_info.location.languages
        )

    async def _format_population(self) -> str:
        """
        Форматирование информации о населении.

        :return:
        """

        # pylint: disable=C0209
        return "{:,}".format(self.location_info.location.population).replace(",", ".")

    async def _format_currency_rates(self) -> str:
        """
        Форматирование информации о курсах валют.

        :return:
        """

        return ", ".join(
            f"{currency} = {Decimal(rates).quantize(exp=Decimal('.01'), rounding=ROUND_HALF_UP)} руб."
            for currency, rates in self.location_info.currency_rates.items()
        )
