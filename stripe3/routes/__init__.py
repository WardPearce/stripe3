from re import sub

from .core import (
    BalanceRoute,
    ChargesRoute,
    CustomersRoute,
    DisputesRoute,
    EventsRoute,
    FilesRoute,
    FileLinksRoute,
    MandatesRoute,
    PaymentIntentsRoute,
    SetupIntentsRoute,
    SetupAttemptsRoute,
    PayoutsRoute,
    ProductsRoute,
    PricesRoute,
    RefundsRoute,
    TokensRoute
)

from .payment_methods import (
    PaymentMethodsRoute,
    BankAccountsRoute,
    CardsRoute,
    SourcesRoute,
    SourcesCustomer
)

from .sessions import SessionsRoute


ROUTES = [
    BalanceRoute,
    ChargesRoute,
    CustomersRoute,
    DisputesRoute,
    EventsRoute,
    FilesRoute,
    FileLinksRoute,
    MandatesRoute,
    PaymentIntentsRoute,
    SetupIntentsRoute,
    SetupAttemptsRoute,
    PayoutsRoute,
    ProductsRoute,
    PricesRoute,
    RefundsRoute,
    TokensRoute,
    PaymentMethodsRoute,
    BankAccountsRoute,
    CardsRoute,
    SourcesRoute,
    SourcesCustomer,
    SessionsRoute
]


for route in ROUTES:
    route = route()

    var_name = sub(
        "([A-Z][a-z]+)",
        r" \1", sub("([A-Z]+)",
        r" \1", route.__class__.__name__  # noqa: E128
    )).split()  # noqa: E124

    route.format()

    globals()["_".join(var_name).upper()] = route
