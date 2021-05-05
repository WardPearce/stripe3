from typing import Any, Dict, Generator, List


class SourceTypesModel:
    bank_account: int
    card: int

    def __init__(self, bank_account: int, card: int,
                 *args, **kwargs) -> None:
        self.bank_account = bank_account
        self.card = card


class ConnectReservedModel:
    amount: int
    currency: str

    def __init__(self, amount: int, currency: str,
                 *args, **kwargs) -> None:
        self.amount = amount
        self.currency = currency


class AmountModel(ConnectReservedModel):
    source_types: SourceTypesModel

    def __init__(self, source_types: SourceTypesModel,
                 *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.source_types = SourceTypesModel(**source_types)


class BalanceModel:
    livemode: bool

    def __init__(self, available: List[Dict[str, Any]],
                 connect_reserved: List[Dict[str, Any]],
                 livemode: bool, pending: List[Dict[str, Any]],
                 *args, **kwargs) -> None:
        self.livemode = livemode

        self.__available = available
        self.__pending = pending
        self.__connect_reserved = connect_reserved

    def available(self) -> Generator[AmountModel, None, None]:
        """
        Yields
        -------
        AmountModel
        """

        for available in self.__available:
            yield AmountModel(**available)

    def pending(self) -> Generator[AmountModel, None, None]:
        """
        Yields
        -------
        AmountModel
        """

        for pending in self.__pending:
            yield AmountModel(**pending)

    def connect_reserved(self) -> Generator[ConnectReservedModel, None, None]:
        """
        Yields
        -------
        ConnectReservedModel
        """

        for connect_reserved in self.__connect_reserved:
            yield ConnectReservedModel(**connect_reserved)
