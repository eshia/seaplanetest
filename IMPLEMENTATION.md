### General thought process

After reading the problem description, I thought a good place to start approaching this was using a shortest path algorithm, as it asks to find the "shortest path". The words would be the nodes in the graph, which are connected if they differ by a letter. I created another function `differByOneLetter(word1, word2)`, which takes in 2 words to see if they can be 'connected' to each other (or differ by a letter). I represented this graph as an adjacency list, `wordGraph`, and went through each pair of words to see if they are connected and added the words to each other's lists in `wordGraph`. I have the `getShortestPath` to run my shortest path algorithm, which uses a BFS traversal and calculates the minimum distance from every node to the single given node. I have a `parentgraph` to store each node's parent, and I use that to figure out the actual path of nodes/words, and return that.

One edge case is that the 2 given start and end words are the same, in which case I just return that word.
Another case is that there is no path found, so I return None.

### Assumptions made / things I was unclear of
For the most part, I tried not to make any extra assumptions and just implemented the function with the given assumptions. The only thing I was unclear of was whether startWord and endWord are legitimate words, since the instructions said "Intermediate words must exist in the dictionary". So I considered them to be legitimate words because of that phrasing.

And then for my implementation, I made the following decisions:
- I assumed `wordDict` to be a dictionary where the key is the word, and the value = True (it exists), so all the keys in this dictionary will have value of True
- I outputted "None" in the case where there is no path for the words