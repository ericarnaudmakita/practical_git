# 1 - Create local repos with git init
git init

# check what's inside the repo
ls -a

# remove git from a project
rm -rf .git/

#the best practice will be to use the 
# the same name of the project folder as repository name

# push an existing repository from the command line
git remote add origin https://github.com/ericarnaudmakita/practical_git.git

# check if we setup correctly the remote repo
git remote -v

# 2 - Copy remote repos to local machines with git clone
git clone https://github.com/ericarnaudmakita/practical_git.git

# 3 - Capture the history snapshots with git add/commit/push
# staging
git add -A

# we can check statuts of our branch
git status

# Commit our changes
git commit - m "add some lignes"

# check the status of our repos
git status

# push the first commit 
git push --set-upstream origin master

# check the status of our repos
git status

# as soon as we updated one file, we can check it out by using the git status and git will let us know 
# about the way to go, example follow: I just change the file and use git status, and below is the result:

"""On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   practical_git.py

no changes added to commit (use "git add" and/or "git commit -a")"""

# since I want to commit and push my updates, then I'll do the following:
git add -A # staging 
git status
git commit -m "add lignes from commit our changes" # commit our changes
# at this stage, I did not push anything yet to my remote repogit
git status

"""On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean"""
git push
git status

# to add a specific file, we don't use git add -A but 
git add file_name
git commit -m "add file_name" # commit our changes
git push

# Sync local and remote repos with git pull
git pull

""" git pull is in fact a short command of two other commands that we can run individualy if wa want:
1 - git fetch : that tells our locam repo to grab the latest changes from our remote repo and store them locally into our local repo without 
including them into our local code yet

2 -  git merge : which tells our local repo to merge in the chnages we get from git fetch into our local code"""

# 4 - Isolate feature development with git branch
git branch new-feature

# 5 - View our branch on repos by typing the following:
git branch

# switch to different branch 
git checkout new-feature
