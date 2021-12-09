from interview.heaviest_prime_word import Word, calculate_top_3_heaviest_words, is_prime


def test_Word():
    assert Word("a").weight == 0
    assert Word("b").weight == 1
    assert Word("c").weight == 2
    assert Word("d").weight == 3
    assert Word("e").weight == 4
    assert Word("f").weight == 5
    assert Word("g").weight == 6
    assert Word("h").weight == 7
    assert Word("i").weight == 8
    assert Word("j").weight == 9
    assert Word("k").weight == 10
    assert Word("l").weight == 11
    assert Word("m").weight == 12
    assert Word("n").weight == 13
    assert Word("o").weight == 14
    assert Word("p").weight == 15
    assert Word("q").weight == 16
    assert Word("r").weight == 17
    assert Word("s").weight == 18
    assert Word("t").weight == 19
    assert Word("u").weight == 20
    assert Word("v").weight == 21
    assert Word("w").weight == 22
    assert Word("x").weight == 23
    assert Word("y").weight == 24
    assert Word("z").weight == 25
    assert Word("abcdefghijklmnopqrstuvwxyz").weight == sum(range(26))
    assert Word("ABCDEFGHIJKLMNOPQRSTUVWXYZ").weight == sum(range(26))


def test_word_with_symbol():
    assert Word("A-B").weight == Word("AB").weight
    assert Word("-',;.?!:...()[]{}\"‘’—a").weight == Word("-',;.?!:...()[]{}\"‘’—A").weight


def test_calculate_top_3_heaviest_words():
    assert calculate_top_3_heaviest_words(content="a b c")[0].weight == 2


def test_less():
    assert Word("a") < Word("b")


def test_more():
    assert Word("b") > Word("a")


def test_max():
    r = [Word("a"), Word("b"), Word("c"), Word("ddd"), Word("impostors"), Word("‘Hold")]

    assert max(r).weight == Word("impostors").weight


def test_is_prime():
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert is_prime(11)


def test_winnings():
    assert Word("winnings").weight == 101


def test_virtue():
    assert Word("virtue").weight == 89
