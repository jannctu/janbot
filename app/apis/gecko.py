import requests

from app.dto.gecko.gecko import GeckoPingOutput


class GeckoApi:
    def __init__(
            self
    ) -> None:
        self.api_url = "https://api.coingecko.com/api/v3"

    def ping(self) -> GeckoPingOutput:
        target_url = self.api_url + "/ping"

        response = requests.get(target_url)
        return GeckoPingOutput(**response.json())

    def get_current_price(self, codename, currency="usd"):
        target_url = self.api_url + "/simple/price"
        response = requests.get(target_url, params={"ids": codename, "vs_currencies": currency})
        return response.json()
