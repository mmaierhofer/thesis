from requests import get
from matplotlib import pyplot as plt

API_KEY = "UY22CZ2I6I49ZY5J5F7A6KF9I14TIK4J43"

BASE_URL = "https://api.etherscan.io/api"

address = "0x8f56682a50becb1df2fb8136954f2062871bc7fc"


def make_api_url(module, action, address, **kwargs):
    url = BASE_URL + \
        f"?module={module}&action={action}&address={address}&apikey={API_KEY}"

    for key, value in kwargs.items():
        url += f"&{key}={value}"

    return url


get_balance_url = make_api_url("account", "balance", address, tag="latest")

response = get(get_balance_url)
data = response.json()

print(data)
