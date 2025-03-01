"""Tests for lint (with no errors) from CLI, interactive, with an EE."""
import os

import pytest

from tests.integration._interactions import Command
from tests.integration._interactions import UiTestStep
from tests.integration._interactions import add_indices
from tests.integration._interactions import step_id

from .base import LINT_FIXTURES
from .base import BaseClass


CLI = Command(
    subcommand="lint",
    cmdline=os.path.join(
        LINT_FIXTURES,
        "no_errors",
    ),
    execution_environment=True,
).join()

steps: tuple[UiTestStep, ...] = (
    UiTestStep(
        user_input=CLI,
        comment="ansible-navigator lint top window",
        present=["no lint issues"],
        search_within_response="Success",
    ),
)

steps = add_indices(steps)


@pytest.mark.parametrize("step", steps, ids=step_id)
class Test(BaseClass):
    """Run the tests for lint from CLI, interactive, with an EE."""

    UPDATE_FIXTURES = False
