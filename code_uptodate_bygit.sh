#!/bin/sh

echo "**** update the code by git ****"

git reset --hard master
git clean -d -fx
git pull origin master
