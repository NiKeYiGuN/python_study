class TestInnerConstant:
    def test_false(self):
        assert isinstance(False, bool)
        assert not False

    def test_true(self):
        assert isinstance(True, bool)
        assert True

    def test_none(self):
        assert not None

    def test_ellipsis(self):
        assert type(...) == type(Ellipsis)

    def test_debug(self):
        assert __debug__
