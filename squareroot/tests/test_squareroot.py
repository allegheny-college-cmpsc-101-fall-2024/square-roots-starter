"""Test suite to ensure that each function words correctly."""

from pytest import approx

from squareroot import __version__

from squareroot import main

# Reference for the use of pytest.approx:
# https://docs.pytest.org/en/7.1.x/reference/reference.html#pytest-approx

# TODO: Write docstring comments for each of these test cases!
# TODO: Make sure that you understand how these test cases work!

def test_version():
    assert __version__ == "0.1.0"


def test_exhaustive_square_root():
    square_root_tuple = main.compute_square_root_exhaustive(25)
    assert square_root_tuple[0] is True
    assert square_root_tuple[1] == approx(4.999)
    assert square_root_tuple[2] == 49990


def test_efficient_square_root():
    square_root_tuple = main.compute_square_root_efficient(25)
    assert square_root_tuple[0] is True
    assert square_root_tuple[1] == approx(5.000305)
    assert square_root_tuple[2] == 13
