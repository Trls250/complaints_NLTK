#NLTK file 5

import pandas as pd
import itertools
import collections
import matplotlib.pyplot as plt

#this file is used to create a visualization of the top words across all categorizations
#before running:
#1. input the csv filename for the starting file, will be the same output filename for NLTK_4. 
#Ensure this file is saved in the same directory as the python script

input_filename = ''
dir = os.getcwd()
print(dir)
full_input_path = os.path.join(dir,input_filename)

#read input csv file into a pandas dataframe
df_1 = pd.read_csv(full_input_path,
					encoding='latin-1'
					)
print(df_1.head())

#1. calculate word frequency

all_words = list(itertools.chain(df_1['important_text_clean']))

#2. count words
count_all_words = collections.Counter(all_words)
print(count_all_words)

#3. create df for most common count with two columns words and counts
count_all_words_df = pd.DataFrame(count_all_words.most_common(50),
									columns=['words','count'])

count_grouped = count_all_words_df.groupby(['words']).size()

#create visualization of top words across all categories

#create bar chart
fig, ax = plt.subplots(figsize=(20,20))
#plot horizontal bar graph
count_all_words_df.sort_values(by='count').plot.barh(x='words',
								y='count',
								ax=ax,
								color="purple"
								)
ax.set_title("Most Common Words across all Categories")

plt.show()