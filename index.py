def func(points):
    rows, cols = len(points), len(points[0])
    row = points[0]

    for r in range(1, rows):
        next_row = points[r].copy()
        left, right = [0]*cols, [0]*cols

        left[0] = row[0]
        for c in range(1, cols):
            left[c] = max(row[c], left[c-1]-1)

        right[cols-1] = row[cols-1]
        for c in range(cols-2, -1, -1):
            right[c] = max(row[c], right[c+1]-1)

        for c in range(cols):
            next_row[c] += max(left[c], right[c])

        row = next_row

    return row


print(func([[1, 2, 3], [1, 5, 1], [3, 1, 1]]))
