from .base import RouteBase


class BalanceRoute(RouteBase):
    get = "/balance"
    transactions = "/balance_transactions"
    list_transaction = "/balance_transactions/{}"


class ChargesRoute(RouteBase):
    _prefix = "/charges"

    create = ""
    list = ""
    capture = "/{}/capture"
    get = "/{}"
    update = "/{}"


class CustomersRoute(RouteBase):
    _prefix = "/customers"

    create = ""
    get = "/{}"
    update = "/{}"
    delete = "/{}"
    list = ""


class DisputesRoute(RouteBase):
    _prefix = "/disputes"

    get = "/{}"
    update = "/{}"
    close = "/{}/close"
    list = "/"


class EventsRoute(RouteBase):
    _prefix = "/events"

    get = "/{}"
    list = ""


class FilesRoute(RouteBase):
    _prefix = "/files"

    _create = "https://files.stripe.com/v1/files"

    get = "/{}"
    list = ""


class FileLinksRoute(RouteBase):
    _prefix = "/file_links"

    post = ""
    id = "/{}"


class MandatesRoute(RouteBase):
    get = "/mandates/{}"


class PaymentIntentsRoute(RouteBase):
    _prefix = "/payment_intents"

    id = "/{}"
    confirm = "/{}/confirm"
    capture = "/{}/capture"
    cancel = "/{}/cancel"
    post = ""
    get = ""


class SetupIntentsRoute(RouteBase):
    _prefix = "/setup_intents"

    id = "/{}"
    confirm = "/{}/confirm"
    cancel = "/{}/cancel"

    get = ""
    post = ""


class SetupAttemptsRoute(RouteBase):
    get = "/setup_attempts"


class PayoutsRoute(RouteBase):
    _prefix = "/payouts"

    id = "/{}"
    cancel = "/{}/cancel"
    reverse = "/{}/reverse"


class ProductsRoute(RouteBase):
    _prefix = "/products"

    id = "/{}"
    post = ""
    get = ""


class PricesRoute(RouteBase):
    _prefix = "/prices"

    id = "/{}"
    get = ""
    post = ""


class RefundsRoute(RouteBase):
    _prefix = "/refunds"

    id = "/{}"
    get = ""
    post = ""


class TokensRoute(RouteBase):
    _prefix = "/tokens"

    post = ""
    get = "/{}"
