from d06 import find_start_of_packet_marker

part_1_examples = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
]


def test_part_1_examples():
    """Test the simple start of packet finder"""
    for signal, start in part_1_examples:
        assert find_start_of_packet_marker(signal) == start


part_2_examples = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
]

def test_part_2_examples():
    """Test the simple start of packet finder"""
    for signal, start in part_2_examples:
        assert find_start_of_packet_marker(signal, packet_len=14) == start
