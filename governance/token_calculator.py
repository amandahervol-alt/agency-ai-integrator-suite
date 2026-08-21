"""
Token & Infrastructure Cost Governance Engine
---------------------------------------------
Tracks model token usage, calculates per-request & monthly API fees across providers,
and provides total cost of ownership (TCO) projections for client AI implementations.
"""

from typing import Dict, Any, Optional
from pydantic import BaseModel, Field

# Pricing per 1,000,000 tokens (USD) as of standard 2026 tiers
MODEL_PRICING: Dict[str, Dict[str, float]] = {
    "gpt-4o": {
        "input_per_m": 2.50,
        "output_per_m": 10.00
    },
    "gpt-4o-mini": {
        "input_per_m": 0.15,
        "output_per_m": 0.60
    },
    "claude-3-5-sonnet": {
        "input_per_m": 3.00,
        "output_per_m": 15.00
    },
    "gemini-1.5-pro": {
        "input_per_m": 1.25,
        "output_per_m": 5.00
    },
    "gemini-1.5-flash": {
        "input_per_m": 0.075,
        "output_per_m": 0.30
    }
}


class TokenUsageReport(BaseModel):
    client_id: str
    model_name: str
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    prompt_cost_usd: float
    completion_cost_usd: float
    total_cost_usd: float


class MonthlyBudgetProjection(BaseModel):
    client_id: str
    daily_request_volume: int
    avg_prompt_tokens: int
    avg_completion_tokens: int
    selected_model: str
    monthly_api_cost: float
    infrastructure_overhead: float
    total_monthly_tco: float
    cost_per_qualified_lead: float


class CostGovernanceCalculator:
    """Utility class for tracking token costs and projecting AI deployment budgets."""

    @staticmethod
    def calculate_request_cost(
        client_id: str,
        model_name: str,
        prompt_tokens: int,
        completion_tokens: int
    ) -> TokenUsageReport:
        """Calculates exact USD cost for a single LLM completion request."""
        pricing = MODEL_PRICING.get(model_name.lower())
        if not pricing:
            # Fallback default pricing if model unrecognized
            pricing = {"input_per_m": 2.50, "output_per_m": 10.00}

        prompt_cost = (prompt_tokens / 1_000_000.0) * pricing["input_per_m"]
        completion_cost = (completion_tokens / 1_000_000.0) * pricing["output_per_m"]
        total_cost = prompt_cost + completion_cost

        return TokenUsageReport(
            client_id=client_id,
            model_name=model_name,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            total_tokens=prompt_tokens + completion_tokens,
            prompt_cost_usd=round(prompt_cost, 6),
            completion_cost_usd=round(completion_cost, 6),
            total_cost_usd=round(total_cost, 6)
        )

    @staticmethod
    def project_monthly_tco(
        client_id: str,
        daily_request_volume: int,
        avg_prompt_tokens: int = 1500,
        avg_completion_tokens: int = 500,
        selected_model: str = "gemini-1.5-flash",
        hosting_cost_usd: float = 25.0  # e.g., Cloud run / Lambda execution overhead
    ) -> MonthlyBudgetProjection:
        """Projects monthly operational costs and TCO for a small business client automation."""
        single_req = CostGovernanceCalculator.calculate_request_cost(
            client_id=client_id,
            model_name=selected_model,
            prompt_tokens=avg_prompt_tokens,
            completion_tokens=avg_completion_tokens
        )

        monthly_requests = daily_request_volume * 30
        monthly_api_cost = single_req.total_cost_usd * monthly_requests
        total_monthly = monthly_api_cost + hosting_cost_usd

        cost_per_lead = round(total_monthly / max(1, (daily_request_volume * 30)), 4)

        return MonthlyBudgetProjection(
            client_id=client_id,
            daily_request_volume=daily_request_volume,
            avg_prompt_tokens=avg_prompt_tokens,
            avg_completion_tokens=avg_completion_tokens,
            selected_model=selected_model,
            monthly_api_cost=round(monthly_api_cost, 2),
            infrastructure_overhead=round(hosting_cost_usd, 2),
            total_monthly_tco=round(total_monthly, 2),
            cost_per_qualified_lead=cost_per_lead
        )


if __name__ == "__main__":
    calc = CostGovernanceCalculator()
    print("--- Single Request Sample ---")
    req = calc.calculate_request_cost("client_ezmarketing_01", "gpt-4o", 2000, 800)
    print(req.model_dump_json(indent=2))

    print("\n--- Small Business 30-Day TCO Projection ---")
    proj = calc.project_monthly_tco("client_ezmarketing_01", daily_request_volume=100, selected_model="gemini-1.5-flash")
    print(proj.model_dump_json(indent=2))
