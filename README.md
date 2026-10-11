# Hi, I'm Franz Xu

**AI systems · Agent infrastructure · Software engineering**

I build AI-enabled software with explicit execution boundaries, reproducible evidence, and understandable failure modes. My work spans enterprise agents, Rust systems, automated code review, on-chain engineering, and shipped iOS products.

I'm pursuing an **MSc in Blockchain Technology at Nanyang Technological University**, graduating **January 2027**, following a bachelor's in **Business Information Technology at the University of Twente**.

**Open to graduate / early-career engineering roles** in AI systems, agent platforms, software infrastructure, and applied AI. I'm also interested in blockchain and security-oriented systems engineering.

---

## Industry engineering

**ICBC — QUEST Requirement Agent**

Designed and primarily implemented the upstream Requirement Agent for ICBC's in-house QUEST platform. The work connects requirements analysis with structured outputs, evidence-backed conclusions, validation gates, and reliable agent workflows.

**Sqills · Siemens Mobility — Software Engineering Internship**

Built **Sqills Mixer**, a Slack bot for recurring colleague matching. Worked with Java, Spring Boot, MyBatis Plus, Redis/Redisson, and Docker in a GitLab/Jira development workflow.

## Open-source contributions

**[pandas — merged regression fix](https://github.com/pandas-dev/pandas/pull/69668)**  
Diagnosed and fixed a regression in `Series.str.zfill` on PyArrow-backed strings: negative widths raised `ArrowInvalid` instead of returning the original string. Contributed the fix and a regression test; reviewed and merged by a core maintainer.

## Selected projects

### [Sovereign Founder OS](https://github.com/IcantFind-a-username/Sovereign-Founder-OS)
**Rust · Local-first software · Agent execution boundaries**

A local-first workspace prototype combining structured business state, six bounded AI employee roles, and a security-oriented Rust execution layer.

- Scoped capabilities and deterministic policy gates separate model proposals from execution authority.
- Bounded Wasm execution, audit records, and explicit ambiguous-effect states make failures inspectable.
- Privacy controls let users inspect what information would be sent to a model.

**Status:** developer preview; feature development paused. It is a product prototype, not a production security guarantee.

[Architecture](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/blob/main/ARCHITECTURE.md) · [Threat model](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/blob/main/THREAT_MODEL.md)

### [Attest](https://github.com/IcantFind-a-username/Attest)
**Python · Differential testing · Evidence-backed AI code review**

An experimental GitHub Action where a model investigates potential defects and a deterministic certification kernel decides which claims have enough evidence to publish.

Generated tests run against the PR head and merge base in network-free, secretless containers. Reports are backed by reproducible receipts; silence is treated as abstention.

**Status:** public release **v0.3.0**; active development paused.

[Release](https://github.com/IcantFind-a-username/Attest/releases/tag/v0.3.0) · [GitHub Marketplace](https://github.com/marketplace/actions/attest-pull-request-review) · [Evidence receipts](https://github.com/IcantFind-a-username/Attest/blob/main/docs/receipts.md)

### On-chain systems research
**DeFi · Historical replay · Transaction simulation**

A private engineering project exploring liquidation mechanics, historical chain-state reconstruction, oracle behavior, simulation, and execution economics. The work emphasizes reproducibility, fail-closed controls, and validating assumptions before real execution.

### Miao Care (喵护)
**iOS · Product engineering · Shipped**

A cat-care companion that I developed from concept through implementation and App Store release. It complements my systems work with hands-on experience in mobile UX and end-to-end product delivery.

### [Corum](https://github.com/IcantFind-a-username/Corum)
**Research · Multi-model evaluation**

A concluded study of dependence-aware consensus among AI reviewers. A central lesson: model agreement is not automatically independent evidence. This informed my later work on separating probabilistic judgment from publication and execution rules.

---

## Engineering interests

| Area | Focus |
| --- | --- |
| **AI systems** | Agent orchestration, structured workflows, evaluation, evidence provenance |
| **Software infrastructure** | Rust, execution boundaries, state machines, auditability, failure recovery |
| **Backend engineering** | Python, Java / Spring Boot, Redis, Docker |
| **Blockchain** | Solidity / Foundry, DeFi mechanics, simulation, applied cryptography |
| **Product delivery** | Turning complex systems into usable software and shipping to users |

I use AI coding tools extensively. Architecture, validation, technical understanding, and responsibility for the result remain mine.

> Build useful systems. Make their assumptions, authority, and failure modes explicit.
