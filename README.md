# 🚀 Agency AI Integrator Suite

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/MCP-1.0-orange.svg)](https://modelcontextprotocol.io/)
[![Security Guardrails](https://img.shields.io/badge/Security-PromptGuard-green.svg)](#security--guardrails)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An enterprise-ready, production-grade **AI Integration & Automation Suite** designed for digital agencies, SMB solutions, and AI integrators. 

This repository demonstrates **Model Context Protocol (MCP)** server architecture, multi-provider intelligent LLM routing, security guardrails, cost & token governance, and client discovery frameworks.

---

## 🌟 Key Pillars & Features

| Module | Location | Key Capabilities |
| :--- | :--- | :--- |
| **Model Context Protocol (MCP)** | [`mcp_server/`](mcp_server/) | FastMCP server exposing tools for CRM lead queries, campaign analytics, and automated action audit logging. |
| **Intelligent Multi-Model Router** | [`workflows/model_router.py`](workflows/model_router.py) | API-first fallback engine across **Google Gemini**, **OpenAI**, and **Anthropic** with automatic failover and latency tracking. |
| **Security Guardrails** | [`security/`](security/) | Prompt injection detection, PII redaction (SSN, Credit Cards), and strict Pydantic output schema validation. |
| **Cost & Token Governance** | [`governance/`](governance/) | Real-time request token pricing, per-client API spend calculator, and 30-day TCO budget projection engine. |
| **Client Discovery & Scope** | [`docs/`](docs/) | Consultative discovery call blueprint, solution architecture diagrams, and proposal templates for SMB clients. |

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    InboundPayload[Inbound Lead / Webhook] --> Guard[Security Guardrail: PromptGuard]
    
    subgraph Security Layer
        Guard -->|Scans for Injection & Redacts PII| Router[Intelligent Model Router]
    end
    
    subgraph Provider Tier
        Router -->|Primary| Gemini[Google Gemini 1.5 Flash]
        Router -->|Failover| OpenAI[OpenAI GPT-4o-mini]
        Router -->|Complex Reasoning| Claude[Anthropic Claude 3.5 Sonnet]
    end

    Gemini --> Validator[Structured Output Validator]
    OpenAI --> Validator
    Claude --> Validator
    
    subgraph Agentic Execution & Tools
        Validator -->|Validated JSON Schema| MCPServer[MCP Server: Agency Tools]
        MCPServer -->|CRM Tool| HubSpot[HubSpot CRM]
        MCPServer -->|Billing Tool| Quickbooks[Quickbooks Online]
        MCPServer -->|Notify Tool| M365[Microsoft 365 / Email]
    end
    
    Validator --> CostTracker[Token & TCO Governance]
```

---

## ⚡ Quickstart & Local Setup

### 1. Clone & Install Dependencies
```bash
git clone https://github.com/your-username/agency-ai-integrator-suite.git
cd agency-ai-integrator-suite
pip install -r requirements.txt
```

### 2. Run Automated Test Suite
```bash
py -m unittest discover tests
```

### 3. Test MCP Server & Tools
```bash
py -m mcp_server.client_runner
```

### 4. Test End-to-End AI Lead Enrichment Pipeline
```bash
py -m workflows.lead_enrichment_agent
```

### 5. Calculate Token & Infrastructure Cost Projection
```bash
py -m governance.token_calculator
```

---

## 🔒 Security & Data Compliance

- **Prompt Injection Filter**: Blocks pattern vectors such as `ignore previous instructions`, `system prompt override`, and malicious script tags.
- **PII Scrubbing**: Automatically replaces SSNs and credit card numbers with `[REDACTED_SSN]` before forwarding payloads to external LLM providers.
- **Output Schema Enforcer**: Ensures zero downstream failures in Quickbooks/HubSpot integrations by enforcing strict JSON validation.

---

## 📄 License & Attribution

Distributed under the MIT License. Built for digital agencies scaling AI automations and client integrations.
