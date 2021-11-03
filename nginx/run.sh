#!/bin/sh

envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf

nginx -g "daemon off;"
