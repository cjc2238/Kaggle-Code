# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 12:08:39 2017

@author: Chad
"""
import pandas as pd
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import re
import string

dataframes = {
    "cooking": pd.read_csv("C:\Users\Chad\Desktop\Stack Exchange Kaggle\Python Code\Kaggle Code\cooking.csv\cooking.csv"),
    "crypto": pd.read_csv("C:\Users\Chad\Desktop\Stack Exchange Kaggle\Python Code\Kaggle Code\crypto.csv\crypto.csv"),
    "robotics": pd.read_csv("../input/robotics.csv"),
    "biology": pd.read_csv("../input/biology.csv"),
    "travel": pd.read_csv("../input/travel.csv"),
    "diy": pd.read_csv("../input/diy.csv"),
}
