from httpx import BasicAuth, AsyncClient, Client


class Base:
    def __init__(self, api_key: str) -> None:
        """Used to interact with the Stripe API.

        Parameters
        ----------
        api_key : str
        """

        self._basic_auth = BasicAuth(
            username=api_key
        )


class Awaiting(Base):
    def __init__(self, *args, **kwargs) -> None:
        """Used to interact with the Stripe API.

        Parameters
        ----------
        api_key : str
        test_mode : bool, optional
            by default False
        """

        super().__init__(*args, **kwargs)

        self._client = AsyncClient(auth=self._basic_auth)


class Blocking(Base):
    def __init__(self, *args, **kwargs) -> None:
        """Used to interact with the Stripe API.

        Parameters
        ----------
        api_key : str
        test_mode : bool, optional
            by default False
        """

        super().__init__(*args, **kwargs)

        self._client = Client(auth=self._basic_auth)
