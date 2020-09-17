for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    l.append([name, score])


def sort_list(l):
    low_score = [[]]
    n = len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j][1] > l[j+1][1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
    f_low = l.pop(0)
    for i in l[:]:
        if f_low[1] == i[1]:
            l.remove(i)
    low_score = [l[0]]
    l.pop(0)
    for i in l:
        if i[1] == low_score[0][1]:
            low_score.append(i)
    s_l = sorted(low_score)
    for i in s_l:
        print(i[0])


sort_list(l)