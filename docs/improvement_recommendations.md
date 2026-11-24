# Usability Review & Improvement Recommendations
**Document Audited:** `stake_leadership_presentation.html` (Saratoga Springs Utah Crossroads Stake Emergency Operations Plan & Ward Toolkit)  
**Review Date:** November 2026  
**Review Lenses:**
1. **Immediate Visual & Technical Bugs** (Deep Dive links, text alignment, layout glitches)
2. **Member Personas:**
   - **Persona A — 65-Year-Old Member / Senior Household ("Sister Margaret")**
   - **Persona B — Newlywed Couple / Single Adult ("Ethan & Maya" / "Jordan", YSA / Renter)**
3. **Ecclesiastical Leadership Personas (Evaluated Against *General Handbook* Chapters 21, 22 & 35):**
   - **Persona C — Stake President**
   - **Persona D — Bishop**
   - **Persona E — Elders Quorum (EQ) President**
   - **Persona F — Ward Relief Society (RS) President**

---

## 1. Visual & Functional Oddities Found (Fixed in Current Pass)

During the code and layout audit of `stake_leadership_presentation.html`, we identified the exact root causes behind the reported deep-dive and word-alignment oddities, plus several related polish issues. **All items in this section have been fixed in `stake_leadership_presentation.html`:**

| # | Issue Observed | Root Cause in Code | Status |
|---|---|---|---|
| 1 | **Deep Dive links & Action column broken/misaligned** | `.screen-only { display: initial; }` set `display: inline` on `<th class="screen-only">`, `<td class="screen-only">`, `<p class="screen-only">`, and `<button class="btn-deep-link screen-only">`. In CSS, `initial` for `display` is always `inline`, which broke table cells in Tab 2's Comparison Grid and overrode `inline-flex` on the Tab 8 Deep Link button. | **Fixed** — removed `.screen-only { display: initial; }` so elements preserve native `table-cell` / `block` / `inline-flex` layout on screen while still hiding cleanly in `@media print`. |
| 2 | **Checklist words split into misaligned columns** (Tab 8 Launch Checklist & Tab 9 Step 8 Checklist) | `.checklist-list li` used `display: flex; gap: 8px;`. Because each `<li>` contained `<span class="chk-box">[ ]</span>` plus bare text nodes and inline `<strong>` tags, CSS Flexbox treated every `<strong>` tag and text run as a separate side-by-side column! | **Fixed** — switched `.checklist-list li` to `display: block; position: relative; padding-left: 28px;` with an absolutely positioned `.chk-box` hanging indent so inline bold/italic text flows naturally. |
| 3 | **Deep Dive jump clipped the disaster heading behind the sticky subtab bar** | `openDisaster()` called `el.scrollIntoView({ block: 'start' })`, scrolling `<h3>Worksheet 2X...</h3>` underneath `.disaster-subtabs` (`position: sticky; top: 0`). Also, clicking a different subtab while scrolled halfway down did not scroll back to the top of the panel, and off-screen mobile subtabs didn't center the active button. | **Fixed** — added `scroll-margin-top: 66px`, auto-centered the active subtab button on mobile, scrolled to the panel top on subtab change, and added browser Back-button (`history.pushState` / `popstate`) + a **"← Back to Hazards Matrix"** link when arriving from a Deep Dive click. |
| 4 | **Raw Markdown asterisks (`*...*`) visible in HTML** | Lines 3520, 4051, 4084, 4116, 4147, 4179, and 4353–4356 contained literal `*italic text*` instead of `<em>...</em>`. | **Fixed** — converted all literal asterisks to semantic `<em>` tags. |
| 5 | **Top navigation bar overflow on tablets / mid-size laptops (769–1180px)** | `.tabs` only enabled horizontal scroll below `768px`, causing the 3 `.nav-cluster` blocks (9 tabs) to spill outside the card on narrow desktop/iPad viewports. | **Fixed** — enabled graceful horizontal scroll / wrap handling across tablet widths. |
| 6 | **Uneven CTA buttons & colliding phone headers** | The 3 Tier cards on Tab 1 had buttons at different vertical heights; `.contact-card h4` had `justify-content: space-between` without `flex-wrap` or `gap`, crowding long facility names and phone numbers; Step 7 & Step 8 forms had hardcoded underscore strings (`______`) that overflowed on mobile. | **Fixed** — flex-aligned Tier card CTAs to the bottom, added wrap/gap to `.contact-card h4`, and replaced overflowing underscore strings with responsive `.fill-line-lg` rules. |

---

## 2. Persona A Review: 65-Year-Old Member ("Sister Margaret")

**Profile:** Age 65, retired or semi-retired, lives with spouse (or recently widowed), uses an iPhone with iOS Larger Text enabled and an iPad at home, prefers printed binders for emergencies, uses a CPAP or keeps daily prescriptions, and may feel intimidated by dense leadership tools or technical acronyms.

### Key Pain Points Discovered

1. **Phone Numbers Are Not Tappable (`tel:` links = 0)**
   - **Problem:** Across Tab 6 (Directory), Tab 3 (Disruptions), and Tab 9 (Member Prep), every emergency number—Intermountain Saratoga Springs ER `(801) 763-3500`, Fire `(801) 766-6505`, Public Works `(801) 404-2468`, Enbridge Gas `1-800-767-1689`, Rocky Mountain Power `1-877-508-5088`, Poison Control `1-800-222-1222`—is plain text. During a stressful 2:00 AM power outage or gas smell, a 65-year-old wearing reading glasses shouldn't have to memorize a 10-digit number and switch apps to dial it.
   - **Recommendation:** Wrap every phone number in `<a href="tel:+18017633500" class="phone-link">(801) 763-3500</a>` with a high-contrast tap target and phone icon on mobile.

2. **Small Fonts, Low-Contrast Muted Text, and Dense Mobile Tables**
   - **Problem:** Many body paragraphs, checklist items, and table cells use `0.78rem–0.86rem` (~12.5–13.8px) and `--text-muted: #64748b` on `#f8fafc` (borderline WCAG AA contrast for older eyes). On an iPhone, the 7-column and 12-column tables require sideways scrolling with no visual cue ("Swipe → to see more").
   - **Recommendation:**
     - Raise base readable copy in Member-facing sections (Tab 1, Tab 6, Tab 9) to at least `16px` (`1rem`) and darken `--text-muted` to `#475569`.
     - Add a one-tap **"A+ Larger Text"** toggle in the header (persisted in `localStorage`) so seniors can immediately bump readability to 115–120% without struggling with pinch-zoom.
     - Increase touch targets on mobile tabs, subtabs, and Deep Dive buttons to at least `44px` height (Apple HIG minimum).

3. **Cognitive Overload: 9 Tabs × 7 Subtabs + Heavy Jargon**
   - **Problem:** Opening the app immediately presents 9 tabs across 3 technical clusters (`The Plan`, `Stake Registers`, `Ward Toolkit`) and terminology that is opaque to a regular member: `WUI Wildfire`, `SN-1` through `SN-8`, `Form W-5`, `UCARES`, `PL 100.0 Hz`, `PEX/SharkBite`, `MERV-13`, `FM Group`, `EOC`, `LZ`, `PM2.5`.
   - **Recommendation:**
     - Add a plain-English **"Start Here — Who Are You?"** 2-card entry banner at the top of Tab 1 (or a simple mode switch): **"I'm a Member / Family (Take Me to Home Prep & Emergency Numbers)"** vs. **"I'm a Ward / Stake Leader (Forms, Registers & Playbooks)"**.
     - Add a collapsible **"Plain-English Glossary"** (or inline parentheticals on first mention: e.g., *"WUI (Foothill/Brush) Wildfire"*, *"Shay Park Helicopter Landing Zone"*).
     - Add an **"Emergency Right Now" Quick Strip** (or floating quick-access drawer) with the top 4 actions/numbers: 911, West-of-River ER, Gas/Power Outage lines, and "Where Do We Gather?" (Building 1, Building 2, Shay Park).

4. **Physical & Practical Gaps for Older Adults in Tab 9 (Member Prep)**
   - **Problem:**
     - Recommending *"5-gal stackable jugs"* (Line 4324) ignores that **a filled 5-gallon water jug weighs ~42 lbs**—unsafe for many 65+ adults with arthritis, bad backs, or knee replacements!
     - No explicit checklist callout for **backup eyeglasses, hearing aid batteries, dentures/adhesive, walker/cane tags, or a printed 1-page Medication & Allergy Card** (vital for EMTs).
     - Some seniors live alone or don't currently know who their ministering companions are and feel shy asking for help with things like strapping a water heater or shutting off a heavy outdoor gas valve.
   - **Recommendation:**
     - Explicitly recommend **1-gallon or 2.5-gallon handled jugs** (8–21 lbs) or cases of sturdy bottles as senior-friendly alternatives to 5-gallon jugs, and note inexpensive siphon pumps so water never has to be lifted.
     - Add a **"Senior & Medical Readiness Box"** in Tab 9 (backup glasses, hearing aid batteries, 1-page medication/doctor card in wallet & fridge, and a reassuring note: *"Need help anchoring a water heater, testing a shut-off valve, or checking your backup battery? Tell your Relief Society or Elders Quorum—that is literally what ministering is for."*).

5. **Form Usability on Paper (Tab 8 & Tab 9 Printouts)**
   - **Problem:** Forms W-1 through W-4 use `table-layout: fixed` without explicit column widths, so `#` takes up as much horizontal space as `Specific Medical / Device Need`—leaving cramped boxes that are hard for seniors or ward clerks to hand-write in with a pen.
   - **Recommendation:** Assign realistic percentage column widths (`#`: 4%, `Code`: 8%, `Specific Need`: 24%, etc.) and increase printable row height to `30–34px` for comfortable handwriting.

---

## 3. Persona B Review: Newlywed Couple / Single Adult ("Ethan & Maya" / "Jordan" — YSA / Renter)

**Profile:** Ages 21–29, either newlyweds renting a townhome/basement apartment or a single adult in **Saratoga Springs SA 11th Ward (YSA)**. Mobile-first (95% phone usage), tight budget, minimal closet/storage space, busy with school/work, may have roommates rather than children, and won't read a 15-page leadership manual unless they immediately see what applies to *them*.

### Key Pain Points Discovered

1. **"This Wasn't Written for Me" — Single-Family Homeowner & Young-Kids Bias**
   - **Problem:** Tab 9 (Member Prep) and the Disaster Playbooks repeatedly assume the reader owns a detached house with kids:
     - Backyard trampolines, decks, fences, garages, fireplaces, 50-gallon water heaters you control, strapping furniture to studs (often prohibited by leases), outdoor propane grills (banned on most townhome/apartment balconies by HOA/fire code!).
     - Step 5 (*"Family Home Evening Activities"*) assumes kids (*"Give each child..."*, *"swap outgrown kids' clothes"*, *"Riverview Elementary reunification"*).
     - Tab 9 water table starts at **2 People** (skipping **1 Person** households—the entire YSA ward and widowed seniors!).
   - **Recommendation:**
     - Add a **1-Person row** (`3 gal` for 72h / `14 gal` for 2 weeks) to the Quick Water Math Table!
     - Add a dedicated **"Renting, Townhome, or Single Adult? Read This!"** callout box in Tab 9 covering:
       - **Small-space storage:** Under-bed water storage (1-gal jugs or flat stackables), closet-floor go-bag, 2-week no-cook pantry (no balcony propane grill needed!).
       - **Lease-safe utility knowledge:** Ask your landlord/HOA *now* where your unit's water shut-off and breaker box are (don't assume you have a private gas meter or water heater access).
       - **Renter's Insurance:** Remind renters that a landlord's policy does **not** cover personal belongings—and check Utah earthquake coverage/deductibles.
       - **YSA / Roommate Buddy Plan:** Because YSA wards have high move-in turnover, designate a **roommate + out-of-area parent/sibling** relay AND a **same-complex ward buddy** in case you don't know your ministering companion yet.

2. **Member Prep Is Buried at Tab 9 (Off-Screen on Mobile!)**
   - **Problem:** When a newlywed or YSA taps a link shared in a Ward text/email on their phone, the app opens on **Tab 1: Overview** (heavy on Stake Council structure, High Council liaisons, and Form W-5). Meanwhile, **Tab 9: Member Prep** is completely off-screen to the far right of the horizontally scrolling nav bar with no scroll indicator! Many young adults will bounce in 15 seconds thinking it's just an internal bishopric document.
   - **Recommendation:**
     - Always share **member-facing links** directly to `?tab=8` (e.g., `...html?tab=8`)—and consider adding a prominent top banner button on Tab 1: **"Just Looking for Your Home Prep Guide? Open Member Prep →"** right above the fold.
     - Add subtle left/right fade indicators on the mobile `.tabs` bar so users immediately realize the bar scrolls sideways.

3. **Static Checklists & Paper-Only Planning Feel Outdated on Mobile**
   - **Problem:** The `[ ]` checkboxes in Step 8 (Tab 9) and the 90-Day Checklist (Tab 8) are plain text—tapping them on a phone does nothing! And Step 7 (*Family Communication & Gathering Plan*) can only be filled out after printing on paper (many newlyweds and YSA don't even own a printer!).
   - **Recommendation:**
     - Make Step 8's checklist **interactive** (real `<input type="checkbox">` saved automatically to the user's phone via `localStorage`) with a motivating progress bar (**"Your Readiness: 6 of 14 items checked"**).
     - Make Step 7's **Household Contact & Gathering Card** fillable right in the browser (stored privately on-device in `localStorage`, never sent to any server), with a **"Save / Screenshot for Lock Screen"** or **"Print Card"** option!
     - Include a **"Share Member Guide"** button (using Web Share API / Copy Link to `?tab=8`) so newlyweds can text the guide straight to their spouse or roommates.

4. **Budget-Friendly Starter Track (Anti-Guilt / Anti-Prepper-Sticker-Shock)**
   - **Problem:** Mentioning a 500–1000Wh lithium power station ($400–$1,000), Berkey gravity filters ($300+), and 2 weeks of supplies can make a college student or newlywed on a $25/week grocery budget feel instantly defeated—even though the text nicely says "without debt."
   - **Recommendation:**
     - Add a **"$20 Starter Kit / Shop-Your-Closet" mini-card** showing what actually costs $0–$20 (refillable 2-liter soda bottles or $1.25 grocery-store water gallons, a $5–$8 Sawyer Mini filter or plain unscented bleach drops, extra $3 cans of chili/peanut butter per shopping trip, phone screenshots of IDs/insurance in a shared cloud folder).

5. **Car & Commuter Reality**
   - **Problem:** Many newlyweds and single adults in Saratoga Springs commute 30–60 minutes to Lehi/Orem/SLC via Redwood Rd or Pioneer Crossing (crossing the Jordan River bridges every workday). If an earthquake hits at 2:00 PM on a Tuesday, they may be stuck *across* the river from home.
   - **Recommendation:** Elevate the **Car Commuter Kit** (walking shoes, warm layer, 2 bottles of water, granola bars, phone cable, printed out-of-state contact card) into a dedicated mini-callout in Tab 9 Step 3.

---

## 4. Ecclesiastical Leadership Usability & *General Handbook* Alignment Review

To ensure this plan serves unpaid Church leaders cleanly under real-world pressure—and aligns faithfully with the *General Handbook: Serving in The Church of Jesus Christ of Latter-day Saints* (especially **Chapter 21: Ministering**, **Chapter 22: Providing for Temporal Needs and Building Self-Reliance**, and **Chapter 35: Care and Use of Meetinghouses**)—we walked through `stake_leadership_presentation.html` from four distinct leadership seats.

### Persona C: Stake President
*Handbook Reference:* `22.9.1` (Stake Presidency leads welfare/self-reliance and trains bishops), `22.9.1.3` (directs stake emergency preparedness/response with a **simple written plan**), `22.9.4` & `22.10.2` (Stake Welfare & Self-Reliance Specialists / working groups), `22.11` (Stake Bishops' Council), `22.12` (community resources), `35.5` & `35.5.5` (Emergency use of meetinghouses, Area Presidency & Facilities Management coordination, no firearms on Church property).

#### Findings & Recommendations
1. **Needs a 1-Page "First-Hour Command Card" (The `22.9.1.3` "Simple Plan" Test)**
   - **Problem:** At 4,700+ lines across 9 tabs and 7 disaster subtabs, the app is an excellent reference manual—but 5 minutes after an earthquake, a Stake President opening it on his phone cannot quickly scan his exact top decisions.
   - **Recommendation:** Add a collapsible or pinned **"Stake President First-Hour Checklist"** card at the top of Tab 1 (or a dedicated printable quick-card): (1) Confirm family safety → (2) Authorize Building 1 & 2 visual safety checks before entry → (3) Establish contact with Bishops & Area Seventy → (4) Authorize emergency meetinghouse use per Handbook `35.5.5` → (5) Submit bulk welfare requests via Saratoga Springs Bishops' Storehouse / Welfare & Self-Reliance Manager.
2. **Missing Handbook Governance Guardrails (`35.5.5` & `35.5`)**
   - **Problem:** The plan discusses opening Building 1 & 2 as warming hubs/shelters and mentions consulting FM about generators, *but omits two critical Chapter 35 policies*: (a) overnight emergency shelter use of a meetinghouse requires coordination with the **Facilities Manager** and **Area Presidency approval** (`35.5.5`), and (b) **firearms and lethal weapons are prohibited on Church property** (`35.5`, except active law enforcement)—a real safety issue to state clearly if community members shelter at a meetinghouse.
   - **Recommendation:** Add a concise **"Handbook `35.5` Meetinghouse Emergency Policy"** callout in Tab 1 and Tab 5 covering Area Presidency/FM coordination for overnight shelter and the Church property weapons policy.
3. **Missing Key Church Escalation Contacts & Non-Binding Legal Language**
   - **Problem:** Tab 6 (Directory) lists local hospitals, police, fire, and the Bishops' Storehouse, but has no blank slots for the **Area Seventy**, **Coordinating Council Chair**, **Church Welfare & Self-Reliance Manager (WSRM)**, or **Church Facilities Management (FM) Manager**. Additionally, Tab 7 Action Items 7 & 8 refer to a *"Mutual-Aid Agreement"* with Saratoga View Senior Living—which can unintentionally imply a formal legal MOU that local leaders are not authorized to sign without Church Legal (OGC) review.
   - **Recommendation:** Add an **"Ecclesiastical & Church Support Contacts (Fill In Locally)"** card to Tab 6, and rename Action Items 7–8 to **"Non-Binding Coordination Summary (No Legal MOU Without Area/Church Legal Review)"**.
4. **Under-Utilization of Stake Specialists (`22.9.4`), Working Groups (`22.10.2`), and Stake Bishops' Council (`22.11`)**
   - **Problem:** Operational work is concentrated heavily on the Stake Presidency, High Council, and Stake RS Presidency, without referencing **Stake Welfare & Self-Reliance / Emergency Specialists (`22.9.4`)** or using **Stake Bishops' Council (`22.11`)** to align Bishops on emergency Bishops' Orders and fast-offering principles.
   - **Recommendation:** Note in Tab 1 and Tab 7 that the Stake Presidency may call a **Stake Emergency Preparedness / Welfare Specialist (`22.9.4`)** or form a small **Stake Council working group (`22.10.2`)** to keep contacts, radio nets, and workshops running without overloading High Councilors.
5. **Anchor Preparedness Explicitly in Handbook `22.1` & `22.1.4` Doctrine**
   - **Problem:** While Tab 9 has warm scriptural framing, explicitly citing **General Handbook `22.1.4`** (paying tithes/offerings, minimizing debt, living within a budget, saving, education, and spiritual/emotional strength alongside food/water storage) protects the stake from drifting into secular "doomsday prepper" culture.

---

### Persona D: Bishop
*Handbook Reference:* `22.6.1` (Bishop's divine mandate under D&C 84:112; exclusive keys to approve fast offerings, Bishops' Orders, and assistance duration), `22.6.2` (delegating frontline temporal care, assessments, and preparedness teaching to EQ & RS Presidents), `22.6.4` (optional Ward Welfare & Self-Reliance Specialist), `22.7` (Ward Council creates a **simple written ward emergency plan** aligned with the stake plan), `22.8` (involving the **Ward Youth Council** in caring for those in need), `22.4.5` (strict confidentiality of assistance and member needs).

#### Findings & Recommendations
1. **Clarify What Only the Bishop Does vs. What He Delegates (`22.6.1` vs. `22.6.2`)**
   - **Problem:** Tab 8 refers generically to "Bishopric" and "Bishop's office" for binders, surveys, and outreach—risking making an already stretched Bishop the operational bottleneck instead of empowering his EQ and RS Presidents as directed in `22.6.2`.
   - **Recommendation:** Add a **"Ward Roles at a Glance (Handbook `22.6`)"** box at the top of Tab 8:
     - **Bishop's Exclusive Keys (`22.6.1`):** Approving fast-offering aid and Bishops' Storehouse orders (EQ/RS Presidents may help prepare orders when asked), directing home-sacrament authorization under Stake President direction, and reporting to the Stake President.
     - **EQ & RS Presidents (`22.6.2`):** Leading frontline ministering check-ins, confidential Form W-1 needs discovery, teaching preparedness, and preparing the anonymized Form W-5 rollup for Ward Council.
     - **Ward Welfare & Self-Reliance Specialist (`22.6.4`, optional):** Maintaining the offline Ward binder, updating Forms W-2/W-3 voluntary skills/gear, and coordinating ward workshops.
2. **Missing a 1-Page "Our Ward Emergency Plan" Cover Sheet (`22.7`)**
   - **Problem:** Tab 8 provides 5 detailed intake tables (W-1 to W-5), *but no 1-page Ward Summary Sheet* that fulfills Handbook `22.7` ("a simple written plan for the ward").
   - **Recommendation:** Add **Form W-0 (1-Page Ward Emergency Summary Card)** at the top of Tab 8 with clean blanks for: Ward Name, Primary & Fallback Gathering Sites, Bishop / EQ Pres / RS Pres / Specialist names & cell phones, Ward HAM operator/callsign, and primary FRS channel.
3. **Offline Binder Vulnerability & Data Retention Policy (`22.4.5`)**
   - **Problem:** Tab 8 Step 7 says *"Keep printed Forms W-1–W-5 in the Bishop's office."* If the meetinghouse is **red-tagged** after an earthquake, leaders cannot enter the Bishop's office! Meanwhile, paper copies of medical needs (Form W-1) require explicit privacy retention rules (`22.4.5`).
   - **Recommendation:** Recommend that the Bishop, EQ President, and RS President each keep an **offline locked/sealed copy** (or encrypted phone PDF) of Form W-1 & W-4 at home, and add a **Consent & Annual Shredding footer** on Form W-1 (*"Collected voluntarily with member consent; shred prior version annually or when a household moves out"*).
4. **Missing Ward Youth Council Integration (`22.8`)**
   - **Problem:** Handbook `22.8` specifically includes the **Ward Youth Council** in welfare and community service, yet youth are barely mentioned in Tab 8.
   - **Recommendation:** Add a **"Safe Ward Youth Service Role (`22.8`)"** callout in Tab 8 & Tab 3 (snow shoveling, assembling hygiene/comfort bags, paired adult-supervised porch deliveries, teaching basic family preparedness)—with strict boundaries keeping youth off roofs, away from chainsaws/downed wires, and under two-deep adult supervision.

---

### Persona E: Elders Quorum (EQ) President
*Handbook Reference:* `8.2.2` & `22.6.2` (under the bishop's direction, oversees ministering brothers, cares for temporal needs, teaches self-reliance and preparedness, coordinates physical service), `21.3` (quarterly ministering interviews).

#### Findings & Recommendations
1. **Survey Fatigue — Embed Intake Into Quarterly Ministering Interviews (`21.3`)**
   - **Problem:** Handing an EQ President 5 blank forms (W-1 through W-5) feels like a massive new administrative census on top of already busy ministering work.
   - **Recommendation:** Explicitly coach EQ & RS Presidents in Tab 8 to **skip cold clipboard surveys**: weave 2 natural questions into **Quarterly Ministering Interviews (`21.3`)** (*"Does anyone in your assigned homes rely on medical power or need extra help in a storm?"* and *"Are there any skills or tools you'd be willing to share with neighbors in an emergency?"*). Likewise, note that **Form W-4** starts by simply printing the existing **LCR Ministering Districts** list and noting nearby neighbor buddies for unassigned homes.
2. **Prevent Duplicate Knocking or Missed Homes (EQ + RS Unified Map Rule)**
   - **Problem:** Most households have both ministering brothers and ministering sisters, while single sisters, part-member homes, or brand-new move-ins may only have one (or neither). Form W-4 doesn't clarify how EQ and RS divide geographic streets so 4 people don't knock on one door while a widowed neighbor gets missed.
   - **Recommendation:** Add a 3-line **Unified EQ + RS Accountability Rule** on Form W-4: Ward Council maps street groups once so every household has **one designated primary check-in companionship** and one backup, reporting into a single combined Ward `Green / Yellow / Red` tally.
3. **Service Crew Safety & Liability Guardrails**
   - **Problem:** EQ Presidents are the ones actually mobilizing chainsaw crews, roof-tarping teams, burst-pipe helpers, and snow-clearing crews (Tab 3: 6A, 6C, 6D). Sending untrained volunteers onto icy roofs or near energized trees creates major injury risk.
   - **Recommendation:** Add a compact **"Work Crew Safety Rules"** callout in Tab 3 (6D/6C) and Tab 5: (a) Never climb steep, wet, or icy roofs; (b) Always work in two-person buddy teams; (c) Zero youth on chainsaws or ladders; (d) Verify with Rocky Mountain Power that lines are de-energized before clearing fallen trees near wires.
4. **Mobile "First-30-Minutes Incident Card" for EQ & RS Presidents**
   - **Problem:** Standing in a driveway during a blackout, an EQ President needs a 5-step operational checklist, not multi-paragraph prose.
   - **Recommendation:** Add a 1-screen **"Ward Incident Quick-Start Card (EQ & RS Presidents)"** in Tab 8: *(1) Family safe → (2) Ping/dispatch District Supervisors → (3) Check offline Form W-1 SN-1/SN-3 priority homes first → (4) Log Green/Yellow/Red count → (5) Send Form W-5 to Bishop & Stake Command*.

---

### Persona F: Ward Relief Society (RS) President
*Handbook Reference:* `9.2.2` & `22.6.2` (under the bishop's direction, co-equal frontline leader with EQ President in temporal care, compassionate service, preparedness teaching, emotional/spiritual resilience, and preparing bishops' orders when asked), `21.3` (ministering interviews), `22.4.5` (confidentiality & dignity), `22.13` (official Church self-reliance courses).

#### Findings & Recommendations
1. **Tone & Dignity Check: Bridging "FEMA Tactical" (Tabs 1–7) and "Christlike Ministering" (Tab 9)**
   - **Problem:** Tabs 1–7 use dense operational language (`SN-1–SN-8 triage codes`, `anonymized transmission slip`, `capability breaks`, `billeting`), whereas Ward RS Presidents lead through personal warmth, compassion, and preserving sisters' dignity (`22.4.5`).
   - **Recommendation:** Add a short **"Ministering with Dignity — Sample Conversation Script"** right above Form W-1 in Tab 8 so ministering sisters feel natural, loving, and non-intrusive when asking about medical power or special needs (*"Our ward wants to be sure that if the power ever goes out in a storm, nobody feels forgotten. Is there anything our presidency should quietly keep in mind for your household?"*).
2. **Missing Real-World Vulnerable Groups RS Presidents Care For Daily**
   - **Problem:** SN-1 through SN-8 overlook four high-reality situations Ward RS Presidents routinely encounter:
     - **Expectant & Postpartum Mothers / Newborns** (SN-7 focuses only on formula/diapers—not a mother 4 days postpartum or in late pregnancy during a winter outage or wildfire evacuation).
     - **Single Parents & Temporarily Solo Spouses** (when a spouse is commuting across the Jordan River or traveling for work).
     - **Acute Mental Health / Emotional Crisis** (disasters trigger severe panic, grief, or crisis—yet **988 Suicide & Crisis Lifeline** isn't listed anywhere in Tab 6 Directory or Tab 9!).
     - **Pets & Service Animals** (isolated seniors and single sisters will frequently refuse wildfire evacuation if pets/service animals have no plan).
   - **Recommendation:** Broaden SN-7 to **Infants, Expectant/Postpartum Mothers & Solo Parents**, add **988 Suicide & Crisis Lifeline** to Tab 6 & Tab 9 Step 6, and add a brief **Service Animal / Pet Evacuation tip** in Tab 3 (6B Wildfire) and Tab 9.
3. **Balanced EQ + RS Workload & Practical Playbooks for Caregiver Duties**
   - **Problem:** Relief Society is assigned heavy caregiving operations (insulin cooler hubs, host-family billeting, porch-drop meals, bereavement care), without showing how Elders Quorum shares the heavy lifting or giving a quick checklist for setting up a safe host-family match or porch-drop network.
   - **Recommendation:** Explicitly pair **EQ + RS jointly** on cooler hubs, host homes, and meal delivery (e.g., EQ handles heavy cooler/ice transport, generators, and driving; RS & EQ share check-ins and meals), and add a 5-bullet **Host-Family & Porch-Drop Quick Checklist** (allergies, stairs/accessibility, pet compatibility, expected duration, privacy).
4. **Connect Preparedness Directly to Official Church Self-Reliance Courses (`22.13`)**
   - **Problem:** Tab 9 Step 6 discusses financial and emotional resilience well, *but doesn't link to official Church Self-Reliance resources* (`selfreliance.ChurchofJesusChrist.org` — *Personal Finances*, *Finding Strength in the Lord: Emotional Resilience*, *Starting & Growing My Business*, *Education for Better Work*).
   - **Recommendation:** Add a **"Year-Round Church Self-Reliance Groups (Handbook `22.13`)"** link box in Tab 9 Step 6 and Tab 8's Q4 Roadmap so Ward RS and EQ Presidents can seamlessly invite members into ongoing self-reliance courses.

---

## 5. Prioritized Improvement Roadmap (Sections 1–4, 6, 8.1 & 8.3)

Reprioritized by **emergency readiness, *General Handbook* compliance, and real-world rollout impact**, summarizing every gap identified across Sections 1–4, Section 6 (Stake RS Presidency pass), Section 8.1 (Personal Crisis Bridge & Lifelines), and Section 8.3 (Home Storage Center Order Form). *(Section 7 architecture split and Section 8.2 standalone Life-Events Companion Playbook are intentionally left separate to weave in later.)*

### P0 — Completed in Current Pass *(Baseline Usability, Installability & Bulk Food Links)*
- [x] **Deep Dive table & button alignment** — Removed `.screen-only { display: initial }` so Hazards Action cells and inline-flex buttons render properly *(Sec. 1)*.
- [x] **Checklist word misalignment (Tabs 8 & 9)** — Replaced flex layout on `.checklist-list li` with hanging-indent block layout so inline `<strong>` tags stop splitting into broken columns *(Sec. 1)*.
- [x] **Deep Dive scroll & return flow** — Added `scroll-margin-top`, active mobile subtab centering, browser Back-button (`popstate`) support, and a **"← Back to Hazards Matrix"** banner *(Sec. 1)*.
- [x] **Visual polish** — Converted raw `*markdown*` italics to `<em>`, fixed tablet nav overflow, bottom-aligned Tab 1 CTA buttons, fixed colliding contact card headers, and replaced overflowing underscores *(Sec. 1)*.
- [x] **Save to Phone Home Screen (PWA)** — Added header install button + OS-aware modal, custom navy/gold app icons (`180px`, `192px`, `512px`, SVG favicon), `manifest.webmanifest`, and offline caching (`sw.js`).
- [x] **Official Home Storage Center Order Form links live** — Linked the hard-to-find U.S. PDF (`US_en.pdf`), Spanish PDF (`US_es.pdf`), Hours & Prices page, and `store.ChurchofJesusChrist.org` across Tab 6 Directory and Tab 9 Step 2 & Step 8, clarifying card-only/no-AmEx rules and Home Storage Center vs. Bishops' Storehouse *(Sec. 8.3; remaining follow-up: add link to Tab 8 Q1 Roadmap)*.

---

### P1 — Completed *(Emergency Access, Confidentiality & Handbook Compliance)*

| # | Source | Status | Improvement | Gap Filled |
|---|---|---|---|---|
| **1.1** | **Sec. 2, 4F, 8.1c** | **Done** | **Clickable `tel:` phone links + Personal Crisis Lifelines** | Fixes 0 tappable phone numbers during a 2:00 AM crisis and adds missing lifelines in Tab 6 & Tab 9: **988 Crisis Lifeline**, **211 Utah**, **Deseret Industries (`104 W Medical Dr`)**, **Utah Workforce Services (`jobs.utah.gov`)**, **Church Employment**, **LDS Family Services** (via Bishop), **Red Cross Fire Relief**, and **Church Abuse Help Line (`1-800-453-3860` — for Bishops/Stake Pres, `GH 38.6.2`)**. |
| **1.2** | **Sec. 4C, 6.4** | **Done** | ***General Handbook* Governance, Legal & Sunday-Meeting Guardrails** | Documents `GH 35.5.5` (Area Presidency + FM approval before overnight chapel shelter), `GH 35.5` (no firearms on Church property), non-binding wording on Saratoga View / Riverview summaries (no unauthorized legal MOUs), `GH 22.1.4` self-reliance doctrine, and fixes Tab 8 Q1–Q4 wording from *"Teach in RS"* to **"5th Sunday Combined Meeting or Optional RS/EQ Activity Night"** (`GH 9.2.1.2` General Conference Sunday lessons). |
| **1.3** | **Sec. 4D, 6.2, 8.1d** | **Done** | **Form W-1 Privacy Rules (`GH 22.4.5`) & Off-Site Binder Backup** | Adds an explicit **consent, functional-needs-only (never clinical diagnoses), "ask before sharing," and annual-shredding notice** on Form W-1, and instructs Bishop + EQ/RS Presidents to keep locked offline copies at home so a red-tagged chapel doesn't block access. |
| **1.4** | **Sec. 4C, 6.3** | **Done** | **Rebalance Tab 6 POCs (`GH 22.9.3`) & Add Ecclesiastical Support Slots** | Moves ERs, hospitals, and Red Cross logistics POCs to **High Council Civil/Public Safety Liaisons** so the 3–4 member Stake RS Presidency isn't overloaded, and adds fill-in slots for **Area Seventy, Coordinating Council Chair, Welfare & Self-Reliance Manager, and FM Manager**. |
| **1.5** | **Sec. 8.1b** | **Done** | **Scope Boundary Sentence (Community Disasters vs. Personal Crises)** | Adds 1 crisp line in Tab 1 & Tab 8 clarifying that community-wide disruptions activate this Operations Plan (`GH 22.9.1.3`), while individual family crises (job loss, house fire, illness) route through normal confidential Ward welfare & ministering (`GH 22.4–22.7`, with the separate Phase 2 companion playbook). |

---

### P2 — Completed *(High-Impact Usability, Delegation & Member Inclusion)*

| # | Source | Status | Improvement | Gap Filled |
|---|---|---|---|---|
| **2.1** | **Sec. 2, 3, 4C–E** | **Done** | **1-Page Crisis Quick-Cards & Top-of-Tab-1 Audience Router** | Adds **Stake President First-Hour Command Card** (`GH 22.9.1.3`), **Form W-0 (1-Page Ward Summary Sheet)** (`GH 22.7`), **EQ/RS First-30-Min Incident Card**, a Member **"Emergency Right Now" Quick Strip**, and a top-of-Tab-1 **"Member Prep →" vs. "Leader Toolkit →"** router so nobody hunts through 9 tabs. |
| **2.2** | **Sec. 4C–E, 6.2, 6.3, 6.4, 8.3** | **Done** | **Ward Delegation, Ministering-Interview Intake & Grab-and-Go RS/EQ Activities** | Adds **Ward Roles at a Glance (`GH 22.6.1–22.6.4`)** separating Bishop's exclusive keys from EQ/RS & optional Ward/Stake Specialists (`22.9.4`, `22.10.2`, `22.11`); positions **Quarterly Ministering Interviews (`GH 21.3`)** as primary Form W-1–W-3 intake (no cold surveys) and LCR districts as Form W-4's base; adds **3–4 zero-prep Ward RS/EQ activity outlines** + Tab 8 Q1 link to the **Home Storage Center Order Form PDF**. |
| **2.3** | **Sec. 4D, 4E** | **Done** | **Unified EQ + RS Street Map, Work Crew Safety & Youth Role (`GH 22.8`)** | Prevents 4 people knocking on one house while single/unassigned homes get missed; adds EQ physical safety rules (no steep/icy roofs, two-person pairs, de-energized lines, zero youth on chainsaws/ladders); adds a safe, adult-supervised **Ward Youth Council (`22.8`)** service role. |
| **2.4** | **Sec. 4F, 6.2, 6.3** | **Done** | **Dignity Script, "Who's Easily Missed?" & Shared EQ/RS Caregiving** | Adds **"Ministering with Dignity"** prompt + **"Who's Easily Missed?"** box above Form W-1 (expectant/postpartum moms, full-time family caregivers, severe anxiety/domestic-safety risks, recent widows, temporarily solo parents); broadens SN-7; adds **Pet/Service-Animal** wildfire tip; splits heavy hauling/ice/power (EQ & High Council Logistics) from joint EQ+RS caregiving on cooler hubs, host homes (5-point safety checklist), and porch-drop meals. |
| **2.5** | **Sec. 6.1, 8.1a** | **Done** | **Zero-Guilt Tone, \$0–\$15 Alternatives & "Everyday Personal Storms" Bridge (Tab 9)** | Adds **"You Are Already More Ready Than You Think"** + **"Preparedness Isn't Just for Earthquakes"** bridge callout (linking the same habits to job loss, house fires, and illness); pairs every expensive gear item (Berkey, \$400–\$1,000 battery station) with a **\$0–\$15 alternative**; replaces clinical `SN-1–SN-8` jargon in Tab 9 with warm plain English. |
| **2.6** | **Sec. 3, 6.5** | **Done** | **Single Adults, Newlyweds & Renters (`SA 11th YSA`) Inclusion** | Adds **1-Person** row (`3 gal / 14 gal`) to Water Math Table, a **"Single Adults, Roommates & Renters"** box (under-bed flat jugs, HOA-safe no-cook pantry, lease-safe shut-offs, renter's insurance), **apartment/complex buddy** guidance for high-turnover YSA units, and broadens *"Parents & Kids / FHE"* headings to **"Household, Roommate & Family Activities."** |
| **2.7** | **Sec. 2** | **Done** | **Senior-Friendly Storage, Medical Card & Accessibility Upgrades** | Recommends **1–2.5 gal jugs / siphon pumps** instead of 42-lb 5-gal jugs; adds **Senior Medical Card** checklist (backup glasses, hearing-aid batteries, 1-page med/allergy card + warm reassurance on asking ministering help); adds **"A+ Larger Text"** toggle, darker `--text-muted` (`#475569`), 44px mobile tap targets, and sideways-scroll cues. |
| **2.8** | **Sec. 4F, 6.4** | **Done** | **Link Official Church Self-Reliance & Emotional Resilience Courses (`GH 22.13`)** | Connects Tab 9 Step 6 and Tab 8 Q4 directly to `selfreliance.ChurchofJesusChrist.org` (*Personal Finances*, *Emotional Resilience*) so RS & EQ Presidents can use the guide year-round. |

---

### P3 — Completed *(Interactive Mobile Experience & Print Polish)*

| # | Source | Status | Improvement | Gap Filled |
|---|---|---|---|---|
| **3.1** | **Sec. 3** | **Done** | **Interactive `localStorage` Checklists & Readiness Progress Bar** | Turns static `[ ]` text in Member Step 8 and Ward 90-Day Launch into tappable checkboxes that save privately on the user's phone with live completion bars. |
| **3.2** | **Sec. 3** | **Done** | **Fillable On-Device Household Contact Card + One-Tap Share** | Lets printer-less newlyweds/YSA fill Step 7 & Step 8 action items on their phone (stored locally, never uploaded), print/save PDF, and share `?tab=8` via native Share Sheet or copy link. |
| **3.3** | **Sec. 2** | **Done** | **Printable Form W-1–W-4 Column Widths & Taller Rows** | Adds explicit `<colgroup>` column percentages and `30–32px` row heights so Ward clerks and seniors can hand-write comfortably on paper. |
| **3.4** | **Sec. 2** | **Done** | **Plain-English Glossary Modal** | Adds a header Glossary modal translating jargon (`WUI`, `SN-1–SN-8`, `RMP Medical Certificate`, `UCARES`, `MERV-13`, `FRS`, `FM Group`, `WSRM`, `LZ`, `EOC`, `PEX`, `LCR`, `GH`) in plain language. |
| **3.5** | **Sec. 3** | **Done** | **"\$20 Starter Budget" & "Jordan River Commuter Car Kit" Mini-Cards** | Removes "prepper sticker shock" for students/newlyweds on tight budgets and addresses workers stranded east of the Jordan River during a daytime quake. |

*(Also linked Rocky Mountain Power's official [Medical Certificate Program](https://www.rockymountainpower.net/my-account/payments/bill-payment-assistance/medical-certificate.html) across Tab 4, Tab 6, Tab 9, and the Plain-English Glossary.)*

---

## 6. Stake Relief Society Presidency Review: Questions & Draft Recommendations (6.1–6.5)

> **How to Use This Section:** Below are the 5 review prompts tailored for the **Stake Relief Society Presidency**, paired with a **simulated pre-review pass from the Stake RS Presidency persona** (*General Handbook* `9.2.1.2`, `9.6`, `22.6.2`, `22.9.3`, `22.13`). Use these draft recommendations to sharpen the plan *before* your review meeting—or hand them to the presidency as a "react-and-edit" starter list so they can easily confirm, tweak, or cross out items.

### 6.1 Tone, Dignity & Peace (`GH 22.1` & `22.4.5`) → *Mapped to Roadmap P2.5*
* **Review Question:** *Does the Member Prep Guide (Tab 9) feel calm, Christ-centered, and doable—especially for sisters on fixed incomes, single mothers, expectant/postpartum moms, newlyweds, and widows?*
* **Stake RS Presidency Perspective & Concrete Recommendations:**
  * **Keep:** The scriptural framing (*"If ye are prepared ye shall not fear"*, Bishop Waddell's *"do what we can do, when we can do it"*), calm family hero visual, and 4-Weekend Quick-Start feel warm and grounded.
  * **Fix (sticker-shock & clinical tone):** Showing **84–112 gallons of water** alongside **\$400–\$1,000 portable lithium stations** and **Berkey filters** can make widows on Social Security, single mothers, or young families feel defeated before starting.
  * **Actionable edits:**
    1. Add a **"You Are Already More Ready Than You Think"** lead box in Tab 9 emphasizing everyday pantry items and loving neighborhood connections over expensive gear.
    2. Pair every costly item with a **\$0–\$15 alternative** (*gravity filter OR boiling/unscented bleach drops*; *battery station OR Rocky Mountain Power Medical Priority + quiet Ward loaner*).
    3. Keep clinical codes (`SN-1–SN-8`) in leadership tables only—in Tab 9 Step 1, use plain warm wording: **"Households Needing Extra Care During an Outage."**

### 6.2 Special Needs & Ministering Interviews (`GH 21.3` & Form W-1) → *Mapped to Roadmap P1.3, P2.2 & P2.4*
* **Review Question:** *Would Ward RS Presidents prefer gathering Form W-1 needs naturally through quarterly ministering interviews rather than a separate survey? Are any vulnerable groups missing from SN-1 through SN-8?*
* **Stake RS Presidency Perspective & Concrete Recommendations:**
  * **Fix (survey resistance & missed sisters):** Cold clipboard surveys stall in busy wards, and proud seniors or struggling sisters often say *"We're fine"* on a formal form. Meanwhile, four vulnerable groups are routinely missed: **expectant/newly postpartum moms**, **full-time family caregivers**, **sisters facing severe anxiety/grief/domestic safety risks**, and **temporarily solo parents**.
  * **Actionable edits:**
    1. Position **Quarterly Ministering Interviews (`GH 21.3`)** and new move-in welcomes as the primary way Form W-1 stays fresh—paired with a 2-sentence **"Ministering with Dignity"** prompt.
    2. Add a **"Who's Easily Missed?"** reminder box right above Form W-1.
    3. Add an explicit privacy instruction on Form W-1: record **functional support needs only** (*"Needs backup power for medical device"*), **never clinical diagnoses** (`GH 22.4.5`).

### 6.3 Shared Load with Elders Quorum (`GH 22.6.2`) & Stake RS Presidency Capacity (`GH 22.9.3`) → *Mapped to Roadmap P1.4, P2.2 & P2.4*
* **Review Question:** *Do the Shelter, Cooler/Insulin Hub, Porch-Drop Meals, Host-Family Billeting, and Saratoga View roles feel realistic—and where should Elders Quorum explicitly share the physical/logistics load?*
* **Stake RS Presidency Perspective & Concrete Recommendations:**
  * **Fix (Stake RS overload):** A 3–4 person Stake RS Presidency (whose own families live in the disaster zone) should **instruct and support Ward RS Presidencies (`GH 22.9.3`)**, not serve as sole crisis dispatcher for 5 hospitals, cooler hubs, host homes, and W-5 spreadsheets simultaneously.
  * **Actionable edits:**
    1. **Rebalance Tab 6 Directory POCs:** Assign **High Council Civil/Public Safety Liaisons** as primary POCs for ERs, hospitals, and Red Cross logistics; keep **Stake RS Presidency** focused on Ward RS support, family welfare/emotional care, and Bishops' Storehouse sister-welfare support.
    2. **Split physical vs. caregiving load with Elders Quorum (`GH 22.6.2`):** EQ/High Council Logistics hauls heavy coolers, ice, water, and backup power; RS & EQ share check-in desks, in-ward host-family matching (using a 5-point safety checklist: allergies, stairs, pets, duration, privacy), and porch-drop meals.
    3. **Use a Stake Working Group / Specialist (`GH 22.9.4` / `22.10.2`):** Call a Stake Emergency/Welfare Specialist to handle W-5 rollups and annual audits.

### 6.4 Ward Relief Society Adoption (Tab 8 — Roadmap & Sunday Meeting Alignment) → *Mapped to Roadmap P1.2, P2.2 & P2.8*
* **Review Question:** *Is the 12-Month Ward Roadmap light enough to weave into Relief Society / 5th Sunday lessons and Church Self-Reliance courses (`GH 22.13`) without feeling like "one more heavy program"?*
* **Stake RS Presidency Perspective & Concrete Recommendations:**
  * **Fix (Handbook `9.2.1.2` Sunday-lesson conflict):** 2nd and 4th Sunday Relief Society meetings are dedicated strictly to **General Conference messages**—telling Ward RS Presidents to *"teach preparedness in RS"* conflicts with Handbook policy.
  * **Actionable edits:**
    1. Change Tab 8 Q1–Q4 roadmap wording to **"5th Sunday Combined Meeting (at Bishopric's invitation) OR Optional RS/EQ Activity Night."**
    2. Include **3–4 "Grab-and-Go" low-prep RS/EQ activity outlines** (*Spring 72-Hr Kit Show-and-Tell*, *Home Storage Center Group Trip*, *15-Minute Household Contact Card Night*).
    3. Link **Emotional Resilience** and **Personal Finances** Self-Reliance groups (`GH 22.13`) directly alongside emergency kits.

### 6.5 Single Adults, Newlyweds & Renters (`SA 11th YSA Ward` & Townhomes/Apartments) → *Mapped to Roadmap P2.6*
* **Review Question:** *What specific additions would help sisters in the **Saratoga Springs SA 11th Ward (YSA)** and townhome/apartment renters feel directly included?*
* **Stake RS Presidency Perspective & Concrete Recommendations:**
  * **Fix (homeowner/young-kids bias):** Single sisters, widows, and newlyweds renting townhomes/apartments feel invisible when headings assume *"Parents & Kids"*, *"backyard trampolines"*, and *"50-gallon water heaters"*, and high YSA roommate turnover outpaces LCR ministering lists.
  * **Actionable edits:**
    1. Add a **"Single Adults, Roommates & Renters"** box in Tab 9 with a **1-Person water row (`3 gal / 14 gal`)**, under-bed flat jugs, HOA-safe no-cook foods, renter's insurance, and asking landlords where unit shut-offs are.
    2. Recommend **apartment/complex buddy check-ins** for SA 11th YSA alongside ministering + an out-of-area parent/sibling relay.
    3. Broaden Tab 9 headings (*"Family Home Evening"* / *"Parents & Kids"*) to **"Household, Roommate & Family Activities"** and add 2 adult/roommate-friendly practice ideas.


---

## 7. Multi-Agent Architecture & Sensitivity Debate: One Document vs. Separated Role Deliverables

**Core Question:** *How should the Stake package this emergency plan so it is relevant to Stake Leaders, Ward Leaders (Bishop, EQ Pres, RS Pres), and Members (65+, families, newlyweds, YSA) without causing member abandonment, Stake-vs-Ward confusion, or exposing sensitive information?*

> **Execution Note:** Because no external Anthropic/OpenAI API keys are configured in this environment (and this Intel i7-4770HQ CPU-only Mac is not suited for running large local models), this debate was conducted between two independent adversarial agents with isolated conversation contexts following the project's Alpha/Beta debate protocol. A matching cross-vendor prompt packet is also saved at [`prompts_for_agents/prompt_architecture_privacy_debate.md`](../prompts_for_agents/prompt_architecture_privacy_debate.md) if you wish to run the same debate across Claude and ChatGPT web interfaces.

### Round 1 — Agent Alpha (Information Architecture & Privacy/Security Specialist)
**Position:** Clean structural separation into four distinct tiers; consolidating everything into one 9-tab PWA titled *"Stake Plan"* fails on usability, *General Handbook* stewardship, and security.

* **Member Abandonment:** Tab 9 (*Member Prep*) is buried behind 8 leadership tabs. Under crisis stress, a 65-year-old or YSA renter landing on Tab 1 (*Three-Tier Command*) bounces before finding water math, shut-offs, or 72-hour kits.
* **Ecclesiastical Boundary Confusion (*General Handbook* `22.9.1.3`, `22.6.1–22.6.2`, `35.5.5`):** Combining Stake operational registers, Ward forms, and Member prep blurs Ward-first ministering stewardship and risks members prematurely self-deploying to uninspected meetinghouses before Stake President/FM clearance (`35.5.5`).
* **Genuine Privacy, Physical Security & Liability Exposure on a Public URL:**
  1. **Saratoga View Memory-Care Security (Tab 4):** Publishing *magnetic memory-care door-release behavior* and *exterior perimeter sentry protocols* on a public URL exposes vulnerable residents' security mechanics and invites untrained volunteers to self-deploy to a private licensed care facility.
  2. **Confidential Member Health Data (`22.4.5` — Tabs 4 & 8):** Bundling Form W-1 (oxygen, CPAP, dialysis, insulin) inside a broadly shared web app raises the risk of leaders accidentally entering or saving live member PHI into shared cloud copies.
  3. **Channel Jamming & Facility Exposure (Tabs 5, 6, 7):** Publishing direct **Area Seventy, FM Manager, Welfare & Self-Reliance Manager, and Bishops' Storehouse** escalation lines risks routine member calls jamming crisis lines. Exposing exact meetinghouse seismic gas-valve / HVAC outside-air damper override details and named/addressed neighborhood equipment inventories creates avoidable physical-security/theft risk.
* **Alpha's Initial Proposal:** Split into 4 separate deliverables: (1) Public Member Guide, (2) LCR-restricted Ward PDF, (3) Access-controlled Stake EOP + separate Saratoga View Annex, and (4) Strictly Offline Confidential Records.

---

### Round 2 — Agent Beta (Volunteer Sustainability & Single-Source-of-Truth Architect)
**Position:** Explicitly concedes Alpha's member UX failure and real security catches, *but challenges the 4-tier split as unmaintainable under unpaid volunteer rotation and fragile at 2:00 AM*.

* **Explicit Concessions to Alpha:**
  1. Burying Member Prep at Tab 9 inside *"Stake Plan"* is a clear usability failure.
  2. Live PHI (completed Forms W-1–W-4) and Saratoga View memory-care magnetic door-release / perimeter-sentry mechanics **must never appear on any hosted web URL**.
* **Where Alpha's 4-Tier Split Breaks Down:**
  1. **Guaranteed Version Drift:** Splitting Tab 3 (*Disruptions*) and Tab 6 (*Directory*) across three separate files guarantees that within one calling cycle (2–5 years), a new volunteer updates Shay Park, Storehouse rules, or a phone number in one file while the other two silently go stale and contradict each other.
  2. **The "2:00 AM Access-Control Trap":** Putting Tier 3 behind a login portal and Tier 2 inside LCR fails catastrophically during an earthquake blackout. Nobody in an unpaid Stake can cleanly provision/revoke logins across 30+ rotating Ward and Stake council leaders—and an expired auth token or uncached LCR PDF at 2:00 AM locks out a newly called Bishop when he needs the plan most.
  3. **Don't Put Private Numbers in HTML at All:** Instead of locking HTML behind a password wall to protect Area Seventy / FM / personal leadership cell numbers, **never hard-code private phone numbers into HTML**—point leaders to **Member Tools / LCR** (already cached on their phones) and printed physical binders.
* **Beta's Counter-Proposal — Single-Source "2 Static Offline PWAs + 1 Offline Binder":**
  1. **`family.html` ("Crossroads Family Prep"):** Public, mobile-first offline Home Screen PWA containing *only* Member Prep, Family-lane actions, public emergency numbers, and *"do not self-deploy to chapels"* guidance.
  2. **`leadership.html` ("Crossroads Leader Ops"):** Unlisted static offline PWA (**no login wall**, zero PHI, zero private cell numbers, zero Saratoga View door-release mechanics) unifying Stake & Ward operational playbooks and blank printable forms offline.
  3. **Strictly Offline Confidential Binder:** Completed W-1–W-4 rosters, Saratoga View security annex, and direct Area/FM/Storehouse escalation sheets live *only* in locked physical binders (audited annually).
  * *Zero-Drift Build:* Generate both `family.html` and `leadership.html` from **one shared canonical data source** so one edit updates both offline PWAs automatically.

---

### Round 3 — Agent Alpha Rebuttal & Convergence Terms
Alpha **endorses Beta's Single-Source "2 PWAs + 1 Offline Binder" hybrid** (agreeing that removing all sensitive data from HTML is strictly safer than brittle login walls), subject to **two hard guardrails** on `leadership.html`:

1. **Pass the "Public-Leak Test" (Assume an Unlisted Link Will Be Forwarded):**
   - Add `<meta name="robots" content="noindex, nofollow">` and a prominent top banner: *"Members: Looking for Family Prep? → Open Family Guide (`family.html`)."*
   - Strip exact meetinghouse seismic gas-valve / HVAC damper override mechanics from Tab 7 (*replace with "Follow printed FM Facility Sheet in Offline Binder"*).
   - Strip Saratoga View magnetic door-release / sentry mechanics from Tab 4 (keep only high-level non-binding coordination role pointing to the Offline Annex).
   - Stamp a bold red footer on every printable Ward Form (W-1–W-4): *"CONFIDENTIAL (`GH 22.4.5`) — NEVER UPLOAD COMPLETED COPIES TO CLOUD DRIVES, EMAIL, OR GROUP TEXTS."*
2. **Prevent Ward-vs-Stake Confusion Inside `leadership.html`:**
   - Add an offline-safe **Role Switcher** (`Ward Leadership` vs. `Stake Leadership`, saved in `localStorage`) so Bishops, EQ Presidents, and Ward RS Presidents land straight on **Form W-0, First-30-Min Incident Card, Ward Forms, and Ward-lane Playbooks**, while Stake leaders land on **Stake Command, Hazard Matrix, Stake Registers, and Stake Actions**—preserving one shared operational picture without cognitive overload.

---

### Round 4 — Consensus Architecture & 3-Tier Sensitivity Classification Matrix

#### A. Exact Sensitivity & Access Classification

| Sensitivity Tier | Where It Lives | Exact Content Included | Explicit Exclusions |
| :--- | :--- | :--- | :--- |
| **Tier 1: Public / Member-Safe** | **`family.html`** (*Public offline PWA: "Crossroads Family Prep"* + printable handout + QR code on Sunday programs) | Tab 9 Member Prep (4-Weekend Plan, Aux Power self-check, Senior & Renter/YSA tracks, Water/Food math, 72-hr kit, Home shut-offs, Contact Card, Checklist); Family-lane quick actions (Tab 3); **Public-only** tappable `tel:` numbers (911, Intermountain ER, Fire, Police, Utilities, 988 Crisis Lifeline, Red Cross); general FRS Ch 1/3/5 & *"check home/ministering first; wait for authorization before going to chapels (`GH 35.5.5`)."* | Zero Stake Council orgs/actions, zero Ward Forms W-1–W-5, zero Saratoga View protocols, zero Area/FM/Storehouse direct escalation lines, zero chapel utility details. |
| **Tier 2: Unlisted Leadership Reference** *(Passes "Public-Leak Test")* | **`leadership.html`** (*Unlisted `noindex` offline PWA: "Crossroads Leader Ops"* with **Ward / Stake Role Switcher** — no login wall) | Role-filtered Stake & Ward views (`GH 22.6` & `22.9` boundary labels): Form W-0 (1-Page Ward Summary), First-Hour / First-30-Min Incident Cards, 7 Disruption Playbooks, Hazard Matrix, HAM/FRS radio plan, anonymized cross-ward capability *categories*, `GH 35.5` meetinghouse rules, 12-Month Ward Roadmap, and **blank printable Forms W-1–W-5** (with red `GH 22.4.5` confidentiality footer). | **Zero** member names/PHI, **zero** private personal/Area/FM cell numbers (point to Member Tools + Binder), **zero** Saratoga View magnetic-door/sentry mechanics, **zero** chapel HVAC/gas-valve override specifics, **zero** named equipment addresses. |
| **Tier 3: Strictly Confidential / Offline-Only** | **Locked Physical Binders** (or local encrypted device PDFs) held by Bishop, EQ Pres, RS Pres, Stake Pres & Riverview Branch Pres — **NEVER hosted online** | (1) Completed **Form W-1** (named medical/aux-power needs, shredded annually per `GH 22.4.5`), named **W-2/W-3** gear/skills, and **W-4** ministering district rosters; (2) **Saratoga View / Riverview Branch Confidential Security Annex** (memory-care egress & perimeter protocols); (3) **Direct Escalation & Facility Sheet** (Area Seventy, Coordinating Council Chair, WSRM, FM Manager, and Building 1 & 2 exact gas-valve/HVAC shutoff locations). | **Never** stored in Google Drive, emailed as attachments, texted in group chats, or committed to any web repository. |

#### B. Single-Source Implementation Blueprint (Zero Version Drift)
Rather than hand-editing two diverging HTML files, build a lightweight **single-source build script** (zero external dependencies, pure Python 3 in this repo) that holds shared truth once—gathering locations, verified public contacts, hazard summaries, and Family/Ward/Stake playbook lanes—and compiles:
1. `family.html` (Public Member PWA + `manifest-family.webmanifest`)
2. `leadership.html` (Unlisted `noindex` Leadership PWA with Ward/Stake Role Switcher + `manifest-leadership.webmanifest`)
3. Printable Offline Annex Templates (for Stake Presidency & Bishop physical binders — never published with live data)

**Result:** Members get a calm, focused, 1-tap Home Screen app tailored to seniors, families, newlyweds, and YSA; Bishops and EQ/RS Presidents get an instant Ward-focused operational view with clear *General Handbook* guardrails; genuinely sensitive care-center security details and member health data never touch the internet; and a future volunteer leader in 2030 can update one shared file and keep everything synchronized in minutes.


---

## 8. Personal & Household Crises ("Everyday Family Disasters"): Job Loss, House Fire & Protracted Medical Emergency

### 8.1 Do Personal Crises Fit in This Document? (Strategic Placement & Concrete Actions)

**Decision:** **Yes — include a lightweight motivational bridge in Tab 9 and verified Personal Crisis Lifelines in Tab 6/Tab 9; No — do not add personal crises as disaster tabs in Tab 3 (keep full life-event playbooks in the separate Phase 2 companion file in 8.2).**

Under *General Handbook* Chapter 22, **community-wide disasters** (`GH 22.9.1.3`) break civic infrastructure and activate Stake Command, HAM nets, and gathering hubs, whereas **personal household crises** (`GH 22.4–22.7`) leave utilities intact and are cared for confidentially through Ward welfare and ministering. Four concrete actions bridge both worlds cleanly inside the Emergency Operations Plan:

| # | Concrete Recommended Action | Roadmap Slot | Strong "Why" Statement |
|---|---|---|---|
| **8.1a** | **Add a compact "Preparedness Isn't Just for Earthquakes" callout near the top of Tab 9 (Member Prep)** showing how the *same* habits (emergency fund, rotating pantry, insurance review, cloud documents) cushion job loss, house fires, and prolonged medical crises—plus a warm invitation to contact your Bishop, RS President, or EQ President early. | **P2.5** | Every ward sees layoffs, serious diagnoses, and occasional house fires *every year*—100× more often than an M7.0 quake. Anchoring preparedness to relatable life storms removes "doomsday prepper" resistance and immediately boosts household adoption. |
| **8.1b** | **Add a 1-sentence scope boundary in Tab 1 & Tab 8** clarifying that this Operations Plan activates for community-wide/infrastructure disruptions (`GH 22.9.1.3`), while individual family crises route through normal confidential Ward welfare & ministering (`GH 22.4–22.7`, with the standalone companion playbook in 8.2). | **P1.5** | Prevents leaders and members from blurring confidential pastoral care (`GH 22.4.5`) with Stake disaster command, keeping the EOP crisp and easy to approve in Stake Council. |
| **8.1c** | **Add a verified "Personal Crisis Lifelines" block (`GH 22.12–22.13`) in Tab 6 & Tab 9:** `988` Crisis Lifeline, `211 Utah`, Deseret Industries (`104 W Medical Dr`), Utah Workforce Services (`jobs.utah.gov`), Church Employment (`employment.ChurchofJesusChrist.org`), LDS Family Services (via Bishop), American Red Cross Fire Relief (`801-373-8580`), and Church Abuse Help Line (`1-800-453-3860` — for Bishops/Stake Pres, `GH 38.6.2`). | **P1.1** | A shocked family—or a newly called Bishop/RS President—cannot hunt down referral numbers at midnight. Centralizing verified Church and Utah lifelines speeds relief and honors `GH 22.4.1` / `22.12`. |
| **8.1d** | **Embed an explicit "Ask Before Sharing" confidentiality rule (`GH 22.4.5`)** in Tab 8 Ward leadership guidance alongside Form W-1's privacy notice. | **P1.3** | Unlike a neighborhood blackout, job loss, illness, and marital strain carry deep privacy needs; explicit consent protects member dignity and prevents well-meaning gossip. |

---

### 8.2 Companion Playbook Extracted (Phase 2 Ministering Resource)

Because personal crises and major life transitions serve a different weekly pastoral cadence (`GH 21`, `22.4–22.8`) than community-wide disaster ops (`GH 22.9.1.3`), all **10 4-Horizon × 3-Tier Playbooks** (*Job Loss, House Fire, Protracted Medical Emergency, Birth/Adoption, Miscarriage/Infant Loss, Death/Bereavement, Getting Married, Children Getting Married Locally, Divorce/Separation,* and *Aging Parents/Retirement/Move-In/Deployment*) have been extracted into their own standalone companion draft:

* **Standalone Companion Guide:** [`docs/life_events_ministering_playbook.md`](life_events_ministering_playbook.md) — ready to float with the Stake Relief Society Presidency as a Phase 2 co-owned ministering resource without bloating the Emergency Operations Plan.

---

### 8.3 Bulk Food Storage Reference: Official Home Storage Center Order Form → *Status: Live in Tab 6 & Tab 9 (P0); Add to Tab 8 Q1 (P2.2)*

**Recommendation:** Everywhere the plan references storing **longer-term bulk food** (30-year #10 cans: wheat, white rice, oats, dry beans, potato flakes, apple slices, dry milk), explicitly separate the two co-located services at **142 W Medical Dr, Saratoga Springs, UT 84045 • (801) 436-8205** and link directly to the hard-to-find official Order Form PDFs:

* **1. Home Storage Center (Open to ALL Families & Community at Cost):**
  * **Official U.S. Order Form PDF (English — Direct Link):** [homestoragecenters.churchofjesuschrist.org/pdf/US_en.pdf](https://homestoragecenters.churchofjesuschrist.org/pdf/US_en.pdf)
  * **Formulario de pedido EE. UU. PDF (Español — for SN-8 Spanish-speaking households):** [homestoragecenters.churchofjesuschrist.org/pdf/US_es.pdf](https://homestoragecenters.churchofjesuschrist.org/pdf/US_es.pdf)
  * **Official Prices, Locations & Hours:** [churchofjesuschrist.org/topics/food-storage/home-storage-center-locations-and-prices](https://www.churchofjesuschrist.org/topics/food-storage/home-storage-center-locations-and-prices)
  * **Online Catalog (Ship-to-Home):** [store.ChurchofJesusChrist.org](https://store.churchofjesuschrist.org) *(Food Storage section)*
  * **Key Visitor Note:** West of Jordan River (adjacent to Deseret Industries at `104 W Medical Dr`). Accepts **debit/credit cards only** (no AmEx, cash, or checks). Call `(801) 436-8205` or check online for current volunteer-staffed hours.
* **2. Bishops' Storehouse (Same Address — Confidential Welfare Aid via Bishop's Order, `GH 22.6.1`):**
  * For households experiencing genuine temporal need (job loss, fire, protracted illness, or disaster) via a confidential **Bishop's Order** prepared with the Ward RS or EQ President (`GH 22.6.1–22.6.2`).
* **Implementation Status:** Already live in `stake_leadership_presentation.html` across Tab 6 Directory and Tab 9 Step 2 & Step 8 (**P0**); remaining minor follow-up is adding the direct PDF link to **Tab 8 Q1 Roadmap** (**P2.2**).
