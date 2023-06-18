# Design

This repository contains Low Level Design (LLD) solutions for different problem statements.

Below are the problem statements. These will be updated as and when I code the solution.

1. Design a parking lot system where you need to provide a token with the parking space number on it to each new entry for the space closest to the entrance. 
Note: When someone leave you need update this space as empty. What data structures will you use to perform the closest empty space tracking, plus finding what all spaces are occupied at a give time.

2. Design a locker (like the one found in Amaozn Hub) where you can store the packages and pickup the package. Returning the package is an extension of this and can be easily implemented by validating the user and package details. 
Note: There will be three types of lockers (small, medium, large) and the packages have to be stored in the respective locker sizes. 

3. Implement a Trie data structure. 
Note: Trie is a powerful data structure. Also known as Prefix tree, it is more flexible to support applications like auto-complete. It's a special data structure used to store strings that can be visualized as a graph

4. Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.
Implement the Twitter class:
. Twitter() Initializes your twitter object.
. void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
. List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
. void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
. void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
