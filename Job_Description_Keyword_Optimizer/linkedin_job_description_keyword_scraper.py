# web scraping
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time
import os

# NLP
from fuzzywuzzy import fuzz
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import preprocess_string, strip_tags, strip_punctuation, \
    strip_multiple_whitespaces, strip_numeric, remove_stopwords
import re

# misc
from collections import defaultdict, Counter
import pickle
from tqdm import tqdm # progess bar

def count_keywords(string):
    CUSTOM_FILTERS = [lambda x: x.lower(), strip_tags, strip_punctuation, strip_multiple_whitespaces,
                     strip_numeric, remove_stopwords]
    return Counter(preprocess_string(string, CUSTOM_FILTERS))

if __name__ == "__main__":
	# asks the user how many job descriptions they would like to find keywords for
	num_jobs = 0
	while num_jobs == 0:
	    try: 
	        num_jobs = int(input("Enter the number of jobs: \n"))
	    except ValueError:
	        print('Not a valid entry.')

	# asks the user for the LinkedIn job urls
	urls = []
	for i in range(num_jobs):
	    urls.append(input("Paste job description URL: \n"))


	# path to the chromedriver executable
	chromedriver = "/Applications/chromedriver"
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver)

	job_descriptions = ''
	for url in urls:
		try:
		    driver.get(url)
		    time.sleep(1)
		    
		    soup = BeautifulSoup(driver.page_source, 'html.parser')
		    
		    job_descriptions += soup.find(class_='description').text
		except:
			print('Invalid URL')
			
	driver.quit()

	# Find important keywords
	keyword_count = count_keywords(job_descriptions)
	sorted_keyword_count = \
	    {key: value for key, value in sorted(keyword_count.items(), key=lambda item: item[1], reverse=True)}

	print('\nImportant Keywords Are: \n')
	for key, value in sorted_keyword_count.items():
		print(key, value)