from .base import RouteBase


class SessionsRoute(RouteBase):
    _prefix = "/checkout/sessions"

    get = "/{}"
    list = ""
    items = "/{}/line_items"
    create = ""
