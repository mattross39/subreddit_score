from re import split
from typing import Counter
import string
import praw
import pandas as pd

#################################################################
subreddit_choice = 'cardistry' #input("Which subreddit would you like to analyze? ")
num_posts = 200
#################################################################
pos_found = []

# Create an instance of reddit class
reddit = praw.Reddit(client_id="omwfS9JaoXFyBAprOCftDg",
                     client_secret="g5TKwq1cO45GgA2NRtuwwqq4p7PnsQ",
                     user_agent="user",
)
 
# Create sub-reddit instance
subreddit = reddit.subreddit(subreddit_choice)
new_subreddit = subreddit.new(limit=num_posts)


# Importing positive words from txt files
pos_file = open("positive_words.txt")
pos_words = pos_file.read().split()
comment_index = 0
# Looping through the posts
for submission in new_subreddit:

    

    #!comment_index = 0
    submission.comments.replace_more(limit=0)
    print(len(submission.comments))
    for comment in submission.comments:
        #Makes comment lowercase
        lower_comment = comment.body.lower()

        # Cleans punctuation from comment
        clean_comment = comment.body.translate(str.maketrans('', '', string.punctuation))
        
        # Splits comment into a list of words
        split_comment = clean_comment.split()
                
        # Adds only positive words
        for word in split_comment:
            if word in pos_words:
                pos_found.append(word)
       
        comment_index += 1
       #! print(str(comment_index))
       #! if comment_index == num_comments:
       #!     break

print(comment_index)
print(Counter(pos_found))
print("pos words = " + str(len(pos_found)))
"""
final_score = avg(post_scores)
print("/r/" + subreddit_choice + " helpfuness score = " + final_score)
"""