"""
Phase Definitions and Debate Task Configurations for Pages 5 to 10 in Sequence.
Each phase maps to a specific worksheet in the Church Emergency Preparedness Guide.
"""

PHASES = {
    "page5": {
        "title": "Page 5: Disaster Review Matrix",
        "worksheet_file": "worksheets/page_05_disaster_review.md",
        "description": "Identify and evaluate likely disasters for the 1-mile radius around 368 W Aspen Hills Blvd, Saratoga Springs, UT 84045 against all 11 disruption categories, tally scores, and establish prioritization.",
        "prompt_task": """Debate and fill out Page 5 (Disaster Review Worksheet).
Scope: 1.0-mile radius around 368 W Aspen Hills Blvd, Saratoga Springs, UT 84045.
Tasks:
1. Debate the top 6 most probable and high-impact disasters specific to this location (Earthquake, WUI Wildfire, Severe Winter Blizzard & Grid Freeze, High Windstorms, Hazmat on Redwood Rd, and Culinary Water Contamination).
2. For each disaster, assess which of the 11 disruptions will occur:
   - Food, Drinking Water, and Cooking
   - Physical Safety
   - Shelter and Clothing
   - Church Meetinghouses, Facilities, and Property
   - Communication
   - Emotional and Spiritual Well-Being
   - Heating and Cooling
   - Medical Services
   - Power Sources
   - Sewer and Water
   - Transportation and Fuel Supply
3. Calculate disruption totals per disaster and column totals per disruption category.
4. Establish which disruptions must be prioritized for planning."""
    },
    "page6a": {
        "title": "Page 6A: Planning for Disruptions — Major Earthquake",
        "worksheet_file": "worksheets/page_06a_disruptions_earthquake.md",
        "description": "Disruption planning for Wasatch Fault M7.0+ earthquake across Short-Term (0-72h), Mid-Term (1-2w), and Long-Term (2+m).",
        "prompt_task": """Debate and fill out Page 6A (Planning for Disruptions: Major Earthquake).
Scenario: Magnitude 7.0+ earthquake along the Wasatch Fault Zone / Utah Lake fault. Liquefaction along Utah Lake shore, ruptured gas mains, water mains fractured, bridge access across Jordan River to Lehi/I-15 compromised.
Tasks:
1. Debate Short-Term Needs (0–72 Hours): Immediate life-safety, gas shut-offs, building safety check of 368 W Aspen Hills Blvd, medical triage at Shay Park, emergency sanitation without flushing, member accounting via ministering network.
2. Debate Mid-Term Needs (1–2 Weeks): Potable water distribution from Lindon Bishops' Storehouse, communal outdoor cooking, host-family billeting for red-tagged homes, debris clearance with chainsaws/generators.
3. Debate Long-Term Needs (2+ Months): Structural reconstruction, FEMA/Church welfare aid, trauma counseling, financial recovery."""
    },
    "page6b": {
        "title": "Page 6B: Planning for Disruptions — WUI Wildfire",
        "worksheet_file": "worksheets/page_06b_disruptions_wildfire.md",
        "description": "Disruption planning for Lake Mountain foothill wildfire rapidly threatening Aspen Hills and Harvest Hills subdivisions.",
        "prompt_task": """Debate and fill out Page 6B (Planning for Disruptions: Wildland-Urban Interface Wildfire).
Scenario: Fast-moving wildfire on Lake Mountain slopes driven by 45+ mph downslope winds toward Aspen Hills Blvd and Redwood Road. Mandatory evacuation order issued for 3,000+ homes.
Tasks:
1. Debate Short-Term Needs (0–72 Hours): Rapid evacuation door-knocking, wheelchair/special needs transport, managing traffic gridlock on Redwood Road (SR-68), N95 smoke respirators, off-site member accountability.
2. Debate Mid-Term Needs (1–2 Weeks): Host-family sheltering in neighboring stakes (Lehi/American Fork), emergency clothing/food from Lindon Bishops' Storehouse, police perimeter re-entry passes, indoor smoke remediation.
3. Debate Long-Term Needs (2+ Months): Post-fire alluvial fan debris flow / flash flood sandbagging at Shay Park gulch, defensible space enforcement, total loss rebuilding support."""
    },
    "page6c": {
        "title": "Page 6C: Planning for Disruptions — Winter Blizzard & Grid Freeze",
        "worksheet_file": "worksheets/page_06c_disruptions_winter_storm_freeze.md",
        "description": "Disruption planning for sub-zero blizzard and multi-day electric grid failure causing home freezing and burst pipes.",
        "prompt_task": """Debate and fill out Page 6C (Planning for Disruptions: Severe Winter Blizzard & Grid Freeze).
Scenario: Sub-zero blizzard (-10°F to 5°F) with 4-day electrical blackout across northern Utah County. Home forced-air furnaces shut down; culinary pipes freezing in exterior walls.
Tasks:
1. Debate Short-Term Needs (0–72 Hours): Life-safety warmth, room consolidation, carbon monoxide poisoning prevention (banning indoor grills/generators), battery power for oxygen concentrators, frozen pipe trickle instructions, meetinghouse warming shelter status.
2. Debate Mid-Term Needs (1–2 Weeks): Quorum plumbing triage (PEX/SharkBite repairs) as thaw begins, neighborhood snowplowing with 4WD trucks, hot communal meals via outdoor propane burners.
3. Debate Long-Term Needs (2+ Months): Basement flood damage extraction, mold prevention, fast offering deductible assistance, home winterization hardening."""
    },
    "page6d": {
        "title": "Page 6D: Planning for Disruptions — High Windstorm & Microburst",
        "worksheet_file": "worksheets/page_06d_disruptions_high_windstorm.md",
        "description": "Disruption planning for severe 70-90+ mph winds damaging roofs, blowing fences and trampolines, and downing power lines.",
        "prompt_task": """Debate and fill out Page 6D (Planning for Disruptions: High Windstorm & Microburst).
Scenario: Severe gap/canyon wind event with sustained 50 mph winds and gusts to 85 mph. Widespread shingle loss, flipped trampolines into power lines, downed live wires, impassable streets.
Tasks:
1. Debate Short-Term Needs (0–72 Hours): Strict indoor shelter order away from windows, downed live wire cordons (Rocky Mountain Power 1-877-508-5088), emergency roof tarping with furring strips once winds drop below 25 mph, clearing fallen trees from Aspen Hills Blvd.
2. Debate Mid-Term Needs (1–2 Weeks): Debris haul-off dumpsters, collective fence-rebuilding work parties across ward boundaries, school and church facility roof inspections.
3. Debate Long-Term Needs (2+ Months): Permanent roofing contractor vetting, trampoline screw-anchor campaign, municipal tree-trimming near overhead power drops."""
    },
    "page6e": {
        "title": "Page 6E: Planning for Disruptions — Hazmat Plume Spill on SR-68",
        "worksheet_file": "worksheets/page_06e_disruptions_hazmat_spill.md",
        "description": "Disruption planning for commercial tanker hazardous chemical spill on Redwood Road requiring hard shelter-in-place.",
        "prompt_task": """Debate and fill out Page 6E (Planning for Disruptions: Hazmat Spill on SR-68 / Redwood Road).
Scenario: Commercial chemical tanker truck overturns on Redwood Road near Aspen Hills Blvd, releasing a dense toxic chlorine/ammonia vapor cloud. Total road closure; wind blowing plume west into subdivisions.
Tasks:
1. Debate Short-Term Needs (0–72 Hours): Immediate emergency shelter-in-place directive (DO NOT evacuate into toxic vapor), sealing doors/windows with plastic sheeting and duct tape, turning off all HVAC/blowers, coordinating with Riverview Elementary (273 W Aspen Hills Blvd) lockdown to prevent frantic parents driving into plume.
2. Debate Mid-Term Needs (1–2 Weeks): Post-clearance home aeration, replacing HVAC furnace filters, medical follow-up for chemical eye/lung irritation with Utah Poison Control (1-800-222-1222).
3. Debate Long-Term Needs (2+ Months): Neighborhood shelter-in-place drills, advocacy on hazardous cargo routes with City/MAG."""
    },
    "page6f": {
        "title": "Page 6F: Planning for Disruptions — Culinary Water Failure",
        "worksheet_file": "worksheets/page_06f_disruptions_water_infrastructure_failure.md",
        "description": "Disruption planning for culinary water main rupture and pressurized irrigation cross-contamination.",
        "prompt_task": """Debate and fill out Page 6F (Planning for Disruptions: Culinary Water Infrastructure Failure & Contamination).
Scenario: Major transmission main rupture or booster pump outage leaves hillside zones without water; untreated secondary irrigation water backflows into culinary pipes. City-wide Boil Water Order issued.
Tasks:
1. Debate Short-Term Needs (0–72 Hours): Mandatory 3-minute rolling boil notice (4,500 ft altitude), strict prohibition against using secondary irrigation water for consumption, immediate water deliveries to infants and elderly, tapping household 55-gallon storage drums.
2. Debate Mid-Term Needs (1–2 Weeks): Staging bulk water trailer / pallets from Lindon Bishops' Storehouse (801-785-0995) at 368 W Aspen Hills Blvd, handwashing sanitation stations to prevent gastrointestinal outbreaks, line flushing support.
3. Debate Long-Term Needs (2+ Months): Home backflow check valve inspections, ward bulk purchase of food-grade 55-gallon water drums and preserver concentrate."""
    },
    "page7": {
        "title": "Page 7: Critical Information — Members with Special Needs",
        "worksheet_file": "worksheets/page_07_special_needs.md",
        "description": "Confidential protocol and standardized tracking categories for members with special medical, mobility, and dependency needs.",
        "prompt_task": """Debate and fill out Page 7 (Critical Information: Members with Special Needs).
Context: Church privacy rules and medical confidentiality prohibit publishing real PII online.
Tasks:
1. Debate the 8 essential vulnerability triage categories for this neighborhood (Electrical life support/oxygen, refrigerated insulin, non-ambulatory wheelchairs, dialysis, seniors living alone, autism/sensory, infant formula dependency, language barriers).
2. Debate the standard operating response protocol for each category during the initial 0-72 hours.
3. Establish the confidential maintenance and update process between the Bishopric, Relief Society President, and Elders Quorum President."""
    },
    "page8": {
        "title": "Page 8: Critical Information — Equipment, Skills & Comms",
        "worksheet_file": "worksheets/page_08_equipment_skills_comms.md",
        "description": "Verified communication frequencies, ham repeaters, and inventory of critical equipment, medical skills, and emergency machinery.",
        "prompt_task": """Debate and fill out Page 8 (Critical Information: Equipment, Skills & Communication Resources).
Scope: 1.0-mile radius around 368 W Aspen Hills Blvd, Saratoga Springs, UT 84045.
Tasks:
1. Debate and verify the exact radio communications plan:
   - Utah County ARES (UCARES) 147.340 MHz (+0.6 MHz, PL 100.0 Hz)
   - Lake Mountain North 145.230 MHz (-0.6 MHz, PL 131.8 Hz)
   - Simplex 146.520 MHz and 147.340 MHz
   - FRS Channel assignments (Ch 1 Calling, Ch 3 Search/Evacuation, Ch 5 Medical/Relief Society)
2. Debate the required equipment and skill roster: emergency physicians, nurses, EMTs, licensed ham operators, CERT teams, dual-fuel generators, chainsaws, snowplows, plumbing isolation gear, and mass cooking setups."""
    },
    "page9": {
        "title": "Page 9: Critical Information — Services & Directory",
        "worksheet_file": "worksheets/page_09_services_directory.md",
        "description": "Authoritative directory of verified local emergency, municipal, medical, utility, and Church welfare resources.",
        "prompt_task": """Debate and fill out Page 9 (Critical Information: Services).
Strict Requirement: Only verified, authentic phone numbers, addresses, and organizations.
Tasks:
1. Verify and document all essential public safety agencies:
   - Saratoga Springs North Fire Station (995 W 1200 N, 801-766-6505)
   - Saratoga Springs Police Dept (367 S Saratoga Rd, Dispatch 801-798-5600, Admin 801-766-6503)
   - Saratoga Springs Emergency Management (319 S Saratoga Rd, 801-766-9793 Ext. 219)
   - Saratoga Springs Public Works After-Hours Water Emergency (801-404-2468)
2. Document nearest hospitals:
   - Holy Cross Hospital Mountain Point Lehi (ER: 385-345-3000)
   - Primary Children's Hospital Miller Family Campus Lehi (ER: 385-531-1200)
   - American Fork Hospital (ER: 801-855-4600)
3. Document utilities, schools, and Church resources:
   - Rocky Mountain Power (1-877-508-5088)
   - Dominion Energy (1-800-767-1689)
   - Utah Poison Control (1-800-222-1222)
   - Lindon Bishops' Storehouse (940 W Center St, Lindon, 801-785-0995)
   - Riverview Elementary School (273 W Aspen Hills Blvd, 385-579-7355)
   - Stake Center (368 W Aspen Hills Blvd, 385-374-0181)
   - Shay Park (516 W Aspen Hills Blvd)
4. Assign specific ward/stake council leaders to contact each entity prior to emergencies."""
    },
    "page10": {
        "title": "Page 10: Actions and Assignments Matrix",
        "worksheet_file": "worksheets/page_10_actions_assignments.md",
        "description": "Gap analysis, council callings responsible, target due dates, and concrete completion metrics.",
        "prompt_task": """Debate and fill out Page 10 (Actions and Assignments).
Scope: Ward/Stake Council implementation for 368 W Aspen Hills Blvd, Saratoga Springs, UT 84045.
Tasks:
1. Conduct a rigorous gap analysis based on Pages 5 through 9.
2. Formulate 10 high-priority operational assignments:
   - Joint reunification protocol with Riverview Elementary (273 W Aspen Hills Blvd)
   - Confidential special needs intake and lithium battery allocation
   - Meetinghouse seismic gas shutoff valve & generator transfer switch evaluation
   - Laminated emergency radio frequency cards and monthly FRS/HAM net
   - Gas meter shut-off tool distribution drive
   - Geographic block captain mapping (12 zones in 1-mile radius)
   - Emergency twin-bucket toilet assembly workshop
   - Secondary irrigation backflow inspection and water drum drive
   - Community CERT sponsorship with Saratoga Springs City EOC
   - Annual multi-ward tabletop evacuation simulation
3. Assign each action to a specific council calling (Bishopric, EQ, RS, Primary, Specialists) with firm 30-, 45-, 60-, 90-, 120-day due dates."""
    }
}
