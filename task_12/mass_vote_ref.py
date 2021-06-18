def MassVote(N, Votes):

    def check_draw(max_vote, vote_percents):
        draw_result = False
        counter = 0
        for item in vote_percents:
            if item == max_vote:
                counter += 1
            if counter > 1:
                draw_result = True
        return draw_result

    percent = (100 / sum(Votes))
    assert percent > 0, "percent can't be less or equal zero"
    percents = []

    for vote in Votes:
        vote_amount = vote * percent
        vote_amount = round(vote_amount, 3)
        percents.append(vote_amount)

    vote_result = 'no winner'
    MOST_VOTED = max(percents)
    if MOST_VOTED > 50.0:
        vote_result = 'majority winner ' + str(percents.index(MOST_VOTED) + 1)
    elif MOST_VOTED <= 50.0 and not check_draw(MOST_VOTED, percents):
        vote_result = 'minority winner ' + str(percents.index(MOST_VOTED) + 1)

    return vote_result
