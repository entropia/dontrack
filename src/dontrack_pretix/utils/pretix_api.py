from typing import Optional

from requests import get


class PretixApiClient:
    def __init__(self, root_url: str, organizer: str, event: str, api_key: str):
        self.api_base = f'{root_url}/api/v1/organizers/{organizer}/events/{event}'
        self.api_key = api_key

    def call_pretix_api(self, endpoint: str, params: Optional[dict] = None) -> dict:
        api_url = f'{self.api_base}/{endpoint}'
        r = get(api_url, headers={'Authorization': self.api_key}, params=params)
        r.raise_for_status()
        return r.json()


    def get_products_in_quota(self, quota_name: str) -> Optional[list]:
        quotas = self.call_pretix_api('quotas').get('results', [])
        for quota in quotas:
            if quota['name'] == quota_name:
                return quota.get('items', [])
        return None


    def get_orderpositions(self, query: dict) -> list:
        return self.call_pretix_api('orderpositions', params=query).get('results', [])
