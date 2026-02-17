def func(n, reserved):
    obj = {}
    res = 0
    reserved.sort()
    reserved.append([-2, 0])
    rows = []
    for i in range(len(reserved)):
        row, seat = reserved[i]
        lastSeat = obj[row] if row in obj else 0
        if row not in obj:
            obj[row] = seat
        obj[row] = seat

        if seat-lastSeat-1 >= 4:
            if lastSeat == 0:
                if seat == 10:
                    res += 2
                elif seat >= 6:
                    res += 1
            elif lastSeat == 1:
                res += 2 if seat == 10 else 1
            elif lastSeat == 2:
                res += 1 if seat >= 8 else 0
            elif lastSeat == 3 and seat >= 8:
                res += 1
            elif lastSeat <= 5 and seat == 10:
                res += 1

        if i < len(reserved)-1 and reserved[i+1][0] != row and (10-seat) > 4:
            if seat in [2, 3,4, 5]:
                res += 1

            elif seat == 1:
                res += 2

            print(row, seat, res)

        rows.append(row)

    return res+(n-len(set(rows))+1)*2, reserved


print(func(3, [[2, 3]]))

# print(func(4, [[2, 10], [3, 1], [1, 2], [
#       2, 2], [3, 5], [4, 1], [4, 9], [2, 7]]))
# print(func(5, [[2, 2], [5, 4], [3, 5], [5, 10], [5, 7], [4, 5]]))

# print(func(5, [[4, 7], [4, 1], [3, 1], [5, 9], [4, 4], [3, 7], [1, 3], [
#       5, 5], [1, 6], [1, 8], [3, 9], [2, 9], [1, 4], [1, 9], [1, 10]]))

# print(func(2, [[1, 5], [2, 8], [2, 10], [2, 2],
#       [1, 6], [1, 10], [1, 1], [2, 5], [1, 2]]))
# print(func(4, [[4, 3], [1, 4], [4, 6], [1, 7]]))
# print(func(2, [[2, 1], [1, 8], [2, 6]]))
