from d01 import solve_two, solve_generic

sample_input_list = [1721, 979, 366, 299, 675, 1456]


# the simple two element one works
def test_two_elemet():
    assert solve_two(sample_input_list) == 514579


# We should get the same value using the generic solver
def test_generic_solver():
    assert solve_generic(sample_input_list, 2020, 2) == 514579
    assert solve_generic(sample_input_list, 2020, 3) == 241861950
