from google.cloud import translate_v3 as translate
import pandas as pd
from bleu import list_bleu
import sacrebleu
from constants import *

class translation_API:
    def __init__(self, project_id = PROJECT_ID, location = LOCATION):
        # Google Cloud project ID
        self.project_id = project_id

        # Create a Translation client
        self.client = translate.TranslationServiceClient()

        # location where machine is located
        self.location = location

        # Construct the parent resource
        self.parent = f"projects/{project_id}/locations/{location}"


        self.LANGUAGE_CODES = LANGUAGE_CODES

    def translate_text(self, text, target_language = 'es', source_language = 'en'):
        """
        Translates text using Google Cloud Translation v3.
        
        Args: 
            text: (str)
                the text to translate into target langauge, English is expected
            target_langage: (str)
                the target_language we are translating into text, see SUPPORTED_LANGS to see supported languages
                default value = 'es' - Spanish
            source_language: (str)
                the source language we are generating our translations from
                defualt value = 'en' - English
        
        Returns:
            type: (str)
            The translated text.
        """
        
        response = self.client.translate_text(
            request={
                "parent": self.parent,
                "contents": [text],
                "mime_type": "text/plain",
                # MIME type of the input text
                "source_language_code": source_language,  # assuming English source language
                "target_language_code": target_language,
            }
        )
        # Extract the translated text from the response
        translated_text = response.translations[0].translated_text

        return translated_text
    

    def translate_in_chunks(self, df, target_language , chunk_size=100):
        """
        Applies a function to a DataFrame column in chunks to manage API calls.

        Args:
            df: (Pandas DataFrame)
                A dataframe with a column of english source dialouge/scripts
            target_language: (string)
                The language code of the language you would like to translate into
                must be a valid language code
            chunk_size: (int)
                The number of rows to process in each chunk.

        Returns:
            type: (pandas Dataframe)
            The DataFrame with the translated column in the target language.
        """

        if target_language not in self.LANGUAGE_CODES:
            print('INVALID LANGUAGE CODE')
            print(f"{target_language} IS NOT A SUPPORTED LANGUAGE, please look at SUPPORTED_LANGS to see all currently supported languges")
            return df
        
        trans_column_name = f'{self.LANGUAGE_CODES[target_language]}_G_translate'
        processed_data = []
        for i in range(0, len(df), chunk_size):
            chunk = df.iloc[i : i + chunk_size].copy()
            processed_chunk = chunk['English'].apply(lambda x: self.translate_text(x, target_language)).tolist()
            chunk[trans_column_name] = processed_chunk
            processed_data.append(chunk)
            # should save to checkpoints within a file then gives last one as a full instance

        translated_df = pd.concat(processed_data)
        return translated_df