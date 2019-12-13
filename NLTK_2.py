#NLTK File Two

import pandas as pd
import re
import nltk
import itertools
import collections

#the purpose of this script is to perform one-time cleanup and standardization
#for further analysis. It is meant to be run after NLTK_1
#before running:
#1. input the excel filenames for the starting file and output file
#input filename will be the output filename of NLTK_1
#ensure these files are saved in the same directory as the python script
#2. input headers on line 54
input_filename = ''
output_filename = ''
dir = os.getcwd()
print(dir)
full_input_path = os.path.join(dir,input_filename)
full_output_path = os.path.join(dir,output_filename)

#read input excel file into a pandas dataframe
#sheet name of the data must be "Sheet1"
df = pd.read_excel(full_input_path,
					sheet_name = "Sheet1",
					encoding="latin-1"
					)
print(df.head())

#further cleanup and standardize data for analysis
s = (df.important_text.str.split(expand=True).stack())
s.index = s.index.droplevel(-1)
s.name = 'important_text'

#remove old column important_text
df = df.drop(['important_text'], axis=1)
df_1 = (df.join(s))

print(df_1)

#remove non-alpha characters from text
def clean_text(row):
	text = row['important_text']
	text = re.sub("[^a-zA-Z", "", str(text))
	return(text)

#apply the function and add a new column for text with non-alpha characters
df_1['important_text_clean'] = df_1.apply(clean_text, axis=1)

#input the column headers in format ["column 1", "column 2"] etc.
#final column name should be "important_text_clean"
headers = [] 

#write to csv
df_1.to_csv('full_output_path', columns = headers)

print(df_1.head())

print("done!")
