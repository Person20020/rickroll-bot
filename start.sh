#!/bin/bash
source /home/kojii/rickroll-bot/venv/bin/activate
cd /home/kojii/rickroll-bot/app
gunicorn -w 2 -b 127.0.0.1:2005 --access-logfile /home/kojii/rickroll-bot/logs/access.log --error-logfile /home/kojii/rickroll-bot/logs/error.log app:app
