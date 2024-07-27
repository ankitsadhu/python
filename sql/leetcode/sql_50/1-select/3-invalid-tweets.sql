--- Find invalid tweet, a tweet is invalid if content column value is greater than 15

SELECT tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 15
