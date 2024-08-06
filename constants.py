
PROJECT_ID = '###ADD YOUR PROJECT ID###'

LOCATION = '###ADD YOUR LOCATION###'

# to be clear this is only the languages that were asked for, not an exaustive list of 
# langauges that google translation API supports
SUPPORTED_LANGS = ['en', 'fr', 'it', 'de', 'es', 'ca', 'ja', 'zh', 'ko', 'pt-BR']

# NOTE:
# here is some tech debt that will def bite if this is ever expanded on
# we want to use the language codes but we also want columns to be the full name of the langauge
# this is just for clarity in the demo and should be ammended if this ever goes near production
LANGUAGE_CODES = {
            'en': 'English',
            'fr': 'French',
            'it': 'Italian',
            'de': 'German',
            'es': 'Spanish',
            'ca': 'Catalan',
            'ja': 'Japanese',
            'zh': 'Chinese',  # Note: This is simplified Chinese.
            'ko': 'Korean',
            'pt-BR': 'Brazilian Portuguese'  # Note the specific code for Brazilian Portuguese
        }
