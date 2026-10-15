"""Automatikus tesztek a Pong játék tiszta logikai függvényeihez."""

import pytest

from pong_logic import bounce_vertical, clamp_paddle_y, has_won, scoring_player


@pytest.mark.parametrize(
    ("current_y", "movement", "limit", "expected"),
    [
        (0, 30, 270, 30),
        (250, 30, 270, 270),
        (-250, -30, 270, -270),
        (100, -30, 270, 70),
        (270, 0, 270, 270),
    ],
)
def test_clamp_paddle_y(current_y, movement, limit, expected):
    assert clamp_paddle_y(current_y, movement, limit) == expected


@pytest.mark.parametrize(
    ("y", "dy", "top", "bottom", "expected"),
    [
        (280, 5, 280, -280, (280, -5)),
        (-280, -5, 280, -280, (-280, 5)),
        (10, 5, 280, -280, (10, 5)),
        (10, -5, 280, -280, (10, -5)),
    ],
)
def test_bounce_vertical(y, dy, top, bottom, expected):
    assert bounce_vertical(y, dy, top, bottom) == expected


@pytest.mark.parametrize(
    ("ball_x", "half_width", "expected"),
    [
        (401, 400, "left"),
        (-401, 400, "right"),
        (400, 400, None),
        (-400, 400, None),
        (0, 400, None),
    ],
)
def test_scoring_player(ball_x, half_width, expected):
    assert scoring_player(ball_x, half_width) == expected


@pytest.mark.parametrize(
    ("score", "winning_score", "expected"),
    [
        (0, 5, False),
        (4, 5, False),
        (5, 5, True),
        (6, 5, True),
    ],
)
def test_has_won(score, winning_score, expected):
    assert has_won(score, winning_score) is expected
