![imdb_logo_2016 svg](https://cloud.githubusercontent.com/assets/10628795/25308017/0a3f13be-277a-11e7-8336-7cfd43e167d9.png)


## IMDb DATASET ANALYSIS

The Internet Movie Database (abbreviated IMDb) is an online database of information related to films, television programs and video games, including cast, production crew, fictional characters, biographies, plot summaries, trivia and reviews.

In this Project, I am going to explore the IMDb dataset which includes 1  flat file:

* movie_metadata
It consists of details of all the movies starting from 1916 right upto 2016. The most important parameters to consider from the data set are information about each movies actors, directors, budget, gross, imdb rating etc.

The project digs deep into the dataset to gain insights into the film industry on the basis of 5 analysis which are somewhat related to each other.


So, the flow of all 5 analysis goes this way:

👍  The three major/ core attributes of the dataset are Directors, Actors and Movies

👍  The dependent attributes of the data set are genre and plot keywords on which movie is entirely dependent upon

👍  The weighted attributes are gross, budget, imdb_score and two of the calculated attributes net and net_percentage

Our majority of the analysis will be focused on finding relation between core and weighted attribute to find relationship between them and understanding patterns

## In the 1st Analysis:
-- We have focused on visualizing the data to get the basic details and some important relationships within the data set. 
It covers all three major attributes with each one being mapped one on one with other attributes to find a relation.

## In the 2nd Analysis:

--After we understood the basic analysis, we will now focus on the two major attributes in the Second analysis,
The second analysis cover's best actor and best director followed by few more insights based on analysis one.

## In the 3rd Analysis: 

-- After gaining insights into the best actor and director, it's time to focus on the third major attribute i.e Movie. Movie's here are dependent on two factor's genre and key_plots.
For this analysis we will be focusing on genre trying to find out which genre movies do well on box office and which finding which core attribute does well in which genre

## In the 4th Analysis:

-- We will be focusing on the second dependent attribute which is plot keyword. Just like genre we will play around with keywords trying to figure out how much role does a plot keyword play in the movie analysis.

## In the 5th and Final Analysis:

-- We will collect all our analysis and relate it with the 5th analysis that finds best actor director combination for the top 5 genres i.e action, drama, thriller, romance and comedy.


In the end we will conclude by relating all the analysis with each other. Take for example:
--If any one is planning to make a movie which is based on genre say Action, then from 5th analysis we can figure out which is the best actor director duo to consider for an action movie.
--After selecting the action director duo, from the 4th analysis which plot keywords we can use f=in order to market the movie for more profit and gross
-- From the third analysis we can come to know what is the trend for that particular genre in recent years. Whether that particular genre is being liked by audience or not. This can help anyone to predict whether this is the right time to release that particular genre movie or not.

So, this is how our analysis can help us relate and predict whether a particular genre would be hit or not and whether it is the right time to release that movie


## ANALYSIS - 1 :
[Click Here to view First Analysis](https://github.com/dhruvkanakia/kanakia_dhruv_spring2017/blob/master/Final/Analysis/Analysis1.ipynb)

-- The first analysis is all about visualing the data to find out different trends in it. 

## Questions covered:
*  Finding out in which year has the most number of films 
* Visualizing IMDb over the years 
* Analysing the gross trend over the years 
* REVENUE PLOT 
* 3-d plot for IMDB vs Budget vs Gross
* Is budget directly related to profit? 
* WITH WHICH FACTOS IS PROFIT ACTUALLY RELATED IN THE DATASET? 
* For the year range 2000-2020 we will find out what was their gross and budget 
* Which country has the highest number of movies? 
* Which language has the highest number of movies?


## Procedure:
Various plots between different attributes were plotted using bar/histogram to get the relationship.


## Insights:
1. It can be concluded that the number of films being released in recent has been increased significantly and the quality of movie has been impacted. 
2. The IMDb score and gross are directly related  
![3dplot](https://cloud.githubusercontent.com/assets/10628795/25309080/1e5ce90e-2791-11e7-94ec-13413c70f5c8.png)
3. High Budget movies aren't really making that profit. More the budget lesser is the profit
![budget_vs_net](https://cloud.githubusercontent.com/assets/10628795/25309084/275a39f8-2791-11e7-8134-2e5a0e64310e.png)
4. The net and net_percentage which is a calculated value is not directly related to any attribute
![corelationplot](https://cloud.githubusercontent.com/assets/10628795/25308783/5544ad00-278a-11e7-9e24-e7908fa582d0.png)
5. 2006 was the year when the budget was the highest and gross was the lowest.


## ANALYSIS -2
[Click to view 2nd Analysis](https://github.com/dhruvkanakia/kanakia_dhruv_spring2017/blob/master/Final/Analysis/Analysis2.ipynb)

-- In this analysis, the net_percentage calculated in the first analysis is used as reference to find more insights into the data.

## Questions covered:
* Top 10 directors who earned the most profit.
* Top 10 directors in terms of IMDb rating
* Best Director overall
* Top 10 Actors whose movie earned the most profit
* Top 10 actors in terms of IMDb rating
* Best Actor Overall
* Which country has the highest mean budget?
*Which country has the highest revenue?
* Which country has the highest number of language in which movies are released?


## Procedure:
1. Used bar plots to find the top directors and actors in terms of IMDb, net percentage and gross over the countries
2. Used Venn diagram to find the best actor and director by finding the intersection between best director and actor on the basis of imdb_score, facebook likes and profit percentage
3. Used pie  to highest number of different language movies released in a country


## Insights:
1. The top 10 grossing Directors are: 

![director_profit](https://cloud.githubusercontent.com/assets/10628795/25309205/874a39a0-2794-11e7-9a37-a59007b98cf9.JPG)

2. Best Director is: 


![bestdir_overall](https://cloud.githubusercontent.com/assets/10628795/25309226/6229ba6e-2795-11e7-9303-ac4fdd59e6fc.png)


3. Best Actors are:

![best_actor](https://cloud.githubusercontent.com/assets/10628795/25309227/6f592454-2795-11e7-9a7c-f2d309db396a.png)


4. USA has the highest number of distinct language movie releases



![languages](https://cloud.githubusercontent.com/assets/10628795/25309231/8fc7ae90-2795-11e7-80b7-f8a338119ece.png)


## Analysis 3: 
[Click here to view Analysis 3](https://github.com/dhruvkanakia/kanakia_dhruv_spring2017/blob/master/Final/Analysis/Analysis3.ipynb)

-- After visualizing the basic data and analyzing the two most important attributes of the dataset(Actors and Directors), It's now time to dig into movie's the third most important component of the data set.
So this analysis is completely based on movie related attributes


## Questions Covered:
* Which are the genre's in the data set?
* Which are the top5 most used genre?
* Which genre manages to get the highest imdb rating?
* Top 5 genre's distribution over the years?
* List of Best actor's in top 5 genres
* Most consistent actor 



## Procedure:
* The genre's column was cleaned and split amongst each director and actor to analyze various details.
The below code is used to separate the three actors list with different genre's

``` python
df_actor = pd.DataFrame(columns = ['actor_123','genre', 'budget', 'gross', 'year','director_name','imdb_score','net','net_percentage','movie_title'])

def actorRemap(row):
    global df_actor
    d = {}
    actors = np.array(row['actors'].split(','))
    n = actors.size
    d['actors']= [row['actors']]*n
    d['genre']= [row['genre']]*n
    d['budget'] = [row['budget']]*n
    d['gross'] = [row['gross']]*n
    d['year'] = [row['year']]*n
    d['director_name']= [row['director_name']]*n
    d['imdb_score']=[row['imdb_score']]*n
    d['net']= [row['net']]*n
    d['net_percentage']= [row['net_percentage']]*n
    d['movie_title']= [row['movie_title']]*n
    d['actor_123'], d['actors_list1'] = [], []
    for actor_123 in actors:
        d['actor_123'].append(actor_123)
        d['actors_list1'].append(actors[actors != actor_123])
    df_actor = df_actor.append(pd.DataFrame(d), ignore_index = True)

df_genre.apply(actorRemap, axis = 1)
df_actor['year'] = df_actor['year'].astype(np.int16)
df_actor = df_actor[['actor_123','genre', 'budget', 'gross', 'year','actors_list1','director_name','imdb_score','net','net_percentage','movie_title']]
```

* Bar plots are used to visualize which genre's have been used most number of times in the data set
* A csv of top 10 actors in each of the top 5 genre's is created and wordcloud's are plotted to find out which actor is the most versatile of all.



## Insights:
1. All in all there are 22 genre's in the data set


![all_wc](https://cloud.githubusercontent.com/assets/10628795/25309462/d98b2812-279b-11e7-9b35-b7b5cff5e8a9.png)

2. Drama has the highest mean imdb rating in the dataset followed by crime, mystery, adventure and romance


![trend_wc](https://cloud.githubusercontent.com/assets/10628795/25309464/0956dd98-279c-11e7-8eb3-d758fcd69d0d.png)


3. The top 5 most used genre are Action, Thriller, Drama, Comedy, Romance. 


![genre_count](https://cloud.githubusercontent.com/assets/10628795/25309482/78890e0c-279c-11e7-969d-f727dd5c51ad.png)



4. The top 5 genre distribution in terms of IMDb rating over the year's shows that Action is the most consistent of all followed by thriller and comedy. It can also be inferred that as year's passed by the industry has fair share of genre in each year especially after 1973. So, 1973 can be termed as a major revolution of film industry.

5. Of the 5 top genre looks like Tom Hanks is the most versatile actor amongst followed by Leonardo Di Caprio. 

![consistent](https://cloud.githubusercontent.com/assets/10628795/25309591/5510d7f4-279f-11e7-9fea-89f17ef6af9a.png)


## Analysis 4

[Click to view this Analysis](https://github.com/dhruvkanakia/kanakia_dhruv_spring2017/blob/master/Final/Analysis/Analysis%204.ipynb)


--After keywords, The other attribute that plays an important role in movie analysis are the plot keywords. So, in this analysis we will look around the relationship between differeny aspects of plot keywords


## Questions Solved:

* Which are the most used plot keywords?
* Top plot keywords  in terms of IMDb rating
* Top plot keywords in terms of Gross
* Top plot keywords in terms of budget
* For the top 5 genres, find out the count as well as average gross for each genre.


## Procedure 

* Wordclouds are used to find the top keywords for budget, Gross, IMDB rating.
* Bokeh charts are used to plot mosk bankable plot keywords


## Insights:

1. The most used plot keywords are love, friend, mother, death. <p align="center">
 
 <img src="https://cloud.githubusercontent.com/assets/10628795/25309968/f4bb7d42-27a7-11e7-821c-36c3ca0fec81.png" width="600" title="Github Logo"> </p>


2. Word cloud of all the keywords used in the data set are: 

![keywords_plot](https://cloud.githubusercontent.com/assets/10628795/25310017/cd1e1960-27a8-11e7-8f5d-138b76c6676c.png)


3. The common word which we can see amongst all the three word cloud are relationhip, sex, girl, death, war, american, movie, character etc.


![common_wordcloud](https://cloud.githubusercontent.com/assets/10628795/25310025/ef16823c-27a8-11e7-9f47-48ae9d90a6ed.png)


4. The most bankable action plot keyword are 


![action_most_bankable](https://cloud.githubusercontent.com/assets/10628795/25310068/d10f96e2-27a9-11e7-9730-a91dd4489faa.png)

5. Best plot keywords for top 5 genres are: Sex, relationship, star, school, woman, death, war, abuse are few of the most common plot keywords

![top5_plot_keyword](https://cloud.githubusercontent.com/assets/10628795/25310065/bc2fbab8-27a9-11e7-81ab-dbbe51ad5a86.png)



## Analysis 5:

[Click to view this Analysis](https://github.com/dhruvkanakia/kanakia_dhruv_spring2017/blob/master/Final/Analysis/Analysis5.ipynb)

-- After we have analyzed all the parameters and their relationship with each other it's time to  analyze how each of the top 5 genre has performed as compared to all the other genres and find the pair's between the actors and directors.



## Questions Solved:

* Mean IMDb of action vs other genre
* DIrector Actor pair who have done most number of films together
* Best Actor Director pair in Action genre
* Same analysis for comedy, thriller, romance, drama

## Procedures:

This procedure is used to find out the most worked pair in action genre

``` python
df1_action= df1.loc[df1['genres'].str.contains('Action')].dropna()
df_dir_act_action = pd.melt(df1_action,id_vars=['director_name'], value_vars=['actor_1_name','actor_2_name','actor_3_name'], value_name='actor').dropna()
# df_dir_act_sort_action
df_dir_act_sort_action= df_dir_act_action[['director_name','actor']].groupby(['director_name','actor']).size().sort_values(ascending = False).reset_index()[:40]
```

## Insights:

1. The mean imdb plot of action vs other genres clearly shows action has not done well when compared with other genre


![download](https://cloud.githubusercontent.com/assets/10628795/25310355/cb2ebf44-27b0-11e7-8ed0-1d3eec35a312.png)


2. Actor director combination who has most number of films together


![action_dir_action](https://cloud.githubusercontent.com/assets/10628795/25310372/eff3394a-27b0-11e7-9be0-86a5e9c9788c.PNG)


3. Best actor director combination in action


![best_actor_dir_pair_action](https://cloud.githubusercontent.com/assets/10628795/25310377/06fe41de-27b1-11e7-8242-37341253301a.PNG)


## Our analysis analysis all the major aspects in the data set and one can easily relate to the analysis to predict whether a movie would be hit a not as well as to take decisions on casting, best time to release a movie, best keywords to use etc.

From the analysis one thing is Obvious BATMAN ROCKS!! Chritsopher Nolan and Christian Bale are in majority of the top 5 list be it best director actor or best director. 
