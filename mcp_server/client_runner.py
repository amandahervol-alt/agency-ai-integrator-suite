"""
MCP Agentic Client Runner
-------------------------
Demonstrates programmatic connection to an MCP server, discovering available tools,
and executing agentic workflows.
"""

import json
from mcp_server.server import get_client_crm_profile, fetch_campaign_performance, record_agent_automation_log


def run_agentic_workflow(client_id: str):
    print(f"=== Starting Agentic MCP Workflow for Client: {client_id} ===")

    # Step 1: Discover client profile via MCP tool
    print("\n[Step 1] Invoking Tool: get_client_crm_profile...")
    profile_json = get_client_crm_profile(client_id)
    print(profile_json)

    # Step 2: Fetch campaign performance metrics via MCP tool
    print("\n[Step 2] Invoking Tool: fetch_campaign_performance...")
    performance_json = fetch_campaign_performance(client_id, days=30)
    print(performance_json)

    # Step 3: Record agent automation audit log via MCP tool
    print("\n[Step 3] Invoking Tool: record_agent_automation_log...")
    audit_json = record_agent_automation_log(
        client_id=client_id,
        action_taken="Generated weekly AI performance report and drafted budget allocation plan",
        system_impact="HubSpot CRM updated & client dashboard notification queued"
    )
    print(audit_json)
    print("\n=== Agentic MCP Workflow Completed Successfully ===")


if __name__ == "__main__":
    run_agentic_workflow("client_101")
