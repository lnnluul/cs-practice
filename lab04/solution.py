def winner(names, scores):

    max_i = 0
    for i in range(len(scores)):
        if scores[i] > scores[max_i]:
            max_i = i
    return names[max_i]

def average(scores):

    if len(scores) == 0:
        return 0.0

    sum = 0.0
    for s in scores:
        sum = sum + s

    return round(sum / len(scores), 2)

def above_average(names, scores):

    sr = average(scores)

    res = []
    for i in range(len(scores)):
        if scores[i] > sr:
            res.append(names[i])

    return res

def ranking(names, scores):

    ind = []
    for i in range(len(names)):
        ind.append(i)

    for i in range(len(ind)):
        for j in range(len(ind) - 1):
            idx1 = ind[j]
            idx2 = ind[j + 1]
            if scores[idx1] < scores[idx2]:

                ind[j], ind[j + 1] = ind[j + 1], ind[j]

    itog = []
    for idx in ind:
        itog.append(names[idx])

    return itog
