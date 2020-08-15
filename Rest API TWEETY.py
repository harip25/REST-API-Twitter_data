
#Using the REST API to collect historical data
import tweepy  
import time

#use your own key and tokens
access_token = " enter here" 
access_token_secret = " enter here" 
consumer_key = " enter here"  
consumer_secret = " enter here"  
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)  
api = tweepy.API(auth,wait_on_rate_limit= True)

#Obtaining Twitter’s Id with the screen name and vice versa
user = api.get_user(screen_name = 'theresa_may')  
print(user.id)

user = api.get_user(747807250819981312)  
print(user.screen_name)


#Gathering the tweets from the Timeline of a certain user
try:  
    for tweet in tweepy.Cursor(api.user_timeline, screen_name="theresa_may", exclude_replies=True, count = 10).items():  
                    tweet_text = tweet.text  
                    time = tweet.created_at  
                    tweeter = tweet.user.screen_name  
                    print("Text:" + tweet_text + ", Timestamp:" + str(time) + ", user:" +  tweeter)  
except tweepy.TweepError:  
    time.sleep(60)


import json    
try:  
    for tweet in tweepy.Cursor(api.user_timeline, screen_name="theresa_may", exclude_replies=True, count = 10).items():  
                    tweet_text = tweet.text  
                    time = tweet.created_at  
                    tweeter = tweet.user.screen_name  
                    tweet_dict = {"tweet_text" : tweet_text.strip(), "timestamp" : str(time), "user" :tweeter}  
                    tweet_json = json.dumps(tweet_dict)  
                    print(tweet_json)  
except tweepy.TweepError:  
    time.sleep(60)

#Gathering the followers of a certain user.
try:   
    followers = api.followers_ids(screen_name="theresa_may")  
except tweepy.TweepError:  
    time.sleep(20)


user_list = ["AaltoUniversity", "helsinkiuni","HAAGAHELIAamk", "AaltoENG"]
follower_list = []  
for user in user_list:  
    try:   
        followers = api.followers_ids(screen_name=user)  
    except tweepy.TweepError:  
        time.sleep(20)  
        continue  
    follower_list.append(followers)

for index, user in enumerate(user_list):  
    print("User: " + user + "\t Number of followers: " + str(len(follower_list[index])))

#--------------another way-----------------------
user_list = ["AaltoUniversity", "helsinkiuni","HAAGAHELIAamk", "AaltoENG"]    
follower_list = []  
for user in user_list: 
    followers = []  
    try:         
        for page in tweepy.Cursor(api.followers_ids, screen_name=user).pages():  
            followers.extend(page)  
    except tweepy.TweepError:  
        time.sleep(20)  
        continue  
    follower_list.append(followers)

for index, user in enumerate(user_list):  
    print("User: " + user + "\t Number of followers: " + str(len(follower_list[index])))

#Collecting the friends of a certain user.
friends = []  
try:   
    for page in tweepy.Cursor(api.friends_ids, screen_name="theresa_may").pages():  
        friends.extend(page)  
except tweepy.TweepError:  
    time.sleep(20)

#Seeing the number of followers/friends of a certain user.
user = api.get_user(screen_name = 'theresa_may')  
print(user.followers_count)  
print(user.friends_count)
#-----------------another way-----------------
user = api.get_user(747807250819981312)
print(user.followers_count)  
print(user.friends_count)


    
