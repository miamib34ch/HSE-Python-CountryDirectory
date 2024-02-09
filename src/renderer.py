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

        return (
            f"Страна: {self.location_info.location.name}",
            f"Столица: {self.location_info.location.capital}",
            f"Регион: {self.location_info.location.subregion}",
            f"Языки: {await self._format_languages()}",
            f"Население страны: {await self._format_population()} чел.",
            f"Курсы валют: {await self._format_currency_rates()}",
            f"Погода: {self.location_info.weather.temp} °C",
            f"Площадь: {self.location_info.location.area}",
            f"Широта столицы: {self.location_info.location.latitude}",
            f"Долгота столицы: {self.location_info.location.longitude}",
        )

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
