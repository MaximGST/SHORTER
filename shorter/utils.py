import uuid
import string

from django.conf import settings

def generate_random_string(string_length = 5):
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace("-","")
    return random[0:string_length]

def get_full_url(code):
    return f'{settings.SITE_URL}{code}'


