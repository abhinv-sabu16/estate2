# import random
# from django.core.mail import send_mail
# from django.conf import settings

# def generate_otp():
#     return str(random.randint(100000, 999999))

# def send_otp_email(email, otp):
#     subject = 'Your OTP Verification Code'
#     message = f'Your OTP code is: {otp}'
#     send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from difflib import get_close_matches

nltk.download("punkt_tab")
nltk.download("stopwords")

responses = {
    "hi": "Hello! How can I assist you?",
    "hello": "Hi there! Need any help?",
    "how are you": "I'm just a bot, but I'm doing great!",
    "what is your name": "I'm a chatbot!",
    "can i buy places":"of couser you can"
}

# Preprocess user input
def clean_text(text):
    words = word_tokenize(text.lower())  # Convert to lowercase & tokenize
    words = [word for word in words if word.isalnum()]  # Remove punctuation
    return " ".join(words)

def get_response(user_message):
    user_message = clean_text(user_message)

    # Find the closest matching response
    match = get_close_matches(user_message, responses.keys(), n=1, cutoff=0.6)

    if match:
        return responses[match[0]]  # Return the best match

    return "Sorry, I didn't understand that."
