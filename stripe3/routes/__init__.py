from .core import (
    BalanceRoute,
    ChargesRoute,
    CustomersRoute,
    DisputesRoute,
    EventsRoute,
    FilesRoute
)


BALANCE_ROUTE = BalanceRoute()
CHARGES_ROUTE = ChargesRoute()
CUSTOMERS_ROUTE = CustomersRoute()
DISPUTES_ROUTE = DisputesRoute()
EVENTS_ROUTE = EventsRoute()
FILES_ROUTE = FilesRoute()


ROUTES = [
    BALANCE_ROUTE,
    CHARGES_ROUTE,
    CUSTOMERS_ROUTE,
    DISPUTES_ROUTE,
    EVENTS_ROUTE,
    FILES_ROUTE
]

for route in ROUTES:
    route.format()
