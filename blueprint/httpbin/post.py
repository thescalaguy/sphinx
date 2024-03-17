import time

from blueprint.httpbin import httpbin
from service.httpbin import HttpBinPost


@httpbin.post("/post")
def post():
    params = {"foo": "bar"}
    json = {"foo": "bar"}
    request = HttpBinPost(params=params, json=json)
    time.sleep(0.5)
    return request.execute()
