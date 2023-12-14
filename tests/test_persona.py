from ..persona import compose_poem, calculate_math

def test_compose_poem():
    poem = compose_poem()
    assert poem != "failed"

def test_calculate_math():
    math_ans = calculate_math()
    assert math_ans != "failed"