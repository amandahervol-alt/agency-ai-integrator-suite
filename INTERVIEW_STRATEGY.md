# 🎯 EZMarketing Interview Game Plan & Cheat Sheet

> **Target Role**: AI Builder Integrator at EZMarketing ($70k - $80k)  
> **Meeting Type**: 30-Minute Interview / Meet & Greet (Tuesday)  
> **Primary Goal**: Demonstrate technical depth (MCP, workflows, security, cost control) and client-facing discovery confidence.

---

## ⏱️ 30-Minute Interview Agenda Breakdown

| Time Window | Segment | Goal & Key Focus |
| :--- | :--- | :--- |
| **0:00 - 0:05** | **Rapport & Elevator Pitch** | Express excitement for EZMarketing's growth into AI solutions; deliver your 2-minute elevator pitch. |
| **0:05 - 0:15** | **GitHub Project Tour (Screen Share)** | Share your screen and walk through `agency-ai-integrator-suite`. Show MCP server, guardrails, and cost engine. |
| **0:15 - 0:25** | **Discovery & Client Scenario Discussion** | Explain how you lead client discovery calls, assess bottlenecks, and translate requirements into proposals. |
| **0:25 - 0:30** | **Questions & Next Steps** | Ask 2 high-leverage strategic questions about EZMarketing's AI roadmap; secure next steps. |

---

## 🗣️ The 2-Minute Elevator Pitch

> *"I specialize in building production-ready AI agents, workflow automations, and system integrations that drive measurable revenue and efficiency for businesses. What drew me to EZMarketing is your vision of bringing AI to small businesses from the ground floor. I don't just write prompts—I architect secure, API-first solutions with Model Context Protocol (MCP), multi-provider failovers (Gemini/OpenAI), strict security guardrails against prompt injection, and transparent token cost tracking. I'm equally comfortable in front of clients leading discovery sessions as I am in code building production integrations with CRMs, Quickbooks, and Microsoft 365."*

---

## 🖥️ 10-Minute GitHub Repository Screen-Share Script

When the interviewer asks to see your projects on GitHub, open **`agency-ai-integrator-suite`** and follow this script:

### Step 1: Open the `README.md` (1 minute)
- Point to the architecture diagram.
- *"I built this suite to reflect how digital agencies should deploy AI in production: API-first, multi-model, secure, and cost-controlled."*

### Step 2: Show the MCP Server (`mcp_server/server.py`) (2 minutes)
- Point out the FastMCP decorator and tools (`get_client_crm_profile`, `fetch_campaign_performance`).
- *"Model Context Protocol is huge for agentic workflows. Instead of hardcoding API calls into prompts, I expose CRM lookups and campaign analytics as standardized MCP tools that LLM agents can call dynamically."*

### Step 3: Highlight AI Security Guardrails (`security/prompt_guard.py`) (2 minutes)
- Show the regex injection scanner and PII redactor.
- *"Small businesses are terrified of data leaks or AI hallucinations. I implement an edge security guardrail that blocks prompt injections and redacts SSNs or credit card data before payloads ever hit model APIs. Plus, I enforce strict Pydantic JSON schema validation on all LLM outputs."*

### Step 4: Show the Cost & Governance Engine (`governance/token_calculator.py`) (2 minutes)
- Show request-level pricing and monthly TCO projection.
- *"In an agency setting, cost management is critical. My governance engine tracks input/output token usage per client and generates 30-day TCO projections so we can present clear ROI and fixed budget expectations to clients."*

### Step 5: Show the Client Discovery Framework (`docs/client_discovery_framework.md`) (2 minutes)
- Briefly display the discovery questionnaire and proposal blueprint.
- *"This bridges engineering with sales—translating discovery calls into clear technical scopes, timelines, and measurable KPIs."*

---

## 💡 Pre-Scripted Answers to Expected Interview Questions

### Q1: "Describe the AI integrations you have built."
> **Answer**: *"I've built end-to-end event-driven AI pipelines and agentic tools. For example, in my agency suite, I built an inbound lead enrichment system where webform submissions trigger prompt security checks, route through Google Gemini 1.5 Flash with fallback to GPT-4o-mini, validate structured JSON output, and invoke MCP tools to update HubSpot CRM and Quickbooks automatically."*

### Q2: "How do you explain MCP (Model Context Protocol) to a non-technical small business owner?"
> **Answer**: *"I tell them: 'Think of MCP as a universal translator and secure adapter plug. Instead of building custom, expensive bridges between every AI tool and your CRM or Quickbooks, MCP gives the AI a standard set of hands and eyes so it can safely read your data and perform tasks inside your existing software without breaking anything.'"*

### Q3: "How do you control API costs and model token usage for agency clients?"
> **Answer**: *"We approach cost with a two-part strategy: First, smart model routing—using fast, low-cost models like Gemini Flash or GPT-4o-mini for 80% of standard tasks, and reserving higher-cost models like Claude 3.5 Sonnet for complex multi-step reasoning. Second, pre-execution budget estimation—we calculate estimated monthly token consumption during client discovery and set automated API rate limits so clients never face surprise bills."*

### Q4: "How do you lead a client discovery call for an SMB (e.g. HVAC, legal, dental)?"
> **Answer**: *"I start by focusing entirely on business bottlenecks rather than technology. I ask: 'Where are your teams spending 5+ hours a week on repetitive tasks?' and 'How fast do inbound leads get answered outside normal hours?' Once we identify the bottleneck, I sketch a 3-stage solution: capture, enrichment, and CRM sync. I then present a clear technical blueprint, token cost estimate, and 3-week pilot scope."*

---

## ❓ 2 Strategic Questions to Ask the Interviewer

1. *"As EZMarketing expands its AI practice, what are the most common platforms your current small business clients rely on (e.g. HubSpot, Salesforce, Quickbooks, Microsoft 365)?"*
2. *"What does a successful first 90 days look like for the AI Builder Integrator role—is the immediate focus more on internal agency workflow automation or scaling client-facing implementations?"*

---

## 📦 Steps to Push this Project to Your GitHub

Run these commands in terminal to push to your personal GitHub account before Tuesday:

```bash
cd C:\Users\manet\.gemini\antigravity\scratch\agency-ai-integrator-suite
git init
git add .
git commit -m "Initial commit: Agency AI Integrator Suite with MCP, Security Guardrails, and Cost Governance"
# Create a new repository on GitHub named "agency-ai-integrator-suite"
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/agency-ai-integrator-suite.git
git branch -M main
git push -u origin main
```
