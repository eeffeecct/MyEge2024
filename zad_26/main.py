k = 2
n = 5
passengers = [(30, 60), (40, 1110), (61, 120),(59, 60) ]
passengers.sort()

cells = [-1] * k
a1 = a2 = 0
for p in passengers:
    for i in range(k): #перебираем номера всех ячеек
        if p[0] >= cells[i]:
            cells[i] = p[1] + 1
            a1 += 1
            a2 = i + 1
            break

cells = [-1] * k
a1 = a2 = 0
for p in passengers:
    free_cells = [i for i in range(k) if p[0] >= cells[i]]
    if len(free_cells) > 0:
        cells[free_cells[0]] = p[1] + 1
        print(free_cells)



# k = 10
# n = 5
# tourists = [(30, 60, 5),(30, 60, 3),(30, 60, 3),(59, 120, 1),(40, 1110, 2)]
#
# rooms = [-1] * k
# for t in tourists:
#     free_rooms = [i for i in range(k) if t[0] >= rooms[i]]
#     if len(free_rooms) >= t[2]:
#         for i in free_rooms[:t[2]]:
#             rooms[i] = t[1]


# n = 5
# li = [43, 40, 32, 40, 30]
# li.sort(reverse=True)

# boxes = [li[0]]
# for b in li:
#     if boxes[-1] - b >= 3:
#         boxes.append(b)
# print(len(boxes), boxes[-1])


# n = 6
# p = [(40, 30), (40,34), (50,64), (50,125), (50, 68), (50, 129)]
# p.sort()

# for l, r in zip(p, p[1:]):
#     if l[0] == r[0] and abs(l[1] - r[1]) - 1 == 3:
#         print(l, r)

























