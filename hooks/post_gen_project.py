"""
Does the following:

1. Inits git if used
2. Deletes dockerfiles if not going to be used
3. Deletes config utils if not needed
"""
from __future__ import print_function

import os
from subprocess import Popen

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def exec(cmds):
    for command in cmds:
        git = Popen(command, cwd=PROJECT_DIRECTORY)
        git.wait()


def init_git():
    GIT_COMMANDS = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "commit", "-a", "-m", "Initial Commit."]
    ]
    exec(GIT_COMMANDS)


def init_gomod():
    GIT_COMMANDS = [
        ["go", "mod", "init", 'github.com/{{ cookiecutter.author }}/{{ cookiecutter.project_name }}'],
    ]
    exec(GIT_COMMANDS)


def init_cobra():
    GIT_COMMANDS = [
        ["go", "get", "github.com/spf13/cobra/cobra"],
        ["cobra", "init", "--pkg-name", 'github.com/{{ cookiecutter.author }}/{{ cookiecutter.project_name }}'],
    ]
    exec(GIT_COMMANDS)


def goGet(pkg):
    GIT_COMMANDS = [
        ["go", "get", "-v", pkg],
    ]
    exec(GIT_COMMANDS)


# default
init_git()
init_gomod()

# optional
if '{{ cookiecutter.use_cobra_cmd }}'.lower() == 'y':
    init_cobra()

if '{{ cookiecutter.web_framework }}'.lower() != 'none':
    goGet('{{ cookiecutter.web_framework }}')

if '{{ cookiecutter.orm }}'.lower() != 'none':
    goGet('{{ cookiecutter.orm }}')

if '{{ cookiecutter.redis }}'.lower() != 'none':
    goGet('{{ cookiecutter.redis }}')
