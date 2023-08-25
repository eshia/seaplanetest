### General thought process



### Assumptions made / things I was unclear of
For the most part, I tried not to make any extra assumptions and just implemented the function with the given assumptions. The only thing I was unclear of was whether startWord and endWord are legitimate words, since the instructions said "Intermediate words must exist in the dictionary". So I considered them to be legitimate words because of that phrasing.

And then for my implementation, I made the following decisions:
- I assumed `wordDict` to be a dictionary where the key is the word, and the value = True (it exists), so all the keys in this dictionary will have value of True
- I outputted "None" in the case where there is no path for the words