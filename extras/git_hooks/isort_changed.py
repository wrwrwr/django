#!/usr/bin/env python
#
# Git hook passing changes through isort.
#
# The hook interface was chosen to match flake8.hooks.git_hook.
# Printing diffs only works with isort > 3.9.0.

import subprocess
import sys

from isort import SortImports, __version__ as isort_version


def git_hook(strict=False, lazy=False, show_diffs=False):
    """
    Runs ``isort`` on added, copied and modified files.

    :param bool strict: if True, the number of files that have
        incorrectly sorted imports is used as the return value, so
        the hook will have a non-zero exit code if there were any
    :param bool lazy: lets you use ``git commit -a``
    :param str show_diffs: prints sorting changes needed for each file
    """
    list_files_cmd = ['git', 'diff-index', '--name-only', '--diff-filter=ACM', 'HEAD']
    if not lazy:
        # Process all files, including those that haven't been staged.
        list_files_cmd.append('--cached')
    files = subprocess.check_output(list_files_cmd).splitlines()

    incorrect_count = 0
    for filename in files:
        if SortImports(filename, check=True, show_diff=show_diffs).incorrectly_sorted:
            incorrect_count += 1

    if strict:
        return incorrect_count
    else:
        return 0


if __name__ == '__main__':
    print("Scanning with isort {}".format(isort_version))
    sys.exit(git_hook(strict=True, lazy=True, show_diffs=True))
