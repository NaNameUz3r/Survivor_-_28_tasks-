def MassVote(N, Votes):

    percent = (100 / sum(Votes))
    percents = []

    for vote in Votes:
        vote_amount = vote * percent
        vote_amount = round(vote_amount, 3)
        percents.append(vote_amount)

    set_percent = set(percents)

    if len(percents) != len(set_percent):
        result = 'no winner'

    res_max = max(percents)
    if res_max > 50.0:
        result = 'majority winner ' + str(percents.index(res_max) + 1)
    elif res_max <= 50.0 and len(percents) == len(set_percent):
        result = 'minority winner ' + str(percents.index(res_max) + 1)

    return result

