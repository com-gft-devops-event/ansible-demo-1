#!/usr/bin/env bash

FILTER=( 
  --filter "label=CUSTOMER=com.gft.devops-event" \
  --filter "label=PROJECT=com.gft.devops-event.ansible-demo-1" \
)

while read c ; do
  #docker container stop -f "$c" 
  docker container stop "$c"
done < <( docker container ls "${FILTER[@]}" --format "{{json .ID}}" | sed 's/"//g' )

while read c ; do
  docker container rm "$c"
done < <( docker container ls -a "${FILTER[@]}" --format "{{json .ID}}" | sed 's/"//g' )

while read i ; do
  docker image rm "$i"
done < <( docker image ls "${FILTER[@]}" --format "{{json .ID}}" | sed 's/"//g' )