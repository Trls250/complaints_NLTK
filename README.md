# Complaints_NLTK
Cleanup, analysis, and visualization for categorized text using python and the natural language toolkit (NLTK).

A set of python scripts to cleanup, analyze and visualize categorized freeformat text. This was initially created to analyze customer complaints but it can be used for analysis around a number of text applications such as tweets, blog posts, feedback forms, emails, articles etc.

## Prerequisites
Prior to running the python scripts please ensure your python library is setup with the correct modules, input data is in the correct format and has been cleaned of invalid characters that might cause processing issues.

### Python Libraries
Ensure you are running Python 3 with pandas, nltk (and all supporting packages installed https://www.nltk.org/data.html), collections, itertools, and matplotlib for visualization.

### Terminology and Concepts Utilized
These instructions assume familiarity with natural language terminology and basic statistics. If these are new concepts there is plenty of reference material available around terms including word tokenization, lemmatization, part-of-speech tagging, stop word removal, standard deviation, and z-score. 

### Data Input File
The input file is required to be an Excel xlsx file with at least two columns of information in a (1) data column and (2) free text field, such as:

| Category  | Text |
| ------------- | ------------- |
| Category 1  | Free text goes here  |
| Category 2  | Free text goes here  |

For analyzing complaints this might look something like this:

| Complaint Category  | Complaint Text |
| ------------- | ------------- |
| Email  | I'm unhappy about my bill  |
| Phone  | I haven't received my bill  |

### Remove Invalid Characters
Its necessary to remove invalid characters from the data to avoid data processing issues. I initially used the CLEAN function in Excel but found it didn't catch all characters. Instead I used the following function to highlight potential fields that might cause issues (B2 is the first cell with free text):

`=SUMPRODUCT(SEARCH(MID(B2,ROW(INDIRECT("1:"&LEN(B2))),1),"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890!@#$%^&*()-+=.,:/\'"""))`

## Overview of files
### Cleanup

Files 1-2 are meant to be run one-time to cleanup and standardize data for analysis

**NLTK 1**

  Load initial data, standardize items to lowercase, tokenize words, POS tag, lemmatize.

**NLTK 2**

  Format dataframe after lemmatization and create dataframe of individual words for analysis.

### Analyze

  Determine word counts and remove outlier words that occur too frequently or infrequently.

**NLTK 3**

Identify words for removal by calculating z-scores aggregated by word. This script creates an Excel extract of this information that is reviewed offline to confirm the words are OK for removal.

**NLTK 4**

Remove words from the dataset that are three or more standard deviations away from the mean.

### Visualize

Create graphics structured around the core words using Matplotlib 

**NLTK 5**

Visualize word counts across all categories

**NLTK 6**

Visualize word counts by categorization
