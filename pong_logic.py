"""A Pong játék grafikus felülettől független, tesztelhető logikája."""


def clamp_paddle_y(current_y, movement, limit):
    """Új ütőpozíciót számol; az ütő nem lépheti át a pálya határát."""
    return max(-limit, min(limit, current_y + movement))


def bounce_vertical(y, dy, top, bottom):
    """Visszapattanás a felső vagy alsó falról; (új_y, új_dy) párt ad."""
    if y >= top:
        return top, -abs(dy)
    if y <= bottom:
        return bottom, abs(dy)
    return y, dy


def scoring_player(ball_x, half_width):
    """Megadja, ki kap pontot, ha a labda elhagyta a pályát."""
    if ball_x > half_width:
        return "left"
    if ball_x < -half_width:
        return "right"
    return None


def has_won(score, winning_score):
    """Igaz, ha a pontszám elérte a győzelemhez szükséges értéket."""
    return score >= winning_score
