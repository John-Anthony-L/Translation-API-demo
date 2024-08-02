import os
import sacrebleu
import bleu
import pandas as pd

def get_filename_without_extension(file_path):
  """
  Extracts the filename without extension from a given file path.

  Args: (str)
      file_path: The path to the file.

  Returns:
      The filename without extension.
  """
  base_name = os.path.basename(file_path)
  filename_without_ext = os.path.splitext(base_name)[0]
  return filename_without_ext

def get_sacreBLEU_score(df, ref_col, hyp_col):
  """
  returns the sacreBLEU score using language-agnostic character level tokenization

  Args:
    df: (pandas Dataframe)

    ref_col: (str)
        the reference translation column
    
    hyp_col: (str)
        the hypothesis [translation we want to evaluat] translation column
  
  Returns:
    (str)
  """
  return sacrebleu.corpus_bleu(df[ref_col].tolist(), [df[hyp_col].tolist()], tokenize = 'char')

def get_BLEU_score(df, ref_col, hyp_col):
    """
    returns the BLEU score

    Args:
        df: (pandas Dataframe)

        ref_col: (str)
            the reference translation column
        
        hyp_col: (str)
            the hypothesis [translation we want to evaluat] translation column
    
    Returns:
        (str)
    """
    return bleu.list_bleu(df[ref_col].tolist(), df[hyp_col].tolist())


def output_results(df, filename):
  """
  creates a CSV file with Spanish and Catalan BLEU scores using language agnostic character level tokenization

  Args:
    df: (pandas Dataframe)
      dataframe containing the reference and hypothesis translation

    filename: (str)
      the input file of what we wish to translate

  """

  results = {}
  results['Spanish'] = get_sacreBLEU_score(df, 'Spanish', 'Spanish_G_translate')
  results['Catalan'] = get_sacreBLEU_score(df, 'Catalan', 'Catalan_G_translate')

  new_file = get_filename_without_extension(filename)
  pd.DataFrame.from_dict(results.items()).rename(columns={0:'Language', 1:'BLEU score'}).to_csv(f'{new_file}_G_translated_metrics.csv', index=False)