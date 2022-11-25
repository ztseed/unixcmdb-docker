#!/bin/bash
python /usr/local/bin/gunicorn unixcmdb.wsgi:application \
--bind 127.0.0.1:8000 \
--workers 2 \
--timeout 30 \
--daemon \
--access-logfile unixcmdb_access.log \
--error-logfile unixcmdb_error.log

echo "webprocess started :"
ps -ef | grep gunicorn | grep -v color 


