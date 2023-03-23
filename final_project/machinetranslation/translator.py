"""
Module for translating from English to French and from French to English
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Translates the given text from English to French
    """
    french_text = language_translator.translate(english_text, model_id='en-fr') \
                    .get_result().get("translations")[0].get("translation")
    return french_text

def french_to_english(french_text):
    """
    Translates the given text from French to English
    """
    english_text = language_translator.translate(french_text, model_id='fr-en') \
                    .get_result().get("translations")[0].get("translation")
    return english_text
