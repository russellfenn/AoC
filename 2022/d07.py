"""
Day 07 - No Space Left on Device

We are given a list of `cd` commands, `ls` commands, and their outputs.
Construct a directory tree from the given commands.

I think a dataclass or two is the best way to go.
"""

from dataclasses import dataclass
from pprint import pprint


@dataclass
class File:
    """Represents a file in our directory listing."""
    name: str
    size: int

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __str__(self):
        return f"{self.name} (file, size={self.size})"

    def __repr__(self):
        return f'File(name="{self.name}", size={self.size})'


@dataclass
class Directory:
    """A directory that contains Files and/or other Directories"""
    name: str
    dirs: dict[str, 'Directory']
    files: list[File]
    depth: int

    def __init__(self, name: str, depth: int = 0):
        self.name = name
        self.dirs = {}
        self.files = []
        self.depth = depth

    def __str__(self):
        output: list(str) = list()
        output.append("  " * self.depth + "- " + f"{self.name} (dir)")
        for directory in self.dirs.values():
            output.append(str(directory))
        for file in self.files:
            output.append("   " * self.depth + "- " + str(file))
        return "\n".join(output)

    def __repr__(self):
        return f"""Directory(name="{self.name}", depth="{self.depth}", dirs={self.dirs}, files={self.files})"""

    def add_file(self, file: File):
        self.files.append(file)

    def add_directory(self, directory):
        directory.depth = self.depth + 1
        self.dirs[directory.name] = directory


# Type alias
Command = list[str]  # This will be the command and its output


def separate_commands(commands: list[str]) -> list[Command]:
    """Commands start with '$'. Return each command and its output
       as a list of strings.
    """
    output: list[list[str]] = list()
    buffer: list[str] = list()
    for line in commands:
        if line.startswith('$'):
            # finish last command and start a new one
            if buffer:
                output.append(buffer)
                buffer = list()
            buffer.append(line)
        else:
            buffer.append(line)
    if buffer:
        output.append(buffer)
    return output


def ls_command(dir_name: str, depth: int, listing: Command) -> Directory:
    """An ls command will look something like
       $ ls
       584 i
       dir d
    """
    d = Directory(name=dir_name, depth=depth)
    for line in listing[1:]:  # skip the first line, it's our cd command
        if line.startswith('dir'):
            _, dirname = line.split(' ')
            d.add_directory(Directory(name=dirname, depth=depth+1))
        else:
            size, filename = line.split(' ')
            d.add_file(File(name=filename, size=int(size)))
    return d


def command_output_parser(commands: list[Command]) -> Directory:
    """Work through the commands to build a directory tree."""
    cwd: list[str] = list()  # store the path down to the cwd
    directory: Directory = None
    for command in commands:
        if command[0].startswith('$ cd'):
            print(command)
        if command[0] == "$ ls":  # the command itself
            directory = ls_command()
            print(directory)
    return directory


if __name__ == "__main__":
    d = Directory(name="/")
    d.add_file(File("f", 29116))
    d.add_file(File("g", 2557))
    d.add_file(File("h.lst", 62596))
    e = Directory(name="e")
    e.add_file(File(name="i", size=584))
    d.add_directory(e)
    pprint(d)
    print(d)
