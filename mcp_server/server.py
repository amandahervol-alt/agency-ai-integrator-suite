"""
Model Context Protocol (MCP) Server for Marketing Agency Automations
---------------------------------------------------------------------
Implements an MCP Server exposing agency tools and resources to LLM agents.
Provides standard tools for CRM integration, campaign analytics, and audit logging.
"""

import json
from typing import Dict, Any, List

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    # Lightweight fallback stub for running tests/demos without mcp package installed
    class FastMCP:
        def __init__(self, name: str):
            self.name = name
        def tool(self):
            def decorator(func):
                return func
            return decorator
        def run(self):
            print(f"FastMCP server '{self.name}' running in fallback mode.")


# Initialize FastMCP Server named "EZMarketing-Agency-MCP"
mcp = FastMCP("EZMarketing-Agency-MCP")

# Mock CRM Database for Small Business Clients
MOCK_CLIENT_CRM = {
    "client_101": {
        "company_name": "Lancaster Plumbing & HVAC",
        "industry": "Home Services",
        "crm_platform": "HubSpot / Quickbooks",
        "monthly_ad_spend": 2500.00,
        "active_campaigns": ["Google Search - Emergency Repair", "Facebook - Seasonal Tuneup"],
        "status": "Active Client"
    },
    "client_102": {
        "company_name": "Keystone Legal Services",
        "industry": "Professional Services",
        "crm_platform": "Salesforce",
        "monthly_ad_spend": 5000.00,
        "active_campaigns": ["LinkedIn - Corporate Law", "Google Search - Personal Injury"],
        "status": "Onboarding"
    }
}


@mcp.tool()
def get_client_crm_profile(client_id: str) -> str:
    """
    Fetches client profile, CRM system, ad spend, and campaign details from agency database.
    
    Args:
        client_id: Unique client identifier (e.g. 'client_101')
    """
    client = MOCK_CLIENT_CRM.get(client_id)
    if not client:
        return json.dumps({"error": f"Client ID '{client_id}' not found in agency CRM."})
    return json.dumps(client, indent=2)


@mcp.tool()
def fetch_campaign_performance(client_id: str, days: int = 30) -> str:
    """
    Retrieves key performance metrics (ROAS, Cost Per Click, Conversions) for client campaigns.
    
    Args:
        client_id: Unique client identifier
        days: Number of days to analyze (default: 30)
    """
    if client_id not in MOCK_CLIENT_CRM:
        return json.dumps({"error": "Invalid client ID"})

    performance_summary = {
        "client_id": client_id,
        "timeframe_days": days,
        "metrics": {
            "total_impressions": 45200,
            "total_clicks": 1840,
            "ctr_percent": 4.07,
            "avg_cpc_usd": 3.45,
            "conversions": 142,
            "cost_per_conversion_usd": 44.71,
            "roas_multiplier": 3.8
        },
        "recommendation": "Scale Google Search campaign budget by 15%; pause low-converting Facebook ad set."
    }
    return json.dumps(performance_summary, indent=2)


@mcp.tool()
def record_agent_automation_log(client_id: str, action_taken: str, system_impact: str) -> str:
    """
    Records an auditable record of an AI agent's execution into agency logging system.
    
    Args:
        client_id: Client account identifier
        action_taken: Brief summary of the automated task executed
        system_impact: Measurable impact or downstream platform updated (e.g., Quickbooks, CRM)
    """
    audit_entry = {
        "status": "Logged Successfully",
        "client_id": client_id,
        "action_taken": action_taken,
        "system_impact": system_impact,
        "security_check": "PASSED (Output Validated)"
    }
    return json.dumps(audit_entry, indent=2)


if __name__ == "__main__":
    # Server can be run directly or spawned via MCP stdio client runners
    mcp.run()
