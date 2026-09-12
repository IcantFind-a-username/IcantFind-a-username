# YIQUN (FRANZ) XU

**Applied AI Engineer · agents, evaluation and guardrails for real financial workflows**

Singapore · +65 9439 8299 · franzxu28@gmail.com · [github.com/IcantFind-a-username](https://github.com/IcantFind-a-username) · [linkedin.com/in/yiqun-xu-8627a8264](https://www.linkedin.com/in/yiqun-xu-8627a8264)

Software engineer with 7 years of hands-on programming, now building production AI agent systems. Sole developer of ICBC QUEST's requirement-intake agent, delivered Aug 2026 and being integrated into the bank's core agent platform for bank-wide release in 2027. Production Java / Spring Boot at Siemens Mobility. Creator of two open-source agent systems (100+ GitHub stars, 2,100+ tests) that treat evaluation, guardrails and honest reporting as the product, not an afterthought. Principle: models propose; deterministic systems verify, constrain and decide. Based in Singapore; MSc at NTU, graduating Nov 2026.

## Experience

**AI Agent Engineer Intern — ICBC Software Development Center · Qichen Future Lab** · Shanghai, on-site · Jul 2026 – Aug 2026<br>
Python · LLM dialogue agent · bank's core in-house agent platform · sole developer, delivered to production

- Sole developer of the Requirement Agent of QUEST, ICBC's core in-house agent platform. Turns vague business requests into machine-verifiable problem bundles through multi-turn Chinese dialogue. Delivered to the core team and integrated as the platform's requirement-intake layer (Aug 2026); now being merged into the QUEST core for bank-wide internal release in 2027 at the largest bank in China by assets.
- Designed the pipeline end to end: clarification and conflict handling → canonical task model → deterministic validation → template routing and slot projection → rendered problem bundle consumed directly by the QUEST core.
- LLM-first reasoning, deterministic authority: domain invariants, a bundle validator, task-migration state merging, multi-layer fault tolerance and regression suites protect the live system from unstable model output. Also prototyped a calibration-weighted multi-agent consensus evaluator.

**Software Development Intern — Sqills (a Siemens Mobility company)** · Enschede, Netherlands, on-site · Feb 2025 – Apr 2025<br>
Java · Spring Boot · Redis · internal tool in daily use · customers include SNCF, Renfe, Amtrak, Eurostar

- Core developer, requirements to release, of an internal Slack meeting-matching bot now in daily company use: Spring Boot backend with Redis caching and Redisson locks that removed race conditions under concurrent matching.
- Integrated a generative-AI API with Slack and Google Calendar; layered prompts and context pruning cut token cost while raising match accuracy. Shipped in Scrum sprints with Docker and GitLab CI/CD.

**Application Developer — Earnit** · Enschede, Netherlands, remote · Apr 2023 – Jun 2023

- Full-stack developer (Java / Javaweb + MySQL) on a recruitment platform for a paying Dutch client: requirements, sprint planning, implementation, code review and delivery.

## Selected projects

**Sovereign Founder OS — a local-first AI operating system for running a one-person company** · Jul 2026 – Present<br>
[github.com/IcantFind-a-username/Sovereign-Founder-OS](https://github.com/IcantFind-a-username/Sovereign-Founder-OS) · creator and sole developer · Rust · 18 crates · ~55k lines · 500+ tests · 7 design RFCs · 104 GitHub stars · Tauri desktop app · Developer Preview

- Six hireable AI employees (requirements analyst, proposal writer, delivery planner, invoice clerk, quality checker, compliance checker) work over a real business graph: leads and customers with pipeline stage and consent, projects with dated tasks, documents with revisions and signed send approvals, invoices and receivables. Each role's prompt is built from a typed input carrying only the facts it may see.
- Employees propose and never act: the founder's approval applies exactly the recorded change through a deterministic policy gate and leaves a device-signed, hash-chained audit event. A cross-crate adversarial suite pins that prompt injection cannot authorise a high-risk action and that capability scope, expiry, replay and tamper checks hold.
- Model output is used only when it validates: a local model (qwen2.5:7b via a loopback-only Ollama adapter) drafts a proposal if its JSON survives the typed struct, field guards and per-role checks; otherwise a deterministic template is used and the record says which, with the rejection class. A money-format guard refused `4.000.000` for a 5,000.00 offer, an invoice that would otherwise be off by three orders of magnitude.
- Evaluated live: all six roles, five runs each in two languages against identical facts, every failure captured verbatim through a logging proxy. Fixed one transport defect that silently failed over to templates while health read "healthy" and two prompt/schema defects; validated output rose from 27/30 to 30/30 (English) and 27/30 to 29/30 (Chinese).
- Compliance as cited data: a 13-rule Singapore pack (GST registration and tax-invoice fields, e-invoicing, corporate tax and ECI, ACRA filings, PDPA consent and DPO, record keeping, contracts, cross-border customers), every rule carrying its authority, source URL and date read; findings are pass / action / review / unknown and never "compliant". A new jurisdiction is a new pack, not a code change.
- A disclosure boundary the caller cannot argue around: unknown fields default to protected, a registered transform must name every field it reads, and before any text could reach a public model the owner sees the exact outbound bytes (customer reduced to `[ORG_1]`, email dropped) and their SHA-256.

**Attest — AI code reviewer that publishes only what it has reproduced** · Aug 2026 – Present<br>
[github.com/IcantFind-a-username/Attest](https://github.com/IcantFind-a-username/Attest) · creator and sole developer · Python 3.11+ · GitHub Action · ~53k lines · 1,600+ tests · 186 decision records · 100+ dated acceptance reports · private pilot

- The model proposes candidate defects (K=5 samples per diff) and writes the prose; a certification kernel that calls no model decides what is published. A generated test must fail on the head commit and pass on the merge base, three runs each way, inside a network-free, secretless container; every published finding carries an offline-verifiable receipt (claim, hunk, exact test bytes, commands, interpreter, environment, seal). Hard cap of three findings per pull request.
- Failure is first-class output: budget exhaustion, unsupported environments and inconclusive evidence become a named `DEFER`, and a silence states how many change units it covers; it is documented as never being a true negative.
- Measured with intervals: crash-class recall on a held-out SWE-bench Verified corpus 5 of 25 (20.0%, Wilson 95% [8.9%, 39.1%]), up from 6.5% entirely through measurement repair and reported as such. Zero false publications across a prospective shadow over 28 real pull requests, 68 independent null controls and 40 held-out controls. 13 of 13 red-team attack classes on the production backend marked and never certified.
- Runs like a product: one workflow file plus one repository secret, the key never leaves the user's runner, fork PRs skipped by two independent gates before any credential enters a step. Mean review cost $0.22 under a hard budget cap, with a dated spend ledger for every development dollar.

**Distributed Banking System — UDP client–server with explicit delivery semantics** · NTU, 4-person team, system design and core development · Java · Nov 2025 – Feb 2026

- Hand-written binary wire protocol over UDP with a server-side push channel; implemented and compared at-least-once vs at-most-once delivery with deduplication and idempotency under simulated packet loss, reordering and delay.

**On-Chain Verifiable Randomness DApp** · NTU, 5-person team, smart-contract lead · Solidity · Chainlink VRF v2.5 · Ethers.js · Mar 2026 – May 2026

- Built the on-chain core: VRF request/callback and retry flow, treasury with house pool and edge, multi-token ERC-20 betting with per-bet limits; owned the Sepolia deployment and the review against oracle and settlement failures.

## Research

**Attention Economics for Agent Messaging — NTU × Taiko (Ethereum L2)** · Trusted Agents Protocol (ERC-8004 identity + XMTP) · TypeScript · 3-person team incl. industry liaison · Jan 2026 – Present

- Built TAP's attention layer (22 commits, +8.2k lines): enqueue-time coalescing, escalation-first rendering and a per-peer attention ledger; benchmarked OpenClaw, Hermes Agent and LangGraph on token efficiency vs task completion. Priced attention on-chain with tiered senders, machine-readable quotes and USDC postage backed by receiver-signed credit certificates.

**Corum — preregistered study of consensus among imperfect AI reviewers** · sole author · Python · Aug 2026, concluded

- Fail-closed experiment with a locked judge and append-only ledgers returned an honest negative result: with a few near-independent reviewers no aggregation formula meaningfully beat reliability-weighted voting. The calibrated posteriors and redundancy discount that survived audit became Attest's ranking core.

**Predicting Student Team Effectiveness from Longitudinal Data — Bachelor thesis** · University of Twente · TScIT 43, first author · Apr 2025 – Jun 2025

- Leakage-safe longitudinal study over 56 teams / 435 students: linear regression vs random forest vs XGBoost with SHAP for behavioural drivers; supervisor recommended submission to a top-tier ACM venue.

## Education

**MSc Blockchain Technology — Nanyang Technological University (NTU), Singapore** · Nov 2025 – Nov 2026<br>
Top grade in Cryptography & Network Security and Blockchain Technology · Distributed Systems · System Design

**BSc Business & Information Technology — University of Twente, Netherlands** · Sep 2022 – Jul 2025<br>
Software Engineering · Databases · Artificial Intelligence · Network Security · Probability & Statistics

## Technical skills

- **AI / agents:** agent harness engineering · tool / function calling · structured outputs with schema validation and typed fallbacks · context engineering · evidence grounding · LLM evaluation, regression suites and held-out measurement with confidence intervals · guardrails and policy-as-code · cost budgeting · Anthropic API · Ollama local models · LangGraph
- **Languages:** Python · Rust · Java · TypeScript / JavaScript · Solidity · SQL
- **Backend / distributed:** Spring Boot · Redis / Redisson · PostgreSQL / MySQL · REST · concurrency · delivery semantics and idempotency · replication and quorum · 2PC / Saga · BFT · crash-safe recovery
- **Trust / security:** WebAssembly sandboxing (Wasmtime) · capability-based access control · Ed25519-signed audit chains · AES-GCM · secretless containers · Solidity / EVM · Chainlink VRF · applied cryptography
- **Infrastructure:** Docker · GitHub Actions · GitLab CI/CD · Linux · Scrum · Claude Code / Codex / Cursor

## Certifications and languages

Meta Back-End Developer Professional Certificate (2024) · Meta Full-Stack Developer Certificate (2023) · Stanford Online: Divide & Conquer, Sorting and Searching, Randomized Algorithms (2023) · Computer Software Copyright Registration, NCAC China (2020)

Mandarin (native) · English (professional working proficiency; every project above is built and documented in English)
