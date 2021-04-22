# initialize new repo
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

# Now, in case we have to clone a remote repo, we do the following
# git clone follows by the link of the repos, example:
git clone https://github.com/ericarnaudmakita/practical_git.git

# Add or stage all the changes that we made
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
git add -A
git status
git commit -m "add lignes from commit our changes"
# at this stage, I did not push anything yet to my remote repogit
git status

"""On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean"""
git push
git status