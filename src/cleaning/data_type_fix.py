import pandas as pd
from src.utils.age_clean import clean_word_to_number

def fix_data_type(df):
   """
   Automatically applies suggested data types to known columns safely. Ignores missing columns
   :param df:
   :return: dataframe
   """

   int_cols = ['age', 'quantity', 'votes']
   for col in int_cols:
       if col in df.columns:
           if col == 'votes':
               df[col] = pd.to_numeric(df[col], errors="coerce").round().fillna(0).astype("Int64")
           elif col in ('age', 'quantity'):
               df[col] = df[col].str.strip().replace("", pd.NA, regex=True)
               df[col] = df[col].apply(clean_word_to_number)
               df[col] = df[col].fillna(df[col].median())
               df[col] = df[col].astype('Int64')




   float_cols = ['cholesterol', 'income', 'duration' 'price', 'score']
   for col in float_cols:
       if col in df.columns:
           if col == 'income':
               df[col] = df[col].str.strip().replace(r"[$]", "", regex=True)
               df[col] = pd.to_numeric(df[col], errors='coerce').astype('float64')
           else:
               df[col] = pd.to_numeric(df[col], errors='coerce').astype('float64')


           # df[col] = df[col].fillna(df[col].mean())


   datetime_cols = ['visit_date','date', 'release_year', 'last_restocked']
   for col in datetime_cols:
       if col in df.columns:
           df[col] = pd.to_datetime(df[col], errors='coerce', format='mixed')

   cat_cols = ['content_rating', 'condition']
   for col in cat_cols:
       if col in df.columns:
           df[col] = df[col].astype('category')


   str_cols = ['phone_number', 'email', 'blood_pressure']
   for col in str_cols:
       if col in df.columns:
           df[col] = df[col].astype(str).str.strip()

   return df