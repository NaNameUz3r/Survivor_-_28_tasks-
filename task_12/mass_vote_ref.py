def MassVote(N, Votes):

    def calculate_votes_percents(vote_numbers):
        percent = (100 / sum(vote_numbers))
        assert percent > 0, "percent can't be less or equal zero"
        vote_percents = []

        for vote in vote_numbers:
            vote_percent = vote * percent
            vote_percent = round(vote_percent, 3)
            vote_percents.append(vote_percent)
        return vote_percents

    def determine_winner(percents_list):
        winner_grade = 'no winner'
        MOST_VOTED = max(percents_list)
        if MOST_VOTED > 50.0:
            winner_grade = 'majority winner ' + str(
                percents_list.index(MOST_VOTED) + 1)
        elif MOST_VOTED <= 50.0 and not is_draw(MOST_VOTED, percents_list):
            winner_grade = 'minority winner ' + str(
                percents_list.index(MOST_VOTED) + 1)

        return winner_grade

    def is_draw(max_vote, vote_percents):
        draw_result = False
        counter = 0
        for item in vote_percents:
            if item == max_vote:
                counter += 1
            if counter > 1:
                draw_result = True
        return draw_result

    vote_percents_list = calculate_votes_percents(Votes)
    election_result = determine_winner(vote_percents_list)
    return election_result
