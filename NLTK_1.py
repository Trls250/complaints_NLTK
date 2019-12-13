#NLTK File One

import pandas as pd
import os
import itertools
import collections
import nltk
from collections import defaultdict
from nltk.corpus inmport stopwords
from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag, post_tag_sents
from nltk.stem import WordNetLemmatizer as wnl
from nltk.tag.perceptron import PerceptronTagger

#before running:
#input the excel filenames for the starting file formatted as per prerequesities and output file
#ensure these files are saved in the same directory as the python script
input_filename = ''
output_filename = ''
dir = os.getcwd()
print(dir)
full_input_path = os.path.join(dir,input_filename)
full_output_path = os.path.join(dir,output_filename)

tagger=PerceptronTagger()

#read input excel file into a pandas dataframe
#sheet name of the data must be "Sheet1"
#this lists columns A-F but can be updated according to your file
df = pd.read_excel(full_input_path,
					sheet_name = "Sheet1"
					usecols="A,B,C,D,E,F",
					encoding="latin-1"
					)
print(df.head())

#Clean and standardize the text for analysis
#1 standardize text as lowercase
#'TEXT' is the column name of the concatenate text to be analyzed
df['TEXT'] = df['TEXT'].str.lower()

#2 tokenize text and put into new column, remove punctuation
def identify_tokens(row):
	words = row['TEXT']
	tokens = nltk.word_tokenize(words)
	token_words = [w for w in tokens if w.isalpha()]
	return token_words

#run function and add into new column titled tokenized_text
df['tokenized_text'] = df.apply(identify_tokens, axis=1)

#3 create part of speech (pos) mapping function that converts pos tags (adjective, noun, etc)
# into values usable by the wordnet lemmatizer

def get_wordnet_pos(word):
	"""Map pos tag to first character lemmatize() acceps"""
	tag = tagger.tag([word])[0][1][0]
	tag_dict = {"J": wordnet.ADJ,
				"N": wordnet.NOUN,
				"V": wordnet.VERB,
				"R": wordnet.ADV}
	return tag_dict.get(tag, wordnet.NOUN)

#4 convert tokenized items with pos tags into standalone lemmatized words
def lemmatizer_list(row):
	lemmatizer = wnl()
	tokenized_words = row['tokenized_text']
	lemmatized_tokens = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in tokenized_words]
	return lemmatized_tokens

#run function and add into new column
df['lemmatized_pos_items'] = df.apply(lemmatizer_list, axis=1)

print(df['lemmatized_pos_items'].head())

#5 remove stopwords
stop_words = set(stopwords.words('english'))

def remove_stop_words(row):
	my_list = row['lemmatized_pos_items']
	important_text = [w for w in my_list if not w in stop_words]
	return(important_text)

#run function and add results into new column

df['important_text'] = df.apply(remove_stop_words, axis=1)
print(df['important_text'].head())

#save data into new file 
df.to_excel(full_output_path, encoding='latin-1', engine='xlsxwriter')
print("done!")