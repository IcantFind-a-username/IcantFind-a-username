# Yiqun (Franz) Xu

**Applied AI Engineer — agents, evaluation and guardrails for real workflows**

Singapore · +65 9439 8299 · franzxu28@gmail.com · [github.com/IcantFind-a-username](https://github.com/IcantFind-a-username) · [linkedin.com/in/yiqun-xu-8627a8264](https://www.linkedin.com/in/yiqun-xu-8627a8264)

Software engineer with 7 years of programming, now building production AI agent systems. Sole developer of ICBC QUEST's requirement-intake agent, delivered in Aug 2026 and being integrated into the bank's core agent platform. Creator of two open-source agent systems (100+ GitHub stars, 2,100+ tests) built around evaluation, guardrails and honest reporting. Principle: models propose; deterministic systems verify, constrain and decide.

## Experience

**AI Agent Engineer Intern — ICBC Software Development Center, Qichen Future Lab** · Jul – Aug 2026  
Shanghai · Python · LLM dialogue agent · sole developer

- Built the Requirement Agent of QUEST, ICBC's core in-house agent platform: multi-turn Chinese dialogue that turns vague business requests into machine-verifiable problem bundles.
- Delivered to the core team as the platform's requirement-intake layer; now being merged into the QUEST core for bank-wide internal release in 2027.
- LLM-first reasoning under deterministic authority: domain invariants, a bundle validator, state merging, layered fault tolerance and regression suites shield the live system from unstable model output.

**Software Development Intern — Sqills (a Siemens Mobility company)** · Feb – Apr 2025  
Enschede, Netherlands · Java · Spring Boot · Redis

- Core developer of an internal Slack meeting-matching bot now in daily company use; Redisson locks removed race conditions under concurrent matching.
- Integrated a generative-AI API with Slack and Google Calendar; layered prompts and context pruning cut token cost while raising match accuracy. Shipped in Scrum sprints with Docker and GitLab CI/CD.

**Application Developer — Earnit** · Apr – Jun 2023  
Enschede, Netherlands · Java · MySQL

- Full-stack developer on a recruitment platform for a paying Dutch client, from requirements and sprint planning to code review and delivery.

## Selected projects

**[Sovereign Founder OS — local-first AI operating system for a one-person company](https://github.com/IcantFind-a-username/Sovereign-Founder-OS)** · Jul 2026 – present  
Creator, sole developer · Rust · 18 crates · ~55k lines · 500+ tests · 104 GitHub stars · desktop app

- Six AI employees (requirements analyst, proposal writer, delivery planner, invoice clerk, quality checker, compliance checker) work over a real CRM, project, document and invoice graph; each role sees only the facts its typed input carries.
- Employees propose, never act: approval applies exactly the recorded change through a deterministic policy gate and leaves a signed, hash-chained audit event. An adversarial suite proves prompt injection cannot authorise a high-risk action.
- A local model (Ollama) drafts only when its JSON passes typed validation and field guards; otherwise a template is used and the record says so. Live evaluation of all six roles in two languages raised validated output from 27/30 to 30/30 after fixing one transport and two schema defects.
- 13-rule Singapore compliance pack (GST, e-invoicing, corporate tax, ACRA, PDPA), every rule citing its source; findings are pass / action / review / unknown, never “compliant”. Before any text reaches a public model the owner sees the exact outbound bytes, PII reduced, and their hash.

**[Attest — AI code reviewer that publishes only what it has reproduced](https://github.com/IcantFind-a-username/Attest)** · Aug 2026 – present  
Creator, sole developer · Python · GitHub Action · ~53k lines · 1,600+ tests · 186 decision records

- The model proposes candidate defects; a kernel that calls no model decides what is published. A generated test must fail on the head commit and pass on the merge base, three runs each, in a network-free container, with an offline-verifiable receipt.
- Measured with intervals: crash-class recall 20.0% (5 of 25, Wilson 95% [8.9%, 39.1%]) on held-out SWE-bench Verified; zero false publications across 28 real pull requests and 108 control diffs; 13 of 13 red-team attack classes contained.
- Runs as a one-file GitHub Action with a bring-your-own key that never leaves the user's runner; mean review cost $0.22 under a hard budget cap. Ranking core came from Corum, my preregistered consensus study that ended in an honest negative result.

**Distributed Banking System — UDP client–server with explicit delivery semantics** · Nov 2025 – Feb 2026  
NTU course project · 4-person team · system design and core development · Java

- Hand-written binary wire protocol with a push channel; compared at-least-once vs at-most-once delivery with deduplication and idempotency under simulated packet loss, reordering and delay.

## Research

**Attention Economics for Agent Messaging — NTU × Taiko (Ethereum L2)** · Jan 2026 – present  
Trusted Agents Protocol (ERC-8004 + XMTP) · TypeScript · 3-person team

- Built TAP's attention layer (+8.2k lines): enqueue-time coalescing, escalation-first rendering and a per-peer attention ledger; benchmarked OpenClaw, Hermes Agent and LangGraph on token efficiency vs task completion.

**Predicting Student Team Effectiveness from Longitudinal Data — Bachelor thesis** · Apr – Jun 2025  
University of Twente · TScIT 43, first author

- Leakage-safe study over 56 teams / 435 students comparing linear regression, random forest and XGBoost with SHAP; supervisor recommended submission to a top-tier ACM venue.

## Education

**MSc Blockchain Technology — Nanyang Technological University, Singapore** · Nov 2025 – Nov 2026  
Top grade in Cryptography & Network Security and Blockchain Technology · Distributed Systems · System Design

**BSc Business & Information Technology — University of Twente, Netherlands** · Sep 2022 – Jul 2025  
Software Engineering · Databases · Artificial Intelligence · Network Security · Probability & Statistics

## Technical skills

- **AI / agents:** agent harness engineering · tool calling · structured outputs with schema validation · context engineering · LLM evaluation and regression suites · guardrails and policy-as-code · cost budgeting · Anthropic API · Ollama · LangGraph
- **Languages:** Python · Rust · Java · TypeScript / JavaScript · Solidity · SQL
- **Backend / systems:** Spring Boot · Redis · PostgreSQL / MySQL · REST · concurrency · idempotency and delivery semantics · crash-safe recovery · WebAssembly sandboxing · signed audit chains · applied cryptography
- **Infrastructure:** Docker · GitHub Actions · GitLab CI/CD · Linux · Scrum · Claude Code / Codex / Cursor

## Certifications and languages

Meta Back-End Developer Professional Certificate (2024) · Meta Full-Stack Developer Certificate (2023) · Stanford Online algorithms courses (2023) · Software Copyright Registration, NCAC China (2020)

Mandarin (native) · English (professional working proficiency)
