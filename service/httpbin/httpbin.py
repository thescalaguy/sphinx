import dataclasses as dc
import abc
import requests
from typing import Any


class _HttpBinRequest(abc.ABC):

    base_url: str = "https://httpbin.org"

    @abc.abstractmethod
    def execute(self) -> Any:
        raise NotImplemented


@dc.dataclass
class HttpBinPost(_HttpBinRequest):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Fusce laoreet lectus neque, in congue purus dapibus et.
    Sed eros elit, luctus ac ante eget, fermentum imperdiet urna.
    Integer rutrum leo sed quam faucibus rutrum. Suspendisse nulla diam, rhoncus id nisi et, aliquet auctor risus.
    In pellentesque, orci quis molestie dignissim, dui massa posuere lorem, ut suscipit orci libero quis sem.
    Etiam ullamcorper turpis at tempus semper.
    Nunc odio massa, feugiat quis sem nec, hendrerit pretium ex.
    Integer varius volutpat interdum.
    """

    params: dict[str, Any] = dc.field(default=dict)
    json: dict[str, Any] = dc.field(default=dict)

    def execute(self) -> Any:
        url = f"{self.base_url}/post"
        headers = {"Content-Type": "application/json"} if self.json else {}
        response = requests.post(
            url=url,
            json=self.json,
            params=self.params,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
