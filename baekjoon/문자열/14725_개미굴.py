n = int(input())  # 먹이 개수


class Trie:
    def __init__(self):
        self.root = {}  # 루트 노드

    def insert(self, word):
        node = self.root

        for ch in word:
            # print(node)
            if ch not in node:
                node[ch] = {}  # 자식 노드
            node = node[ch]
            # print(node)
            # print()
        node[0] = True  # 리프 노드

    def print_trie(self, level, node):
        if 0 in node:  # 리프 노드 종료
            return
        for ch in sorted(node):  # 정렬된 자식 노드 출력
            print("--" * level + ch)
            self.print_trie(level + 1, node[ch])


trie = Trie()

for _ in range(n):
    info = list(input().split())
    trie.insert(info[1:])

trie.print_trie(0, trie.root)
