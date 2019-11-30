# complaints_NLTK
NLTK cleanup, analysis, and visualization for categorized text using python.

A set of python scripts that are used to cleanup, analyze and visualize freeformat text organized in categorizations. This is a modification I did of project to analyze customer complaints but it can be modified for use where there is any general categorization around a set of text such as tweets, blog posts, general feedback, etc.

## Prerequisites
Prior to running these python scripts please ensure the input data is in the correct input format and has been cleaned

### Python Libraries
Ensure you are running Python 3 with pandas, nltk (with all packages installed), collections, itertools, and matplotlib.

### NLTK Terminology and Concepts
This assumes familiarity with Natural Language processing terminology and basic statistics. Terms specific to Natural Language include word tokenization, lemmatizing, Point of Speech Tagging, stop words, standard deviation, and z-score. Visualization utilizes the matplotlib library. Documentation for this information is available elsewhere.

### Data Input File
The input data is required to be an Excel xlsx file with at least two columns of categorized data column and free text field, such as:

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
To avoid issues with processing the data its necessary to remove invalid characters from your data. Excel has the CLEAN function but I found it doesn't catch all characters and used the following function to highlight potential fields that might cause issues (B2 is the first cell with free text):

`=SUMPRODUCT(SEARCH(MID(B2,ROW(INDIRECT("1:"&LEN(B2))),1),"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890!@#$%^&*()-+=.,:/\'"""))`

## Overview of files
### Cleanup

Files meant to be run one-time to cleanup and standardize data for analysis

**NLTK 1**

  Load initial data, standardize items to lowercase, tokenize words, POS tag, lemmatize.

**NLTK 2**

  Format dataframe after lemmatize and create dataframe of individual words used for analysis.

### Analyze

  Determine word counts and identify outlier words for removal that occurr too frequently or infrequently.

**NLTK 3**

Calculate z-scores of individual words to determine which can be removed. Creates Excel extract of this information that is analyzed offline.

**NLTK 4**

Remove words from the dataset that are three or more standard deviations away from the mean

### Visualize

Create graphics focused on the mean set of words using Matplotlib 

**NLTK 5**

Visualize counts across all categories

**NLTK 6**

Visualize words by category
