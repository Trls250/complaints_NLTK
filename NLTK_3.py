#NLTK file 3

import pandas as pd
import numpy as np
import re
import nltk
import itertools
import collections

#the purpose of this script is to review the entire set of complaints and determine
#the most common words as well as their z-scores in order to remove outliers.
#before running:
#1. input the csv filename for the starting file and output file
#input filename will be the output filename of NLTK_2. Ensure these files are saved in the same directory as the python script
#2. the output filename is excel and will contain the outlier words that should be removed
# as they are too common or too infrequent
input_filename = ''
output_filename = ''
dir = os.getcwd()
print(dir)
full_input_path = os.path.join(dir,input_filename)
full_output_path = os.path.join(dir,output_filename)

#read input excel file into a pandas dataframe
#sheet name of the data must be "Sheet1"
df = pd.read_csv(full_input_path,
					encoding='latin-1'
					)
print(df.head())

#1 calculate word frequency
all_words = list(itertools.chain(df_1['important_text_clean']))

#2 count words
count_all_words = collections.Counter(all_words)
print(count_all_words)

#create dataframe for counts and calculate z-score of words to remove
WC_DF = pd.DataFrame.from_dict(count_all_words, orient='index',columns=['count']).reset_index()
print(WC_DF.head())

outliers = WC_DF[WC_DF['count'] > WC_DF['count'].mean() + 3 * WC_DF['count'].std()]

outliers.to_excel(output_filename)

print("done!")