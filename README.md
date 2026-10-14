# Reading Unfamiliar Code

Work out what a program you did not write actually does, using an AI tutor as
a tool rather than an oracle.

- [AI Use on This Assignment](#ai-use-on-this-assignment)
- [Setup](#setup)
- [Instructions](#instructions)
- [Submitting](#submitting)

## AI Use on This Assignment

This assignment is the one place in Mod 1 where asking an AI about code is the
assignment rather than a shortcut around it. You still write every word of the
response yourself, and you do not ask it to find the bugs for you.

Use it the way you would use a colleague who knows the language better than
you do and has never seen this program:

> You are acting as a tutor. I am reading a program I did not write. Explain
> what a line or a function does when I ask, and answer questions about Python
> itself. Do not tell me what the program is for, do not look for bugs, and do
> not suggest changes. If I state what I think the code does, tell me whether
> my reasoning holds, without giving me the answer.

The difference matters. "What does `round(x, 2)` do?" is a question about
Python. "What is wrong with this function?" asks the model to do the work this
assignment is about.

Your findings have to come from running the code. A model will tell you what a
program probably does, confidently, and it is wrong often enough that trusting
it is how you ship a bug.

## Setup

Clone this repo into `development/mod-1` and `cd` into it. Make a draft branch
before you start.

```sh
git clone [your_repo]
cd [your_repo]
git checkout -b draft
```

There is no virtual environment and nothing to install. The program is in
`app/orders.py`.

## Instructions

This assignment has three steps, in order. **Do not skip ahead to reading the
code.**

### 1. Predict

Open `predictions.py`. It lists seven calls into `app/orders.py`. Fill in what
you think each one returns, reading the code but running nothing.

Guessing is fine. The point is to commit before you find out.

### 2. Check

```sh
python3 check.py
```

It shows what you said beside what the program actually does.

**A prediction that does not match is a finding, not a mistake.** It marks a
place where the program does something other than what a careful reader
expects, and that is worth more than the ones you got right.

### 3. Write

Answer the prompt in `short_response.md`.

Pushing runs the same check on GitHub and reports in the **Actions** tab
whether every prediction is filled in and whether a response is written. It
does not score whether your predictions were right, because being wrong is the
exercise working.

Aim for a response with these qualities. Your instructor will give you
feedback on each one:

- [ ] Addresses all parts of the prompt
- [ ] Accurately uses relevant technical terminology
- [ ] Is free of grammar and spelling mistakes (double check with Grammarly!)
- [ ] Uses markdown to enhance readability (preview in VS Code with
      Command/Control + Shift + V)
- [ ] Is easy to comprehend

## Submitting

```sh
git add -A
git commit -m "your message"
git push
```

Open a pull request to your instructor for feedback.
