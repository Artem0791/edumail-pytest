import pytest

fruits = ('apple', 'orange', 'pineapple', 'banana', 'peach',)
fruits_count = {'apple': 17, 'orange': 23, 'pineapple': 19, 'banana': 11, 'peach': 9}


def test_check_item_in_tuple():
    x = 'banana'
    assert x in fruits


# negative test
def test_try_append_item_in_tuple():
    try:
        fruits.append('watermelon')
        x = 'watermelon'
        assert x in fruits
    except AttributeError:
        pass


def test_letter_a_in_item():
    for f in fruits:
        assert 'a' in f


def test_check_item_count():
    expected_count = 17
    assert fruits_count['apple'] == expected_count


def test_append_new_fruit():
    new_fruit = {'kiwi': 7}
    fruits_count.update(new_fruit)
    assert 'kiwi' in fruits_count
    fruits_count.popitem()


@pytest.mark.parametrize("min_value", [0, 3, 5, 6, 7, 8, 9])
def test_check_fruits_count(min_value):
    for f in fruits_count.values():
        assert f >= min_value
