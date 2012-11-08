from nose.tools import assert_equal

from letterpress import Game

def test_game():
    # Construct a new game.
    game = Game(
        '''
        yzdao
        bpzlk
        dbxol
        qslbc
        nirhs
        ''',
        word_list=set(['block']),
    )

    # Start with scores at zero, and no taken tiles.
    assert_equal(game.score('blue'), 0)
    assert_equal(game.score('red'), 0)
    assert_equal(game.locked('blue'), [])
    assert_equal(game.locked('red'), [])

    # Play a word that locks a tile.
    game.play(
        'blue',
        [(3, 3), (4, 2), (3, 2), (4, 3), (4, 1)], # "lock"
    )

    assert_equal(game.score('blue'), 5)
    assert_equal(game.score('red'), 0)
    assert_equal(game.locked('blue'), [(4, 2)])
    assert_equal(game.locked('red'), [])
