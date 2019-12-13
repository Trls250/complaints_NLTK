#NLTK file 4

import pandas as pd

#the purpose of this file is to remove the words in NLTK_3
#that are too common or too infrequent
#before running:
#1. input the csv filename for the starting file formatted and output file
#input filename will be the same as input filename as NLTK_3. Ensure these files are saved in the same directory as the python script
#2. word_remove_list is the name of the excel file that contains the list of words to remove in column A.
#3. the output filename is csv and will need to have the headers input
#input headers on line 51
# as they are too common or too infrequent


input_filename = ''
word_remove_list = ''
output_filename = ''
dir = os.getcwd()
print(dir)
full_input_path = os.path.join(dir,input_filename)
full_output_path = os.path.join(dir,output_filename)

#read input csv file into a pandas dataframe
df_1 = pd.read_csv(full_input_path,
					encoding='latin-1'
					)
print(df_1.head())

#load list of words to remove
df_2 = pd.read_excel(word_remove_list,
					sheet_name="Sheet1",
					usecols="A",
					encoding='latin-1'
					)

to_remove = df_2['Word'].values.tolist()
print(to_remove)

#create new dataframe that has the words removed
df_3 = df_1[~df_1['important_text_clean'].isin(to_remove)]

print(df_3.head())

#input the column headers in format ["column 1", "column 2"] etc.
#final column name should be "important_text_clean"
headers = [] 

df_3.to_csv(full_output_path, columns = headers)

print("done!")