from dataclasses import dataclass


@dataclass(frozen=True)
class Authentication:
    """How a request to the proxy server is authenticated."""

    api_key: str