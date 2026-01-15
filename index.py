def solve():
    n, m = map(int, input().split())

    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[ry] = rx

    for _ in range(m):
        a, b, l = map(int, input().split())
        a -= 1
        b -= 1
        for i in range(l):
            union(a + i, b + i)

    # Komponentlar soni
    roots = set(find(i) for i in range(n))
    print(len(roots))
