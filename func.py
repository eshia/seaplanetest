# Design and implement a function in Python that takes two words and a dictionary of words as input. 
# Your function should return the shortest possible path between the two words by changing one 
#   letter at a time. Each change is one path step.

# You can assume that:

# Both the start and end words are lowercase strings of varying lengths.
# The start and end words can be different lengths.
# Only one letter can be changed, added, or deleted at a time.
# Each intermediate word must exist in the dictionary of words

# --------------------

# EXAMPLE 1:

# words = ["bat", "cat", "bath", "bathe", "path", "ice", "mice", "twice", "wrath", "can", "cane", "cape", 
#  "chase", "chose", "choose", "goose", "choke", "pith", "pits", "sits", "mits", "mite", "fits"]
# wordDict = {word:True for word in words}

# INPUT: startWord = "bat", endWord = "ice", wordDict = wordDict

# OUTPUT: "bat - bath - path - pith - pits - mits - mite - mice - ice"

# ---------------------

def shortestWordPath(startWord, endWord, wordDict):
    # edge cases
    if startWord == endWord: # if same word, Shortest Word Path is just that word
        return startWord
    
    wordList = list(wordDict.keys())
    if startWord not in wordDict:
        wordList.append(startWord)
    if endWord not in wordDict:
        wordList.append(endWord)

    # build graph of all words in wordDict
    # nodes are each word. they are bi-connected via edge if they differ by 1 letter
    def differByOneLetter(word1, word2):
        # cat (change): bat, pat, sat, mat, rat
        # cat (add): scat, coat, cart, cast, cats, cate
        # cat (delete): at
        len1 = len(word1)
        len2 = len(word2)
        if abs(len1 - len2) > 1:
            return False

        if len1 == len2: # look for 'change'
            countChange = 0
            for i in range(len1):
                if word1[i] != word2[i]:
                    countChange += 1
                if countChange > 1:
                    return False
            return True
        else:
            smallerWord = word1 if len1 < len2 else word2
            biggerWord = word1 if len1 > len2 else word2
            # checking 'add' vs 'delete' is same now
            smallPointer = 0
            foundDiff = False
            for i in range(len(biggerWord)):
                if smallPointer == len(smallerWord):
                    return True # the addition happened at the end
                if not foundDiff and biggerWord[i] != smallerWord[smallPointer]:
                    foundDiff = True
                elif foundDiff and biggerWord[i] != smallerWord[smallPointer]:
                    return False
                else:
                    smallPointer += 1
            return True
        
    # build wordGraph as adj list representation
    wordGraph = {word:[] for word in wordList}
    for i in range(len(wordList)):
        for j in range(len(wordList)):
            if wordList[i] != wordList[j]: # not same word
                # if they differ by single letter, then connect them
                if differByOneLetter(wordList[i], wordList[j]):
                    wordGraph[wordList[i]].append(wordList[j])


    def getShortestPath(graph, startNode, endNode):
        # set new dict, spgraph (key=node, val=weight) to have weights:
            # endNode = 1
            # all the rest nodes = +inf
        spgraph = {key:float('inf') for key in graph.keys()}
        spgraph[endNode] = 1
        # set parentgraph (key=node, val=their parent) 
        parentgraph = {key:None for key in graph.keys()}
        
        visited = set()
        queue = []
        def bfs(node):
            queue.append(node)
            visited.add(node)
            while queue:
                curr = queue.pop(0)
                currweight = spgraph[curr]
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        if 1 + currweight < spgraph[neighbor]:
                            spgraph[neighbor] = 1 + currweight
                            parentgraph[neighbor] = curr
                        visited.add(neighbor)
                        queue.append(neighbor)

        bfs(endNode)
        if spgraph[startNode] == float('inf'): # no path exists
            return None

        # now use parentgraph to get the actual path
        path = []
        curr = startNode
        while curr != endNode:
            path.append(curr)
            curr = parentgraph[curr]
        path.append(endNode)

        return " - ".join(path)


    return getShortestPath(wordGraph, startWord, endWord)