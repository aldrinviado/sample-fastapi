from app.calculations import add


def test_add():
    print("testing to add function")
    sum = add(5,3)
    assert sum == 41111