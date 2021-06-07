
#   Git commands

#T# Table of contents

#C# Basic usage
#C# Management of remote locations
#C# Working with a remote repository
#C# Commits and staging area
#C# Branches
#C# Submodules
#C# Configuration
#C# Git Large File Storage (LFS)

#T# Beginning of content

#C# Basic usage

# |-------------------------------------------------------------
#T# create a git repository in a given directory
git init

#T# clone a git repository that is stored in a given URL, this creates a directory with the name of the project
# SYNTAX git clone url1
git clone https://github.com/UPBGE/upbge.git #| creates a dir named 'upbge'

#T# after modifying files in a git project, add them to the staging area
git add -A #| this adds all the modified files to the staging area

#T# create a new commit of the project
git commit -m "commit message"

#T# if the project is stored as a remote repository, push the new commits to said repository
git push

#T# see the git log, it shows the former commits with a bit of their metadata
git log
# |-------------------------------------------------------------

#C# Management of remote locations

# |-------------------------------------------------------------
#T# see origin repository location (and remote repos)
git remote -v #| -v is for verbose

#T# add a remote location
# SYNTAX git remote add remote1 url1
git remote add origin https://github.com/Polirecyliente/proy1

#T# remove a remote location
# SYNTAX git remote rm remote1
git remote rm origin

#T# set the url of a given remote, this allows for example to change from HTTPS to SSH access, by changing the protocol from https to git
# SYNTAX git remote set-url remote1 url1
git remote set-url origin https://github.com/Polirecyliente/proy1 #| use https
git remote set-url origin git@github.com:Polirecyliente/proy1.git #| use git for ssh
# |-------------------------------------------------------------

#C# Working with a remote repository

# |-------------------------------------------------------------
#T# fetch changes in a remote repository
# SYNTAX git fetch remote1
git fetch origin

#T# pull changes from a branch in a repository
# SYNTAX git pull remote1 branch1
git pull origin master

#T# push a given branch to a repository
# SYNTAX git push remote1 branch1
git push origin master
# |-------------------------------------------------------------

#C# Commits and staging area

# |-------------------------------------------------------------
#T# unstage all staged files
git reset

#T# uncommit the most recent commit, preserving the changes made in the most recent commit
git reset HEAD^

#T# uncommit the most recent commit, deleting any changes made in the most recent commit
git reset --hard HEAD^

#T# reattach HEAD to the most recent commit of a given branch
# SYNTAX git checkout branch1
git checkout master

#T# restore deleted or changed files that have not been staged
# SYNTAX git restore path1/file1
git restore . # restores files recursively

#T# create a tag for the HEAD commit, e.g. for a new version 
# SYNTAX git tag -a tag_name1 -m "tag message"
#T# the -a flag makes an annotated tag (it has meta-data like date, etc)
git tag -a v1.0 -m "version 1.0"

#T# push tags to a remote repository with the --tags flag
git push origin --tags

#T# delete a tag
# SYNTAX git tag -d tag_name1
git tag -d v1.0
# |-------------------------------------------------------------

#C# Branches

# |-------------------------------------------------------------
#T# see the branch upstream repository
# SYNTAX git branch -vv
#T# the upstream appears in blue color (if nothing is blue then the branch has no upstream)
git branch -vv

#T# set a branch upstream repository
# SYNTAX git push --set-upstream remote1 branch1
git push --set-upstream origin master

#T# see the differences between two branches
# SYNTAX git diff remote1/branch1 branch2
git diff master origin/master

#T# Check out a particular commit, so the directory structure and files revert to how they were in that commit.
git checkout 'commit_hash1'

#T# 'commit_hash1' is a string with at least the first four characters of a commit's hash. A commit's hash can be seen with `git log`, commonly in orange color, for example 'commit 4c7bae4b36c21f88c9ba1bf8b24be3a5927c8fbd', the hash appears in from of the word 'commit'

#T# Create a new branch and check it out.
git branch new_branch1
git checkout new_branch1

#T# Merge two branches together.
git checkout branch1
git merge branch2

#T# This merges the commits from both branches, and places the result as a new commit on top of `branch1`

#T# Rebase a branch on top of its base branch. A rebase applies the commits of a branch, on top of its base branch.
git rebase base1 branch1

#T# This is commonly done to reapply the commits of a branch, on top of the master branch
git rebase master branch1
# |-------------------------------------------------------------

#C# Submodules

# |-------------------------------------------------------------
#T# create a git project within a project, a submodule
# SYNTAX git submodule add project1
#T# the submodule can be embedded in the main project
git submodule add ./path/to/project1 path/to/project1

#T# clone a git project with submodules
git submodule init
git submodule update

#T# list submodules and nested submodules
git submodule status --recursive

#T# remove a submodule with the following four steps
# SYNTAX git submodule deinit submodule1
# SYNTAX git rm submodule1
# SYNTAX delete submodule from the .git/config file
# SYNTAX rm -rf .git/modules/submodule1
# |-------------------------------------------------------------

#C# Configuration

# |-------------------------------------------------------------
#T# see current user configuration
git config --list

#T# change global user with the --global flag
git config --global user.name "New-user-name"
git config --global user.email "New-email@email.dom"

#T# change local user per project without the --global flag
git config user.name "New-user-name"
git config user.email "New-email@email.dom"

#T# save the git password of the user
git config credential.helper store
#| the password gets stored in the next login prompt (i.e. a pull, push, etc)
# |-------------------------------------------------------------

#C# Git Large File Storage (LFS)

# |-------------------------------------------------------------
#T# Git LFS is a git related application that facilitates the use of large files in repositories, because with it, only a pointer to the latest version of a large file is pulled (and not all of its versions), the actual large file is stored in a cache, if another version is wanted it is pulled via git checkout

#T# install the git lfs package
sudo apt install git-lfs

#T# change to the dir of a repository and install lfs for that repository, so it can be used with that project
cd dir1/project1 #| dir1/project1 represents the relative path of the root directory of project1
git lfs install

#T# tracked files are treated as large files
# SYNTAX git lfs track file1
git lfs track "*.png" #| tracks .png files

#T# get the actual files instead of their file pointers
git lfs fetch
git lfs pull

#T# the .gitattributes file must be part of the project if it already isn't
# |-------------------------------------------------------------