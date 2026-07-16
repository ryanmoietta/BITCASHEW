def rank_opportunities(data):

    ranked = sorted(
        data,
        key=lambda x: x["confidence"],
        reverse=True
    )

    return ranked[:3]




def long_term_pick(data):

    scores = []


    for coin in data:

        score = 0


        if coin["trend"] == "BULLISH":
            score += 30


        if 40 < coin["rsi"] < 65:
            score += 20


        if coin["volume"] == "HIGH":
            score += 20


        score += coin["confidence"] / 5


        scores.append(
            (
                coin["name"],
                score
            )
        )


    scores.sort(
        key=lambda x: x[1],
        reverse=True
    )


    if scores:
        return scores[0][0]


    return "N/A"
