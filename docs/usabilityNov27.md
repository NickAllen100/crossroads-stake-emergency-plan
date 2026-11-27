# Crossroads Stake EOP V4 — Usability Test Report (Nov 27, 2026)

**Scope:** End-to-end usability testing of `stake_leadership_presentationV4.html` (`sw.js` `v4.14`) across **3 roles** (**Stake Leader**, **Ward Leader**, **Household Member**) in **Emergency Mode** and **Non-Emergency (Peacetime)** scenarios, including the `Stake → Ward → Member` rollout chain, Tab 4B Action Items, Ward Forms (`W-0`–`W-5`), and `Form W-5` Audit vs. Live Care Updates to Stake.

**Test Method:** Automated Headless Google Chrome CDP sweeps across Desktop (`1280×800`), Mobile (`375×812`), Emergency Mode (`Home` & `Command` sub-views), and `@media print` (`m1-std`, `ward-pack`, `stake-kit`), plus manual workflow walkthroughs of every form and handoff link.

---

## 1. Executive Summary

The core architecture (role-based tabs, single-screen Emergency Mode, cascading `#prefill=` links, 1-tap G/Y/R Member check-in, and two-way `W-5` / Stake broadcasts) is strong and has **zero horizontal overflow at 375px mobile** across all 13 tested states.

However, the walkthrough uncovered **7 blatant usability gaps**—most critically that **Stake only received Annual Audit columns from `#w5=` (dropping Live Care Update Part 0 G/Y/R counts, Pool Needs, and Urgent Unmet Needs)** and that **Ward Leaders in Emergency Mode could not reach `Form W-5` without exiting Emergency Mode**. All 7 blatant issues were fixed immediately in `stake_leadership_presentationV4.html` (`sw.js` `v4.14`) and re-verified to **0 audit findings** in Headless Chrome.

---

## 2. Blatant Issues Found & Fixed Immediately

| # | Severity | Role / Scenario | Finding | Fix Applied & Verified |
|---|---|---|---|---|
| **1** | **Critical** | **Ward → Stake (`Form W-5` Live vs. Audit)** | `Form W-5` let Wards toggle `Live Care Update` vs `Annual Audit` and enter Part 0 (`Total / Checked / G / Y / R / Unacct / Displaced / Injuries`), Part B `Need`, and `Urgent Unmet Needs`, **but `#w5=` only carried Annual Audit columns** (`SN-1–8` + `Pools 1–8 Avail`), and Stake Tab 4 had no Live Accountability Board to receive live emergency updates. | Added a dedicated **Live Emergency Ward Accountability & Unmet Needs Board** (`#stake-live-board`) with auto-summed **STAKE LIVE TOTAL** at the top of Tab 4's `#form-stake-register`. Upgraded `#w5=` encode/review/import so `Live Care Update` imports Part 0 counts, Pool Needs, Urgent Unmet Needs, timestamp, and any filled Part A/B counts, while `Annual Audit` updates only the Annual Readiness Register. On confirm, Stake/Ward leaders jump directly to the updated board. |
| **2** | **Critical** | **Ward Leader — Emergency Mode** | In Emergency Mode (`Command` view), `#ward-pane-3c` was completely hidden. Tapping `Form W-5` or `Open Printable Forms` exited Emergency Mode back to Peacetime just to send a T+60m Live `W-5` update to Stake. | Kept `#ward-pane-3c` visible in Ward Emergency Mode **showing ONLY `Form W-5`** (paper-only `W-1`, `W-2/3`, and `W-4/6` stay hidden). Updated `jumpToForm('W-5')` to stay in Emergency Mode and added a 1-tap **Jump to Live Form W-5 ↓** button on the Ward Emergency card. |
| **3** | **Major** | **Ward Forms (`W-0` → `W-5` Sync)** | Typing Ward Name on `Form W-0` (or accepting a `Ward Council` `#prefill=` link) left `Form W-5`'s Ward Name input blank, causing confusion and blank printed headers. | Auto-synced `v4_ward_name` ↔ `v4_w5_ward` whenever the other field is blank (both on typing and on `#prefill=` import). |
| **4** | **Major** | **Ward Forms (`W-1`, `W-2/3`, `W-4/6` vs. `W-5`)** | Users opening Tab `3C` saw 3 large non-editable tables (`W-1`, `W-2/3`, `W-4/6`) above fillable `Form W-5` with no clear cue explaining why `W-1–W-4/6` aren't typeable, and had to scroll past 3 sheets to reach `Form W-5`. | Added explicit **Paper-Only Binder Form — Print & Write By Hand (Never Stored Online)** tags on `W-1`, `W-2/3`, and `W-4/6`, added a **Jump to Fillable Form W-5 ↓** button at the top of `3C`, and updated `W-5` `Submitted By` placeholder to `"Role only (e.g., Ward Prep Spec)"` so leaders don't type member names. |
| **5** | **Major** | **Accessibility — Member (`2A`) & Ward (`3B`) Checklists** | Headless Chrome audit flagged all 31 checklist checkboxes (`v4_prep_kit_1..10`, `v2_chk_q1..10`, `v2_chk_s1..4`, `v4_w90_1..7`) as unlabelled inputs because sibling `<label>` tags lacked `for` / `aria-label`, and clicking checklist text did not toggle the checkbox. | Auto-assigned descriptive `aria-label` from each item's text and enabled click-to-toggle on checklist label text (while preserving clickable inline `Form M-1` / `GH` links). |
| **6** | **Minor** | **Ward Forms (`Form W-5` Mode Clarity)** | Selecting `Annual Audit (Mar 31)` left live-only `Part 0 (G/Y/R/Injuries)` looking identical to Live mode, risking unnecessary data entry during peacetime audits. | Added `.w5-annual-mode` styling that dims Part 0 and displays a clear banner: *"Annual Audit Mode selected — Part 0 (Live G/Y/R/Injuries) is skipped for March 31 Annual Audits."* |
| **7** | **Minor** | **Stake Rollout (`Tab 4B` Action #4)** | Action #4 (`Collect First 7-Ward Form W-5 Rollup`) referenced Ward delivery without a direct shortcut to share the Stake prefill link. | Added an inline `screen-only` **Share Stake Setup to Wards** button directly inside Action #4 on Tab `4B`. |

---

## 3. Scenario-by-Scenario Usability Matrix

### A. Non-Emergency (Peacetime) Scenarios

| Persona | Scenario Tested | Status | Notes |
|---|---|---|---|
| **Stake Leader** | **Tab 4B Action List & Cadence:** Check items, assign Owner & Due Date, reload persistence, print standalone Council handout (`stake-action-list`), launch `Share Stake Setup to Wards`. | **PASS** | 12 phased items, 3-tier cadence, and Action #4 Share shortcut work cleanly on desktop and 375px mobile. |
| **Stake Leader** | **Stake → Ward Rollout (`#prefill=`):** Fill `Sheet S-A` (`Stake Pres`, `Prep Rep Mobile #`, `HC Tracks`), generate `Stake → Ward` link, verify `#hash`-only transport and `W-1` exclusion. | **PASS** | Clean `#prefill=` hash; immediately stripped via `history.replaceState` after Review & Accept. |
| **Stake Leader** | **Annual Audit (`Mar 31`) Rollup:** Receive Ward Annual `Form W-5` `#w5=` link, review counts, import into Tab 4 Annual Readiness Register, verify `STAKE TOTAL` auto-sums. | **PASS** | Blank fields omitted from `#w5=` so existing Stake numbers are never clobbered with `0`. |
| **Ward Leader** | **Accept Stake Link → Fill `W-0` → Share to Ward Council & Members:** Open `Stake → Ward` link, enter Ward Name/FRS/Rally/Bishopric/Member Check-In #, verify `W-5` Ward Name auto-fills, share `Ward → Members` link. | **PASS** | Cascading `Stake → Ward → Member` flow works end-to-end with zero Stake roster leakage to Members. |
| **Ward Leader** | **Ward Forms (`3C`) & 90-Day Checklist (`3B`):** Distinguish paper-only forms (`W-1`, `W-2/3`, `W-4/6`) from fillable `W-5`, check `3B` 7-step checklist, print 5-Sheet Ward Binder. | **PASS** | Paper-only tags and **Jump to Fillable Form W-5 ↓** remove scrolling friction; all `3B` checkboxes accessible and click-to-toggle. |
| **Member** | **Tab 2A Family Preparedness Worksheet:** Water/food calculator, shutoff locations, 72-hr kit & Tier A/B checklists, JSON Export/Import, Clear This Device, Print Worksheet. | **PASS** | All `2A` checkboxes accessible; `v4_m1_household` & `v4_m1_leader_phone` sync 1:1 with `Form M-1`. |
| **Member** | **Accept Ward Setup Link & Share Family Plan:** Open `Ward → Members` `#prefill=` with pre-existing Out-of-Area Relay, choose `Fill Blank Fields Only`, share `Family → Family` link. | **PASS** | Preserves personal contacts while populating Ward/FRS/Rally/Check-In #; zero `?query` PII. |

### B. Emergency Mode Scenarios

| Persona | Scenario Tested | Status | Notes |
|---|---|---|---|
| **Member** | **Emergency Mode + Hazard Picker + 1-Tap Status to Leader:** Activate Emergency Mode, tap a hazard tile, tap `YELLOW` + note → `sms:`, tap `RED` → verify `CALL 911 FIRST` (`tel:911`) above SMS button, test blank phone inline input + Copy fallback. | **PASS** | Clean single-screen focus; RED 911 guardrail prominent; composer hidden in `@media print`. |
| **Ward Leader** | **Emergency Mode (`Home First` → `Ward Command`):** Switch to Ward Command, view `Form W-0/0B`, jump to Live `Form W-5` *without exiting Emergency Mode*, enter Part 0 G/Y/R + Pool Needs + Urgent Needs, send Live `#w5=` + SMS to Stake. | **PASS** | Paper-only `W-1`/`W-2/3`/`W-4/6` stay out of the way; Live `Form W-5` is immediately reachable in Crisis Mode. |
| **Stake Leader** | **Emergency Mode (`Stake Command`) + Live `#w5=` Import + Broadcast:** Open Ward's Live `#w5=` link, review Part 0 + Pool Needs + Urgent Needs, confirm import into `#stake-live-board`, verify `STAKE LIVE TOTAL` auto-sums, compose & copy/SMS Stake Update Broadcast to Wards. | **PASS** | Full two-way live emergency loop now works end-to-end without losing Part 0 accountability or urgent needs. |

---

## 4. Prioritized Post-Audit Recommendations & Backlog

### A. Quick Wins Worth Doing Next (Low Effort, High Operational Value)
1. **1-Tap `"Reset Live Board (Keep Annual Register)"` on Tab 4 (`#stake-live-board`):** After a tabletop drill or real event ends, a confirmed reset button lets the Stake Prep Rep clear Part 0 live counts (`Total / G / Y / R / Displaced / Injuries / Urgent`) without manually backspacing 70 cells or touching the March 31 Annual Readiness Register.
2. **Print-Preview Split Check on Stake Sheet 3 (`#form-stake-register`):** Now that Stake Sheet 3 holds both the Live Board and the Annual Register, verify in browser print preview whether keeping them on 1 tight sheet or splitting them onto `Stake Sheet 3A (Live Board)` and `Stake Sheet 3B (Annual Register)` reads best for 2:00 AM binders.
3. **Host-Aware Share Link Guard (`file://`):** If a leader opens the HTML directly from disk (`file://`) and clicks Share or Copy `#prefill=` / `#w5=` Link, display a 1-line tip (or default to the hosted GitHub Pages URL `https://nickallen100.github.io/crossroads-stake-emergency-plan/stake_leadership_presentationV4.html`) so links open cleanly on other phones.
4. **Stake / Ward Local JSON Backup & Restore:** Members already have `Export / Import Backup (.json)` on Tab `2A`, while Stake and Ward leaders (`W-0`, `W-5`, `S-A`, `S-B`, Tab `4B` Action List, and Stake Register) currently rely on `localStorage` + share links. Adding a local JSON backup/restore for Stake/Ward leaders protects against browser cache clears and simplifies calling transitions (while keeping `Form W-1` and `W-2/3` strictly excluded).

### B. Optional Post-MVP Enhancements (If Leaders Request Them)
1. **Digital `Form W-4/6` Tally Scratchpad (Zero Names):** `Form W-4/6` (Ministering District Rollup) is intentionally paper-only for offline resilience and simplicity. If Ward Clerks later want to tally Districts 1–12 (`Homes / Green / Yellow / Red / Unacct`) on a tablet and click **"Copy Ward Totals → Form W-5 Part 0"**, it would eliminate manual addition during a live sweep (ensuring zero member names are entered).
2. **Spanish / Accessibility Support (`SN-8`):** Consider adding a Spanish-language `Form M-1` Fridge Card or printable `SN-8` flyer link if helpful for wards in the stake.
3. **Minor Polish Noted in Adversarial Reviews:**
   - Only sync `#w5-stake-phone` from `W-0` during `#prefill=` when `v4_ward_stake_sms` was actually applied (so a manually typed number isn't reset).
   - Tighten `hh 1` ward matching in `resolveW5WardSlug` so non-standard strings like `"HH 12"` cannot match `Harvest Hills 1st`.

---

## 5. Recommended 10-Minute Human Verification Before Rollout

All 9 GitHub issues (`#1`–`#9`, including Epic `#5`) are labeled `review` on GitHub and live on `main` (`v4.15`). Before sharing with Stake Council or Bishops:
1. **iPhone + Android Live Test:** Open the GitHub Pages URL on one iPhone and one Android phone, add to Home Screen, enable **Airplane Mode** to verify offline PWA load, then re-enable signal and verify:
   - Member **YELLOW** & **RED** (`Call 911` guardrail + `sms:` prefill).
   - Cascading **Stake → Ward → Member** `#prefill=` link via text message.
   - Ward **Live Form W-5** → `#w5=` link → Stake **Live Accountability Board** import.
2. **Physical Print Test:** Print 1 copy each of **Fridge Card (`m1-std`)**, **15pt Senior Large Print (`m1-large`)**, **5-Sheet Ward Binder (`ward-pack`)**, **Stake Command Kit (`stake-kit`)**, and **Stake Rollout Action List (`stake-action-list`)** to verify page breaks and margins on physical paper.
3. **Header Check:** Confirmed simplified header (`Emergency Plan & Recovery Guide` with subtitle `Saratoga Springs Utah Crossroads Stake`, commit `083c90c`).

