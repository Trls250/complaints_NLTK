#NLTK file 6
import pandas as pd
import nltk
import itertools
import collections
import matplotlib.pyplot as plt

print(nltk.__file__)

#this file is used to create a visualization of the top words by categorizations
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

#the CAT field is a placeholder value for the category column
#needs to be updated to appropriate column
count_series = df_1.groupby(['CAT', 'important_text_clean']).size()

#create dataframe with count column
df_2 = count_series.to_frame(name = 'count').reset_index()

#create dataframe with 25 largest word counts by category
#25 can be adjusted to whichever count is most appropriate
df_3 = df_2.set_index(['important_text_clean']).groupby('CAT')['count'].nlargest(25).reset_index()
print(df_3.head())

#create visualization
plt.figure(figsize=(10,10), facecolor='white')

plot_number = 1

for category, selection in df_3.groupby("CAT"):
	ax = plt.subplot(11,3, plot_number)
	selection.plot(kind='barh',
						x='important_text_clean',
						y='count',
						ax=ax,
						label=category,
						color="purple",
						figsize=(30,40))
	ax.set_title(category)
	plot_number = plot_number + 1
plt.tight_layout()