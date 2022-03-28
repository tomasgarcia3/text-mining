from audioop import avg
from itertools import count
from black import out
from imdb import Cinemagoer
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# search movie
movie1 = ia.search_movie("Spider Man")[9] #Tobey Maguire - Spider-Man (2002)
movie2 = ia.search_movie("Spider Man")[12] #Andrew Garfield - The Amazing Spider-Man (2012)
movie3 = ia.search_movie("Spider Man")[9] #Tom Holland - Spider-Man: Homecoming (2017) NOT ENOUGH REVIEWS

def reviews(movie):
    """Takes a movie from the database and returns the list of reviews available for that movie."""
    movie_reviews = ia.get_movie_reviews(movie.movieID)
    return movie_reviews

# print(reviews(movie3)) #NOT AVAILABLE

def list_ratings(movie_reviews):
    """Takes a list of reviews and extracts the rating value for each review. It excludes any review with rating value as "None"."""
    ratings = []
    for reviews in movie_reviews['data']['reviews']:
        rating = reviews['rating']
        ratings.append(rating)
    ratings = filter(None,ratings)
    return ratings

def avg_ratings(ratings):
    """Takes a list of ratings and counts how many ratings are in the list. It also sums all the ratings together and then takes the average value."""
    total = 0
    count = 0
    for rating in ratings:
        total = total + rating
        count +=1
    return total/count

def list_sentiment_reviews(movie_reviews):
    "Takes the list of reviews and creates a new list which adds the VADER analysis of each text in the reviews."
    sid = SentimentIntensityAnalyzer()
    sentiments = []
    for reviews in movie_reviews['data']['reviews']:
        review = reviews['content']
        sentiments.append(sid.polarity_scores(review))
    return sentiments

def average_neg(sentiments):
    "Takes a list of VADER values and sums all the negative results. It also counts how many results are in the list and then takes the average."
    neg = 0
    count = 0
    for sentiment in sentiments:
        neg = neg + sentiment['neg']
        count +=1
    return neg/count

def average_neu(sentiments):
    "Takes a list of VADER values and sums all the neutral results. It also counts how many results are in the list and then takes the average."
    neu = 0
    count = 0
    for sentiment in sentiments:
        neu = neu + sentiment['neu']
        count +=1
    return neu/count

def average_pos(sentiments):
    "Takes a list of VADER values and sums all the positive results. It also counts how many results are in the list and then takes the average."
    pos = 0
    count = 0
    for sentiment in sentiments:
        pos = pos + sentiment['pos']
        count +=1
    return pos/count

def average_compound(sentiments):
    "Takes a list of VADER values and sums all the compound results. It also counts how many results are in the list and then takes the average."
    compound = 0
    count = 0
    for sentiment in sentiments:
        compound = compound + sentiment['compound']
        count +=1
    return compound/count

def output(movie):
    "Takes a movie and then different functions to print out a results table with the analysis of the success of the movie from fans review perspective."
    print(movie)
    movie_reviews = reviews(movie)
    ratings = list_ratings(movie_reviews)
    avg_rating = avg_ratings(ratings)
    print(f'The average rating is {avg_rating}')
    sentiment_list = list_sentiment_reviews(movie_reviews)
    avg_neg = round(average_neg(sentiment_list),4)
    print(f'The average negativity is {avg_neg*100}%')
    avg_neu = round(average_neu(sentiment_list),4)
    print(f'The average neutrality is {avg_neu*100}%')
    avg_pos = round(average_pos(sentiment_list),4)
    print(f'The average positivity is {avg_pos*100}%')
    avg_compound = round(average_compound(sentiment_list),4)
    print(f'The average compound is {avg_compound*100}%')

if __name__ == "__main__":
    output(movie1)
    output(movie2)
