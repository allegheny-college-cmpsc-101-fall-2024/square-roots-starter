"""Perform square root calculation with exhaustive and efficient approaches."""

from pyinstrument import Profiler  # type: ignore

from typing import Tuple

from enum import Enum

import typer

from rich.console import Console

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a Profiler object to support timing program code segments
profiler = Profiler()


class SquareRootCalculationingApproach(str, Enum):
    """Define the name for the approach for calculation of the square root."""

    EXHAUSTIVE = "exhaustive"
    EFFICIENT = "efficient"


def human_readable_boolean(answer: bool) -> str:
    """Produce a human-readable Yes or No for a boolean value of True or False."""
    # the provided answer is True
    if answer:
        return "Yes"
    # the provided answer is False
    return "No"


def compute_square_root_exhaustive(
    x: int, epsilon: float = 0.01
) -> Tuple[bool, float, int]:
    """Compute the square root of a number using an exhaustive method."""
    # TODO: define the step size using the margin of error squared
    # TODO: initialize the number of guesses to zero
    # TODO: initialize the answer to 0.0
    # TODO: while the approximation is not within epsilon and
    # the computed answer is less than or equal to the value
    # of x, keep searching for the value of the square root
    # --> TODO: move to the next answer to consider
    # --> TODO: increase the number of guesses
    # TODO: not able to find the correct answer, return many things:
    # --> False to indicate that the answer was not found
    # --> Current best approximation for the answer
    # --> Number of guesses taken so far in search
    # TODO: able to find the correct answer, so return these things:
    # --> True to indicate that the answer was found
    # --> Current best approximation for the answer
    # --> Number of guesses taken so far in search
    # TODO: remove this placeholder when you write the code above
    return (False, 0.0, 0)

def compute_square_root_efficient(
    x: int, epsilon: float = 0.01
) -> Tuple[bool, float, int]:
    """Perform an efficient square root approximation using the efficient bisection method."""
    # Note, this function must work correctly for x's larger and smaller than 1
    # TODO: initialize the number of guesses to zero
    # TODO: initialize the lower bound to zero
    # TODO: initialize the upper bound to the maximum between 1 and the input value
    # TODO: compute the best guess for the answer as the "mid point" between high and low
    # TODO: continue to search for answers as long as the current one is not within epsilon
    # --> TODO: increase the count of the number of guesses
    # --> TODO: narrow the search space by next looking at smaller values
    # --> TODO: narrow the search space by next looking at higher values
    # --> TODO: compute a new best guess for the answer
    # TODO: not able to find the correct answer, so return many things:
    # --> False to indicate that the answer was not found
    # --> Current best approximation for the answer
    # --> Number of guesses taken so far in search
    # TODO: able to find the correct answer, so return these things:
    # --> True to indicate that the answer was found
    # --> Current best approximation for the answer
    # --> Number of guesses taken so far in search
    # TODO: remove this placeholder when you write the code above
    return (False, 0.0, 0)


@cli.command()
def squareroot(
    number: int = typer.Option(5),
    profile: bool = typer.Option(False),
    approach: SquareRootCalculationingApproach = SquareRootCalculationingApproach.EFFICIENT,
) -> None:
    """Use iteration to perform square root computation of a number and then perform profiling to capture execution time."""
    # create a console for rich text output
    console = Console()
    # create an empty response from the function that computes the square root
    square_root_tuple: Tuple[bool, float, int] = (False, 0.0, 0)
    # use the efficient square root computation algorithm
    if approach.value == SquareRootCalculationingApproach.EFFICIENT:
        # TODO: use conditional logic to handle both of these cases
        # TODO: make sure to carefully review the project description on
        # the Proactive Programmers web site for a detailed discussion
        # of these steps
        # TODO: perform profiling on the execution of the square root computation
        # TODO: do not perform profiling
    # use the exhaustive square root computation algorithm
    elif approach.value == SquareRootCalculationingApproach.EXHAUSTIVE:
        # TODO: use conditional logic to handle both of these cases
        # TODO: make sure to carefully review the project description on
        # the Proactive Programmers web site for a detailed discussion
        # of these steps
        # TODO: perform profiling on the execution of the square root computation
        # TODO: do not perform profiling
    # display the results of the square root computation
    was_root_found = square_root_tuple[0]
    square_root_solution = square_root_tuple[1]
    number_guesses = square_root_tuple[2]
    console.print(f":abacus: Attempting to calculate the square root of {number}!")
    console.print()
    console.print(
        f":sparkles: Was this search for the square root successful? {human_readable_boolean(was_root_found)}"
    )
    console.print(
        f":sparkles: How many guesses did it take to compute the solution? {number_guesses}"
    )
    console.print(
        f":sparkles: The best approximation for the square root of {number} is {square_root_solution}"
    )
    # display the results of the profiling if that option was requested
    if profile:
        console.print()
        console.print(
            f":microscope: Here's profile data from performing square root computation on {number}!"
        )
        profiler.print()
