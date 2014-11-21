#!/usr/bin/env python
#
# Runs all hooks with names starting with this script's name.
#
# Executes all hooks, even if some fail, collecting their exit codes
# and only exiting successfully if all sub-hooks have succeeded.

import glob
import os
import stat
import subprocess
import sys


def is_executable(filename):
    try:
        return stat.S_IXUSR & os.stat(filename)[stat.ST_MODE]
    except OSError:
        # Likely a broken link.
        return False


# Only hooks with file name starting with the prefix will be run.
prefix = os.path.basename(__file__)

# Git directory, in most cases just '.git'.
git_cmd = ('git', 'rev-parse', '--git-dir')
git_dir = subprocess.check_output(git_cmd).strip()

# Find hooks to be run, making sure to exclude this one ;-)
pattern = os.path.join(git_dir, 'hooks', prefix + '?*')
hooks = filter(is_executable, glob.iglob(pattern))

# Run all and collect their exit codes.
args = sys.argv[1:]
exit_codes = [subprocess.call([hook] + args) for hook in hooks]

# Return zero only if all sub-hooks succeeded.
sys.exit(any(exit_codes))
