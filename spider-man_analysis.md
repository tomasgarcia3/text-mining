# Assignment 2: Who is the better Spider-Man?

## Project Overview:

For this assignment, I used IMDB Moview Reviews as my data source. I was able to get this data by running the cinemagoer package on Command Prompt. My first look at the data was from the movie “The Dark Knight”, I immediately saw potential in the data this company collects on reviews. Growing up I always liked spider-man movies so I decided to use these movies to analyze which actor had done a better role in the superhero job. Although my initial plan was to gather information from all three actors, I then found out that Tom Hollands' first appearance as spider-man in Spider-Man: Homecoming had no reviews in the data. Therefore my I decided to continue my analysis but only look at the first spider-man movie for Tobey Maguire and Andrew Garfield. I analyzed the text reviews by doing natural language processing. What I created in my code were multiple functions that would allow me to get the sentiment for each movie in the form of an average. I took the VADER of each review and then took the overall average, on top of that I also did the average for ratings placed in the reviews. What I ended up learning from this experiment was to find out that The Amazing Spider, acted by Andre Garfield was less liked than Spider-Man, acted by Tobey Maguire. 

## Implementation:

The major components of my code begin at the moment I selected the movies. They are a lot of movies in the database under the name “Spider-Man”. Therefore from the two movies I select, they are adequately located from the list. The code I programmed for my analysis can be used to analyze any movie in the database with sufficient data. The architecture of my code is represented by my last function: output(), in which the whole purpose was to put all functions together and print the desired analysis in a much easier way to interpret. The entire value in my code comes from the implementation of sentinel analysis of each review. This is possible through the program called VADER available in the Natural Language Toolkit. Using this program I was able to successfully obtain a sentiment analysis of each review to then take an average for the indicated movie. Potentially this can be used to see the negativity behind each review and determine which was better liked. 

A design decision I went through was to make the code work properly for any movies review analysis. I could have just analyzed each movie individually calling functions by movie names but what would be the potential utility of that. What I wanted to create was a program that would have the future potential of analyzing movies reviews of multiple movies and making recommendations according to that. This is easily evident by looking at the doctrine and functionality of all the functions I wrote in the program. Essentially the reviews can be taken from any movie selected from IMDB. The reviews of this movie will be run over a series of functions that will perform the sentiment analysis and provide an overall result for the sentiment of each movie taken from the reviews. This data design allows for possible scalability in the future when analyzing lots of movies. 

## Results:

Tobey Maguire: Spider-Man 
Spider-Man
The average rating is 8.1
The average negativity is 7.33%
The average neutrality is 72.8%
The average positivity is 19.869999999999997%
The average compound is 92.07%

Andrew Garfield: The Amazing Spider-Man
The average rating is 6.2
The average negativity is 6.959999999999999%      
The average neutrality is 76.1%
The average positivity is 16.919999999999998%     
The average compound is 80.75%

From my analysis of the two movies, it was clear that Tobey Maguire was better liked as Spider-Man than Andrew Garfield. Spider-Man had much better reviews than The Amazing Spider-Man in terms of positive sentiment. Although negativity was slightly inverse, Spider-Man still had a better overall compound of the review. In VADER, the closer compound is to 1, the more positive the overall review was. I also decided to take the average of all the ratings given for each review, and not surprisingly, Spider-Man was nearly two points greater than The Amazing Spider-Man. 

Essentially how VADER works is that it returns four values of analysis within a text. These values are based on the sentiment of the text and the type of words the reviewers used when writing each review. Essentially the text is divided into a negative, neutral, and positive percentage based on how many words belong to each connotation. In the end, the analysis also comes up with a compound value from 0 to 1. The closer that number is to 1 the more positive the text. Tobey Maguire had a compound percentage of 92.07% while Andre Garfield had a compound of 80.75%. Although both numbers were considerably high, a difference of nearly 12% is big when comparing similar movies performed by different actors. 

## Reflection

The process when well because I was able to identify the data and what were some of the keys and values it had as well as understand the lists of items. I was able to extract the desired information and create lists that I would further use to analyze the data. I was able to convert the text into a sentiment review, by importing this algorithm and applying it to the text. Overall I think the process went well and the desired results were extracted. Just like any process, there is always room for improvement. I think the code could potentially be written in fewer lines, however, I do not believe I reach that level of coding yet. I also think that further analysis could have been done on multiple lists of movies with more parameters and algorithms. This level of analysis could have been possible given more time and practice. Although there could be an improvement to be done, I do believe my code satisfied the purpose of my analysis. Overall the development of this program went well. I was able to test the data to see if every function was giving me the desired outcome using print(). I did this until I had reached what I expected to get. Going forward I feel more comfortable importing data from different website datasets. This experience will definitely be useful for the final project in this class.  
