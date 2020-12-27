#! python3
# Python script to Search social media for mentions of brands and collect the comments/tweets/etc.
# Count mentions of each and perform sentiment analysis on the strings.

import praw
import pandas as pd
from secrets import client_id, client_secret, user_agent
from pathlib import Path
from brands import fashion

# Provide your own reddit api credentials in a secrets file.
reddit = praw.Reddit(
    client_id=client_id, client_secret=client_secret, user_agent=user_agent
)


def create_comments_df(subreddit_):
    """Returns a pandas df with the information about comments from this year.

    Inputs
    -----
    str: subreddit to be searched.
    Return
    ------
    Pandas dataframe with all the data from the praw object.m
    """
    subreddit = reddit.subreddit("malefashionadvice")
    submission_list = subreddit.top(
        time_filter="year", limit=1000
    )  # generator of submissions in the subreddit
    comment_list = []
    for submission in submission_list:
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            comment_list.append(comment)

    df = pd.DataFrame([vars(comment) for comment in comment_list])
    df2 = df.loc[:, ["link_id", "id", "score", "body"]]
    df2["Subreddit"] = subreddit
    return df2


def brand_check(df, brandlist):
    """Checks comment body against a list of brands to see if it mentions any.
    Adds what brand was found if any in the brands column.

    Inputs
    ------
    Dataframe you will search over and a list of brands in a separate file.
    Return
    ------
    Dataframe with column indicating what brand was found in the values.
    """

    df["Brand"] = df.body.str.extract(pat=brandlist, expand=False)
    return df


# This could take quite a long time due to reddit api limits and the amount of posts
# we parse through so only use this if you need a lot of data you don't already have.
# This one also asks you if you want to save as csv just in case.
def create_multsub_df(subredditlist):
    df = [create_comments_df(subreddit) for subreddit in subredditlist]
    comb_df = pd.concat(df)
    reply = input("Would you like to save the file dataframe to csv? (Y or N)")
    if reply == "N":
        pass
    elif reply == "Y":
        filename = input("What filename would you like to save as?")
        p = Path.cwd() / "data" / f"{filename}.csv"
        comb_df.to_csv(path_or_buf=p)
        print("Done.")
    return comb_df


subreddits = ["malefashionadvice"]
subreddit = "malefashionadvice"
filename = ""
p = Path.cwd() / "data" / filename
# df = pd.read_csv(p)

# Comment this out if you already have the data you want.
df = create_comments_df(subreddit)

df2 = brand_check(df, fashion)
print(df2["Brand"].value_counts())
