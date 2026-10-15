"""Pushes orders to a (fake) partner API. INTENTIONALLY INSECURE: TLS verification is off."""
import requests

PARTNER_URL = "https://partner.example.com/api/orders"


def push(order: dict) -> int:
    return requests.post(PARTNER_URL, json=order, timeout=10, verify=True).status_code
