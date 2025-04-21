from .settings import OAUTH_ADMIN_GROUP
from .settings import OAUTH_STAFF_GROUP


staff_permissions = [
    'donations.register_donation',
]

admin_permissions = [
    'donations.list_donations',
    'log.view_log'
]

permissions = {
    OAUTH_STAFF_GROUP: staff_permissions,
    OAUTH_ADMIN_GROUP: staff_permissions + admin_permissions,
}
