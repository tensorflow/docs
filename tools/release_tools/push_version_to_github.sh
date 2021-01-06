#!/bin/bash
# Run this from your github clone.
# It assumes you have tensorflow_docs as the "upstream" remote.

OLD_BRANCH=$1
NEW_BRANCH=$2

if [ -n "$OLD_BRANCH" ]; then
  echo "OLD_BRANCH=$OLD_BRANCH"
else
  echo '$OLD_BRANCH is unset' && exit;
fi

if [ -n "$NEW_BRANCH" ]; then
  echo "NEW_BRANCH=$NEW_BRANCH"
else
  echo '$NEW_BRANCH is unset' && exit
fi

# Print commands while running, and fail if a command fails
set -e
set -x

# Merge the previous releases's docs into the current.
git checkout master
git pull upstream master

git fetch upstream
git branch -D $NEW_BRANCH || echo "failed -> branch doesn't exist -> that\'s ok"
# Checkout the upstream branch, if it doesn't exist create it from master
git checkout  --track upstream/"$NEW_BRANCH" || (git checkout -b "$NEW_BRANCH")
# Merge the previous version. If that gives a merge-conflict, auto-resolve and commit.
git merge upstream/$OLD_BRANCH --message "merge $OLD_BRANCH" ||  (grep -l "<<<<<<<" -r | xargs git checkout --ours && git commit -am "merge $OLD_BRANCH")

# Overwrite the ditectory with the contents from tensorflow/en/versions
rm -rf site/en/api_docs/python
python ../tensorflow/tensorflow/tools/docs/generate2.py --output_dir=site/en/api_docs/python --code_url_prefix="https://github.com/tensorflow/tensorflow/blob/${NEW_BRANCH}/tensorflow"

# Commit and push to your github.
git add site/en/api_docs/
git commit -am "Update docs to $NEW_BRANCH"
git push -f origin $NEW_BRANCH
