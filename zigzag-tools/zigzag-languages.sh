#!/usr/bin/env bash

# Install needed translation packages
# Usage: zigzag-languages [-y]

declare -r FILE_INSTALLED=$(mktemp)
declare -r FILE_LANGPACKS=$(mktemp)
declare -r ZYPPER='zypper --no-refresh'

export LC_ALL="C"

rpm -qa --qf "%{NAME}-lang\n" |
    sort >$FILE_INSTALLED

$ZYPPER -x search -u "*-lang"      |
    grep -oP '(?<=name=").*?(?=")' |
    sort >$FILE_LANGPACKS

to_install=$(comm -12 $FILE_INSTALLED $FILE_LANGPACKS)
rm $FILE_INSTALLED $FILE_LANGPACKS

if [ -n "$to_install" ]; then
    sudo $ZYPPER install $@ $to_install
fi
