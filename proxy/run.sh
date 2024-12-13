#!/bin/sh

set -e

envsubst < /etc/nginx/default.conf.tbl > /etc/nginx/conf.d/default.conf
nginx -g 'daemon off;'