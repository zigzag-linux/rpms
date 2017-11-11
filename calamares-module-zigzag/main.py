#!/usr/bin/python3
from libcalamares.utils import target_env_call

def pretty_name():
    return "Run postinstall job for Zigzag"


def run():
    return_code = target_env_call(['zigzag-write-configuration', '--force', 'postinstall'])

    if return_code != 0:
        return (
            "Failed to run zigzag-write-configuration on the target",
            "The exit code was {}".format(return_code)
            )
