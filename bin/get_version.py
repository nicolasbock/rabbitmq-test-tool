#!/usr/bin/env python3

import subprocess


def get_version():
    """Get current version from git."""
    try:
        git = subprocess.run(['git', 'describe', '--tags'],
                             stdout=subprocess.PIPE, universal_newlines=True,
                             check=True)
        full_version = git.stdout.strip()
    except AttributeError:
        git = subprocess.Popen(['git', 'describe', '--tags'],
                               stdout=subprocess.PIPE, universal_newlines=True)
        stdout_raw, _ = git.communicate()
        git.wait()
        full_version = stdout_raw.strip()
    except Exception:
        print("Cannot read version")
        raise
    if full_version[0] == 'v':
        full_version = full_version[1:]

    try:
        git = subprocess.run(['git', 'describe', '--tags', '--abbrev=0'],
                             stdout=subprocess.PIPE, universal_newlines=True,
                             check=True)
        abbreviated_version = git.stdout.strip()
    except AttributeError:
        git = subprocess.Popen(['git', 'describe', '--tags', '--abbrev=0'],
                               stdout=subprocess.PIPE, universal_newlines=True)
        stdout_raw, _ = git.communicate()
        git.wait()
        abbreviated_version = stdout_raw.strip()
    except Exception:
        print("Cannot read version")
        raise
    if abbreviated_version[0] == 'v':
        abbreviated_version = abbreviated_version[1:]

    local_version = full_version.replace(abbreviated_version, '')

    if len(local_version) > 0:
        version = (abbreviated_version + '+'
                   + local_version[1:].replace('-', '.'))
    else:
        version = abbreviated_version

    return version


if __name__ == "__main__":
    print(get_version())
