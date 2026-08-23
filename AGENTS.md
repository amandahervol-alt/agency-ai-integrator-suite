# Agency AI Integrator Suite — AI Orchestration Guide
AGENTS.md — Antigravity Orchestration Architecture

This repository defines an enterprise multi-agent integration framework for AI agencies and systems integrators.

## Core Pillars & Architecture

### 1. Model Context Protocol (MCP) Tier (`mcp_server/`)
- FastMCP server exposing tools for CRM profile queries, campaign analytics, and compliance audit logging.
- Follows MCP specifications compatible with Antigravity IDE and Claude Desktop.

### 2. Multi-Model Intelligent Router (`workflows/model_router.py`)
- Automatic failover across Anthropic Claude, OpenAI, and Google Gemini.
- Real-time token usage calculation and request cost attribution.
- Zero-config offline simulation mode for local testing without active API keys.

### 3. Security & Compliance Middleware (`security/`)
- `PromptGuard`: Pre-inference inspection for prompt injection patterns and automatic PII redaction (SSNs, credit cards).
- `StructuredOutputValidator`: Enforces strict Pydantic schemas on probabilistic LLM responses to eliminate downstream integration bugs.

### 4. Cost Governance & TCO Engine (`governance/`)
- Real-time request cost tracking.
- 30-day client TCO projections and cost-per-qualified-lead calculators.

## Antigravity IDE Compatibility
- MCP server can be registered in Antigravity or local MCP configurations (`mcp_config.json`).
- All agent workflows enforce Pydantic structured output validation.
