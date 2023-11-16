#!/bin/bash

git status
echo "Do you wish to deploy the changes?"
select yn in "Yes" "No"; do
  case $yn in
    Yes ) git add . && git commit && git push && rm -rf public/ resources/ && hugo && firebase deploy;;
    No ) exit;;
  esac
  exit
done

