#!/bin/bash

while getopts p: option; do
  case "$option" in
    H) HOST=${OPTARG} ;;
    p) PORT=${OPTARG} ;;
  esac
done

APP_HOST=${HOST:-127.0.0.1}
APP_PORT=${PORT:-8000}

cat <<EOF
App Host: $APP_HOST
App Port: $APP_PORT
EOF
read -rp "App Configuration. Continue (y/n) :" config_complete

if [ "$config_complete" != "y"  ]; then
  echo "Incorrect Configuration. Exit..."
  exit 1
fi

export APP_HOST=$APP_HOST APP_PORT=$APP_PORT

docker-compose up app
