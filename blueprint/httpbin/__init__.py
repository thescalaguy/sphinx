from flask import Blueprint

httpbin = Blueprint("httpbin", __name__)

from . import post
