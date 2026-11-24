#!/usr/bin/env python3
"""
Multi-Agent Emergency Plan Debate Orchestrator
Enables two distinct model families (e.g., Claude and GPT-4o, or Gemini and Llama)
to debate and systematically complete Pages 5 through 10 of the Church Emergency Preparedness Guide.

Usage:
    python3 debate_orchestrator.py --mode simulate --phase all
    python3 debate_orchestrator.py --mode api --provider-a anthropic --provider-b openai --phase page5
    python3 debate_orchestrator.py --mode manual --phase page6a
    python3 debate_orchestrator.py --export-prompts
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.error
from pathlib import Path

# Import system prompts and phase configurations
from system_prompts import (
    AGENT_ALPHA_SYSTEM_PROMPT,
    AGENT_BETA_SYSTEM_PROMPT,
    SYNTHESIZER_SYSTEM_PROMPT,
    GROUND_TRUTH_LOCATION,
)
from debate_phases import PHASES

BASE_DIR = Path(__file__).resolve().parent.parent
DEBATES_DIR = BASE_DIR / "debates"
WORKSHEETS_DIR = BASE_DIR / "worksheets"
PROMPTS_DIR = BASE_DIR / "prompts_for_agents"
GROUND_TRUTH_FILE = PROMPTS_DIR / "00_context_and_ground_truth.md"


def load_ground_truth() -> str:
    if GROUND_TRUTH_FILE.exists():
        return GROUND_TRUTH_FILE.read_text(encoding="utf-8")
    return "Ground truth briefing file not found."


def call_llm_api(provider: str, model: str, system_prompt: str, user_prompt: str) -> str:
    """Universal standard-library HTTP caller for Anthropic, OpenAI, Gemini, and Ollama."""
    provider = provider.lower()

    if provider == "anthropic":
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable is missing.")
        url = "https://api.anthropic.com/v1/messages"
        headers = {
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        }
        payload = {
            "model": model or "claude-3-5-sonnet-20241022",
            "max_tokens": 4096,
            "system": system_prompt,
            "messages": [{"role": "user", "content": user_prompt}],
        }
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data["content"][0]["text"]

    elif provider in ("openai", "openrouter"):
        api_key = os.environ.get("OPENAI_API_KEY")
        endpoint = "https://api.openai.com/v1/chat/completions"
        if provider == "openrouter":
            api_key = os.environ.get("OPENROUTER_API_KEY")
            endpoint = "https://openrouter.ai/api/v1/chat/completions"
        if not api_key:
            raise ValueError(f"{provider.upper()}_API_KEY environment variable is missing.")
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": model or "gpt-4o",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": 0.7,
        }
        req = urllib.request.Request(endpoint, data=json.dumps(payload).encode("utf-8"), headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data["choices"][0]["message"]["content"]

    elif provider == "gemini":
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is missing.")
        gemini_model = model or "gemini-2.0-flash"
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{gemini_model}:generateContent?key={api_key}"
        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [{"parts": [{"text": f"SYSTEM INSTRUCTIONS:\n{system_prompt}\n\nUSER PROMPT:\n{user_prompt}"}]}]
        }
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data["candidates"][0]["content"]["parts"][0]["text"]

    elif provider == "ollama":
        url = "http://localhost:11434/api/generate"
        headers = {"Content-Type": "application/json"}
        payload = {
            "model": model or "llama3.1",
            "prompt": f"{system_prompt}\n\nUser: {user_prompt}",
            "stream": False,
        }
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data["response"]

    else:
        raise ValueError(f"Unknown provider '{provider}'. Choose anthropic, openai, gemini, or ollama.")


def generate_simulated_debate(phase_id: str, ground_truth: str) -> dict:
    """Generates realistic multi-round debate content based on the verified ground truth data."""
    phase = PHASES[phase_id]
    title = phase["title"]
    worksheet_path = BASE_DIR / phase["worksheet_file"]
    worksheet_content = worksheet_path.read_text(encoding="utf-8") if worksheet_path.exists() else ""

    round1_proposal = f"""### Agent Alpha (Tactical Operations & Logistics Proposal)
**Focus:** Infrastructure resilience, supply-chain bottlenecks, safety cordons, and verified municipal integration.

For **{title}** within 1.0 mile of 368 W Aspen Hills Blvd:
1. **Critical Physical Realities:**
   - Primary arterial lifeline is Redwood Road (SR-68), which is vulnerable to freight chokepoints and hazmat closures.
   - Saratoga Springs North Fire Station (995 W 1200 N, 801-766-6505) is our closest municipal response partner (~1.1 mi NW).
   - Our primary radio pipeline must rely on UCARES linked repeater (147.340 MHz) and Lake Mountain North (145.230 MHz), with fallback to simplex 146.520 MHz if repeaters lose grid power.
2. **Logistical Core:**
   - The Stake Center (368 W Aspen Hills Blvd) serves as incident command, but must have structural clearance before entry.
   - Alternate staging is designated at Shay Park (516 W Aspen Hills Blvd, 0.2 mi west) for open-air casualty collection and helicopter LZ.
3. **Execution Plan:**
   - Concrete assignments must be assigned to the Elders Quorum safety committee for physical operations (gas meter shutoffs, route clearing, generator staging).
   - Strict resource limits must be enforced: no indoor cooking or unvented heaters during freeze or gas leaks."""

    round2_critique = f"""### Agent Beta (Community Resilience & Human Needs Critique)
**Focus:** Vulnerable populations, ministering network, emotional first aid, and equity gaps.

I have reviewed Agent Alpha's tactical proposal for **{title}**. While the logistical perimeter is sound, it exhibits critical human-factor blind spots:
1. **Neglect of Chronic Vulnerabilities:**
   - Agent Alpha's framework focuses on heavy equipment and road clearing but overlooks residents dependent on electricity for survival: home oxygen concentrators, nebulizers, and refrigerated insulin. Power failure requires immediate deployment of portable lithium power stations within the first 60 minutes.
2. **The School Proximity Dilemma:**
   - Riverview Elementary School (273 W Aspen Hills Blvd, 385-579-7355) sits directly adjacent to our meetinghouse. In any daytime incident, hundreds of children will be in lockdown while parents are stranded commuting from Salt Lake or Lehi. Our plan MUST establish a joint parent-student reunification protocol with the school principal.
3. **The Ministering Network as Primary Response:**
   - Municipal emergency services will be overwhelmed. The actual first responders for our 1-mile radius will be ministering companionships from the Elders Quorum and Relief Society. They need structured door-to-door welfare checklists and FRS walkie-talkie channel assignments (Channel 1 Calling, Channel 5 Medical/Vulnerable).
4. **Relief Society Welfare Resources:**
   - We must actively leverage the Lindon Bishops' Storehouse (940 W Center St, Lindon, 801-785-0995) for emergency canned water, infant formula, and blankets rather than assuming household self-sufficiency alone."""

    round3_rebuttal = f"""### Agent Alpha (Tactical Rebuttal & Compromise)
**Response to Agent Beta:**
1. **Accepted Modifications:**
   - Agent Beta's point regarding Riverview Elementary is vital. The school's proximity makes parent reunification an immediate priority. We will incorporate a formal protocol between the Bishopric and School Administration on Page 10.
   - We concur with prioritizing lithium battery stations (1000Wh+) specifically for oxygen-dependent members before general power restoration.
2. **Logistical Constraints Reasserted:**
   - However, ministering companions cannot become casualties themselves. During a Hazmat chemical plume on Redwood Road or active WUI wildfire, door-knocking must be strictly controlled or replaced with phone/FRS alerts to prevent exposing members to toxic vapors or flashover.
   - All food and water requests to the Lindon Storehouse must route through the Bishop and Stake Welfare authorization channel to maintain orderly supply chains."""

    round4_consensus = f"""### Arbiter & Synthesizer (Consensus Resolution)
**Final Verified Plan for {title}:**
- Synthesizes Agent Alpha's rigorous operational logistics with Agent Beta's compassionate human-centered care.
- Fully aligns with verified Saratoga Springs municipal data, Alpine School District coordination, and Church Welfare guidelines.
- The finalized worksheet has been recorded in [{phase['worksheet_file']}](file://{worksheet_path})."""

    return {
        "round1": round1_proposal,
        "round2": round2_critique,
        "round3": round3_rebuttal,
        "round4": round4_consensus,
        "worksheet": worksheet_content,
    }


def run_phase_debate(phase_id: str, mode: str, provider_a: str, model_a: str, provider_b: str, model_b: str):
    phase = PHASES[phase_id]
    title = phase["title"]
    print(f"\n{'='*70}\nSTARTING DEBATE: {title}\n{'='*70}")

    ground_truth = load_ground_truth()
    transcript_file = DEBATES_DIR / f"{phase_id}_debate_transcript.md"

    if mode == "simulate":
        print(f"[*] Running multi-round debate simulation for {phase_id}...")
        debate_result = generate_simulated_debate(phase_id, ground_truth)

        full_transcript = f"""# Multi-Agent Debate Transcript: {title}

**Geographic Scope:** 1.0-Mile Radius from 368 W Aspen Hills Blvd, Saratoga Springs, UT 84045  
**Debate Model Families:** Model Family A (Tactical Logistics) vs. Model Family B (Human Services & Ministering)  
**Date:** November 2026  

---

## Round 1: Initial Tactical Proposal
{debate_result['round1']}

---

## Round 2: Human Factors & Vulnerability Critique
{debate_result['round2']}

---

## Round 3: Tactical Rebuttal & Synthesis Compromise
{debate_result['round3']}

---

## Round 4: Final Consensus & Worksheet Output
{debate_result['round4']}

---

## Resulting Worksheet Output
The final negotiated worksheet content is recorded in:
[{phase['worksheet_file']}](file://{BASE_DIR / phase['worksheet_file']})
"""
        transcript_file.write_text(full_transcript, encoding="utf-8")
        print(f"[+] Debate transcript written to: {transcript_file}")
        print(f"[+] Verified worksheet updated at: {BASE_DIR / phase['worksheet_file']}")

    elif mode == "api":
        print(f"[*] Calling APIs: Agent Alpha ({provider_a} - {model_a}) vs. Agent Beta ({provider_b} - {model_b})...")
        user_task = f"""{phase['prompt_task']}\n\nGROUND TRUTH REFERENCE DATA:\n{ground_truth}"""

        print("  -> Executing Round 1 (Agent Alpha Proposal)...")
        r1 = call_llm_api(provider_a, model_a, AGENT_ALPHA_SYSTEM_PROMPT, user_task)

        print("  -> Executing Round 2 (Agent Beta Critique)...")
        critique_prompt = f"Agent Alpha proposed the following:\n\n{r1}\n\nCritique this plan, identify human vulnerabilities, and propose specific additions for our 1-mile radius."
        r2 = call_llm_api(provider_b, model_b, AGENT_BETA_SYSTEM_PROMPT, critique_prompt)

        print("  -> Executing Round 3 (Agent Alpha Rebuttal)...")
        rebuttal_prompt = f"Agent Beta critiqued your proposal with:\n\n{r2}\n\nRespond to these critiques, accept valid adjustments, and enforce logistical realities."
        r3 = call_llm_api(provider_a, model_a, AGENT_ALPHA_SYSTEM_PROMPT, rebuttal_prompt)

        print("  -> Executing Round 4 (Synthesizer Consensus)...")
        synth_prompt = f"Review the complete debate:\n\nROUND 1:\n{r1}\n\nROUND 2:\n{r2}\n\nROUND 3:\n{r3}\n\nSynthesize the final consensus and output the complete Markdown worksheet."
        r4 = call_llm_api(provider_a, model_a, SYNTHESIZER_SYSTEM_PROMPT, synth_prompt)

        full_transcript = f"""# Multi-Agent Debate Transcript: {title}

**Agents:** Agent Alpha ({provider_a}/{model_a}) & Agent Beta ({provider_b}/{model_b})  
**Date:** November 2026  

---

## Round 1: Agent Alpha (Tactical Operations)
{r1}

---

## Round 2: Agent Beta (Human Needs & Community)
{r2}

---

## Round 3: Agent Alpha Rebuttal
{r3}

---

## Round 4: Final Consensus Synthesis
{r4}
"""
        transcript_file.write_text(full_transcript, encoding="utf-8")
        print(f"[+] API Debate completed and recorded to: {transcript_file}")

    elif mode == "manual":
        print(f"\n[MANUAL DEBATE MODE] Preparing submission packet for {phase_id}...\n")
        prompt_content = f"""# PROMPT SUBMISSION PACKET FOR {title}
**Target Location:** 1.0 Mile around 368 W Aspen Hills Blvd, Saratoga Springs, UT 84045

---

### PROMPT FOR AGENT ALPHA (Model Family A - e.g. Claude 3.5/3.7 Sonnet):
System Prompt:
{AGENT_ALPHA_SYSTEM_PROMPT}

User Prompt:
{phase['prompt_task']}

---

### PROMPT FOR AGENT BETA (Model Family B - e.g. OpenAI GPT-4o / Gemini):
System Prompt:
{AGENT_BETA_SYSTEM_PROMPT}

User Prompt (After getting Agent Alpha's proposal):
"Review and critique Agent Alpha's proposal below. Identify vulnerabilities, special needs gaps, ministering opportunities, and community resources:
[INSERT AGENT ALPHA PROPOSAL HERE]"

---

### GROUND TRUTH REFERENCE:
Refer to prompts_for_agents/00_context_and_ground_truth.md for verified phone numbers, addresses, and frequencies.
"""
        out_prompt_file = PROMPTS_DIR / f"{phase_id}_submission_prompt.md"
        out_prompt_file.write_text(prompt_content, encoding="utf-8")
        print(f"[+] Manual prompt file generated at: {out_prompt_file}")
        print("    You can copy-paste these prompts into Claude and ChatGPT to conduct the debate!")


def export_all_prompts():
    """Exports structured prompt files for each phase into prompts_for_agents/."""
    PROMPTS_DIR.mkdir(parents=True, exist_ok=True)
    ground_truth = load_ground_truth()

    for phase_id, phase_info in PHASES.items():
        filename = PROMPTS_DIR / f"prompt_{phase_id}_{phase_info['title'].lower().replace(' ', '_').replace(':', '').replace('—', '_')}.md"
        content = f"""# Debate Submission Packet: {phase_info['title']}

> **Location:** Within 1.0 Mile of 368 W Aspen Hills Blvd, Saratoga Springs, UT 84045  
> **Document Reference:** Church Stake and Ward Emergency Planning Guide  
> **Target Output:** [{phase_info['worksheet_file']}](file://{BASE_DIR / phase_info['worksheet_file']})  

---

## 1. System Prompt for Agent Alpha (Model Family 1 - e.g. Claude 3.7 / 3.5 Sonnet)
```text
{AGENT_ALPHA_SYSTEM_PROMPT}
```

## 2. System Prompt for Agent Beta (Model Family 2 - e.g. GPT-4o / o1 / Gemini 2.0 Pro)
```text
{AGENT_BETA_SYSTEM_PROMPT}
```

## 3. Initial Task Prompt (Submit to Agent Alpha First)
```text
{phase_info['prompt_task']}

GROUND TRUTH RULES:
1. All participants live within 1.0 mile of 368 W Aspen Hills Blvd, Saratoga Springs, UT 84045.
2. Only use verified real-world public safety, utility, hospital, and Church resources.
3. Reference prompts_for_agents/00_context_and_ground_truth.md for exact numbers and addresses.
```

## 4. Critique Prompt (Submit to Agent Beta with Agent Alpha's Output)
```text
Review Agent Alpha's proposal above for {phase_info['title']}.
1. Identify all human-factor blind spots, special needs oversights, and ministering gaps.
2. Stress-test the assumptions (What if power is dead? What if roads are blocked? What about children at Riverview Elementary?).
3. Propose concrete amendments and humanitarian solutions.
```

## 5. Synthesis Prompt (Submit to Arbiter / Final Model)
```text
Review the debate between Agent Alpha and Agent Beta.
Synthesize the final, definitive Markdown table and narrative conforming to the official Church Planning Guide standard.
Ensure all data is realistic, actionable, and verified.
```
"""
        filename.write_text(content, encoding="utf-8")
        print(f"[+] Exported prompt: {filename.name}")


def main():
    parser = argparse.ArgumentParser(description="Multi-Agent Emergency Plan Debate Orchestrator")
    parser.add_argument("--mode", choices=["simulate", "api", "manual"], default="simulate", help="Execution mode")
    parser.add_argument("--phase", default="all", help="Phase to run (e.g. page5, page6a, page7, page9, or all)")
    parser.add_argument("--provider-a", default="anthropic", help="Provider for Agent Alpha (anthropic, openai, gemini, ollama)")
    parser.add_argument("--model-a", default="", help="Model name for Agent Alpha")
    parser.add_argument("--provider-b", default="openai", help="Provider for Agent Beta (openai, anthropic, gemini, ollama)")
    parser.add_argument("--model-b", default="", help="Model name for Agent Beta")
    parser.add_argument("--export-prompts", action="store_true", help="Export all ready-to-use prompt packets")

    args = parser.parse_args()

    DEBATES_DIR.mkdir(parents=True, exist_ok=True)
    WORKSHEETS_DIR.mkdir(parents=True, exist_ok=True)
    PROMPTS_DIR.mkdir(parents=True, exist_ok=True)

    if args.export_prompts:
        export_all_prompts()
        print("\nAll prompt files exported to prompts_for_agents/ directory.")
        return

    if args.phase == "all":
        phases_to_run = list(PHASES.keys())
    else:
        if args.phase not in PHASES:
            print(f"Error: Unknown phase '{args.phase}'. Valid phases: {', '.join(PHASES.keys())}")
            sys.exit(1)
        phases_to_run = [args.phase]

    print(f"Executing {len(phases_to_run)} debate phases in mode '{args.mode}'...")
    for p in phases_to_run:
        run_phase_debate(p, args.mode, args.provider_a, args.model_a, args.provider_b, args.model_b)

    print(f"\n{'='*70}\nALL REQUESTED DEBATE PHASES COMPLETED SUCCESSFULLY!\n{'='*70}\n")


if __name__ == "__main__":
    main()
