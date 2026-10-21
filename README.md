<div align="center">

# Franz Xu

### Build with curiosity. Verify with evidence.

Open-source contributor and independent developer working on **AI agent infrastructure and on-chain systems**.
I find, reproduce, and report regressions in Python libraries, and fix them when I can.

[Open source](#open-source-contributions) · [Current projects](#current-projects) · [Earlier work](#earlier-work)

</div>

---

## Open-source contributions

I contribute to Python libraries such as **pandas**, **SciPy**, and **Scapy**, mostly by finding regressions in recently merged changes, reducing them to small reproducible examples, and reporting them upstream.

**pandas: merged for pandas 3.1.** While testing pandas `main`, I found that `Series.str.zfill` raised `ArrowInvalid: Negative buffer resize` for a negative width on PyArrow-backed strings. That was a regression: pandas 3.0.x returned the strings unchanged. I reported it and then fixed it, with a regression test that runs across all string backends.

- Issue: [pandas #69486](https://github.com/pandas-dev/pandas/issues/69486), *`Series.str.zfill` with a negative width raises "Negative buffer resize" on pyarrow-backed strings (regression on main)*
- Fix: [pandas #69668](https://github.com/pandas-dev/pandas/pull/69668), *REGR: fix `Series.str.zfill` raising `ArrowInvalid` for negative width with pyarrow-backed strings* (merged, milestone 3.1)

Other reports:
[pandas #71188](https://github.com/pandas-dev/pandas/issues/71188) · [pandas #71189](https://github.com/pandas-dev/pandas/issues/71189) ·
[SciPy #26410](https://github.com/scipy/scipy/issues/26410) · [SciPy #26411](https://github.com/scipy/scipy/issues/26411) · [SciPy #26413](https://github.com/scipy/scipy/issues/26413) ·
[Scapy #5201](https://github.com/secdev/scapy/issues/5201) · [Scapy #5202](https://github.com/secdev/scapy/issues/5202) · [Scapy #5228](https://github.com/secdev/scapy/issues/5228) · [Scapy #5229](https://github.com/secdev/scapy/issues/5229)

## Current projects

### [agent-orchestra](https://github.com/IcantFind-a-username/agent-orchestra)
*One request in, five audited stages out, coordinated across the AI tools I already use.*

A personal orchestration base that has my own AI tools work on a task together instead of in separate windows. One request goes through five fixed stages: **plan → implement → independent review → test → summarize**. The implementer and the reviewer must come from different providers, and the kernel enforces that rule rather than leaving it to a prompt.

- **Durable state.** Tasks, stages, artifacts, and events live in SQLite, so a killed process resumes only the unfinished stages.
- **Independent review.** Each task gets an isolated worktree, and review is pinned to a specific commit SHA.
- **Approvals bound to one operation.** Each approval is tied to an operation digest and revision. If the change differs from what was shown, the approval is invalid.
- **Honest cost.** If a cost is unknown, it shows as `unknown`, never `$0`.
- **Native iPhone console.** A SwiftUI app (iOS 17+, no third-party dependencies) for submitting tasks, viewing history and stage details, and approving actions.

**Ground rules:** single user, loopback only. Each tool is reached only through its provider's official CLI or API, signed in with my own account and used under that provider's terms. The kernel never reads, copies, or stores credentials or session tokens. When a tool hits a rate limit, a quota, or an auth error, the task stops and waits. It does not switch accounts or work around limits. No sharing, pooling, or reselling of access.

**Python 3.12+ · zero runtime dependencies · SwiftUI · Apache-2.0**
Open source: the orchestration kernel (it ships with mock adapters only) and the iOS app. The fuller version with real tool integrations is private.

### [Pocket · dsh-iphone-control](https://github.com/IcantFind-a-username/dsh-iphone-control)
*DeepSeek Harness in your pocket: an unofficial community plugin.*

A native iPhone app plus a mobile web UI (PWA) for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DSH) running on your own computer. It connects over your own Tailscale network: no public ports and no third-party relay. DSH keeps listening only on `127.0.0.1`.

- Streaming replies with collapsible reasoning, and tool-call cards that show status, arguments, and output
- Session switching, new sessions, and a stop button that actually cancels the current turn
- Image attachments, plus per-turn stats (tokens, tok/s, cache-hit rate, duration)
- A balance panel that reads the local ledger of [dsh-whale-widget](https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget)
- Pairing token kept separate from DSH's own browser cookie

**DSH host plugin (JavaScript) · SwiftUI · PWA · Tailscale · MIT**

## Earlier work

- **[Sovereign Founder OS](https://github.com/IcantFind-a-username/Sovereign-Founder-OS):** local-first workspace with bounded AI roles and a Rust capability-based execution layer. Development has stopped.
- **[Attest](https://github.com/IcantFind-a-username/Attest):** evidence-first AI code review, released as an experimental GitHub Action (v0.3.0). Development has stopped.
- **[Corum](https://github.com/IcantFind-a-username/Corum):** concluded, preregistered study of dependence-aware consensus among AI reviewers. Its honest negative result shaped Attest.
- **[OneTapVocal](https://github.com/IcantFind-a-username/OneTapVocal):** one-tap pitch correction for singing videos. Paused.

## Beyond the public repos

**On-chain systems.** A private project exploring liquidation mechanics, historical state reconstruction, oracle behavior, and execution economics. It tests protocol assumptions against chain data and simulation.

**Agents at work.** I designed and did most of the implementation of the Requirement Agent for ICBC's QUEST platform. At Sqills, I built a Slack bot for recurring colleague matching.

## Ideas I keep coming back to

- **Intelligence and authority are separate design problems.** A good proposal still needs an execution boundary.
- **Claims should come with evidence.** Reproductions, tests, and explicit assumptions make a result easier to inspect.
- **"I don't know" belongs in the state machine.** Abstention, unknown cost, and ambiguous outcomes deserve honest representation.
- **A negative result can change the next design.**

I use AI coding tools extensively and disclose it where projects ask. I own the architecture, the validation, and the work of understanding what ships.

---

<sub>University of Twente · Business Information Technology → Nanyang Technological University · MSc in Blockchain Technology</sub>
