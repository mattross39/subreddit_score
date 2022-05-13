from re import split
from typing import Counter
import string
import praw
import pandas as pd

#################################################################
subreddit_choice = 'cardistry' #input("Which subreddit would you like to analyze? ")
num_posts = 1
num_comments = 1
#################################################################
post_scores = []

# Create an instance of reddit class
reddit = praw.Reddit(client_id="omwfS9JaoXFyBAprOCftDg",
                     client_secret="g5TKwq1cO45GgA2NRtuwwqq4p7PnsQ",
                     user_agent="user",
)
 
# Create sub-reddit instance
subreddit = reddit.subreddit(subreddit_choice)
new_subreddit = subreddit.top(limit=num_posts)


all_words = []
# Importing positive words and negative words from txt files
pos_file = open("positive_words.txt")
pos_words = pos_file.read().split()
neg_file = open("negative_words.txt")
neg_words = neg_file.read().split()


# Looping through the posts
for submission in new_subreddit:
    comment_index = 0
    sub_pos = {}
    sub_neg = {}


    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        # Cleans punctuation from comment
        clean_comment = comment.body.translate(str.maketrans('', '', string.punctuation))
        
        # Splits comment into a list of words
        split_comment = clean_comment.split()
        
        for word in split_comment:
            #TODO: 

        #TODO: Convert to lowercase         
        # Adds words from comment to master count
        all_words.extend(split_comment)
        
        comment_index += 1
        if comment_index == num_comments:
            break

print(Counter(all_words))

"""
final_score = avg(post_scores)
print("/r/" + subreddit_choice + " helpfuness score = " + final_score)
"""