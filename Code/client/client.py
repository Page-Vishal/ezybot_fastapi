import os
from groq import Groq

api_key = os.getenv('GROQ_API_KEY')

client = Groq()