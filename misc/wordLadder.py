def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    visited = set()
    queue = []
    visited.add(beginWord)
    queue.insert(0,beginWord)
    pathLength = 0
    while queue:
        w = queue.pop()
        pathLength += 1
        words = findOneLetterDiffWords(w,wordList)
        for oneW in words:
            if oneW == endWord:
                return pathLength
            if oneW not in visited:
                visited.add(oneW)
                queue.insert(0,oneW)
    return None

def findOneLetterDiffWords(word, wordList):
    return [w for w in wordList if sum(a!=b for a,b in zip(word,w)) == 1]

print(findOneLetterDiffWords('hit',["hot","dot","dog","lot","log","cog"] ))
#print(ladderLength('hit','cog',["hot","dot","dog","lot","log","cog"]))
