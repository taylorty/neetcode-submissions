class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        dictionary = defaultdict(set)
        # dictionary = {char: set() for word in words for char in word}
        # indegree = defaultdict(int)
        indegree = Counter({char: 0 for word in words for char in word})
        for i, word in enumerate(words):
            if i == len(words) - 1:
                continue
            next_word = words[i + 1]
            # Edge case: word 2 is a shorter prefix of word 1
            if len(word) > len(next_word) and word.startswith(next_word):
                return ''
            # compare(word, next_word)
            # print(min(len(word), len(next_word)))
            for j in range(min(len(word), len(next_word))):
                char1 = word[j]
                char2 = next_word[j]
                # print(dictionary)
                if char1 != char2:
                    if char2 not in dictionary[char1]:
                        dictionary[char1].add(char2)
                    # if char1 not in indegree:
                    #     indegree[char1] = 0
                        indegree[char2] += 1
                    break
        q = deque()
        # q = deque([char for char in indegree if indegree[char] == 0])
        for key in indegree:
            if indegree[key] == 0:
                q.append(key)
        # print(indegree)
        res = ""
        while q:
            curr = q.popleft()
            res += curr
            for next_char in dictionary[curr]:
                indegree[next_char] -= 1
                if indegree[next_char] == 0:
                    q.append(next_char)
                
        # Cylce detection: if we visited fewer nodes than there are vectors in our graph, there's a cycle - return an empty string
        if len(res) < len(indegree): return ''
        # print(dictionary)
        return res
