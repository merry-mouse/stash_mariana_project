from my_project.main import generate_random_string


def test_generate_random_string_length():
    # Checking if the output str has expected length
    length = 20
    result = generate_random_string(length)
    assert len(result) == length


def test_generate_random_string_randomness():
    # Checking if all generated strings are different
    result1 = generate_random_string()
    result2 = generate_random_string()
    result3 = generate_random_string()
    result4 = generate_random_string()
    result5 = generate_random_string()
    random_set = {result1, result2, result3, result4, result5}
    assert len(random_set) == 5
