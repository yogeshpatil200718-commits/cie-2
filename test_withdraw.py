from withdraw import withdraw

def test_success():
    assert withdraw(1000, 400) == (600, "Success")

def test_fail():
    assert withdraw(500, 800) == (500, "Insufficient Balance")