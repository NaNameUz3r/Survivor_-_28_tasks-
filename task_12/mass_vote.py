def MassVote(N, Votes):

    percent = (100 / sum(Votes))
    percents = []

    for vote in Votes:
        vote_amount = vote * percent
        vote_amount = round(vote_amount, 3)
        percents.append(vote_amount)

    result = 'no winner'
    res_max = max(percents)

    def check_draw(max_vote, vote_percents):
        counter = 0
        draw_result = False
        for item in vote_percents:
            if item == max_vote:
                counter += 1
        if counter > 1:
            draw_result = True
        return draw_result

    if res_max > 50.0:
        result = 'majority winner ' + str(percents.index(res_max) + 1)
    elif res_max <= 50.0 and not check_draw(res_max, percents):
        result = 'minority winner ' + str(percents.index(res_max) + 1)

    return result

