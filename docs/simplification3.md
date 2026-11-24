# Crossroads Stake EOP — V3 Live-Test Review & V4 Clarity Blueprint (`simplification3.md`)

**Audited Baseline:** [stake_leadership_presentationV3.html](file:///Users/nickallen/code/Emergency%20plan/stake_leadership_presentationV3.html) (`2,874` lines) compared against V1 [stake_leadership_presentation.html](file:///Users/nickallen/code/Emergency%20plan/stake_leadership_presentation.html) (`8,571` lines)  
**Triggering Live-Test Feedback:**
1. **Confusing Disruption Pill Highlight (Tab 5):** On every individual hazard card (`2A–2G`), `★ 6. Emotional & Spiritual` was permanently highlighted in teal while none of the other pills were—looking like a stuck filter or UI bug—and clicking the top 11 filter chips didn't highlight pills inside the hazard cards.
2. **Comprehensive Per-Hazard Family Prep Was Lost (Tabs 2 & 5):** While V3 restored general self-reliance (Water Math, 8-Essential Kit, Pantry, 4 Drills), it dropped V1's concrete, per-hazard home preparedness details (strapping water heaters & bookcases, tethered non-sparking gas wrench, 30-ft defensible space & `≥½` gas tank in Red Flag season, winter car kit & CO alarm, 15" trampoline earth augers, 4–6 mil Hazmat sheeting + fan/damper shutoffs, zero illegal secondary-water cross-connection, sick-room kit).
3. **Ward Actions Felt Jumbled — Brevity Eliminated Clarity (Tabs 3 & 5):** Tab 3 interleaved dense crisis forms (`W-0/0B`), peacetime paragraph blocks, calendars, blank write-in grids (`W-1`–`W-5`), and a duplicate bottom onboarding drawer while omitting V1's **`Ward Roles at a Glance`** and **`First 90 Days 7-Step Launch`**. Meanwhile, semicolon-packed compression jammed 5–7 distinct actions across Household, Ward, and Stake into single 45–65-word run-on bullets.

**5-Agent Review Panel:** UX Designer · Trainer / Instructional Designer · Lead Process Engineer · Radical Simplifier · Relief Society Presidency Compassion Reviewer.

---

## Core V4 Law: Clarity Over Compression

> **Brevity is not simplicity.** Compressing 5 crisp, role-labeled bullets into one 60-word semicolon sentence saves 4 lines of HTML while destroying 2:00 AM comprehension. **V4 Guardrail:** *Cut copy-paste duplication—never whitespace, short verb-first bullets, or explicit role ownership.* Keep every bullet concise (~10–18 words) with zero multi-role semicolon walls, while keeping V3's 5-tab navigation, 1-tap `EMERGENCY RIGHT NOW` Crisis Mode, and **8-sheet Crisis Print Kit** 100% intact.

---

## 1. Fix Tab 5 Disruption Pills & Two-Way Interactive Sync (`UX`, `Trainer`, `Simplifier`, `RS`)

- **Root Cause in V3:** Hardcoding `<span class="h-pill spirit">★ 6. Emotional & Spiritual</span>` first (breaking `1–11` numerical order) in bright teal (`#ccfbf1`—identical to `.d-chip.active`) with no legend looked like a broken/stuck selection, while the top `.d-chip` filter bar ignored `2A–2G`.
- **V4 Implementation:**
  1. **Uniform Neutral Default & Strict Numerical Order (`1`–`11`):** Remove `.spirit` and the stray `★` from all hazard cards and from top chip `#6`. Prefix each card's strip plainly: **`Impacted Disruptions (X of 11):`** with uniform light-slate pills and a subtle 4-cluster color dot (matching the top 11-category table).
  2. **Two-Way Interactive Sync:** Clicking any top `.d-chip` (or clicking any `.h-pill` inside a hazard card) highlights the matching row in the top table, **dynamically highlights every matching pill across all 7 hazard cards (`2A–2G`)** in solid navy, gently dims non-impacted hazard cards (`opacity: 0.45`), and shows a crisp reset bar (*"Filtering by 10. Sewer & Water — impacts 4 of 7 local hazards · [Reset]"*).
  3. **Honor Emotional & Spiritual Care in Action:** Express `#6 Emotional & Spiritual` through warm, specific EQ/RS ministering bullets inside every hazard's Ward column rather than a mysterious icon.

---

## 2. Restore Comprehensive Per-Hazard Family Preparedness (`Trainer`, `UX`, `RS`, `Simplifier`)

Restore 100% of V1's concrete, Saratoga Springs–specific household prep across all 7 hazards—surfaced clearly in **two places**: (a) a compact **"Prepare Your Home for Our 7 Local Hazards"** card on **Tab 2** (`data-mode="prep"`, tagged with `Homeowner / Renter / Senior` clarity so renters and seniors effortlessly skip inapplicable items) and (b) the dedicated `Before → Household / Family` bullet column inside every Tab 5 hazard playbook:

| Hazard | Comprehensive V1 Household Prep Details Restored in V4 |
|---|---|
| **2A. Earthquake** | Strap water heater & tall bookcases/TVs to wall studs; tether non-sparking gas wrench at meter *(homeowners)*; label breaker panel & water-heater cold inlet; bedside shoes/flashlight; practice Drop-Cover-Hold (April ShakeOut) & outside rally spot. |
| **2B. Wildfire** | Clear tall dry grass, weeds, firewood & gutters 30 ft from decks/fences; keep gas tanks **≥½ full** during Red Flag season; stage N95s, waterproof IDs/photos & pet carriers/leashes/meds by exit; pick north (SR-73) & out-of-area rally spots; seniors/non-night drivers plan Early-Evac on Watch. |
| **2C. Winter Freeze** | Caulk drafts, disconnect outdoor hoses & insulate exposed spigots; test battery CO alarm; stage 1 warm-room kit (indoor tent, cold-rated bags/wool blankets, CO-safe heat only); stock winter car kit (ice scraper, shovel, traction sand, blanket); protect insulin from freezing. |
| **2D. Windstorm** | Install **15" steel earth augers** on trampolines; clear apartment balconies & secure sheds/patio gear; prune dead limbs near roofs/power drops; stage heavy tarp & duct tape. |
| **2E. Hazmat Plume** | Stage 5-min quick-seal kit (**4–6 mil plastic sheeting, duct/painter's tape, scissors**) in a closet; show household thermostat fan, bath-fan & fireplace damper shutoffs; enable WEA alerts; save Poison Control (`1-800-222-1222`); basement renters pre-arrange an upstairs room; know Riverview Elem seal-in-place rule. |
| **2F. Water Outage** | Verify **zero illegal cross-connection** with untreated Utah Lake secondary irrigation water; label outdoor spigots *Non-Potable*; store hollow-fiber/gravity filter + unscented bleach alongside 3-min boil rule; know water-heater cold-inlet isolation; easy-lift 1–2.5 gal jugs + `\$10` siphon for seniors. |
| **2G. Disease** | Stock Home Sick-Room Kit (adult & pediatric acetaminophen/ibuprofen, oral electrolytes, broth/crackers, thermometer, pulse oximeter, masks, soap/wipes); plan sick bedroom/bath ventilation; build modest cash buffer; solo/YSA pick daily text "sick-day buddy." |

---

## 3. Un-Jumble Tab 3 (Ward Ministering & Forms) & Tab 5 (`2A–2G`) (`UX`, `Process`, `Trainer`, `RS`, `Simplifier`)

### 3.1 Tab 3 Clean 3-Sub-Tab Architecture *(Auto-Locks to `3A` in Crisis Mode; Print Profile `ward-pack` Still Prints All 5 Clean Offline Sheets)*
Eliminate interleaving between forms, ministering blocks, calendars, and a redundant bottom onboarding drawer:
- **Sub-Tab `3A` — Ward Roles & Active Response (`0–72h`, Crisis-Ready):**
  1. **`Ward Roles at a Glance`** (restoring V1's scannable ownership grid across all 6 Ward lanes: **Bishopric `GH 22.6.1`**, **Elders Quorum `GH 8.2.2/22.6.2`**, **Ward Relief Society `GH 9.2.2/22.6.2/9.3.3`**, **Ward Clerk**, **Ward Welfare Specialist `GH 22.6.4`**, and **Ward Youth Council `GH 22.8`**).
  2. **Linear Step-by-Step Crisis Sequence (`0–60m → 1–72h → T+72h → T+14d`)** with crisp verb-first bullets.
  3. **Ward Sheet 1 (`Form W-0` & `Form W-0B`)** cleanly formatted with generous spacing (including *"Knock to love, not just to count"* and offline Storehouse/fast-offering rules).
- **Sub-Tab `3B` — Year-Round Ministering, 90-Day Launch & Prep (`data-mode="prep"`):**
  1. **EQ & RS Ministering Across All 4 Horizons** — rewritten from dense paragraphs into crisp, role-labeled bullets (`Bishopric:`, `Elders Quorum:`, `Relief Society:`, `Clerk / Specialist:`) + V1's dignified `GH 21.3` conversation starter.
  2. **First 90 Days: 7-Step Ward Launch Checklist** (restored from V1, interactive `localStorage` checkboxes!).
  3. **Unified Year-Round 4-Quarter Rhythm & 4 Grab-and-Go Activity Nights** (`GH 8.2.1.2 / 9.2.1.2 / 9.3.3`).
  4. **10-Min New Ward Leader Onboarding + Mandatory `GH 22.4.5` Calling-Release Shred Gate** & **45-Min 5th-Sunday Teaching Flow** (deleting the duplicate bottom drawer completely).
- **Sub-Tab `3C` — Printable Offline Ward Binder (`Forms W-1`, `W-2/3`, `W-4/6`, `W-5`):**
  - Isolates all 4 blank write-in paper templates consecutively so empty grids never break up the Ward action narrative on screen (while `Print 5-Sheet Ward Binder` seamlessly prints `W-0/0B` + `W-1`–`W-5` across 5 crisp offline sheets!).

### 3.2 Tab 5 (`2A–2G`) — 4 Color-Banded Horizons × 3 Separated Columns
- Replace every semicolon-chained bullet inside `2A–2G` with **4 clean horizon bands** (`Before / Prep` · `0–72 Hours` · `1–2 Weeks` · `2+ Months`), each rendered as a **3-column grid (`Household / Family` | `Ward: Bishop, EQ & RS` | `Stake Support`)** with 2–4 short, verb-first bullets per lane.
- Wire a synchronized **Horizon Filter Pill Bar** (`All 4 Stages` | `Before` | `0–72h` | `1–2 Wks` | `2+ Mo`) so councils can view all 4 stages or isolate any single time horizon across both the Universal Playbook and all 7 hazards simultaneously!

---

## 4. Target V4 Metrics
- **Target Size:** `~3,400–3,700` HTML lines (still **~57% leaner than V1's `8,571` lines** with zero copy-paste boilerplate).
- **Crisis Mode & Print Profiles:** 100% preserved (`M-1 Std`, `M-1 15pt Large Print`, `Ward 5-Sheet Binder`, `Stake 2-Sheet Kit`, `Full Archive`).
- **Validation Gates:** `0` HTML tag errors, `0` JS syntax errors, `0` stray `★ 6` highlights, `100%` V1 per-hazard family prep restored, and two-way disruption + horizon filter sync verified.
