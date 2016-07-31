#!/bin/sh

echo "**** update the code by git ****"

git clean -d -fx
git pull origin master
