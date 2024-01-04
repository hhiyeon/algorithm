from collections import defaultdict

n = int(input())
books = defaultdict(int)

for _ in range(n):
    title = input()
    books[title] += 1

sorted_books = sorted(books.items(), key=lambda x: [-x[1], x[0]])
print(sorted_books[0][0])
