from send_email import send_email
import threading
import mock


@mock.patch.object(threading.Thread, 'start', autospec=True)
def test_send_message(mock_start):
    send_email(sender='from@', subject='sub', recipients=['name@send_email.com'], text_body='Hi', html_body=None)
    assert mock_start.called
