# Franz Xu

> Couldn't find a username — found a harder question:
>
> **How do we trust an AI agent with real authority?**

I build trustworthy AI infrastructure in the open — systems designed to stay
user-controlled, recoverable, and independent of any single model or platform.
My working thesis: an agent should be constrained by code and cryptography, not
by our hope that it behaves. Models are replaceable; user data is not.

## Building

### [Sovereign Founder OS](https://github.com/IcantFind-a-username/Sovereign-Founder-OS) · [Developer Preview](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/blob/main/ROADMAP.md)

[![CI](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/actions/workflows/ci.yml)
[![Stars](https://img.shields.io/github/stars/IcantFind-a-username/Sovereign-Founder-OS)](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/stargazers)
[![License](https://img.shields.io/github/license/IcantFind-a-username/Sovereign-Founder-OS)](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/blob/main/LICENSE)

<!-- sfos-status:start -->
**Status** (auto-updated weekly): CI on `main`: passing · last commit: 2026-08-14 · 5 design RFCs · no tagged release · checked 2026-08-26
<!-- sfos-status:end -->

A local-first, open-source operating system for running a one-person company
with AI agents **without surrendering data, decisions, or authority** to any
model, plugin, or provider — a design I call *Mutually Constrained Autonomy*.

It is a 16-member Rust workspace built around thirteen runtime crates and one
rule: **what the model suggests and what the system allows are separated.**
Sensitive authority comes from deterministic policy code and explicit human
approval, never from the model's own say-so.

```mermaid
flowchart TD
    U["Untrusted external content<br/>data only, never instructions"] --> M["AI planner<br/>proposes plans and actions"]
    M -- "proposal only, no authority" --> P{"Deterministic policy engine<br/>scope, risk, data class"}
    P -- "deny: fail closed" --> L
    P -- "high-risk action" --> H["Human owner approval<br/>signed approval evidence"]
    P -- "allowed" --> C
    H --> C["Capability token V2<br/>single-use, scoped, time-bound,<br/>bound to the exact invocation"]
    C --> S["Sandboxed executor<br/>import-free Wasmtime, fuel + memory limits"]
    S --> E["Brokered local effect<br/>rooted outbox write"]
    E --> L["Audit ledger<br/>Ed25519-signed hash chain"]
    L -. "evidence and state feed the next cycle" .-> M
```

*Target authority loop: model output passes a deterministic policy engine;
approved actions receive single-use, scoped, time-bound capability tokens;
untrusted code runs in an import-free wasmtime sandbox; every action lands in
an Ed25519-signed hash-chained audit ledger. Every stage is backed by an
implemented primitive; the assembled end-to-end path is currently labeled
Experimental — see the
[Roadmap](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/blob/main/ROADMAP.md).
(Simplified: artifact admission and the durable authority store are omitted
from the diagram.)*

What that looks like in the codebase today:

- **[Policy is code, not a prompt](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/tree/main/crates/policy)**
  — authorization decisions are deterministic, testable, and enforced outside
  the model.
- **[Authority expires](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/tree/main/crates/capability)**
  — actions run on single-use, scoped, time-bound capability tokens bound by
  signed approval evidence to the exact request they authorize.
- **[Every important action leaves evidence](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/tree/main/crates/audit-ledger)**
  — an Ed25519-signed, hash-chained audit ledger that detects tampering.
- **[Untrusted by default](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/tree/main/crates/sandbox)**
  — plugin and model output run inside a WebAssembly (wasmtime) sandbox, with
  untrusted code compiled in resource-limited, killable worker processes.
- **[Local-first state](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/tree/main/crates/vault)**
  — a per-entry encrypted vault and an append-only ledger that live on your
  machine under keys you hold.

The design is written down before it ships: five design
[RFCs](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/tree/main/rfcs)
(two approved as implementation targets), a cross-crate
[adversarial security-invariant test suite](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/blob/main/tests/adversarial/tests/security_invariants.rs),
and CI that enforces `clippy -D warnings`, formatting, dependency audit,
secret scanning, and file-size limits on every change.

**Honest about maturity.** This is a Developer Preview, and the project labels
current vs. planned work rather than claiming absolute security. Transactional
and revocable authority, a dual-root SQLCipher vault with recovery, hardened
model-routing boundaries, and the full Founder OS workflow are designed and in
active development — not finished features.

[Architecture](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/blob/main/ARCHITECTURE.md) ·
[Threat Model](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/blob/main/THREAT_MODEL.md) ·
[Security Policy](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/blob/main/SECURITY.md) ·
[Contributing](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/blob/main/CONTRIBUTING.md) ·
[RFCs](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/tree/main/rfcs) ·
[Roadmap](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/blob/main/ROADMAP.md)

## Other Work

- **[US Stock Helper](https://github.com/IcantFind-a-username/us-stock-helper)**
  — an in-development, read-only AI research copilot for U.S. equities
  (Python, 8 services): TD Setup (nine-count), candlestick patterns, and
  order-flow participation-proxy analysis over completed bars only. Read-only
  by construction: no package contains a broker, trade context, or
  order-submission interface — it analyzes, never places orders.

## Background

At the University of Twente I moved from Technical Computer Science into
Business Information Technology to work where software engineering, business
systems, and product meet (pre-2022 work lived on GitLab). After a bachelor's
thesis on machine-learning predictive modelling, I am now pursuing an MSc in
Blockchain Technology at Nanyang Technological University, Singapore. Industry
work includes the upstream Requirement Agent for ICBC's in-house QUEST
platform (2026, designer and primary implementer) and a multi-agent consensus
evaluation algorithm (internal).

## Connect

Open to security/infrastructure internships and collaboration on secure agent
runtimes — design review of the capability model is especially welcome.
Contributions start at
[CONTRIBUTING.md](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/blob/main/CONTRIBUTING.md)
or the [open issues](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/issues).

[LinkedIn](https://www.linkedin.com/in/yiqun-xu-8627a8264) (Yiqun "Franz" Xu) ·
[Email](mailto:franzxu28@gmail.com)
