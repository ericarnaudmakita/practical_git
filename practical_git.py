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