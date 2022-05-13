import praw
import pandas as pd

#################################################################
subreddit_choice = 'cardistry' #input("Which subreddit would you like to analyze? ")
num_posts = 2
num_comments = 3
post_scores = []
#################################################################

# Create an instance of reddit class
reddit = praw.Reddit(client_id="omwfS9JaoXFyBAprOCftDg",
                     client_secret="g5TKwq1cO45GgA2NRtuwwqq4p7PnsQ",
                     user_agent="user",
)
 
# Create sub-reddit instance
subreddit = reddit.subreddit(subreddit_choice)
new_subreddit = subreddit.new(limit=num_posts)

# Looping through the posts
for submission in new_subreddit:
    index = 0
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        #print(comment.body)
               
        
        index += 1
        if index == num_comments:
            break