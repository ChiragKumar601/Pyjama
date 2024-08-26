from celery import shared_task
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_email_task(subject, message, recipient_list, from_email=None, fail_silently=False):
    try:
        logger.info(f"Sending email to {recipient_list} with subject '{subject}'.")
        
        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=fail_silently
        )
        
        logger.info(f"Email sent successfully to {recipient_list}.")
    except Exception as e:
        logger.error(f"Failed to send email to {recipient_list}. Error: {e}")

    logger.debug("Exiting the send email task.")
