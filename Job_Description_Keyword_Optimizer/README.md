# Job Description Keyword Optimizer

A very good way to ensure your resume is suitable for the job you're applying for is to optimize your resume with keywords. Unlike buzzwords like "passionate" or "driven," which can be considered fluffy, keywords showcase the soft skills and hard skills you possess that qualify you for your target job.

If you're unsure of which keywords to use in your resume, then this is for you. This repo can be used to identify the terms that are frequently used throughout your desired job positions. If you possess these skills or qualifications, you can easily incorporate these terms into your resume.

**Files In This Repo:**  

- **job_description_keyword_optimizer.ipynb**
	- Allows the user to copy-and-paste job multiple descriptions into the notebook, which then identifies the most common keywords used.
- **linkedin_job_description_keyword_scraper.ipynb**
	- Scrapes LinkedIn for job descriptions using Selenium and BeautifulSoup, which then identifies the most common keywords used.
- **linkedin_job_description_keyword_scraper.py**
	- Same as its .ipynb equivalent. Made to be used in terminal if the user wishes.
	
## Getting Started
Download the files and relevant libraries onto your system.  

### Built With
- Python 3.7
- Libraries
	- Gensim
	- BeautifulSoup
	- Selenium
		- [Chrome Webdriver](https://chromedriver.chromium.org/downloads "Chrome Webdriver")

## Executing The Program
Follow the jupyter notebooks in order or run the .py file.

The user will be asked to:  
	1. Input the number of job descriptions they want analyzed.  
	2. Input LinkedIn URLs or Job Descriptions.  

## Future Work
- Further filter out the keyword outputs by adding additional stopwords specific to job descriptions.  

## Version History
- **1.0**
	- Initial Release

## Authors
- **Adrian Laus**