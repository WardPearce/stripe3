from .base import RouteBase


class BalanceRoute(RouteBase):
    get = "/balance"
    transactions = "/balance_transactions"
    list_transaction = "/balance_transactions/{}"


class ChargesRoute(RouteBase):
    create = "/charges"
    list = "/charges"
    capture = "/charges/{}/capture"
    get = "/v1/charges/{}"
    update = "/v1/charges/{}"


class CustomersRoute(RouteBase):
    create = "/customers"
    get = "/customers/{}"
    update = "/customers/{}"
    delete = "/customers/{}"
    list = "/customers"


class DisputesRoute(RouteBase):
    get = "/disputes/{}"
    update = "/disputes/{}"
    close = "/disputes/{}/close"
    list = "/disputes"


class EventsRoute(RouteBase):
    get = "/events/{}"
    list = "/events"


class FilesRoute(RouteBase):
    _create = "https://files.stripe.com/v1/files"
    get = "/files/{}"
    list = "/files"
