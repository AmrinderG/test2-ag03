#!/bin/bash
from github import Github
g = Github('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')
repo = g.get_repo('test-ag03')
setup_file = repo.get_contents("database_setup.py)

if [ ! -f setup_file ]; then
    echo "Database file not found, creating..."
    python setup.file
fi
gunicorn -w 4 -b 0.0.0.0:10000 Backend_api:app
