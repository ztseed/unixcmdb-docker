#!/bin/bash

ps -ef | grep gunicorn | grep -v color | awk '{print $2}' | xargs kill -9

echo "webservice stop!"
