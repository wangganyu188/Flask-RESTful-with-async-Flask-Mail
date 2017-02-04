import mock
from utils import async_task
import threading


@mock.patch.object(threading.Thread, 'start', autospec=True)
def test_async_task_runs_thread(mock_start):

    @async_task
    def long_running_job():
        return True

    long_running_job()
    assert mock_start.called

