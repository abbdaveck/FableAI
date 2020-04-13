import requests, praw

clienntid = "GiCDIfxk0kkViQ"

secret = "S5toq6NicSGibQxL8Ujc2b0rLXs"

name = "r/nosleep_scraper"

reddit = praw.Reddit(client_id= clienntid, client_secret= secret, user_agent=name)

hot_posts = reddit.subreddit('NoSleep').top(limit=10000)

txt = open("top10000.txt", "w", encoding="utf-8")

for post in hot_posts:
    body = post.selftext
    b = txt.write(str(body) + "\n \n" )

txt.close()
