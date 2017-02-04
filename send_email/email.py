from flask_mail import Message

from app import app
from app import mail
from utils.decorators import async_task


def send_email(subject, sender, recipients, text_body, html_body=None, **kwargs):
    app.logger.info("send_email(subject='{subject}', recipients=['{recp}'], text_body='{txt}')".format(sender=sender, subject=subject, recp=recipients, txt=text_body))
    msg = Message(subject, sender=sender, recipients=recipients, **kwargs)
    msg.body = text_body
    msg.html = html_body

    app.logger.info("Message(to=[{m.recipients}], from='{m.sender}')".format(m=msg))
    _send_async_email(app, msg)


@async_task
def _send_async_email(flask_app, msg):
    """ Sends an send_email asynchronously
    Args:
        flask_app (flask.Flask): Current flask instance
        msg (Message): Message to send
    Returns:
        None
    """
    with flask_app.app_context():
        mail.send(msg)
