from django.shortcuts import render
from django.http import HttpResponse
from recipe.models import Recipe
from users.models import CustomUser
from .tasks import send_email_task
import logging
from celery import shared_task

from config.settings import base

# Configure logger
logger = logging.getLogger(__name__)

EMAIL_HOST_USER = base.EMAIL_HOST_USER


@shared_task
def send_email_view(request):
    user_email_messages = {}
    users = CustomUser.objects.all()
    
  
    try:
        logger.info(f"Found {users.count()} users.")

        for user in users:
            
            user_recipes = Recipe.objects.filter(author=user)

            if not user_recipes.exists():
                logger.info(f"No recipes found for user {user.username}.")
                continue

            message = f"Dear {user.username},\n\n"
            message += "Here is a summary of the likes you have received on your recipes:\n\n"
            
            for recipe in user_recipes:
                logger.info(f"Recipe is:{recipe} which is made by {user.username}")
                recipe_likes = recipe.get_total_number_of_likes()
                message += f"Recipe: {recipe.title}\n"
                message += f"Likes: {recipe_likes}\n\n"

            message += "Thank you for using our service!\n\n"
            message += "Best regards,\nYour Recipe App Team"

            user_email_messages[user.email] = message
        
        # Send emails asynchronously using Celery
        for email, message in user_email_messages.items():
            logger.info(f"Sending email to {email}.")
            send_email_task.delay(
                subject="Your Recipe Likes Summary",
                message=message,
                recipient_list=[email],
                from_email=EMAIL_HOST_USER,
            )
            

        logger.info(f'Emails sent asynchronously! Total users notified: {len(user_email_messages)}.')

        return HttpResponse(f'Emails sent asynchronously! Total users notified: {len(user_email_messages)}')

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return HttpResponse("An error occurred while sending emails.", status=500)
