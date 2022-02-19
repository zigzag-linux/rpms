#!/usr/bin/env bash

set -e
declare -r VERSION_COMMENT="Upload from GitHub"
declare -r PROJECT="home:mkrwc:zigzag:devel"

upload_file()
{
    local package=$1; shift
    local path=$1; shift
    local file=`basename $path`

    curl --silent --show-error --fail \
    --request PUT \
    --url "https://api.opensuse.org/source/${PROJECT}/${package}/${file}?rev=upload" \
    --header "Authorization: Basic ${AUTH_SECRET}" \
    --header "Content-Type: text/plain" \
    --data-binary "@${path}"
}

create_commit()
{
    local package=$1; shift

    curl --silent --show-error --fail \
    --request POST \
    --url "https://api.opensuse.org/source/${PROJECT}/${package}?cmd=commit" \
    --data-urlencode "comment=${VERSION_COMMENT}" \
    --header "Authorization: Basic ${AUTH_SECRET}"
}

if [ $# -eq 0 ]; then
    exit 0
fi

IFS=',' read -ra FILES <<< "$1"
readarray -t SORTED < <(printf '%s\n' "${FILES[@]}" | sort)

for ((index=0; index < ${#SORTED[@]}; index++)); do
    this_file=${SORTED[index]}
    this_package=`basename $(dirname $this_file)`
    next_file=${SORTED[index+1]:-NO_FILE}
    next_package=`basename $(dirname $next_file)`

    upload_file $this_package $this_file

    if [ $this_package != $next_package ]; then
        create_commit $this_package
    fi
done
