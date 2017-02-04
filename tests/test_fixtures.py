from flask import Flask


def test_create_app_fixture(app):
    assert app and isinstance(app, Flask)


def test_create_testapp_fixture(testapp):
    assert testapp
