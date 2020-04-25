#!/bin/bash

# Install needed translation packages
# Usage: zigzag-languages [-y]

lang_short=${LANG:0:2}
lang_full=${LANG:0:5}

zypper="zypper --no-refresh"
awk_filter="/-lang |-$lang_short |-$lang_full /{print \$4}"
to_install=$($zypper packages -u --recommended | awk "$awk_filter" | tr '\n' ' ')

if [ -n "$to_install" ]; then
    sudo $zypper install $@ $to_install
fi
