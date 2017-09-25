"""
acc

Usage:
  acc -h | --help
  acc --version
  acc validate [<file>]
  acc generate

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  acc validate                      Will by default search for a 'acc.yml' file
  acc validate descriptor.yml       Will validate a the 'descriptor.yml' file 

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/pjuarezd/acc-cli
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import acc.commands
    options = docopt(__doc__, version=VERSION)

    for (k, v) in options.items(): 
        if hasattr(acc.commands, k) and v:
            module = getattr(acc.commands, k)
            acc.commands = getmembers(module, isclass)
            command = [command[1] for command in acc.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()