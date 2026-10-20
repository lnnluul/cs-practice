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
