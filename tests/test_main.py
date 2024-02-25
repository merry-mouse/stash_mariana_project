import string

import pytest

from my_project.main import generate_random_string


def test_generate_random_string_length():
    # Checking if the output str has expected length
    length = 20
    result = generate_random_string(length)
    assert len(result) == length
