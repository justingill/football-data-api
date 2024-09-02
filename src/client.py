import requests
from typing import Mapping, Any


class FootballDataClient:

    def __init__(self, api_key: str) -> None:
        self.base_url = "https://api.football-data.org/v4/"
        self.api_key = api_key

    def _create_auth_header(self):
        return {"X-Auth-Token": self.api_key}

    def get_areas_list(self) -> Mapping[str, Any]:
        response = requests.get(
            self.base_url + "/areas",
            headers=self._create_auth_header(),
        )
        if response.ok:
            return response.json()
        else:
            return ""

    def get_competitions_list(self):
        response = requests.get(
            self.base_url + "/competitions",
            headers=self._create_auth_header(),
        )
        if response.ok:
            return response.json()
        else:
            return ""

    def get_teams_list(self, limit: str = "100", offset: str = "100"):
        response = requests.get(
            self.base_url + f"/teams?limit={limit}&offset={offset}",
            headers=self._create_auth_header(),
        )
        if response.ok:
            return response.json()
        else:
            return ""

    def get_areas(self, area_id: str):
        response = requests.get(
            self.base_url + f"/areas/{area_id}",
            headers=self._create_auth_header(),
        )
        if response.ok:
            return response.json()
        else:
            return ""

    def get_competitions(self, competition_id: str):
        response = requests.get(
            self.base_url + f"/competitions/{competition_id}",
            headers=self._create_auth_header(),
        )
        if response.ok:
            return response.json()
        else:
            return ""

    def get_teams(self, team_id: str):
        response = requests.get(
            self.base_url + f"/teams/{team_id}",
            headers=self._create_auth_header(),
        )
        if response.ok:
            return response.json()
        else:
            return ""
