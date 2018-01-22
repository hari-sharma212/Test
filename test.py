import json


def no_century(str):
    data = json.loads(str)
    op = {}
    for row in data:
        if row[0] not in op:
            op[row[0]] = [row[1]]
        else:
            value = op[row[0]]
            value.append(row[1])
            op[row[0]] = value
    return len([country for country, scores in op.iteritems() if not max(scores) >= 100])
