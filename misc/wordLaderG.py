def ladderLength(beginWord, endWord, wordList):
    graph = {}
    for word in wordList:
        for i in range(len(word)):
            bucket = word[:i] + "_" + word[i+1:]
            if bucket in graph:
                graph[bucket].append(word)
            else:
                graph[bucket] = []
    visited = set()
    queue = [(beginWord,1)]
    while queue:
        word, steps = queue.pop()
        if word == endWord:
            return steps
        if word not in visited:
            visited.add(word)
            for i in range(len(word)):
                neighsBucket = word[:i] + "_" + word[i+1:]
                ns = graph.get(neighsBucket,[])
                for neight in ns:
                    queue.insert(0, (neight, steps + 1))

print(ladderLength('hit','cog',["hot","dot","dog","lot","log","cog"]))
