# Works on my machine

## Three places, and Github
Think of sending a parcel. Your desk is where you work on thing. The open box is what you have chosen to send. Taping the box shut and writing a label makes it a parcel. The post office is where it goes in the end. Git has the same four places:
1. Your desk - The working folder: the files you edit.
2. The open box - The staging area: what goes into the next commit.
3. The sealed parcel, with its label - A commit in the history, write its message.
4. The post office - Github.

A change goes through three places on your computer before it reaches Github:
Working folder => git add => Staging area => git commit => History (saved commits) => git push => Github.
The first three places are on your computer. Only git push sends anything to Github.

- `git add` puts a change in the staging area: it marks it for the next commit.
- `git commit` saves everything in the staging area as one point in the history.
- `git push` sends you new commits to Github.
- `git status` shows what has changed, and what is staged.
- `git diff` shows the changed lines.
- `git log` shows the history. 
- None of `git status`, `git diff` and `git log` change anything.

## Good commit messages
A commit message says what the change does, so that someone can read the history a year later. In this course, as in mmost projeects: short, with a capital letter first, and written as an order.
Read it as *this commit will... : this commit will fix the price per square meter for empty rows*.

- Fix => Fix the price per square meter for empty rows.
- Changes => Handle missing values in the cleaning step.
- Updated the file after meeting => Describe the project.

## Branches
A branch is a line of work on its own. You can try something on a branch while main stays as it was, and merge the branch into main when its ready:
- `git switch -c add-notes` makes a new branch called add-notes, and moves you to it. `-c` (create) is what makes the branch. Without it, `git switch` only moves to a branch that already exists.
- `git switch main` moves you back to main.
- `git merge add-notes`, run on main, brings the branch's commits to main.
- `git branch -d add-notes` deletes the branch after the merge. `-d` (delete) is safe: Git refuses if the branch has commits that are not merged yet.

## Conflicts
If two branches change the same line, Git cannot choose for you. the merge stops with a conflict, and Git write both versions into the file, between markers:

```text
<<<<<<< HEAD
the line as it is on the branch you are on
=======
the line as it is on the branch you merge
>>>>>>> better-title
```

You resolve it: edit the file so that it says what it should, and delete the three marker lines.
Then `git add` the fine, and `git commit`.

## requirements.txt
Your project needs packages, like pytest now and pandas later. requirements.txt lists them, with exact versions, so that anyone can install the same ones:
- `python -m pip freeze > requirements.txt` writes every package in your virtual environment to the file. `-m` (module) has Python run one of its modules, so `python -m pip` is the pip of the Python you are using: the one in your virtual environment.
- `python -m pip install -r requirements.txt` installs every package in the file. `-r` (requirements) has pip read the list of packages from a file.

`.venv` stays out of Git, and requirements.txt goes in. The file is small, and it is all someone needs to build the same environment.
