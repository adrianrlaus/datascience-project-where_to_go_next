
import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import pairwise_distances
from scipy.sparse import coo_matrix
import pickle

# match input string to the cloesest city_and_country avaialable
def match_words(input_word):
    closest_word = []

    for index in range(0,len(city_country_dict)):
        # quantitative value of how close the words are to each other
        # higher the better
        sort_ratio = fuzz.token_sort_ratio(input_word, city_country_dict[index]) 
        closest_word.append((sort_ratio, index))
    
    # return the index location of the city that is closest
    return max(closest_word)[1]

# This function creates TFIDF vectors for documents that have already been tokenized
# normally a document has to be a single string of words, not a list
def tfidf_for_tokens(tokenized_corpus):

    def identity_tokenizer(text):
        return text
    
    tfidf = TfidfVectorizer(tokenizer=identity_tokenizer, stop_words=None, lowercase=False)    
    rec_matrix = tfidf.fit_transform(tokenized_corpus)
    
    return rec_matrix.todense(), tfidf.get_feature_names()

# places is the places the user has gone to 
# should be a list of city AND country to be more specific(some countries have cities with the same name)
def collab_user_user_recommender_tfidf(user_input):
    
    # placeholder. new user hasnt visited any places yet
    new_user_input = np.zeros(len(city_country_dict))
    
    # fix the incorrect spelling here
    places = []
    for city in user_input:
        city_index = match_words(city)
        places.append(city_country_dict[city_index])


    places_index = []
    for city in places:
        city_index = match_words(city) # index of the place the've been to
        new_user_input[city_index] = 1 # change the array of zeros to 1 where the user has been
        places_index.append(city_index)
        
    # calculate new coo matrix
    new_coo = coo_matrix(new_user_input) 
    
    # transform coo only since we have the model already fitted
    new_user_vec = collab_svd_model.transform(new_coo) 
    new_user_dist = pairwise_distances(new_user_vec, collab_user_vec,metric='cosine')
    
    
    most_similar_users= [user_dict[index] for index in new_user_dist[0].argsort()]
    
    possible_recs = []
    i = 0
    for user in most_similar_users:
        if len(possible_recs) < int(len(most_similar_users)*0.01): # top 1% closest to you, skipping users that 
                                                            # add empty strings bc they only went to 1 or 2 places
            rec = []
            rec = [place for place in user_visited_dict[user] 
                   if place not in places]

            if ' '.join(rec) != '':
                possible_recs.append(rec)
            i+=1
    
    # convert top 1% closest users to TFIDF values and return high sum over the users
    tfidf_dense_matrix, column_names = tfidf_for_tokens(possible_recs)

    tfidf_df = pd.DataFrame(tfidf_dense_matrix)
    tfidf_df.columns = column_names
    recommendations = pd.DataFrame(tfidf_df.sum().sort_values(ascending=False)).reset_index()
    recommendations.columns = ['city_recommendation', 'score']

    list_of_recs = recommendations['city_recommendation'].values.tolist()
    for i in range(1,11):
        print(f'{i}. {list_of_recs[i-1]}')

def wiki_svd_recommender(input_city): 

    city_index = match_words(input_city)
    recs = [city_country_dict[index] for index in wiki_svd_city_dist[city_index].argsort()[1:total_num_recs]]

    print(f'\nIf you want a city more like {city_country_dict[city_index]}, I would recommend:\n')

    for i in range(10):
    	print(f'{i+1}. {recs[i]}')

if __name__ == "__main__":

	# Total number of recommendations wanted
	total_num_recs = 21


	# Open necessary pickes
	with open('city_country_dict.pkl', 'rb') as picklfile:
	    city_country_dict = pickle.load(picklfile)
	with open('user_dict.pkl', 'rb') as picklfile:
	    user_dict = pickle.load(picklfile)
	with open('user_visited_dict.pkl', 'rb') as picklfile:
		user_visited_dict = pickle.load(picklfile)
	with open('collab_svd_model.pkl', 'rb') as picklfile:
	    collab_svd_model = pickle.load(picklfile)
	with open('collab_user_vec.pkl', 'rb') as picklfile:
	    collab_user_vec = pickle.load(picklfile)
	with open('wiki_svd_city_dist.pkl', 'rb') as picklfile:
		wiki_svd_city_dist = pickle.load(picklfile)



	print("\nHello! Welcome to Where To Go Next? A Hybrid Travel Recommender!\n")
	
	print("Let's create a travel history for you. Input some cities that you've been to or would like to go. Please enter the city and country one at a time. When you are done, type 'done':\n")

	input_cities = []
	answer = ''
	while answer != 'done':
		answer = input()
		input_cities.append(answer)

	del input_cities[-1]

	# Collaborative filtering model
	for city in input_cities:
		city_index = match_words(city)
		print('You entered: ', city_country_dict[city_index])

	print("\n")
	print("\nBased on other users that liked the places you've entered, I would recommend:\n")
	collab_user_user_recommender_tfidf(input_cities)

	# Content based filtering model
	for city in input_cities:
		wiki_svd_recommender(city)












