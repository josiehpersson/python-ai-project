## What the repo must contain
- The code and the data: Everything needed to go from raw data to a trained model. The history should show that the work grew over time, not a single commit in January.
- The report in README.md: Two or four pages about the problem, the data, the model, the result, and what the model cannot do.
- A prediction step: A script, or a small app, that loads the saved model and makes a predicition for new input.

## The report
It should answer six questions:
- Which problem? What do you predict and is it classification or regression?
- Which dataset, and where from? With a link.
- How did you prepare the data? This is where the table from Module 7 belongs: what was wrong, what you did and why.
- Which model, and why?
- How good did it get? With metrics that suit the problem, interpreted in words, not just printed.
- What can it not do? (See The reflection below).

### The prediction step
A script that loads the saved model and answers for new input, for example:
python scripts/predict.py --living-area 68 --rooms 3 --district Majorna

What matters: The prediction step ,ust never see the training data. It loads a finished model from a file. That is the difference between a notebook that happens to work and something that can be used. A command-line script is enough for G. If you want to build an interface, a small web page with Streamlit is fine too.
- If the model file is larger than about 50mg, it should not be in the repository. Github does not accept files over 100mb. Add models/ to .gitignore, and write in README.md how the model is created by train.py, or your own training script.
- Nothing in the project may require a paid account, an API key or a cloud service. Everything must run on your computer.
- Language. You may write the report in english or swedish. The vode, with its variable and file names, is in english, as in the modules.
- You may use AI, as you would at work. For example to debug, to read documentation, or to have something explained. You are responsible for everything in your repository, including what an AI tool suggested: if you do not understand a line, find out what it does before you keep it. Being able to explain every part of your code is one of the requirements for G.

### The reflection
This is the part most people underestimate. Do not write about AI in general. Write about your model. 
- For which inpts is it most wrong, and why?
- Which groups or cases are under-represented in your data?
- What would happen if someone actually made decisions with this model?
- What should it not be used for?
Half a page of concrete answers is worth moe than three pages about AI and society. The questions cannot be answered without having looked at your own results, and that is the oint. Module 12 shows how.

### What you submit 
A link to your repository on Github, on ItsLearning. Nothing else is uploaded, and nothing is recorded or presented orally. What is assessed is the repository as it looks at the deadline.

If your repository is public you dont need to do the steps below.
The repository is private if you created it as in Module 01, and then it has to be readable, or it cannot be assessed. Invite the Github user neurohrone as a collaborator before you submit:
1. Open your repository on Github and click Setting, in the row of tabs under the repository's name.
2. In the menu to the left, under Access, click Collaborators.
3. Github asks you to confirm that its you, confirm.
4. Click Add people, type neurothrone, and click the name in the list.
5. Click the green button that adds neurothrone to your repository.
Github sends an invitation. Your teacher accepts it, and can then read the repsitory.

### Checklist before you submit
https://codex-pyai.pages.dev/examination/project/?#checklist-before-you-submit

### If you get stuck
Get in touch as early as you can. The earlier, the more options there are, and the last week is the worst time to raise something.
- Switch datasets is yous does not work. It is not a defeat. A dataset that is too small, too messy or missing what you want to predivt costs more time than it is worth.
- Do the smallest project that gets G first. A submission that works on time is almost always better than a perfect one that is late, because a resubmission can never give VG.