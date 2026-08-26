# Franz Xu

> I couldn't find a username. I found something harder:
>
> **How do we trust an AI agent with real authority?**

I build trustworthy AI infrastructure in the open — systems designed to stay
user-controlled, recoverable, and independent of any single model or platform.
My working thesis: an agent should be constrained by code and cryptography, not
by our hope that it behaves.

## Building

### [Sovereign Founder OS](https://github.com/IcantFind-a-username/Sovereign-Founder-OS) · Developer Preview

[![Rust](https://img.shields.io/badge/Rust-1.97-000000?logo=rust)](https://github.com/IcantFind-a-username/Sovereign-Founder-OS)
[![License](https://img.shields.io/badge/License-Apache--2.0-blue)](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/blob/main/LICENSE)
[![Maturity](https://img.shields.io/badge/Maturity-Developer%20Preview-orange)](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/blob/main/ROADMAP.md)

A local-first, open-source operating system for running a one-person company
with AI agents **without surrendering data, decisions, or authority** to any
model, plugin, or provider — a design I call *Mutually Constrained Autonomy*.

It is a 15-crate Rust workspace built on one rule: **what the model suggests
and what the system allows are separated.** Sensitive authority comes from
deterministic policy code and explicit human approval, never from the model's
own say-so.

What that looks like in the codebase today:

- **Policy is code, not a prompt** — authorization decisions are deterministic,
  testable, and enforced outside the model.
- **Authority expires** — actions run on single-use, scoped, time-bound
  capability tokens bound by signed approval evidence to the exact request they
  authorize.
- **Every important action leaves evidence** — an Ed25519-signed, hash-chained
  audit ledger that detects tampering.
- **Untrusted by default** — plugin and model output run inside a WebAssembly
  (wasmtime) sandbox, with untrusted code compiled in resource-limited,
  killable worker processes.
- **Local-first state** — a per-entry encrypted vault and an append-only
  ledger that live on your machine under keys you hold.

The design is written down before it ships: five accepted RFCs, a cross-crate
adversarial security-invariant test suite, and CI that enforces
`clippy -D warnings`, formatting, dependency audit, secret scanning, and
file-size limits on every change.

**Honest about maturity.** This is a Developer Preview, and the project labels
current vs. planned work rather than claiming absolute security. Transactional
and revocable authority, a dual-root SQLCipher vault with recovery, hardened
model-routing boundaries, and the full Founder OS workflow are designed and in
active development — not finished features.

[Repository](https://github.com/IcantFind-a-username/Sovereign-Founder-OS) ·
[Architecture](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/blob/main/ARCHITECTURE.md) ·
[Manifesto](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/blob/main/MANIFESTO.md) ·
[Threat Model](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/blob/main/THREAT_MODEL.md) ·
[Roadmap](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/blob/main/ROADMAP.md)

## Current Focus

Secure AI runtimes · Capability-based authorization · Local-first systems ·
Tamper-evident audit · Sandboxing (WebAssembly) · Applied cryptography

## Background

I started programming in 2019 and registered my first software copyright in
2020. At the University of Twente I moved from Technical Computer Science into
Business Information Technology to work where software engineering, business
systems, and product meet. Much of my early work lived on GitLab, so my public
GitHub history begins in 2022. After a bachelor's thesis on machine-learning
predictive modelling, I am now pursuing an MSc in Blockchain Technology at
Nanyang Technological University, Singapore.

## Selected Work

- **[Sovereign Founder OS](https://github.com/IcantFind-a-username/Sovereign-Founder-OS)**
  — secure, model-agnostic agent runtime and a reference Founder OS built on it
  (Rust; policy-as-code, capability tokens, tamper-evident audit, WASM sandbox).
- **[US Stock Helper](https://github.com/IcantFind-a-username/us-stock-helper)**
  — an in-development, read-only AI research copilot for U.S. equities. It
  monitors watchlists and combines real-time news, technical signals, and
  market sentiment to surface unusual activity and learn from trade reviews.
  Current capabilities include TD Sequential, candlestick-pattern, and
  ownership/activity analysis; personalized preference learning and a 13-agent
  adviser council adapted from the open-source
  [AI Hedge Fund](https://github.com/virattt/ai-hedge-fund) project are in
  development.
- **ICBC QUEST Requirement Agent** — designer and primary implementer of the
  upstream Requirement Agent for ICBC's in-house QUEST platform (internal
  project).
- **Multi-Agent Consensus Evaluation Algorithm** — an original multi-agent
  consensus algorithm for objective AI evaluation (internal implementation).

## Principles

> **Models are replaceable. User data is not.**
>
> **Authority must expire** — permission should be narrow, time-bound, and
> revocable.
>
> **Security is not a premium feature.** No AI should become a business's
> single point of failure.

## Connect

[LinkedIn](https://www.linkedin.com/in/yiqun-xu-8627a8264) · [Email](mailto:franzxu28@gmail.com)
