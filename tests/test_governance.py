import pytest

from app.services.governance import ApprovalGate, ApprovalState


def test_approval_requires_review() -> None:
    gate = ApprovalGate()
    with pytest.raises(ValueError):
        gate.approve()


def test_happy_path_to_approval() -> None:
    gate = ApprovalGate()
    gate.submit()
    gate.approve()
    assert gate.state is ApprovalState.APPROVED
