from .base import RouteBase


class PaymentMethodsRoute(RouteBase):
    _prefix = "/payment_methods"

    get = "/{}"
    post = "/{}"
    attach = "/{}/attach"
    detach = "/{}/detach"


class BankAccountsRoute(RouteBase):
    _prefix = "/customers/{}/sources"

    get = "/{}"
    post = "/{}"
    verify = "/{}/verify"
    delete = "/{}"
    list = "?object=bank_account"


class CardsRoute(RouteBase):
    _prefix = "/customers/{}/sources"

    get = "/{}"
    post = ""
    update = "/{}"
    delete = "/{}"
    list = "?object=card"


class SourcesRoute(RouteBase):
    _prefix = "sources"

    get = "/{}"
    post = "/{}"


class SourcesCustomer(RouteBase):
    _prefix = "/customers/{}/sources"

    post = ""
    delete = "/{}"
