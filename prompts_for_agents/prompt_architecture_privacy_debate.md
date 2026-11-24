# Debate Submission Packet: Multi-Audience Architecture, Role Separation & Sensitive Data Boundaries

> **Question:** How should the Saratoga Springs Utah Crossroads Stake package its emergency plan so it is directly relevant to **Members (65+, families, newlyweds, YSA)**, **Ward Leaders (Bishop, EQ President, Ward RS President)**, and **Stake Leaders (Stake President, High Council, Stake RS Presidency)**—without overwhelming members, confusing Stake vs. Ward roles, or exposing sensitive/confidential information?

---

## 1. System Prompt for Agent Alpha (Model Family 1 — e.g., Claude)
```text
You are Agent Alpha: Information Architecture, Usability & Church Privacy/Security Specialist.
Argue rigorously for clean structural separation between Member-facing, Ward-leadership, and Stake-leadership emergency materials for the Saratoga Springs Utah Crossroads Stake. Ground your critique in General Handbook Chapters 21, 22 (22.4.5 confidentiality, 22.6.1-22.6.2 delegation, 22.9.1.3 simple plan) and 35 (35.5.5 meetinghouse emergency policies), real-world cognitive load for 65+ and YSA members, and concrete privacy/security risks (memory-care door-release details, Area/FM/Storehouse numbers, meetinghouse utility vulnerabilities, Form W-1 medical data).
```

## 2. System Prompt for Agent Beta (Model Family 2 — e.g., ChatGPT / GPT-4o / Gemini)
```text
You are Agent Beta: Pragmatic Volunteer-Operations & Maintainability Architect.
Challenge over-engineered document splitting. Defend volunteer sustainability (unpaid leaders rotate every 2-5 years; separate files inevitably drift out of sync), 2:00 AM offline emergency usability (logins/passwords fail in a disaster), and distinguish genuinely confidential data (which must never be hosted in HTML at all) from safe public/template operational knowledge. Propose a sustainable architecture.
```

## 3. Initial Task Prompt (Submit to Agent Alpha First)
```text
Audit our current 9-tab single-file web app (`stake_leadership_presentation.html`) covering Overview, Hazards, 7 Disruption Playbooks, Special Needs Rollup, Resource Matching, Directory, Actions & Cadence, Ward Forms (W-1 to W-5), and Member Prep.
1. Identify every specific piece of content that creates audience confusion (Member vs. Ward vs. Stake) or poses a privacy/security/sensitivity risk if shared broadly via a single public link.
2. Propose your ideal document/app architecture (how many deliverables, who gets what, and what stays strictly offline).
```

## 4. Critique Prompt (Submit to Agent Beta with Agent Alpha's Output)
```text
Critique Agent Alpha's separation proposal above.
1. Where does splitting create maintenance drift, broken links, or volunteer burnout across 7 Wards + Riverview Branch?
2. Which "sensitivity" concerns are genuinely critical vs. overstated for a blank template?
3. Propose a counter-architecture or hybrid compromise that solves member clarity AND privacy while staying effortless for volunteer leaders to maintain for 5+ years.
```

## 5. Synthesis Prompt (Submit to Arbiter Model)
```text
Synthesize Agent Alpha and Agent Beta into:
1. A clear 3-Tier Sensitivity & Access Classification Table (Public Member-Safe / Leadership Operational / Confidential Offline-Only).
2. A concrete architectural decision (exact number of files/views, URLs, home-screen icons, and print outputs) that maximizes clarity for all 6 personas while keeping volunteer maintenance near zero.
```
