from services.simple_services import say_hello, are_you_sure

def test_empty_and_useless():
    pass


def test_say_hello():
    expected_hello = "hello foo !"

    hello = say_hello("foo")

    assert hello == expected_hello

def test_are_your_sure_when_is_sure():
    expected_return = "I'm sure!"

    answer = are_you_sure(True)

    assert answer == expected_return

def test_are_your_sure_when_is_not_sure():
    expected_return = "Not sure!"

    answer = are_you_sure(False)

    assert answer == expected_return
