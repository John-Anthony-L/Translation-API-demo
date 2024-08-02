import sys
import pandas as pd
from translation_API import translation_API
from constants import *
import helper

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please provide a file name as an argument.")
    else:
        file_path = sys.argv[1]
        to_translate_df = pd.read_excel(file_path)

        translate_api = translation_API()
        for lang in SUPPORTED_LANGS[1:]:
            print(f"translating into {LANGUAGE_CODES[lang]}")
            to_translate_df = translate_api.translate_in_chunks(to_translate_df, lang)

        out_file = f'{helper.get_filename_without_extension(file_path)}_G_translated_full.xlsx'
        
        to_translate_df.to_excel(out_file)
        print(f'{out_file} generated')

        # now comparing and saving results, assuming we have Spanish and Catalan
        helper.output_results(to_translate_df, file_path)