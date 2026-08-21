# System Architecture & Technical Specifications

This repository serves as a showcase of **production-grade AI engineering, agentic architecture, security guardrails, and cost governance** designed for digital agencies and SMB client integrations.

---

## 1. Architectural Pillars

### Pillar A: Model Context Protocol (MCP) Integration
- Built using the official Model Context Protocol standard (`FastMCP`).
- Decouples AI decision-making from hardcoded APIs by exposing agency capabilities (CRM profile lookup, campaign analytics, automated logging) as standardized tools.

### Pillar B: Multi-Provider Resilience & Intelligent Routing
- Eliminates single-vendor lock-in by providing dynamic failover across **Google Gemini**, **OpenAI**, and **Anthropic**.
- Implements latency measurement and cost-based routing (e.g., routing high-volume standard queries to low-cost Flash models, reserving frontier models for complex multi-step reasoning).

### Pillar C: Enterprise Security & Guardrails
- **Input Verification**: Sanitizes prompts for prompt injection vulnerabilities, system prompt override patterns, and unwanted scripts.
- **PII Scrubbing**: Automatically detects and redacts SSNs and credit card numbers prior to model inference.
- **Output Schema Governance**: Enforces schema validation using Pydantic, ensuring LLMs generate 100% compliant JSON payloads.

### Pillar D: Token & Infrastructure Cost Analytics
- Real-time USD cost calculation per request based on exact token input/output metrics.
- 30-day TCO projections for client proposals, allowing transparent budget conversations with non-technical business owners.

---

## 2. Data & Execution Flow

```
[Inbound Webhook / Form]
       │
       ▼
[Security Middleware] ──── (Unsafe) ────► [Reject Payload & Log Alert]
       │
    (Safe)
       ▼
[Intelligent Router] ─── (Outage) ───► [Fallback Provider]
       │
       ▼
[LLM Inference]
       │
       ▼
[Output Validator]   ──── (Invalid) ──► [Trigger Retry / Diagnostic Alert]
       │
    (Valid)
       ▼
[MCP Server & Tools] ───────────────► [HubSpot / Quickbooks / M365]
       │
       ▼
[Cost Governance Log]
```
