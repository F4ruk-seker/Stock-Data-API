from dataclasses import dataclass
from requests.auth import HTTPBasicAuth
import scrapers


@dataclass
class ApiTaskModel:
    url: str
    data_type: str  # json | dict
    auth: HTTPBasicAuth
    data: list | dict = [], {}
    success_codes: list[int] = 200,


@dataclass
class TaskModel:
    kwargs: dict
    scraper: scrapers
    api_task: ApiTaskModel
