"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests
from dataclasses import dataclass
from typing import Dict, Tuple
from .utils.retries import RetryConfig
from .utils import utils


SERVERS = [
    'https://examples.apimatic.io/apps/calculator',
    # This environment connect to the LIVE calculator API
]
"""Contains the list of servers available to the SDK"""

@dataclass
class SDKConfiguration:
    client: requests.Session
    server_url: str = ''
    server_idx: int = 0
    language: str = 'python'
    openapi_doc_version: str = '1.0'
    sdk_version: str = '0.11.0'
    gen_version: str = '2.248.1'
    user_agent: str = 'speakeasy-sdk/python 0.11.0 2.248.1 1.0 calculator'
    retry_config: RetryConfig = None

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url:
            return utils.remove_suffix(self.server_url, '/'), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], {}
