
# Square Roots - Specification Lab

[![build](../../actions/workflows/build.yml/badge.svg)](../../actions/)
![Platforms: Linux, MacOS, Windows](https://img.shields.io/badge/Platform-Linux%20%7C%20MacOS%20%7C%20Windows-blue.svg)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-blue.svg)](https://github.com/psf/black)
[![Commits: Conventional](https://img.shields.io/badge/Commits-Conventional-blue.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Discord](https://img.shields.io/discord/872320492936257537?logo=discord)](https://discord.gg/kjah8MFYbR)

## Introduction

In this assignment you will implement a CLI that can run two different
algorithms to find a square root.

## Learning Objectives

By completing this assignment you will:

1. Use git and GitHub to manage source code file changes
2. Implement a Command Line Interface in Python
3. Use Poetry to run a Command Line Interface
4. Implement exhaustive and binary search methods to compute square roots
5. Use a profiler to characterize the speed of the algorithms
6. Write clearly about the programming concepts in this assignment

## Quick Links

- Due date: Check Discord or the
  [Course Materials Schedule](https://github.com/allegheny-college-cmpsc-101-fall-2024/course-materials/blob/main/Schedule.md)
- Policy on
  [Tokens](https://github.com/allegheny-college-cmpsc-101-fall-2024/course-materials#tokens)
- [Token Form for Automatic Extension](https://forms.gle/y9Mz55hQKr84wzvXA)
- Policy for
  [Assignment Evaluation](https://github.com/allegheny-college-cmpsc-101-fall-2024/course-materials#assignment-evaluation)
- Policy for [Assignment Submission](https://github.com/allegheny-college-cmpsc-101-fall-2024/course-materials#assignment-submission).
- [#data-structures Discord channel](https://discord.com/channels/877320365825749002/1274744318124359732)
- [Starter repo](https://github.com/allegheny-college-cmpsc-101-fall-2024/square-roots-starter)

## Policy Reminders

Students are reminded to uphold the Honor Code. Cloning this assignment
repository is a commitment to the latter.

For this assignment, you may use class materials, the textbook, notes,
and the internet, including AI, for reference and learning. AI may **not** be
used to generate answers that you submit. All code and writing that are turned
in **must be your own work and your own words**. Copying or otherwise
representing ChatGTP or other AI outputs as your own work or your own words is
not permitted.

Please ask questions freely in Lab, on the #data-structures Discord channel,
TL office hours, instructor office hours, or by opening a GitHub Issue with
@emgraber tagged at least 24 hours before the deadline.

Modifications to the gatorgrade.yml file are not permitted without explicit
instruction.

## Project Goals

This assignment invites you to implement a program with a Command Line
Interface that has the ability to use two different algorithms for
approximating the square root of a number. The two approaches are called
`exhaustive` and `efficient`. Can you guess which one might be faster?

For a given step size and a tolerated margin of error,
the `exhaustive` algorithm iteratively checks if each candidate answer is
within the margin of error for the square root's approximation. In contrast,
the `efficient` algorithm will use bisection search to rapidly prune the search to
the best possible approximation of the number's square root.

In addition to adding source code and documentation to the provided Python
files, you will conduct an experiment to determine which algorithm is the
fastest and estimate by how much it is faster.

## Project Access

After accepting you individual repository with the GitHub Classroom link,
use the `git clone` command to download the project from GitHub to
your computer. Now you are ready to add source code and documentation to the
project!

## Expected Output

The square root calculation program in this lab is called
`squareroot`. The program accepts through its CLI a single integer
value for which it will compute the square root using either an `efficient` or
an `exhaustive` approach. Finally, the `squareroot` program offers a `--profile`
flag that causes it to use the
[Pyinstrument](https://github.com/joerick/pyinstrument) package to collect
timing information about the speed of the chosen method. If you use Poetry
to run the program with the command `poetry run squareroot --number 25000
--approach exhaustive --profile` it produces the following output:

```shell
🧮 Attempting to calculate the square root of 25000!

✨ Was this search for the square root successful? Yes
✨ How many guesses did it take to compute the solution? 1581139
✨ The best approximation for the square root of 25000 is 158.1139000041253

🔬 Here's profile data from performing square root computation on 25000!

  _     ._   __/__   _ _  _  _ _/_   Recorded: 10:25:39  Samples:  507
 /_//_/// /_\ / //_// / //_'/ //     Duration: 0.508     CPU time: 0.508
/   _/                      v4.0.3

Program: squareroot --number 25000 --approach exhaustive --profile

0.507 squareroot/main.py:106
└─ 0.507 compute_square_root_exhaustive  squareroot/main.py:36
   ├─ 0.396 [self]
   └─ 0.111 abs  <built-in>:0
         [2 frames hidden]  <built-in>
```

If you run the program with the command `poetry run squareroot --number 25000
--approach efficient --profile` then it produces output like:

```shell
🧮 Attempting to calculate the square root of 25000!

✨ Was this search for the square root successful? Yes
✨ How many guesses did it take to compute the solution? 27
✨ The best approximation for the square root of 25000 is 158.11389312148094

🔬 Here's profile data from performing square root computation on 25000!

  _     ._   __/__   _ _  _  _ _/_   Recorded: 10:29:41  Samples:  0
 /_//_/// /_\ / //_// / //_'/ //     Duration: 0.000     CPU time: 0.000
/   _/                      v4.0.3

Program: squareroot --number 25000 --approach efficient --profile

No samples were recorded.
```

It is worth noting that the `exhaustive` algorithm took `1581139` guesses to
approximate the square root of `25000` while the `efficient` algorithm only
needed `27`! This shows that `efficient`'s bisection search algorithm is
significantly faster than the `exhaustive` approach. Interestingly, the
[Pyinstrument](https://github.com/joerick/pyinstrument) package reports that it
could not record any performance data for `squareroot` when the program runs in
`efficient` mode. Why do you think that this is the case? Is there any way to
overcome this issue by, for instance, reconfiguring Pyinstrument or changing the
input that you pass to the program? Overall, how much faster is `efficient` in
comparison to `exhaustive`? You can use the following equations to calculate the
percentage change in execution time when running `squareroot` in `efficient`
mode instead of the `exhaustive` mode.

$$
T_{\Delta} = \frac{T_x - T_f}{T_x} \times 100
$$

$T_f$ denotes the execution time of `efficient` mode and $T_x$ denotes the
execution time of `exhaustive` mode. $T_{\Delta}$ is the percentage change
in the execution time when running `squareroot` in `efficient` mode instead
of `exhaustive` mode.

Finally, to understand why `efficient` is
faster than `exhaustive` you should study each function's source code and the
textbook's content in chapter 3.

To learn more about how to run this program, you can type the command `poetry
run squareroot --help` to see the following output showing how to use `squareroot`:

```shell
Usage: squareroot [OPTIONS]

  Use iteration to perform square root computation of a number and then
  perform profiling to capture execution time.

Options:
  --number INTEGER                [default: 5]
  --profile / --no-profile        [default: False]
  --approach [exhaustive|efficient]
                                  [default: efficient]
  --install-completion            Install completion for the current shell.
  --show-completion               Show completion for the current shell, to
                                  copy it or customize the installation.

  --help                          Show this message and exit.
```

Please note that the provided source code does not contain all of the
functionality to produce this output. As explained in the next section, you are
invited to add the missing features and ensure that `squareroot` produces the
expected output. Once the program is working correctly, it should produce output
similar to that shown in this section.

>Don't forget that if you want to run the `squareroot` program you must use
>your terminal to first go into the GitHub repository containing this project
>and then go into the `squareroot/` directory that houses the project's code.
>Finally, remember that before running the program you must run `poetry
>install` to add the dependencies.

## Adding Functionality

If you study the file `squareroot/squareroot/main.py` you will see that it has
many `TODO` markers that designate the parts of the program that you need to
implement before `squareroot` will produce correct output. In summary, you
should implement the following functions for the `squareroot` program:

- `def compute_square_root_exhaustive(x: int, epsilon: float = 0.01) -> Tuple[bool, float, int]`
- `def compute_square_root_efficient(x: int, epsilon: float = 0.01) -> Tuple[bool, float, int]`

Importantly, you will notice that both `compute_square_root_efficient` and
`compute_square_root_exhaustive` accept the same types of inputs and produce the
same types of outputs. In particular, the parameter called `x` is the number
whose square root the function will compute and `epsilon` is the tolerance
parameter describing how close the approximation of `x`'s square root must be.
The notation `Tuple[bool, float, int]` that describes the output of these
functions shows that they each return three values. The first variable in the
return value is a `bool` indicating whether or not the function found an answer
within the tolerance of `epsilon`. Finally, the second returned variable is a
`float` for the calculated value of the square root and the third one is an
`int` for the number of guesses that the algorithm took.

You will also notice that there are some `TODO` markers in the `squareroot`
function of the `main` module. In the scope of the conditional logic statement
`if approach.value == SquareRootCalculationingApproach.efficient` on lines `1`
through `7`, the program should call the function
`compute_square_root_efficient` depending on whether the `profile` variable
specified on the command-line is `True` or `False`. If `profile` is `True`, then
the program should use Pyinstrument to measure its execution time, as
illustrated on lines `3` through `5`. However, if `profile` is `False`, then the
program should only call the `compute_square_root_efficient` as shown on line
`7`. As lines `9` through `15` show, the function should take analogous steps
for its `exhaustive` mode, calling the `compute_square_root_exhaustive` instead
of `compute_square_root_efficient`.

```python linenums="1"
if approach.value == SquareRootCalculationingApproach.efficient:
    if profile:
        profiler.start()
        square_root_tuple = compute_square_root_efficient(number)
        profiler.stop()
    else:
        square_root_tuple = compute_square_root_efficient(number)
# use the exhaustive square root computation algorithm
elif approach.value == SquareRootCalculationingApproach.exhaustive:
    if profile:
        profiler.start()
        square_root_tuple = compute_square_root_exhaustive(number)
        profiler.stop()
    else:
        square_root_tuple = compute_square_root_exhaustive(number)
```

Once you have correctly resolved all of the `TODO` markers in the `squareroot`
program, it should produce the expected output described in the previous
section. With that said, please bear in mind that, when running `squareroot`
with the `--profile` flag it will produce different profiling data depending on
the performance of your computer.

### Gatorgrade

After you have added functionality and checked that your code produces the
expected output, the command `gatorgrade --config config/gatorgrade.yml`
will check your work with the automatic grader. If
your work meets the baseline requirements and adheres to the best practices that
proactive programmers adopt you will see that all the checks pass when you run
`gatorgrade`. All checks must pass in order to get 100% on this lab. All other
gatorgrade score are graded as 0%. Note, modifications to the gatorgrade.yml file
are not permitted without explicit instruction.

### Helper Tasks

Helper tasks are run in the terminal with the poetry environment activated.
The format of the commands are always `poetry run task xyz`...where `xyz`
is the helper task name.

If you study the source code in the `pyproject.toml` file you will see that it
includes the following section that specifies different executable "helper
task" names like `ruff`, `fix`, `ruffdetails`, etc.

```toml
[tool.taskipy.tasks]
```

If you are in the `squareroot` directory that contains the
`pyproject.toml` file, the helper tasks
make it easy to run commands like `poetry run task ruff` to automatically run
the ruff linter designed to check the Python source code in your program
to confirm that your source code adheres to industry standards for formatting.
You can also use the command `poetry run task fix` to automatically reformat the
source code. `poetry run task ruffdetails` will print out detailed linting errors
that point to exactly what ruff views as a linting error. Make sure to examine
the `pyproject.toml` file for other convenient tasks that you can use to both
check and improve your project!

If your program has
all of the anticipated functionality, you can run the command `poetry run task
test` and see that the test suite produces output like the following.

```shell
collected 3 items

tests/test_squareroot.py ....
```

## Project Reflection

Once you have finished all of the previous technical tasks, you can use a text
editor to answer all of the questions in the `writing/reflection.md` file. For
instance, you should provide the output of the Python program in a fenced code
block, explain the meaning of the Python source code segments that you
implemented and tested, compare and contrast the performance of different
implementations of the square root calculation, and answer all of the other
questions about your experiences in completing this project.

### Project Assessment

You may make an unlimited number of reattempts at submitting
source code and technical writing that meet all aspects of the project's
specification. This spec lab is graded pass/fail. Gatorgrade reports of 100%
meeting all the spec receive a grade of 100%. All other gatorgrade reports
result in a grade of 0%.

## Project Overview

After cloning this repository to your computer, please take the following
steps:

- Use the `cd` command to change into the directory for this repository.
- Specifically, you can change into the program directory by typing `cd squareroot`.
- Install the dependencies for the project by typing `poetry install`.
- Run the program in its two different modes by typing:
  - `poetry run squareroot --number 25 --approach exhaustive`
  - `poetry run squareroot --number 25 --approach exhaustive --profile`
  - Please note that the program will not work unless you add the required
    source code at the designated `TODO` markers.
- Confirm that the program is producing the expected output by looking in the
  appropriate section of the project description on the Proactive Programmers
  web site.
- Run the automated grading checks by typing `gatorgrade --config config/gatorgrade.yml`.
- You may also review the output from running GatorGrader in GitHub Actions.
- Respond to the technical writing prompts in the `writing/reflection.md` file.
- Please make sure that you completely delete the `TODO` markers and their
  labels from all of the provided source code and `writing/reflection.md`
- Submit work to GitHub using git in the terminal
  - Open a terminal
  - `cd` to the project directory on your computer
  - type `git status` to see a list of files you have updated
  - type `git add .` to "stage" your files
  - type `git commit -m "PUT YOUR OWN SHORT MESSAGE"`
  - type `git push origin main`
  - type your ssh passphrase if requested
