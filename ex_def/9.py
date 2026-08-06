def f_max(l):
    m = 0

    for elem in l:
        if elem > m:
            m = elem
    return m

print(f_max([4, 6, 8, 24, 12, 2]))