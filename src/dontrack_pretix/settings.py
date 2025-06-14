try:
    from . import local_settings  # type: ignore
except (ImportError, ModuleNotFoundError):
    local_settings = None

PRETIX_ROOT_URL: str = getattr(local_settings, 'PRETIX_ROOT_URL', 'https://pretix.eu')
PRETIX_API_KEYS: dict = getattr(local_settings, 'PRETIX_API_KEYS', {})
PRETIX_DONATION_QUOTA: str = getattr(local_settings, 'PRETIX_DONATION_QUOTA', 'DONATION')