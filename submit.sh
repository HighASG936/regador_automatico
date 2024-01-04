#/usr/bin/bash

#Check repo's status
git status

#Submit to my git server
git checkout master
git add .
read -p "Name of commit: " name_commit
git commit -m " ${name_commit} "
git push origin master

#submit to github
git checkout main
git pull origin master
git push github main

#Turn back to master branch
git checkout master

#Check on log
git log --oneline
