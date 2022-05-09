echo off
chcp 65001

set branch="master"
set input=%1%
git add .
git commit -m %input%
git push -u origin %branch%

echo "--- your input content: %input%"
