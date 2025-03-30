import pandas as pd
import os
import nltk
import glob

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron, LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

from bs4 import BeautifulSoup

nltk.download('wordnet', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt_tab', quiet=True)

absoluteSourcePath =  os.path.dirname(__file__)
# Finds out the path to the source code location

subFolder = os.path.join(absoluteSourcePath, "China")
# Subfolder named Chine with the dataset inside in the same location as the script

regexForDirectory = os.path.join(subFolder, "China_*.parquet")
# print(regexForDirectory), this one gets the general path into the regex for getting all dataset files

allFiles = glob.glob(regexForDirectory)  # Get all files from the global directory.
# print(allFiles), we get ALL the files into this variable

allFiles = allFiles[:20]
print(len(allFiles))

datasetFile = pd.concat([pd.read_parquet(f) for f in allFiles], ignore_index=True)
# Used to get the dataset file name which contains the columns

print(datasetFile.shape)

# usefulColumnList = ["post_text", "application_name", "post_language"]
# # Get out the useful column headings in the dataset

# inputData = pd.read_csv(datasetFile, sep='\t', usecols=usefulColumnList, on_bad_lines='skip', low_memory=False)
# # Read dataset as CSV, seperator is TAB and SKIP any error giving lines while only using the columns
# # for star rating and the review body (such as 20773 with 22 tokens instead of 15?).

# print('\nThree sample reviews, along with their ratings include: \n')
# print(inputData.sample(3, random_state=10), "\n")
# # Getting a sample of 3 reviews to confirm workings
# # TO DO: Process data to remove unknown characters and spaces, etc, Perform Contractions, Remove stopwords, perform lemmatization
