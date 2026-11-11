from enum import StrEnum

from pydantic import BaseModel, Field, StringConstraints
from typing import Annotated


class Category(StrEnum):
    ACTION_REQUIRED = "action_required"
    INFORMATIONAL = "informational"
    SCHEDULING = "scheduling"
    CUSTOMER_SUPPORT = "customer_support"
    FINANCIAL = "financial"
    MARKETING = "marketing"
    OTHER = "other"


class Priority(StrEnum):
    URGENT = "urgent"
    HIGH = "high"
    NORMAL = "normal"
    LOW = "low"


class TriageRequest(BaseModel):
    message: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=20000)]


class TriageResult(BaseModel):
    category: Category
    priority: Priority
    summary: str = Field(min_length=1, max_length=240)
    action_items: list[str] = Field(max_length=10)

