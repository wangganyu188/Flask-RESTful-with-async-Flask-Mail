import pytest
from webtest import TestApp

from app import create_app
from app.settings import DevConfig

_app = create_app(DevConfig)


@pytest.yield_fixture()
def app():
    ctx = _app.test_request_context()
    ctx.push()
    yield _app
    ctx.pop()


@pytest.fixture()
def testapp(app):
    return TestApp(app)
