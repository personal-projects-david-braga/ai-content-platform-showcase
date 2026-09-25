from __future__ import annotations

from enum import Enum
from typing import Annotated, Literal

from pydantic import BaseModel, Field, StringConstraints


NonEmpty = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=240)]


class Layout(str, Enum):
    TITLE = "title"
    TWO_COLUMN = "two_column"
    METRICS = "metrics"


class TextBlock(BaseModel):
    kind: Literal["text"] = "text"
    text: NonEmpty


class MetricBlock(BaseModel):
    kind: Literal["metric"] = "metric"
    label: NonEmpty
    value: NonEmpty


ContentBlock = TextBlock | MetricBlock


class SlideIR(BaseModel):
    title: NonEmpty
    layout: Layout
    blocks: list[ContentBlock] = Field(min_length=1, max_length=8)


class DeckIR(BaseModel):
    title: NonEmpty
    slides: list[SlideIR] = Field(min_length=1, max_length=20)


class RenderedArtifact(BaseModel):
    title: str
    version: int
    checksum: str
    status: Literal["draft", "approved"]
    payload: dict
