#!/usr/bin/env python
#
# Git hook passing changes through flake8.
#
# Almost the same as "flake8 --install-hook", except that it ignores
# environment variables and prints a heading with version.

import sys

from flake8 import __version__ as flake8_version
from flake8.hooks import git_hook

if __name__ == '__main__':
    # If you see the hook scanning non-Python files and ignoring style
    # settings, make sure you have the newest flake8 installed for the
    # default Python version.
    print("Scanning with flake8 {}".format(flake8_version))
    sys.exit(git_hook(strict=True, lazy=True))
