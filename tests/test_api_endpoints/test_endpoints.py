import mock
import threading


def test_get_index(testapp):
    resp = testapp.get('/')
    assert resp and resp.status_code == 200


@mock.patch.object(threading.Thread, 'start', autospec=True)  # comment out to send emails during tests
def test_send_email(mock_start, testapp):
    response = testapp.get("/0.1/send_email/?recipients=['example@email.com']")
    assert response.status_code == 200 and mock_start.called
