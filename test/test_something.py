from MyPkg.code import do_something


def test_something_func():
    assert do_something() == 42


def test_fail_this():
    assert 1 == 2
