from d07 import (
    File,
    Directory,
    separate_commands,
    command_output_parser,
    ls_command,
)


EXAMPLE_COMMANDS = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

EXAMPLE_TREE_OUTPUT = """- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)
"""


def test_simple_file():
    f = File(name="/", size=84)
    assert repr(f) == 'File(name="/", size=84)'


def test_simple_directoryy():
    d = Directory(name="/")
    d.files.append(File("f", 29116))
    # d.files.append(File("g", 2557))
    # d.files.append(File("h.lst", 62596))
    assert repr(d) == 'Directory(name="/", dirs=[], files=[File(name="f", size=29116)])'


def test_command_separator():
    """Verify that the separate_commands method correctly
       splits the input into commands and their output.
    """
    commands: list[list[str]] = separate_commands(EXAMPLE_COMMANDS.splitlines())
    assert len(commands) == 10
    assert len(commands[0]) == 1  # $ cd /
    assert len(commands[1]) == 5


def test_ls_commans():
    """Ensure a ls command works"""
    ls_command_output: list[str] = [
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
    ]
    root_dir: Directory = ls_command(dir_name="/", depth=0, listing=ls_command_output)
    expected = Directory(name="/", depth=0)
    expected.add_directory(Directory(name="a", depth=1))
    expected.add_file(File(name="b.txt", size=14848514))
    expected.add_file(File(name="c.dat", size=8504156))
    expected.add_directory(Directory(name="d", depth=1))
    assert root_dir == expected
