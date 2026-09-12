import html, subprocess
import os; S=os.path.dirname(os.path.abspath(__file__))
NAME="Yiqun (Franz) Xu"
TAG="Applied AI Engineer — agents, evaluation and guardrails for real workflows"
CONTACT=["Singapore","+65 9439 8299","franzxu28@gmail.com","github.com/IcantFind-a-username","linkedin.com/in/yiqun-xu-8627a8264"]
LINKS={"github.com/IcantFind-a-username":"https://github.com/IcantFind-a-username","linkedin.com/in/yiqun-xu-8627a8264":"https://www.linkedin.com/in/yiqun-xu-8627a8264"}
SUMMARY=("Software engineer with 7 years of programming, now building production AI agent systems. "
 "Sole developer of ICBC QUEST's requirement-intake agent, delivered in Aug 2026 and being integrated into the bank's core agent platform. "
 "Creator of two open-source agent systems (100+ GitHub stars, 2,100+ tests) built around evaluation, guardrails and honest reporting. "
 "Principle: models propose; deterministic systems verify, constrain and decide.")

# sections: list of (heading, [entries]); entry = dict(title, meta, date, bullets, link)
SECTIONS=[
("Experience",[
 dict(title="AI Agent Engineer Intern — ICBC Software Development Center, Qichen Future Lab", meta="Shanghai · Python · LLM dialogue agent · sole developer", date="Jul – Aug 2026", bullets=[
  "Built the Requirement Agent of QUEST, ICBC's core in-house agent platform: multi-turn Chinese dialogue that turns vague business requests into machine-verifiable problem bundles.",
  "Delivered to the core team as the platform's requirement-intake layer; now being merged into the QUEST core for bank-wide internal release in 2027.",
  "LLM-first reasoning under deterministic authority: domain invariants, a bundle validator, state merging, layered fault tolerance and regression suites shield the live system from unstable model output."]),
 dict(title="Software Development Intern — Sqills (a Siemens Mobility company)", meta="Enschede, Netherlands · Java · Spring Boot · Redis", date="Feb – Apr 2025", bullets=[
  "Core developer of an internal Slack meeting-matching bot now in daily company use; Redisson locks removed race conditions under concurrent matching.",
  "Integrated a generative-AI API with Slack and Google Calendar; layered prompts and context pruning cut token cost while raising match accuracy. Shipped in Scrum sprints with Docker and GitLab CI/CD."]),
 dict(title="Application Developer — Earnit", meta="Enschede, Netherlands · Java · MySQL", date="Apr – Jun 2023", bullets=[
  "Full-stack developer on a recruitment platform for a paying Dutch client, from requirements and sprint planning to code review and delivery."]),
]),
("Selected projects",[
 dict(title="Sovereign Founder OS — local-first AI operating system for a one-person company", link="https://github.com/IcantFind-a-username/Sovereign-Founder-OS", meta="Creator, sole developer · Rust · 18 crates · ~55k lines · 500+ tests · 104 GitHub stars · desktop app", date="Jul 2026 – present", bullets=[
  "Six AI employees (requirements analyst, proposal writer, delivery planner, invoice clerk, quality checker, compliance checker) work over a real CRM, project, document and invoice graph; each role sees only the facts its typed input carries.",
  "Employees propose, never act: approval applies exactly the recorded change through a deterministic policy gate and leaves a signed, hash-chained audit event. An adversarial suite proves prompt injection cannot authorise a high-risk action.",
  "A local model (Ollama) drafts only when its JSON passes typed validation and field guards; otherwise a template is used and the record says so. Live evaluation of all six roles in two languages raised validated output from 27/30 to 30/30 after fixing one transport and two schema defects.",
  "13-rule Singapore compliance pack (GST, e-invoicing, corporate tax, ACRA, PDPA), every rule citing its source; findings are pass / action / review / unknown, never “compliant”. Before any text reaches a public model the owner sees the exact outbound bytes, PII reduced, and their hash."]),
 dict(title="Attest — AI code reviewer that publishes only what it has reproduced", link="https://github.com/IcantFind-a-username/Attest", meta="Creator, sole developer · Python · GitHub Action · ~53k lines · 1,600+ tests · 186 decision records", date="Aug 2026 – present", bullets=[
  "The model proposes candidate defects; a kernel that calls no model decides what is published. A generated test must fail on the head commit and pass on the merge base, three runs each, in a network-free container, with an offline-verifiable receipt.",
  "Measured with intervals: crash-class recall 20.0% (5 of 25, Wilson 95% [8.9%, 39.1%]) on held-out SWE-bench Verified; zero false publications across 28 real pull requests and 108 control diffs; 13 of 13 red-team attack classes contained.",
  "Runs as a one-file GitHub Action with a bring-your-own key that never leaves the user's runner; mean review cost $0.22 under a hard budget cap. Ranking core came from Corum, my preregistered consensus study that ended in an honest negative result."]),
 dict(title="Distributed Banking System — UDP client–server with explicit delivery semantics", meta="NTU course project · 4-person team · system design and core development · Java", date="Nov 2025 – Feb 2026", bullets=[
  "Hand-written binary wire protocol with a push channel; compared at-least-once vs at-most-once delivery with deduplication and idempotency under simulated packet loss, reordering and delay."]),
]),
("Research",[
 dict(title="Attention Economics for Agent Messaging — NTU × Taiko (Ethereum L2)", meta="Trusted Agents Protocol (ERC-8004 + XMTP) · TypeScript · 3-person team", date="Jan 2026 – present", bullets=[
  "Built TAP's attention layer (+8.2k lines): enqueue-time coalescing, escalation-first rendering and a per-peer attention ledger; benchmarked OpenClaw, Hermes Agent and LangGraph on token efficiency vs task completion."]),
 dict(title="Predicting Student Team Effectiveness from Longitudinal Data — Bachelor thesis", meta="University of Twente · TScIT 43, first author", date="Apr – Jun 2025", bullets=[
  "Leakage-safe study over 56 teams / 435 students comparing linear regression, random forest and XGBoost with SHAP; supervisor recommended submission to a top-tier ACM venue."]),
]),
("Education",[
 dict(title="MSc Blockchain Technology — Nanyang Technological University, Singapore", meta="Top grade in Cryptography & Network Security and Blockchain Technology · Distributed Systems · System Design", date="Nov 2025 – Nov 2026"),
 dict(title="BSc Business & Information Technology — University of Twente, Netherlands", meta="Software Engineering · Databases · Artificial Intelligence · Network Security · Probability & Statistics", date="Sep 2022 – Jul 2025"),
]),
]
SKILLS=[
 ("AI / agents","agent harness engineering · tool calling · structured outputs with schema validation · context engineering · LLM evaluation and regression suites · guardrails and policy-as-code · cost budgeting · Anthropic API · Ollama · LangGraph"),
 ("Languages","Python · Rust · Java · TypeScript / JavaScript · Solidity · SQL"),
 ("Backend / systems","Spring Boot · Redis · PostgreSQL / MySQL · REST · concurrency · idempotency and delivery semantics · crash-safe recovery · WebAssembly sandboxing · signed audit chains · applied cryptography"),
 ("Infrastructure","Docker · GitHub Actions · GitLab CI/CD · Linux · Scrum · Claude Code / Codex / Cursor"),
]
CERTS="Meta Back-End Developer Professional Certificate (2024) · Meta Full-Stack Developer Certificate (2023) · Stanford Online algorithms courses (2023) · Software Copyright Registration, NCAC China (2020)"
LANGS="Mandarin (native) · English (professional working proficiency)"

def e(s): return html.escape(s, quote=False)

# ---------- HTML ----------
css="""
@page { size: A4; margin: 15mm 16mm; }
body { font-family: "Liberation Sans", Arial, Helvetica, sans-serif; font-size: 9.8pt; line-height: 1.42; color:#1a1a1a; margin:0; }
.name { font-size: 21pt; font-weight: 700; letter-spacing: 0.5px; margin:0; }
.tag { font-size: 10.5pt; color:#333; margin: 2px 0 4px 0; }
.contact { font-size: 9pt; color:#555; margin-bottom: 10px; }
.contact a { color:#555; text-decoration:none; }
.summary { margin: 0 0 6px 0; }
h2 { font-size: 9.2pt; letter-spacing: 2px; text-transform: uppercase; color:#222; border-bottom: 1px solid #bbb; padding-bottom: 2px; margin: 14px 0 7px 0; font-weight:700; }
.entry { margin-bottom: 8px; }
.head, .meta { break-after: avoid; }
li { break-inside: avoid; }
.head { display:flex; justify-content:space-between; align-items:baseline; gap:12px; }
.title { font-weight:700; }
.title a { color:#1a1a1a; text-decoration:none; }
.date { color:#555; white-space:nowrap; font-size: 9pt; }
.meta { color:#555; font-size: 9pt; margin: 0 0 2px 0; }
ul { margin: 2px 0 0 0; padding-left: 15px; }
li { margin: 0 0 2px 0; padding-left: 2px; }
.skills p { margin: 0 0 3px 0; }
.skills b { color:#222; }
"""
h=[f"<!doctype html><html><head><meta charset='utf-8'><title>{e(NAME)} — CV</title><style>{css}</style></head><body>"]
h.append(f"<p class='name'>{e(NAME)}</p><p class='tag'>{e(TAG)}</p>")
h.append("<p class='contact'>"+" · ".join(f"<a href='{LINKS[c]}'>{e(c)}</a>" if c in LINKS else e(c) for c in CONTACT)+"</p>")
h.append(f"<p class='summary'>{e(SUMMARY)}</p>")
for heading,entries in SECTIONS:
    h.append(f"<h2>{e(heading)}</h2>")
    for en in entries:
        t=e(en['title']); 
        if en.get('link'): t=f"<a href='{en['link']}'>{t}</a>"
        h.append("<div class='entry'>")
        h.append(f"<div class='head'><span class='title'>{t}</span><span class='date'>{e(en['date'])}</span></div>")
        if en.get('meta'): h.append(f"<p class='meta'>{e(en['meta'])}</p>")
        if en.get('bullets'): h.append("<ul>"+"".join(f"<li>{e(b)}</li>" for b in en['bullets'])+"</ul>")
        h.append("</div>")
h.append("<h2>Technical skills</h2><div class='skills'>"+"".join(f"<p><b>{e(k)}:</b> {e(v)}</p>" for k,v in SKILLS)+"</div>")
h.append(f"<h2>Certifications and languages</h2><div class='skills'><p>{e(CERTS)}</p><p>{e(LANGS)}</p></div>")
h.append("</body></html>")
open(f"{S}/cv.html","w").write("\n".join(h))

# ---------- Markdown ----------
m=[f"# {NAME}","",f"**{TAG}**","",
   " · ".join(f"[{c}]({LINKS[c]})" if c in LINKS else c for c in CONTACT),"",SUMMARY,""]
for heading,entries in SECTIONS:
    m.append(f"## {heading}"); m.append("")
    for en in entries:
        t=f"[{en['title']}]({en['link']})" if en.get('link') else en['title']
        m.append(f"**{t}** · {en['date']}  ")
        if en.get('meta'): m.append(en['meta'])
        if en.get('bullets'):
            m.append(""); m.extend(f"- {b}" for b in en['bullets'])
        m.append("")
m.append("## Technical skills"); m.append("")
m.extend(f"- **{k}:** {v}" for k,v in SKILLS); m.append("")
m.append("## Certifications and languages"); m.append(""); m.append(CERTS); m.append(""); m.append(LANGS); m.append("")
open(f"{S}/applied-ai-engineer.md","w").write("\n".join(m))

out=f"{S}/Yiqun_Xu_CV_Applied_AI_Engineer.pdf"
subprocess.run(["/opt/pw-browsers/chromium-1194/chrome-linux/chrome","--headless=new","--no-sandbox","--disable-gpu","--no-pdf-header-footer",f"--print-to-pdf={out}",f"file://{S}/cv.html"],capture_output=True)
from pdfminer.high_level import extract_pages, extract_text
n=sum(1 for _ in extract_pages(out)); print("pages:",n)
if n>1: print("page2 words:", len(extract_text(out,page_numbers=[1]).split()))
