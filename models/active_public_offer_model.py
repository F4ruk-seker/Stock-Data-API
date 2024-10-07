from dataclasses import dataclass


@dataclass
class ActivePublicOfferingModel:
    title: str
    url: str | None
    detail: dict

