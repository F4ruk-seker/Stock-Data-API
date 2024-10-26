from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from typing import Dict, NoReturn, List, LiteralString, Any
from config.settings.base import DEFAULT_FROM_EMAIL
from logging import getLogger
from celery import shared_task


logger = getLogger(__name__)


@shared_task
def new_active_public_asset_alerts(user_mail: LiteralString, context: Dict[str, Any], subject: LiteralString) -> NoReturn:
    try:
        html_content = render_to_string('new_active_public_asset_alert.html', context)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(subject, text_content, DEFAULT_FROM_EMAIL, user_mail)
        email.attach_alternative(html_content, "text/html")
        email.send()
    except Exception as exception:
        logger.exception(exception)
