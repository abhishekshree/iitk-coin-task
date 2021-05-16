#!/bin/sh

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"rollno":"200028"}' \
  http://localhost:8080/coins