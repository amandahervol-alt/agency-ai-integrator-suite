"""
Output Validation & Schema Governance Middleware
------------------------------------------------
Validates raw LLM outputs against strict structural Pydantic schemas,
ensuring production safety before sending data to CRMs, APIs, or client dashboards.
"""

import json
from typing import Type, TypeVar, Optional, Tuple, Dict, Any
from pydantic import BaseModel, ValidationError

T = TypeVar("T", bound=BaseModel)


class StructuredOutputValidator:
    """Validates and parses raw text responses into structured Pydantic models."""

    @staticmethod
    def parse_and_validate(raw_llm_text: str, target_schema: Type[T]) -> Tuple[Optional[T], Optional[str]]:
        """
        Parses JSON from raw text output and validates against target Pydantic schema.
        Handles markdown codeblock removal automatically.
        """
        cleaned_text = raw_llm_text.strip()

        # Strip markdown ```json ... ``` codeblocks if present
        if cleaned_text.startswith("```"):
            lines = cleaned_text.splitlines()
            if lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].startswith("```"):
                lines = lines[:-1]
            cleaned_text = "\n".join(lines).strip()

        try:
            data_dict = json.loads(cleaned_text)
            validated_obj = target_schema.model_validate(data_dict)
            return validated_obj, None
        except json.JSONDecodeError as e:
            return None, f"JSON Parsing Error: {str(e)}"
        except ValidationError as e:
            return None, f"Schema Validation Error: {str(e)}"


# Sample Output Schema for Marketing Automation
class LeadQualificationOutput(BaseModel):
    lead_score: int  # 0 to 100
    industry: str
    key_pain_points: list[str]
    recommended_ai_solution: str
    estimated_monthly_budget: float
    next_action: str


if __name__ == "__main__":
    valid_sample = """
    ```json
    {
        "lead_score": 85,
        "industry": "HVAC & Plumbing Services",
        "key_pain_points": ["Manual booking delays", "After-hours customer missed calls"],
        "recommended_ai_solution": "24/7 AI Voice & SMS Booking Assistant",
        "estimated_monthly_budget": 500.00,
        "next_action": "Schedule Discovery Demo"
    }
    ```
    """
    obj, err = StructuredOutputValidator.parse_and_validate(valid_sample, LeadQualificationOutput)
    if obj:
        print("--- Output Schema Validation Passed ---")
        print(obj.model_dump_json(indent=2))
    else:
        print(f"Validation Failed: {err}")
