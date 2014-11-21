#!/usr/bin/env bash
#
# Installs Django's git hooks. Requires Bash 4.

# Hooks that are to be installed; a {destination: source} dictionary
# with base names of files.
declare -A hooks=(
    ['pre-commit']='run_all.sh'
    ['pre-commit-flake8']='flake8_changed.py')

# Where are the source files and where should they be linked from.
src_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/git_hooks/"
dest_dir="$(git rev-parse --git-dir)/hooks/"

# Create a symbolic link in .git/hooks for each hook.
for dest_name in "${!hooks[@]}"; do
    src_name="${hooks[$dest_name]}"
    src_path="${src_dir}${src_name}"
    dest_path="${dest_dir}${dest_name}"

    if [[ -e $dest_path ]]; then
        if [[ ! $src_path -ef $dest_path ]]; then
            echo "Skipping .git/hooks/$dest_name as it already exists," \
                 "please remove it or add a suffix if you would like" \
                 "to run a custom hook together with Django's hooks."
        fi
    else
        echo "Installing $src_name as .git/hooks/$dest_name."
        ln --symbolic -- "$src_path" "$dest_path"
    fi
done
