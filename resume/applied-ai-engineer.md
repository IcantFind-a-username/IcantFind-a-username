# Franz (Yiqun) Xu

**Applied AI Engineer — agents, evaluation and guardrails for real workflows**

Singapore · franzxu28@gmail.com · [linkedin.com/in/yiqun-xu-8627a8264](https://www.linkedin.com/in/yiqun-xu-8627a8264) · [github.com/IcantFind-a-username](https://github.com/IcantFind-a-username)

<!-- TODO before sending: phone number; confirm the dates marked [ ] below. -->

## Summary

Engineer who ships AI systems end to end: LLM agents with typed inputs and
validated outputs, deterministic policy gates outside the model, offline-verifiable
audit trails, and evaluation harnesses that report intervals rather than
anecdotes. Sole author of two open-source production-shaped systems in 2026:
a local-first Rust operating system for running a one-person company with six
bounded AI employees (CRM, proposals, invoicing, Singapore compliance checks),
and a Python GitHub Action that lets an LLM review pull requests but only
publish claims it has reproduced. Designed and primarily implemented the
upstream Requirement Agent for ICBC's in-house QUEST platform. Comfortable
saying what a system cannot do: every number below links to a measurement.

## Skills

- **AI engineering:** LLM agents and workflows, tool/role design, structured
  output with schema validation and typed fallbacks, prompt repair driven by
  captured transcripts, local models (Ollama) and hosted APIs (Anthropic),
  evaluation harnesses, guardrails and policy-as-code, cost budgeting.
- **Languages:** Rust (~55k lines in production-shaped open source), Python
  3.11+ (~53k lines, pytest, ruff, mypy), JavaScript/TypeScript (JSDoc-typed,
  `tsc --checkJs`).
- **Systems:** Ed25519 signing, AES-GCM, hash-chained ledgers, capability
  tokens, WebAssembly sandboxing (Wasmtime), containerised execution, GitHub
  Actions, CI gates (clippy `-D warnings`, dependency audit, secret scanning).
- **Domain:** CRM and lead pipelines, quotes/proposals/invoices, receivables,
  document drafting and approval flows, Singapore GST/ACRA/PDPA rule checks,
  privacy-preserving data disclosure.

## Selected work

### Sovereign Founder OS — creator and sole maintainer (2026 – present)

Local-first, open-source AI operating system for running a one-person company.
Rust workspace of 18 crates, ~55k lines, 500+ tests, 7 accepted design RFCs,
Tauri desktop shell, bilingual (English/中文) web UI. Developer Preview; the
repository labels every boundary as current, experimental or target.
[github.com/IcantFind-a-username/Sovereign-Founder-OS](https://github.com/IcantFind-a-username/Sovereign-Founder-OS)

- **Six AI employees over a real business graph.** Requirements analyst,
  proposal writer, delivery planner, invoice clerk, quality checker and
  compliance checker operate on leads, customers, projects, dated tasks,
  documents with revisions, invoices and receivables. Each role's prompt is
  built from a typed `RoleInput` carrying only the facts it may see, so a role
  cannot widen its own view of the company.
- **Propose, never act.** Employees return a proposal and mutate nothing; the
  founder's approval applies exactly the recorded change through a
  deterministic policy gate and leaves a device-signed, hash-chained audit
  event. Prompt injection cannot authorise a high-risk action, and a
  cross-crate adversarial suite pins that and the token scope, expiry, replay
  and tamper invariants.
- **Validated model output with honest provenance.** A local model
  (`qwen2.5:7b` via a loopback-only Ollama adapter) drafts a proposal only when
  its JSON survives the typed struct, field guards and per-role checks;
  otherwise a deterministic template is used and the decision record says
  which, with the rejection reason (`not_json`, `truncated`, `wrong_shape`).
  A format guard on money fields refused `"4.000.000"` for a 5,000.00 offer,
  an invoice that would otherwise have been off by three orders of magnitude.
- **Measured, then fixed.** Live evaluation of all six roles, five runs each
  in two languages against identical facts, with every failing response
  captured verbatim through a logging proxy. Found one transport defect
  (chunked responses silently failing over to the template while health showed
  "healthy") and two prompt/schema defects; validated output rose from 27/30 to
  30/30 (English) and 27/30 to 29/30 (Chinese).
- **Compliance as data, cited.** A 13-rule Singapore pack (GST registration
  and tax-invoice fields, e-invoicing, corporate tax and ECI, ACRA filings,
  PDPA consent and DPO, record keeping, contracts, cross-border customers).
  Every rule carries its issuing authority, source URL and date read; findings
  are pass / action / review / unknown and never "compliant". A new
  jurisdiction is a new pack, not a code change.
- **A disclosure boundary the caller cannot argue around (RFC 0004).** Fields
  of unknown sensitivity default to protected; a registered, versioned
  transform must name every field it reads, so growing the data model cannot
  start leaking. Before any text could reach a public model the owner sees the
  per-field disposition, the exact outbound bytes (customer reduced to
  `[ORG_1]`, email dropped) and their SHA-256.

### Attest — evidence-first AI pull-request review, GitHub Action (2026 – present)

Python 3.11+, ~53k lines of source and ~53k of tests (1,600+ tests), 186
numbered decision records, 100+ dated acceptance reports. Private pilot.
[github.com/IcantFind-a-username/Attest](https://github.com/IcantFind-a-username/Attest)

- **The model proposes; a kernel that calls no model decides what may be
  said.** An LLM samples defect candidates (K=5) from a diff; candidates are
  ranked, then a generated test must fail on the head commit and pass on the
  merge base, three runs each way, inside a network-free, secretless
  container. Only that reproduction, an intent check and a hard cap of three
  findings per PR decide publication. Every published finding carries an
  offline-verifiable receipt (claim, hunk, exact test bytes, commands,
  interpreter, environment, seal).
- **Failure is a first-class output.** Budget exhaustion, unsupported
  environments and inconclusive evidence become a named `DEFER`; silence
  states how many change units it covers and is documented as never being a
  true negative.
- **Numbers with intervals, and what they are not.** Crash-class recall on a
  held-out SWE-bench Verified corpus: 5 of 25 (20.0%, Wilson 95% [8.9%,
  39.1%]), up from 6.5% entirely through measurement repair, and reported as
  such. Zero false publications across a prospective shadow over 28 real
  pull requests, 68 independent null controls and 40 held-out controls.
  Structural-note noise floor 1.47% [0.26%, 7.87%]. 13 of 13 red-team attack
  classes dispatched on the production backend were marked and never
  certified.
- **Operated like a product.** Installed as a one-file workflow plus one
  repository secret; the key never leaves the user's runner. Fork PRs are
  skipped by two independent gates before any credential enters a step, with
  no comment that could read as "reviewed, nothing found". Mean review cost
  $0.22 under a hard `budget-usd` cap; a dated spend ledger tracks every
  dollar of development and dogfood against an owner-set cap.

### Corum — preregistered research on multi-reviewer consensus (2026, concluded)

Fail-closed study of dependence-aware aggregation among imperfect AI
reviewers. Returned an honest negative result: with a few near-independent
reviewers no aggregation formula meaningfully beat reliability-weighted
voting. The calibrated posteriors and redundancy discount that survived audit
became Attest's ranking core. Preregistration, locked judge, append-only
ledgers, bit-reproducible results.

## Experience

**ICBC — QUEST platform, Requirement Agent** · designer and primary implementer · 2026 <!-- TODO: months, engagement type -->

- Designed and primarily implemented the upstream Requirement Agent for the
  bank's in-house QUEST platform: the component that turns raw business
  requirements into structured, reviewable inputs for downstream automation.
- Built a multi-agent consensus evaluation algorithm for objective assessment
  of AI outputs, later falsified and refined in the open through Corum.
  <!-- TODO: add one measured outcome (throughput, review time, adoption) if it can be shared. -->

## Education

- **Nanyang Technological University, Singapore** — MSc Blockchain Technology, in progress <!-- TODO: start year, expected graduation -->
- **University of Twente, Netherlands** — BSc, Technical Computer Science then Business Information Technology; bachelor's thesis on machine-learning predictive modelling <!-- TODO: years -->

## Languages

English (professional working language, all projects above are written and
documented in English) · Chinese (native)
