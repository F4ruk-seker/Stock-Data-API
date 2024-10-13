from dataclasses import dataclass


@dataclass
class OfferModel:
    name: str = ''
    code: str = ''
    logo: str = ''
    url: str = ''
    current_price: int = 0
    max_price: int = 0
    min_price: int = 0
    percentage: str = ''
    last_update: str = ''
    chart: str = ''
