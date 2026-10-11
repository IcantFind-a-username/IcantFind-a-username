<div align="center">

# Franz Xu

### Build with curiosity. Verify with evidence.

Independent developer exploring **AI agents, local-first systems, and on-chain software**.  
Sometimes that means a Rust execution kernel. Sometimes it means an app for taking care of cats.

[Projects](#things-ive-built) · [Open-source contributions](#small-fixes-real-impact) · [Engineering notes](#ideas-i-keep-coming-back-to)

</div>

---

## The questions behind the code

Most of my projects start with a question I can't leave alone.

**What should an AI agent actually be allowed to do?**  
**What makes a generated claim worth trusting?**  
**What happens when a system fails halfway through an action?**

I explore those questions by building things: execution boundaries, differential tests, local-first workspaces, and small products people can use. I'm interested in the parts where a convincing demo has to become understandable software.

## Things I've built

### [Sovereign Founder OS](https://github.com/IcantFind-a-username/Sovereign-Founder-OS)
*A workspace for a one-person company, with AI employees that have boundaries.*

Structured company state, six bounded AI roles, and a Rust execution layer. Agents propose work; scoped capabilities and deterministic policies govern effects. Privacy controls make the outgoing model context inspectable.

This is where I explore authority, local ownership, and what an agent should do when an action's outcome is uncertain.

**Rust · Local-first · Wasm · Capability-based execution**  
Developer preview / prototype · feature development paused

[Architecture](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/blob/main/ARCHITECTURE.md) · [Threat model](https://github.com/IcantFind-a-username/Sovereign-Founder-OS/blob/main/THREAT_MODEL.md)

### [Attest](https://github.com/IcantFind-a-username/Attest)
*An AI code reviewer that has to bring receipts.*

The model investigates a possible defect. Generated tests run against the PR head and merge base in network-free, secretless containers. A deterministic certification kernel decides whether the evidence supports publishing a claim.

The interesting part is knowing when there is enough evidence to say something—and when to abstain.

**Python · Differential testing · Reproducible evidence**  
Released as an experimental GitHub Action · **v0.3.0** · development paused

[Release](https://github.com/IcantFind-a-username/Attest/releases/tag/v0.3.0) · [Marketplace](https://github.com/marketplace/actions/attest-pull-request-review) · [Receipts](https://github.com/IcantFind-a-username/Attest/blob/main/docs/receipts.md)

### [Corum](https://github.com/IcantFind-a-username/Corum)
*What does agreement between AI reviewers actually tell us?*

A concluded study of dependence-aware multi-model consensus. Its most useful lesson shaped the projects above: reviewers can agree for the same wrong reason. Aggregation alone cannot supply the evidence a system is missing.

**Multi-model evaluation · Dependence · Negative results**

## Beyond the public repos

**On-chain systems.** A private project exploring liquidation mechanics, historical state reconstruction, oracle behavior, and execution economics. A place to test protocol assumptions against chain data and simulation.

**Miao Care (喵护).** A cat-care companion I took from concept to iOS App Store release. A smaller, everyday problem—and a chance to make something useful outside the terminal.

**Agents at work.** I designed and primarily implemented the Requirement Agent for ICBC's QUEST platform. At Sqills, I built a Slack bot for recurring colleague matching. Both gave me practical problems to think through beyond my own projects.

## Small fixes, real impact

**[pandas #69668 — merged](https://github.com/pandas-dev/pandas/pull/69668)**

Fixed a regression in `Series.str.zfill` on PyArrow-backed strings: negative widths raised `ArrowInvalid` instead of returning the original string. The contribution includes a regression test.

I like this scale of contribution too: find a concrete failure, understand it, and leave behind a test.

## Ideas I keep coming back to

- **Intelligence and authority are separate design problems.** A good proposal still needs an execution boundary.
- **Claims should come with evidence.** Reproductions, tests, and explicit assumptions make a result easier to inspect.
- **“I don't know” belongs in the state machine.** Abstention and ambiguous outcomes deserve honest representation.
- **Local-first should be visible to the user.** People should be able to see what stays on their device and what leaves it.
- **A negative result can change the next design.** I keep the limitations alongside the things that worked.

I use AI coding tools extensively. I own the architecture, the validation, and the work of understanding what ships.

---

<sub>University of Twente · Business Information Technology → Nanyang Technological University · MSc in Blockchain Technology</sub>
