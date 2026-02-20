# LAB_01 - Revision

## Team 26
**Team Members:**
- Kamilla VAISOVA - Exercise 2
- Diméo ZHANG - Exercises 1, 4
- Yannick ZHANG - Exercise 3

---
## Exercise Descriptions

### Exercise 1: Friend Request Timeline
The proposed solution follows a modular design by breaking down the messaging analysis into four distinct functions—counting uppercase letters, total alphabetic characters, specific punctuation marks, and detecting character repetitions—which allows each feature to be tested and maintained independently for better code clarity. This modular structure is orchestrated by a main function that calculates the "caps ratio" and applies specific logical thresholds to classify messages as CALM, URGENT, or AGGRESSIVE, while also flagging potential spam if any character is repeated more than three times consecutively. 

### Exercise 2: Mutual friends detection using sets
In this exercise, we used sets to make friends recommendations to other users. Each user has a set of friends and based on different operations, such as intersection, difference, union or the jaccard similarity, we are able to obtain different sets and the coefficient of similarity of friend sets. For the function that suggests friends, we recommend 2nd degree connections, so friends of your friends that you do not follow, and to do that we iterate through each friend in the user’s friend set and look at their friends. For each friend-of-a-friend, we check that the person is not the user themselves and is not already in the user’s friend list. If both conditions are satisfied, we add them to a suggestion set to avoid duplicates.
In terms of complexity, basic set operations like intersection, union, and difference are efficient and have an average time complexity of O(n), where n is the size of the sets. This is because Python sets are implemented using hash tables, which allow fast lookups and insertions.
The friend suggestion function has higher complexity. Since it iterates over each friend and then over each friend’s friends, its average time complexity is approximately O(n · m), where n is the number of the user’s friends and m is the average number of friends they have. In dense networks, this can approach O(n²).

### Exercise 3: Friend Recommendation by Common Interests
To implement the recommendation system we need to measure the similarities between profile.To do that we use cosine similarity formula to give a number that show us how similar two profile are .Then we have to detect wich profile can influence the user the most.To do that we sort them and after we compare their interest with the user interest to find interests that is not discovered yet,allowing us to generate recommendations.
We have seen that the complexity of these algorithm depends mainly on the number of interests that people have and the number of people.To optimize this process, we could use Sparse Matrix representations (like a dictionary of non-zero values or an inverted index). Since most users only have a few interests out of the thousands possible, we can skip calculations for "0" values. This significantly reduces both the memory footprint and the number of operations required, as we only process active interests.

### Exercise 4: Mutual Followers Matrix
The FollowerMatrix structure implements a directed social graph using a 2D boolean array where each cell indicates whether one user follows another. The core functions consist of Follow and Unfollow, which update the matrix entries, and Is_following, which verifies the existence of a specific connection. The system retrieves lists of people through Get_following, which checks the row associated with a user, and Get_followers, which examines the corresponding column to see who follows them. Furthermore, the solution identifies mutual follow pairs where two users follow each other and calculates an influence score to measure a person's total engagement relative to the overall size of the network.

---

## Complexity Analysis Summary

Exercise, Time complexity, Space complexity
- Ex 1: Friend Request Timeline, O (n), O(1), Loops traverse the n -character string to count patterns.
- Ex 2: Mutual friends detection, O(m·n), O(m·n)
- Ex 3: Friend recommendations by interests, O(U·I + U log U), O(UI)
- Ex 4: Mutual Followers Matrix, O(N²), O(N²), Initializes and traverses a fixed 2D grid to store all possible connections and detect reciprocal relationships between users.
