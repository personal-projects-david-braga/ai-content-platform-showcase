from dataclasses import dataclass
from enum import Enum


class ApprovalState(str, Enum):
    DRAFT = "draft"
    IN_REVIEW = "in_review"
    APPROVED = "approved"
    REJECTED = "rejected"


@dataclass
class ApprovalGate:
    state: ApprovalState = ApprovalState.DRAFT

    def submit(self) -> None:
        if self.state is not ApprovalState.DRAFT:
            raise ValueError("Only draft content can be submitted")
        self.state = ApprovalState.IN_REVIEW

    def approve(self) -> None:
        if self.state is not ApprovalState.IN_REVIEW:
            raise ValueError("Only content in review can be approved")
        self.state = ApprovalState.APPROVED

    def reject(self) -> None:
        if self.state is not ApprovalState.IN_REVIEW:
            raise ValueError("Only content in review can be rejected")
        self.state = ApprovalState.REJECTED
