class RouteBase:
    _ran = False
    _prefix = None

    def __init__(self, route: str = "https://api.stripe.com/v1") -> None:
        """Used for formatting route objects.

        Parameters
        ----------
        route : str, optional
            URL of API, by default "https://api.stripe.com"
        """

        self.route = route

    def format(self) -> None:
        """Used to format URL.
        """

        if self._ran:
            return

        routes = [
            attr for attr in dir(self.__class__)
            if not callable(getattr(self.__class__, attr))
            and not attr.startswith("__")
            and not attr.startswith("_")
        ]

        for var_name in routes:
            value = "{}{}/{}".format(
                self.route,
                "/" + self._prefix if self._prefix else "",
                getattr(
                    self,
                    var_name
                )
            )

            if value[-1:] == "/":
                value = value[:-1]

            setattr(
                self,
                var_name,
                value
            )
