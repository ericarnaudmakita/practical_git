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
""" since we did not yet commit any commit to new branch, it's iso-forme with the master one
After creating the new branch and commited the commits, we need to use the command below
to be sure that the new branch is up-stream with the origin prior to push"""
git push --set-upstream origin new-feature

# NB: any commit we commit within that branch will stay in that branch instaed of the master branch
# For instance, we're going to create a new file called newFeature.py and commit it
touch newFeature.py
git add -A # staging 
git commit -m "add the file newFeature.py"
ls -a # will show newFeature.py in the content of the directory
# to verify what we say, we can checkout the master branch or another branch 
# and we will see that that file does not exist there
git checkout master
ls -a

# to create a branch and checkout directly we can use the following:
git checkout -b newFeature-2
# that will create the branch newFeature-2 and checkout to it directly
# in case we want to get back direcrtly to the branch we were before checkout 
git checkout -

# 6 - Sync branches with get merge
""" here we did a small example for a better understanding:
we fist create a new branch called: url-slug.
then we create a file call getURLSlug.py
then we will combined it back with our main master branch.
NB: before combining, we first need to checkout to the branch we want to combine (master)
our feature into"""

git checkout -b url-slugs
touch getURLSlug.py
git add -A
git commit -m "add url-slugs"
git checkout master
git merge url-slugs

""" here is the results of the merge
Updating 3132246..4092f6c
Fast-forward
 getURLSlug.py | 4 ++++
 1 file changed, 4 insertions(+)
 create mode 100644 getURLSlug.py"""

 # now we can check the status of our branch
 git status

 # and then push to the remote
 git push

 # now since we have merged our feature with the main branch we can now freely delete our branch
 git branch -d url-slugs

 # 7 - Resolve merge conflicts wirh git status
 """ here we want to update a feature getMonthName.py inside ou master branch,
 which was created longtime ago.
 """
 git add -A
 git commit -m "add some comments"
 git push # won't work because I did not pull the remote commit
 git pull # won't work because of the below conflict

"""remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
From https://github.com/ericarnaudmakita/practical_git
   17e22e0..02c1c3a  master     -> origin/master
Auto-merging getMonthName.py
CONFLICT (content): Merge conflict in getMonthName.py
Automatic merge failed; fix conflicts and then commit the result."""

# the above message appears when we change the local and remote file at the same
# line of code, so we need first to fix conflicts and then commit the result
git status

"""On branch master
Your branch and 'origin/master' have diverged,
and have 2 and 1 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
	both modified:   getMonthName.py

no changes added to commit (use "git add" and/or "git commit -a")"""

""" So here the above message shows that the unmerged file is getMonthName.py because
that aws both modified.
So we will first open the file in our local machine, and inspect it: as follow"""
def getMonthName():
<<<<<<< HEAD
	# use the list comprehension for such things
=======
    """ this function capitalizes the each month in the months liste"""
>>>>>>> 02c1c3a4d9ff4b41fa711f9d379bf618566be861
    months = ['january', 'february','march', 'april']
    converted_months = [x.title() for x in months]

    # use the list comprehension for such things
    
    return converted_months

 """ what does it says is that the first part :
 <<<<<<< HEAD
	# use the list comprehension for such things
=======
is our change, and the second part below the equal marker till >>> 02... is the remote change
From here we do have 3 cases:

1 - keep our changes and discard the remote changes
2 - discard our changes and keep the remote changes
3 -  we can keep a piece of each
We will be using the case 3
"""
git add -A
git commit -m "combined the comments"
git push

# 8 - Save uncommitted changes with git stash
""" let's say we create a new feature getEPLClubs.py where at the beggining we put 
top 6 clubs that we know, and then we are request to don't put the top 6 according to 
their names but rather according to the actual position, so we need to change out function
statments because this is considered as  a bug.
To fix that bug, we need to create a new branch. The issue here is that if we create new branch now
it will copy over the uncommit changes in our feature. Since we are not yet done with don't 
want to create a new commit because we want to our feature to work properly, therefore we 
will do the following"""

git add -A
git stash # will make our repos back to the stage before the bug (the uncommited changes are in .git)

# now we can create our new branch to fix the bug
git checkout -b hotfix-dashes # here we will fix the bug then we will switch to master and merge that branch to master







































