"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import operationtype as shared_operationtype
from typing import Optional


@dataclasses.dataclass
class CalculateRequest:
    operation: shared_operationtype.OperationType = dataclasses.field(metadata={'path_param': { 'field_name': 'operation', 'style': 'simple', 'explode': False }})
    r"""The operator to apply on the variables"""
    x: float = dataclasses.field(metadata={'query_param': { 'field_name': 'x', 'style': 'form', 'explode': True }})
    r"""The LHS value"""
    y: float = dataclasses.field(metadata={'query_param': { 'field_name': 'y', 'style': 'form', 'explode': True }})
    r"""The RHS value"""
    



@dataclasses.dataclass
class CalculateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    res: Optional[str] = dataclasses.field(default=None)
    

