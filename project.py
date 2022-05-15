from re import split
from typing import Counter
import string
import praw
import pandas as pd

#################################################################
subreddit_choice = 'bowling' #input("Which subreddit would you like to analyze? ")
num_posts = 100
#################################################################
pos_found = []
comment_index = 0
question_index = 0

# Create an instance of reddit class
reddit = praw.Reddit(client_id="omwfS9JaoXFyBAprOCftDg",
                     client_secret="g5TKwq1cO45GgA2NRtuwwqq4p7PnsQ",
                     user_agent="user",
)
 
all_submissions = []
def scrape_subreddit():
    subreddit = reddit.subreddit(subreddit_choice)
    new_subreddit = subreddit.hot(limit=num_posts)
    for submission in new_subreddit:
        all_submissions.append(submission)

# Importing positive words from txt files
pos_file = open("positive_words.txt")
pos_words = pos_file.read().split()

scrape_subreddit()

# Looping through the posts
for submission in all_submissions:
    if '?' in submission.title:
        submission.comments.replace_more(limit=0)
        #print(len(submission.comments))
        print(submission.title)
        
        for comment in submission.comments:
        #Makes comment lowercase
            lower_comment = comment.body.lower()

            # Cleans punctuation from comment
            clean_comment = lower_comment.translate(str.maketrans('', '', string.punctuation))

            # Splits comment into a list of words
            split_comment = clean_comment.split()

            # Adds only positive words
            for word in split_comment:
                if word in pos_words:
                    pos_found.append(word)
       
            comment_index += 1
        question_index += 1
    else: 
        print('not a question')


print(question_index)
print(comment_index)
print(Counter(pos_found))
print("pos words = " + str(len(pos_found)))
"""
final_score = avg(post_scores)
print("/r/" + subreddit_choice + " helpfuness score = " + final_score)
"""