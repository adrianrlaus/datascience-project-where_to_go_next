# Where To Go Next? A Hybrid Travel Recommender

Travel histories for over 3000 individual users and descriptions of 1000+ different cities were scraped from Nomadlist and Wikivoyage to create a travel recommendation system. The model utilizes both collaborative and content-based filtering to create unique, hybrid recommendations that will be much more useful than your typical blog search.  

- **Collaborative Filtering** - Recommendations based on the "Travel History" you will create.  

- **Content-Based Filtering** - Recommendations for each city entered. Based on the city's WikiVoyage Description.

**Techniques/Tools used in this project were:**

- BeautifulSoup and Selenium for web-scraping
- NLP for text processing
- Dimensionality Reduction
- Pairwise Cosine Distances

## Getting Started
Download the files and relevant libraries onto your system.  

### Built With
- Python 3.7
- Libraries
    - Sklearn
	- Gensim
    - spaCy
	- BeautifulSoup
	- Selenium

## Executing The Program
To create recommendations:  

1. Run the where_to_go_next_recommender.py file.
2. The user will be prompted to create their own "Travel History" of places they've been to, or would like to go.
3. The output would be a combination of collaborative and content-based recommendations. 

## Version History
- **1.0**
	- Initial Release

## Authors
- **Adrian Laus**  

## Acknowledgments
- A big thanks to my professors and classmates at Metis.
