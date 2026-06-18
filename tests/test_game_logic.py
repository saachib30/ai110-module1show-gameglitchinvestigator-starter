from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_wrong_guess_subtracts_points():
    # A wrong guess should cost 5 points, never add them.
    # Use an even attempt number, which is where the "Too High" bug shows up.
    assert update_score(current_score=20, outcome="Too High", attempt_number=2) == 15
    assert update_score(current_score=20, outcome="Too Low", attempt_number=2) == 15
