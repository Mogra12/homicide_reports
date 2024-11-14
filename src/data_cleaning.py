import pandas as pd
import shutil


# read the dataset
df = pd.read_csv('/home/mogra/Desktop/Projetos python/Data_Science/Projetos-Portifolio/homicide_reports/data/database.csv', low_memory=False)
pd.set_option('display.max_columns', None)


# drop missing data
def missingdata_cleaner():
      df['Perpetrator Age'].replace('Unknow', '0')
      df['Perpetrator Age'] = pd.to_numeric(df['Perpetrator Age'], errors='coerce')
      df['Perpetrator Age'].fillna(0).astype(int)
      df['Perpetrator Age'] = df['Perpetrator Age'].replace([float('inf'), -float('inf')], 0).fillna(0).astype(int)
      df.drop(df[df['Perpetrator Age'] == 0].index, inplace=True)


def drop_colunmns():
      #cleaning columns
      df.drop(['Record ID'], axis=1, inplace=True)


def db_constructor():
      # create the cleaned database
      df.to_csv('clean_database.csv')
      # move the database to data folder
      shutil.move('clean_database.csv','data')


missingdata_cleaner()
drop_colunmns()
db_constructor()
