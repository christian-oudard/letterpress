from nose.tools import assert_equal

from letterpress import Game

def test_lock():
    # Test the way that locked tiles are created.

    game = Game(
        '''
        xxxxx
        xxxxk
        xxxol
        xxxbc
        xxxxx
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

def test_use_locked():
    # Don't change the color of locked tiles.

    game = Game(
        '''
        capxx
        txxxx
        xxxxx
        xxxxx
        xxxxx
        ''',
        word_list=set(['cat', 'cap']),
    )

    # Play a word that locks a tile.
    game.play(
        'blue',
        [(0, 0), (1, 0), (0, 1)], # "cat"
    )
    assert_equal(game.tiles[(0, 0)].locked, True)
    assert_equal(game.tiles[(0, 0)].color, 'blue')
    assert_equal(game.score('blue'), 3)
    assert_equal(game.score('red'), 0)

    # Play a word using a locked tile. Its color doesn't change.
    game.play(
        'red',
        [(0, 0), (1, 0), (2, 0)], # "cap"
    )
    assert_equal(game.tiles[(0, 0)].locked, False)
    assert_equal(game.tiles[(0, 0)].color, 'blue')
    assert_equal(game.score('blue'), 2)
    assert_equal(game.score('red'), 2)
