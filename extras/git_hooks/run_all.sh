#!/usr/bin/env bash
#
# Runs all hooks with names starting with this script's name.
#
# Executes all hooks, even if some fail, collecting their exit codes
# and only exiting successfully if all sub-hooks have succeeded.

prefix="$(basename $0)"
hooks_dir="$(git rev-parse --git-dir)/hooks/"
exit_codes=()

for hook in "$hooks_dir"*; do
    if [[ $hook =~ ^"${hooks_dir}${prefix}". && -x $hook ]]; then
        "$hook" "$@"
        exit_codes+=($?)
    fi
done

for exit_code in "${exit_codes[@]}"; do
    [[ $exit_code == 0 ]] || exit $exit_code
done
