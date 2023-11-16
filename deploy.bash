#!/bin/bash

git status && git add . && git commit && git push && rm -rf public/ resources/ && hugo && firebase deploy