#! /bin/bash

res=$(git remote -v | grep upstream)

if [ -z "$res" ]
then
    git remote add upstream "https://github.com/Harvard-CS145/cs145-23-project1.git"
fi

git pull upstream main --allow-unrelated-histories