
#   git commands

#T# create a git repo in a folder with git init
git init

#T# see origin repository location (and remote repos) with git remote -v, v is for verbose output
git remote -v

#T# add a remote location with git remote add remoteName url
git remote add origin https://github.com/Polirecyliente/proy1

#T# remove a remote location with git remote rm remoteName
git remote rm origin

#T# fetch changes in remote repo with git fetch repo
git fetch origin

#T# see diff between branches with git diff repo1/branchA repo2/branchB
git diff master origin/master

#T# pull changes from a branch in a repo with git pull repo branch
git pull origin master

#T# push a given branch to a repo with git push repo branch
git push origin master

#T# create a git project within a project with git submodule add repo1, the submodule can be embedded in the main project:
git submodule add ./path/to/proy path/to/proy

#T# clone a git project with submodules with
# git submodule init; git submodule update
git submodule init
git submodule update

#T# list submodules a nested submodules with git submodule status --recursive
git submodule status --recursive

#T# remove a submodule
git submodule deinit submoduleName
git rm submoduleName
# delete submodule from .git/config
# remove submodule dir in .git/modules/submoduleName
rm -rf .git/modules/submoduleName

#T# unstage all staged files with git reset
git reset

#T# uncommit last commit with git reset --hard HEAD^
git reset --hard HEAD^

#T# set the git logs with git log
git log

#T# if the HEAD is detached, reattach with git checkout branch
git checkout master

#T# restore deleted or changed files with git restore fileNames
git restore .

#T# see a branch upstream with git branch -vv, the upstream appears in blue color (if nothing is blue, the branch has no upstream)
git branch -vv

#T# set a branch upstream repo with git push --set-upstream repo branch
git push --set-upstream origin master

#T# create a tag for a special commit, like a new version with 
# git tag -a tagName -m "tag message"
#T# the option -a makes an annotated tag (it has meta-data like date, etc). NOTE: the tag will NOT create a commit, it will be applied to the HEAD commit
git tag -a v1.0 -m "version 1.0"

#T# push tags to remote repo with the --tags flag
git push origin --tags

#T# delete a tag with git tag -d tagName
git tag -d v1.0

#T# see current user configuration with git config --list
git config --list

#T# change global user with the --global flag
git config --global user.name "New-user-name"
git config --global user.email "New-email@email.dom"

#T# change local user per project without the --global flag
git config user.name "New-user-name"
git config user.email "New-email@email.dom"

#T# save git password with git config credential.helper store
git config credential.helper store
#T# the password gets stored in the next login prompt (i.e. a pull, push, etc)