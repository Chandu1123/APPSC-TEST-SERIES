#!/usr/bin/env python3
"""
APPSC Group 1 & Group 2 — Authentic Exam-Standard Current Affairs & Static GS Compiler
======================================================================================
Generates 40 individually crafted, high-rigor APPSC Group-I and Group-II Main/Prelims
standard Multiple Choice Questions (MCQs) covering National, International, Science & Tech,
Union & AP Budget/Economic Survey, Supreme Court Constitutional Rulings, Defence, Environment,
Indices/Reports, and Andhra Pradesh State Current Affairs seamlessly integrated with Static GS.
"""

import argparse
import datetime
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "tests_db.json")

AUTHENTIC_CA_EXAM_QUESTIONS = [
    {
        "subject": "Indian Polity & Constitution",
        "topic": "Sixteenth Finance Commission & Constitutional Fiscal Federalism",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to the Sixteenth Finance Commission of India and constitutional provisions governing fiscal federalism, consider the following statements:\n"
            "1. The Sixteenth Finance Commission, chaired by Dr. Arvind Panagariya, was constituted by the President under Article 280 of the Constitution to make recommendations for the five-year award period 2026–2031.\n"
            "2. Under Article 275 of the Constitution, the Commission recommends principles governing Grants-in-Aid of the revenues of States out of the Consolidated Fund of India.\n"
            "3. Recommendations made by the Finance Commission regarding vertical tax devolution under Article 270 are legally binding on the Union Government and cannot be modified by Parliament.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: The 16th Finance Commission is chaired by Dr. Arvind Panagariya (with Ritvik Ranjanam Pandey as Secretary) for the award period April 1, 2026 to March 31, 2031.\n"
            "• Statement 2 is correct: Article 275 provides for Statutory Grants-in-Aid to States on the recommendation of the Finance Commission.\n"
            "• Statement 3 is incorrect: The recommendations of the Finance Commission under Article 280 are advisory in nature and not legally binding on the Union Government, though by convention its devolution formula is accepted."
        ),
        "source": "Sixteenth Finance Commission Terms of Reference & Constitution of India (Articles 270, 275, 280)"
    },
    {
        "subject": "Indian Polity & Constitution",
        "topic": "Supreme Court Constitution Bench on Sub-Classification of Scheduled Castes",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "In the context of the Supreme Court's 7-Judge Constitution Bench judgment in 'State of Punjab vs. Davinder Singh' regarding sub-classification within Scheduled Castes, consider the following statements:\n"
            "1. The Bench overruled the 2004 'E.V. Chinnaiah vs. State of Andhra Pradesh' judgment and held that Scheduled Castes do not constitute a homogeneous class for all purposes.\n"
            "2. State Governments are permitted to sub-classify Scheduled Castes under Articles 15(4) and 16(4) based on quantifiable empirical data of inter-se backwardness and inadequate representation in state services.\n"
            "3. The judgment empowers State Legislatures to directly add or delete castes from the Presidential List of Scheduled Castes under Article 341(2) without parliamentary legislation.\n\n"
            "How many of the statements given above are correct?"
        ),
        "options": [
            "Only one statement",
            "Only two statements",
            "All three statements",
            "None of the statements"
        ],
        "correct_index": 1,
        "explanation": (
            "Only two statements (Statements 1 and 2) are correct; Statement 3 is incorrect.\n"
            "• Statements 1 and 2 are correct: The 6:1 majority 7-Judge Constitution Bench overruled E.V. Chinnaiah (2004) and upheld states' power to create sub-quotas within the SC reservation quota based on empirical data of inter-se backwardness.\n"
            "• Statement 3 is incorrect: Under Article 341(2), only Parliament by law can include in or exclude from the Presidential List any caste, race, or tribe. Sub-classification for reservation does not amount to altering the Presidential List."
        ),
        "source": "Supreme Court 7-Judge Constitution Bench Ruling & Article 341 of Constitution"
    },
    {
        "subject": "Indian & AP Economy",
        "topic": "Andhra Pradesh Socio-Economic Survey & Swarna Andhra @ 2047 Vision",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "Consider the following statements regarding the 'Swarna Andhra @ 2047' Vision and the structure of Andhra Pradesh's economy:\n"
            "1. The 'P4' governance framework introduced under Swarna Andhra @ 2047 stands for 'Public-Private-People Partnership' aimed at eradicating extreme poverty by linking affluent mentors/institutions with the bottom 20% households.\n"
            "2. Agriculture and Allied Sectors (comprising Crop Husbandry, Livestock, Forestry, and Fisheries/Aquaculture) contribute more than 30% to Andhra Pradesh's Gross State Value Added (GSVA), which is significantly higher than the all-India average.\n"
            "3. In Andhra Pradesh's GSVA composition within the primary sector, the economic value output of the Horticulture and Livestock sub-sectors is lower than that of traditional foodgrain cereals.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: The P4 (Public-Private-People Partnership) model is the flagship zero-poverty initiative under Swarna Andhra @ 2047.\n"
            "• Statement 2 is correct: Agriculture & Allied sectors account for ~34–35% of Andhra Pradesh's GSVA (compared to ~18% nationally).\n"
            "• Statement 3 is incorrect: Within AP's primary sector, Horticulture, Livestock, and Fisheries/Aquaculture are the dominant value drivers and far exceed traditional foodgrain crops in GSVA contribution."
        ),
        "source": "AP Socio-Economic Survey & Swarna Andhra @ 2047 Vision Document"
    },
    {
        "subject": "Geography of India & AP",
        "topic": "Polavaram National Irrigation Project & Godavari Basin",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to the Polavaram Multipurpose National Irrigation Project and the Godavari river system in Andhra Pradesh, consider the following statements:\n"
            "1. Section 90 of the Andhra Pradesh Reorganization Act, 2014 explicitly declared the Polavaram Irrigation Project to be a National Project, with the Union Government bearing 100% of the irrigation component cost.\n"
            "2. Phase-I operational storage of the Polavaram reservoir is designed at the +41.15 metres contour level, whereas the Full Reservoir Level (FRL) of the project is +45.72 metres.\n"
            "3. The Sabari River, a major right-bank tributary of the Godavari originating in the Western Ghats, merges with the Godavari downstream of the Dowleswaram Cotton Barrage.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 only",
            "1 and 2 only",
            "2 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 1,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: Section 90 of the AP Reorganization Act, 2014 declared Polavaram a National Project.\n"
            "• Statement 2 is correct: Phase-I water storage is pegged at the +41.15m contour to enable gravity flow via the Right and Left Main Canals, while the Full Reservoir Level (FRL) is +45.72m (+150 feet).\n"
            "• Statement 3 is incorrect: The Sabari River is a LEFT-bank tributary of the Godavari (originating in the Sinkaram hills of the Eastern Ghats in Odisha) and joins the Godavari at Kunavaram, upstream of Polavaram."
        ),
        "source": "Ministry of Jal Shakti & Section 90 of AP Reorganization Act, 2014"
    },
    {
        "subject": "AP History & Reorganization",
        "topic": "National Industrial Corridor Nodes in Andhra Pradesh & Schedule XIII",
        "question_type": "Pair Matching",
        "question": (
            "Consider the following industrial nodes in Andhra Pradesh and the National Industrial Corridors under which they are being developed:\n"
            "1. Kopparthy Industrial Node (YSR Kadapa District) — Visakhapatnam–Chennai Industrial Corridor (VCIC)\n"
            "2. Orvakal Industrial Node (Kurnool District) — Hyderabad–Bengaluru Industrial Corridor (HBIC)\n"
            "3. Krishnapatnam Industrial Node (SPSR Nellore District) — Chennai–Bengaluru Industrial Corridor (CBIC)\n\n"
            "How many of the above pairs are correctly matched?"
        ),
        "options": [
            "Only one pair",
            "Only two pairs",
            "All three pairs",
            "None of the pairs"
        ],
        "correct_index": 2,
        "explanation": (
            "All three pairs are correctly matched.\n"
            "• Andhra Pradesh is the only state in India where three National Industrial Corridors converge:\n"
            "  1. Kopparthy (YSR Kadapa district, 2,596 acres) is developed under the Visakhapatnam–Chennai Industrial Corridor (VCIC).\n"
            "  2. Orvakal (Kurnool district, 2,621 acres) is developed under the Hyderabad–Bengaluru Industrial Corridor (HBIC).\n"
            "  3. Krishnapatnam (SPSR Nellore district) is developed under the Chennai–Bengaluru Industrial Corridor (CBIC).\n"
            "• Schedule XIII of the AP Reorganization Act, 2014 mandates Central support for industrial corridors in the successor state of Andhra Pradesh."
        ),
        "source": "NICDC / DPIIT Cabinet Approvals & Schedule XIII of AP Reorganization Act, 2014"
    },
    {
        "subject": "Science, Tech & Environment",
        "topic": "NASA–ISRO Synthetic Aperture Radar (NISAR) Mission",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to the NASA–ISRO Synthetic Aperture Radar (NISAR) satellite mission, consider the following statements:\n"
            "1. NISAR is the first satellite mission to use dual-frequency Synthetic Aperture Radar on a single platform, combining an L-band (24 cm wavelength) radar provided by NASA/JPL and an S-band (12 cm wavelength) radar developed by ISRO.\n"
            "2. It is launched into a Geostationary Transfer Orbit (GTO) at an altitude of 35,786 km above the equator using ISRO's PSLV-XL launch vehicle.\n"
            "3. Using SweepSAR technique and repeat-pass radar interferometry, NISAR maps global land and ice-sheet deformation every 12 days under all weather and day-night conditions.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "1 and 3 only",
            "2 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 1,
        "explanation": (
            "Statements 1 and 3 are correct; Statement 2 is incorrect.\n"
            "• Statement 1 is correct: NASA's JPL provides the L-band SAR and 12m deployable mesh reflector, while ISRO's Space Applications Centre (SAC) provides the S-band SAR and I-3K spacecraft bus.\n"
            "• Statement 2 is incorrect: NISAR is placed into a polar Sun-Synchronous Dawn-Dusk Low Earth Orbit (~747 km altitude) by ISRO's GSLV Mk-II (GSLV-F16), not into Geostationary Orbit by PSLV.\n"
            "• Statement 3 is correct: Microwave radar penetrates clouds and vegetation canopy day and night, imaging the entire globe on a 12-day cycle."
        ),
        "source": "ISRO–NASA NISAR Technical Dossier"
    },
    {
        "subject": "Indian & AP Economy",
        "topic": "Union Budget Fiscal Glide Path & RBI Monetary Policy Committee",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "Examine the following statements regarding India's fiscal consolidation framework and the Reserve Bank of India's Monetary Policy Committee (MPC):\n"
            "1. Under the Union Government's revised fiscal consolidation roadmap, from FY 2026–27 onwards the operational medium-term fiscal anchor shifts toward keeping the fiscal deficit each year such that Central Government Debt as a percentage of GDP stays on a declining path.\n"
            "2. Under Section 45ZB of the RBI Act, 1934, the Monetary Policy Committee comprises six members, where the RBI Governor possesses a second or casting vote in the event of an equality of votes.\n"
            "3. The Standing Deposit Facility (SDF), which serves as the floor of the Liquidity Adjustment Facility (LAF) corridor, requires the Reserve Bank of India to pledge equivalent central government dated securities as collateral to commercial banks.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: After bringing the Union Fiscal Deficit below 4.5% of GDP, the medium-term fiscal anchor from FY 2026–27 focuses on a declining Central Government Debt-to-GDP ratio.\n"
            "• Statement 2 is correct: The 6-member MPC (3 from RBI, 3 nominated by Central Govt) has a quorum of 4 members, and the RBI Governor has a casting vote in case of a tie.\n"
            "• Statement 3 is incorrect: Under Section 17 of the RBI Act (amended in 2018), the Standing Deposit Facility (SDF) is a collateral-free liquidity absorption tool—RBI does NOT need to provide government securities as collateral."
        ),
        "source": "Union Budget FRBM Statement & Reserve Bank of India Act, 1934"
    },
    {
        "subject": "AP History & Reorganization",
        "topic": "Classical Languages of India & Early Telugu Epigraphy",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to the Classical Languages of India and the epigraphical history of Andhra Pradesh, consider the following statements:\n"
            "1. Following the inclusion of Marathi, Pali, Prakrit, Assamese, and Bengali by the Union Cabinet, the total number of officially recognized Classical Languages in India stands at eleven.\n"
            "2. The Kalamalla Inscription (c. 575 CE) in YSR Kadapa district, issued by the Renati Chola ruler Dhananjaya Erikal Mutturaju, is recognized as the earliest extant complete prose inscription in the Telugu language.\n"
            "3. The Centre of Excellence for Studies in Classical Telugu (CESCT), functioning under the Central Institute of Indian Languages (CIIL), has its permanent campus located in Visakhapatnam.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: The 11 Classical Languages are Tamil (2004), Sanskrit (2005), Kannada (2008), Telugu (2008), Malayalam (2013), Odia (2014), Marathi, Pali, Prakrit, Assamese, and Bengali.\n"
            "• Statement 2 is correct: The Kalamalla inscription of Erikal Mutturaju Dhananjaya (Renati Cholas) is the earliest complete Telugu inscription.\n"
            "• Statement 3 is incorrect: The Centre of Excellence for Studies in Classical Telugu (CESCT) was shifted from Mysuru and established at Venkatachalam in SPSR Nellore district (not Visakhapatnam)."
        ),
        "source": "Ministry of Culture Notification & Epigraphia Andhrica"
    },
    {
        "subject": "Indian Society & Welfare",
        "topic": "PM-JANMAN, Dharti Aaba Abhiyan & PVTGs of Andhra Pradesh",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "Consider the following statements regarding tribal welfare missions and Particularly Vulnerable Tribal Groups (PVTGs) in Andhra Pradesh:\n"
            "1. The Pradhan Mantri Janjati Adivasi Nyaya Maha Abhiyan (PM-JANMAN) targets socio-economic saturation of 75 PVTGs across 18 States and the UT of Andaman & Nicobar Islands through 11 critical interventions implemented by 9 Ministries.\n"
            "2. Out of the tribal communities residing in Andhra Pradesh, six groups—Chenchu, Gadaba, Khond, Konda Reddi, Konda Savara, and Porja—are officially notified as PVTGs (including their sub-groups).\n"
            "3. Scheduled Areas in Andhra Pradesh are administered under the Sixth Schedule of the Constitution through Autonomous District Councils.\n\n"
            "How many of the statements given above are correct?"
        ),
        "options": [
            "Only one statement",
            "Only two statements",
            "All three statements",
            "None of the statements"
        ],
        "correct_index": 1,
        "explanation": (
            "Only two statements (Statements 1 and 2) are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: PM-JANMAN (outlay Rs. 24,104 crore) focuses specifically on 75 PVTGs across 18 States and A&N Islands via 11 interventions of 9 Ministries, complemented by the broader Dharti Aaba Janjatiya Gram Utkarsh Abhiyan (Rs. 79,156 crore across ~63,000 villages).\n"
            "• Statement 2 is correct: The notified PVTGs of Andhra Pradesh are Chenchu, Bodo Gadaba/Gutob Gadaba, Dongria Khond/Kutia Khond, Konda Reddi, Konda Savara, and Bondo Porja/Khodu Porja/Parengi Porja.\n"
            "• Statement 3 is incorrect: Scheduled Areas in Andhra Pradesh are governed under the FIFTH Schedule (Article 244(1)) and the PESA Act, 1996 (not the Sixth Schedule, which applies only to Assam, Meghalaya, Tripura, and Mizoram)."
        ),
        "source": "Ministry of Tribal Affairs Annual Report & Fifth Schedule of the Constitution"
    },
    {
        "subject": "Science, Tech & Environment",
        "topic": "National Green Hydrogen Mission & AP Integrated Clean Energy Policy",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to the National Green Hydrogen Mission and Andhra Pradesh's clean energy initiatives, consider the following statements:\n"
            "1. Under the official Green Hydrogen Standard notified by the Ministry of New and Renewable Energy (MNRE), hydrogen produced via electrolysis or biomass conversion qualifies as 'Green Hydrogen' only if non-biogenic greenhouse gas emissions do not exceed 2 kg of CO2 equivalent per kg of H2.\n"
            "2. The SIGHT (Strategic Interventions for Green Hydrogen Transition) programme provides financial incentives for both indigenous electrolyser manufacturing and green hydrogen production.\n"
            "3. India's largest integrated Green Hydrogen Hub by NTPC Green Energy Limited is being developed at Pudimadaka in Anakapalli district on the Andhra Pradesh coast.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 3,
        "explanation": (
            "All three statements (1, 2 and 3) are correct.\n"
            "• Statement 1 is correct: MNRE's Green Hydrogen Standard defines Green Hydrogen as having well-to-gate emissions of not more than 2 kg CO2 equivalent per kg H2 averaged over 12 months.\n"
            "• Statement 2 is correct: SIGHT (outlay Rs. 17,490 crore out of Rs. 19,744 crore total mission outlay) funds two components: Component-I (Electrolyser manufacturing) and Component-II (Green Hydrogen production).\n"
            "• Statement 3 is correct: The NTPC Green Hydrogen Hub is located at Pudimadaka in Anakapalli district (near Visakhapatnam), a flagship project under the AP Integrated Clean Energy Policy."
        ),
        "source": "MNRE National Green Hydrogen Mission & AP Integrated Clean Energy Policy"
    },
    {
        "subject": "Indian Polity & Constitution",
        "topic": "Bharatiya Nyaya Sanhita (BNS), BNSS, BSA & Constitutional Protections",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "Consider the following statements regarding the three criminal laws—Bharatiya Nyaya Sanhita (BNS), Bharatiya Nagarik Suraksha Sanhita (BNSS), and Bharatiya Sakshya Adhiniyam (BSA):\n"
            "1. Under the Bharatiya Nagarik Suraksha Sanhita (BNSS), the visit of a forensic expert to the crime scene to collect forensic evidence is mandatory for all offences punishable with imprisonment of seven years or more.\n"
            "2. The Bharatiya Nyaya Sanhita (BNS) introduces 'Community Service' as a statutory form of punishment for minor offences such as petty theft and public intoxication.\n"
            "3. Under Article 20(1) of the Constitution, substantive criminal offences newly created under the BNS apply retrospectively to acts committed prior to July 1, 2024.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: Section 176(3) of the BNSS mandates compulsory forensic crime-scene investigation for offences punishable with 7 years or more imprisonment.\n"
            "• Statement 2 is correct: Section 4 of the BNS adds Community Service as one of the six statutory punishments.\n"
            "• Statement 3 is incorrect: Article 20(1) prohibits ex-post-facto criminal legislation; hence offences committed before July 1, 2024 continue to be governed by the erstwhile IPC, 1860."
        ),
        "source": "Ministry of Home Affairs Gazette & Article 20 of the Constitution"
    },
    {
        "subject": "Science, Tech & Environment",
        "topic": "ISRO Space Roadmap: Gaganyaan, Chandrayaan-4 & Bharatiya Antariksh Station",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to ISRO's space exploration missions approved by the Union Cabinet, consider the following statements:\n"
            "1. The Human-Rated LVM3 (HLVM3) launch vehicle used for the Gaganyaan mission employs a Crew Escape System (CES) powered by quick-acting solid motors and uses the CE-20 cryogenic engine in its upper stage.\n"
            "2. The Chandrayaan-4 mission is configured as a lunar sample-return mission featuring five spacecraft modules (Propulsion, Descender, Ascender, Transfer, and Re-entry modules) launched across two separate LVM3 rockets.\n"
            "3. The Venus Orbiter Mission (VOM) and the first module of the Bharatiya Antariksh Station (BAS-1) are designed to operate at the Sun–Earth Lagrange Point L2.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: HLVM3 consists of S200 solid boosters, L110 liquid core stage, C25 cryogenic upper stage (CE-20 engine), and an active Crew Escape System.\n"
            "• Statement 2 is correct: Chandrayaan-4 comprises 5 modules stacked in two composites launched by two LVM3 vehicles, which dock in orbit to bring lunar samples back to Earth.\n"
            "• Statement 3 is incorrect: Bharatiya Antariksh Station (BAS-1) will operate in Low Earth Orbit (~400 km altitude), while the Venus Orbiter Mission will orbit planet Venus (not Sun-Earth L2)."
        ),
        "source": "Department of Space / ISRO Cabinet Approvals"
    },
    {
        "subject": "Indian & AP Economy",
        "topic": "National Mission on Natural Farming & APCNF (RySS)",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "In the context of the National Mission on Natural Farming (NMNF) and the Andhra Pradesh Community Managed Natural Farming (APCNF) programme, examine the following statements:\n"
            "1. The APCNF programme implemented by Rythu Sadhikara Samstha (RySS) of the Government of Andhra Pradesh was awarded the prestigious Gulbenkian Prize for Humanity for its contribution to climate-resilient food systems.\n"
            "2. In the four core pillars of Indian Natural Farming, 'Whapasa' refers to the microbial seed coating prepared from indigenous cow dung, cow urine, and lime, whereas 'Beejamrit' refers to maintaining a 50:50 air-and-moisture balance in soil pores.\n"
            "3. 'Pre-Monsoon Dry Sowing' (PMDS), pioneered in drought-prone districts of Andhra Pradesh under APCNF, utilizes multi-species green cover crops and atmospheric dew/pre-monsoon showers to enable 365 days of living roots in the soil.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "1 and 3 only",
            "2 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 1,
        "explanation": (
            "Statements 1 and 3 are correct; Statement 2 is incorrect (interchanged definitions).\n"
            "• Statement 1 is correct: APCNF (implemented by RySS) won the 2024 Gulbenkian Prize for Humanity.\n"
            "• Statement 2 is incorrect: 'Beejamrit' is the microbial seed treatment, whereas 'Whapasa' is the soil aeration condition where both air and water molecules are present in soil pores.\n"
            "• Statement 3 is correct: Pre-Monsoon Dry Sowing (PMDS / Navadhanya) is a signature scientific innovation of APCNF maintaining 365-day green cover."
        ),
        "source": "Ministry of Agriculture & Rythu Sadhikara Samstha (RySS), Govt. of AP"
    },
    {
        "subject": "Science, Tech & Environment",
        "topic": "BioE3 Policy, CAR-T Cell Therapy & Gene Editing",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to the 'BioE3 Policy' (Biotechnology for Economy, Environment and Employment) and recent biotherapeutic breakthroughs in India, consider the following statements:\n"
            "1. Formulated by the Department of Biotechnology (DBT), the BioE3 Policy establishes Bio-Artificial Intelligence (Bio-AI) Hubs and Biofoundries to scale high-performance biomanufacturing across six thematic sectors including smart proteins and carbon capture.\n"
            "2. 'NexCAR19', India's first indigenous Chimeric Antigen Receptor T-cell (CAR-T) therapy developed by IIT Bombay and Tata Memorial Centre (ImmunoACT), genetically modifies a patient's B-lymphocytes using bacterial plasmids to cure Type-1 Diabetes.\n"
            "3. In CRISPR-Cas9 genome editing, a single guide RNA (sgRNA) directs the Cas9 endonuclease enzyme to introduce a double-stranded break at a specific target sequence adjacent to a Protospacer Adjacent Motif (PAM).\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "1 and 3 only",
            "2 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 1,
        "explanation": (
            "Statements 1 and 3 are correct; Statement 2 is incorrect.\n"
            "• Statement 1 is correct: The BioE3 Policy drives sustainable biomanufacturing via Biofoundries and Bio-AI hubs across 6 thematic verticals.\n"
            "• Statement 2 is incorrect: NexCAR19 (Actalycabtagene autoleucel) modifies a patient's T-lymphocytes (not B-lymphocytes) to target the CD19 antigen on B-cell lymphomas and leukaemias (blood cancers, not Type-1 Diabetes).\n"
            "• Statement 3 is correct: CRISPR-Cas9 relies on guide RNA and a PAM sequence recognition site for targeted DNA cleavage."
        ),
        "source": "Department of Biotechnology (BioE3 Policy) & CDSCO"
    },
    {
        "subject": "Indian Society & Welfare",
        "topic": "Andhra Pradesh Welfare Schemes: NTR Bharosa, Talliki Vandanam, Annadata Sukhibhava & Deepam-2.0",
        "question_type": "Pair Matching",
        "question": (
            "Consider the following welfare schemes implemented by the Government of Andhra Pradesh and their core provisions:\n"
            "1. NTR Bharosa — Monthly social security pension of Rs. 4,000 for senior citizens/widows and Rs. 6,000 to Rs. 15,000 for categories of persons with disabilities.\n"
            "2. Annadata Sukhibhava — Annual financial assistance of Rs. 20,000 per eligible farmer family (inclusive of the Central PM-KISAN component).\n"
            "3. Deepam-2.0 — Provision of three free domestic LPG cylinder refills per year (one every four months) via Direct Benefit Transfer to eligible women beneficiaries.\n"
            "4. Talliki Vandanam — Financial assistance of Rs. 15,000 per annum restricted only to the eldest child in a family studying in Government colleges.\n\n"
            "How many of the above pairs are correctly matched?"
        ),
        "options": [
            "Only one pair",
            "Only two pairs",
            "Only three pairs",
            "All four pairs"
        ],
        "correct_index": 2,
        "explanation": (
            "Only three pairs (Pairs 1, 2, and 3) are correctly matched; Pair 4 is incorrect.\n"
            "• Pairs 1, 2, and 3 are correct: NTR Bharosa enhanced pensions to Rs. 4,000 (and Rs. 6,000/Rs. 15,000 for disabled/bedridden), Annadata Sukhibhava provides Rs. 20,000/year to farmers, and Deepam-2.0 provides 3 free LPG cylinders per year.\n"
            "• Pair 4 is incorrect: A defining feature of 'Talliki Vandanam' is that Rs. 15,000 per annum is provided for EVERY school-going child (Classes I to XII) in an eligible household without restricting the number of children in a family."
        ),
        "source": "Andhra Pradesh State Budget & Welfare Department G.O.s"
    },
    {
        "subject": "Science, Tech & Environment",
        "topic": "National Quantum Mission & One Nation One Subscription (ONOS)",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to the National Quantum Mission (NQM) and the 'One Nation One Subscription' (ONOS) initiative, consider the following statements:\n"
            "1. Under the National Quantum Mission (outlay Rs. 6,003.65 crore), four Thematic Hubs (T-Hubs) have been established at IISc Bengaluru, IIT Madras, IIT Bombay, and IIT Delhi focusing on Quantum Computing, Quantum Communication, Quantum Sensing & Metrology, and Quantum Materials & Devices respectively.\n"
            "2. The 'One Nation One Subscription' (ONOS) scheme is coordinated by the Information and Library Network (INFLIBNET), an autonomous Inter-University Centre of the University Grants Commission (UGC) headquartered at Gandhinagar.\n"
            "3. Under ONOS, access to international scholarly journals is restricted solely to Indian Institutes of Technology (IITs) and central CSIR laboratories, excluding state government universities.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: The 4 Thematic Hubs of the National Quantum Mission are hosted at IISc Bengaluru (Quantum Computing), IIT Madras with C-DOT (Quantum Communication), IIT Bombay (Quantum Sensing & Metrology), and IIT Delhi (Quantum Materials & Devices).\n"
            "• Statement 2 is correct: INFLIBNET (Gandhinagar, Gujarat) is the central implementing agency for ONOS (outlay Rs. 6,000 crore for 2025–2027).\n"
            "• Statement 3 is incorrect: ONOS covers over 6,300 institutions including ALL Central AND State government-managed higher education institutions and R&D laboratories."
        ),
        "source": "Department of Science & Technology (NQM) & Ministry of Education (ONOS)"
    },
    {
        "subject": "Indian Polity & Constitution",
        "topic": "Digital Personal Data Protection (DPDP) Act & Right to Privacy",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to the Digital Personal Data Protection (DPDP) Act, 2023 and its operational framework, consider the following statements:\n"
            "1. The Act applies to the processing of digital personal data within India, as well as outside India if such processing is in connection with any activity related to offering goods or services to Data Principals within India.\n"
            "2. Appeals against orders of the Data Protection Board of India (DPBI) lie before the Telecom Disputes Settlement and Appellate Tribunal (TDSAT), which functions as a digital appellate tribunal under the Act.\n"
            "3. For processing the personal data of a 'Child', the Act defines a child as any individual who has not completed the age of fourteen years.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: Section 3 provides extraterritorial jurisdiction when goods/services are offered to Data Principals in India.\n"
            "• Statement 2 is correct: Under Section 29 of the DPDP Act, TDSAT is designated as the Appellate Tribunal to hear appeals against decisions of the Data Protection Board of India.\n"
            "• Statement 3 is incorrect: Section 2(f) of the DPDP Act defines a 'Child' as an individual who has not completed the age of EIGHTEEN years (18 years, not 14 years), requiring verifiable parental consent."
        ),
        "source": "Digital Personal Data Protection Act, 2023 (MeitY)"
    },
    {
        "subject": "Science, Tech & Environment",
        "topic": "Indigenous Defence Technology: Mission Divyastra (Agni-5 MIRV), Rudram-II & Zorawar",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "Consider the following statements regarding indigenous defence systems developed by the Defence Research and Development Organisation (DRDO):\n"
            "1. 'Mission Divyastra' demonstrated the flight test of the Agni-5 ballistic missile equipped with Multiple Independently Targetable Re-entry Vehicle (MIRV) technology, allowing a single missile to deliver multiple nuclear warheads to distinct geographic targets.\n"
            "2. 'Rudram-II' is an indigenously developed solid-propelled air-to-surface anti-radiation/multi-role missile designed for Suppression of Enemy Air Defences (SEAD).\n"
            "3. Project 'Zorawar', jointly developed by DRDO and Larsen & Toubro, is a nuclear-powered attack submarine constructed at the Shipbuilding Centre in Visakhapatnam.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: Mission Divyastra tested Agni-5 (>5,000 km range, 3-stage solid-fuelled ICBM) with indigenous MIRV technology.\n"
            "• Statement 2 is correct: Rudram-II is an air-launched hypersonic/supersonic surface-attack and anti-radiation missile.\n"
            "• Statement 3 is incorrect: 'Zorawar' is an indigenous 25-tonne amphibious High-Altitude Light Tank (named after General Zorawar Singh) designed for mountainous warfare in Eastern Ladakh, not a nuclear submarine."
        ),
        "source": "Ministry of Defence / DRDO Press Releases"
    },
    {
        "subject": "Geography of India & AP",
        "topic": "Amaravati Capital City, CRDA & Geography of Krishna River Basin",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to the greenfield capital city of Amaravati in Andhra Pradesh and its geographical setting, consider the following statements:\n"
            "1. Amaravati Capital City is situated on the right (southern) bank of the Krishna River in Guntur district, upstream of the Prakasam Barrage.\n"
            "2. Multilateral financial assistance of Rs. 15,000 crore (~$1.6 billion) for Phase-I trunk infrastructure and flood-mitigation works in Amaravati is co-financed by the World Bank and the Asian Development Bank (ADB).\n"
            "3. The Kondaveeti Vagu, which flows through the Amaravati capital region, is a perennial snow-fed tributary of the Godavari River.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: Amaravati lies on the southern (right) bank of the Krishna River in Guntur district, upstream of the Prakasam Barrage at Vijayawada.\n"
            "• Statement 2 is correct: The World Bank ($800 million) and Asian Development Bank ($800 million) jointly committed Rs. 15,000 crore for Amaravati Phase-I infrastructure.\n"
            "• Statement 3 is incorrect: Kondaveeti Vagu is a seasonal monsoon-fed stream in the Krishna basin (famous for the Kondaveeti Vagu Lift Scheme that pumps floodwater into the Krishna River upstream of Prakasam Barrage), not a snow-fed tributary of the Godavari."
        ),
        "source": "APCRDA, Department of Economic Affairs & AP Geography"
    },
    {
        "subject": "Indian & AP Economy",
        "topic": "PM Surya Ghar: Muft Bijli Yojana & PM-KUSUM",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "Consider the following statements regarding flagship solar energy schemes in India:\n"
            "1. Under 'PM Surya Ghar: Muft Bijli Yojana' (total outlay Rs. 75,021 crore), Central Financial Assistance (CFA) for residential rooftop solar is capped at Rs. 78,000 for systems of 3 kW and above, while Group Housing Societies receive Rs. 18,000 per kW for common facilities up to 500 kW.\n"
            "2. Under the scheme, one 'Model Solar Village' is developed in every district of the country to act as a peer-learning hub for rural solar adoption.\n"
            "3. Unlike PM-KUSUM which falls under the Ministry of New and Renewable Energy (MNRE), PM Surya Ghar Yojana is implemented exclusively by the Ministry of Coal.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: PM Surya Ghar provides CFA of Rs. 30,000/kW up to 2 kW (Rs. 60,000) and Rs. 18,000 for the 3rd kW (total Rs. 78,000 cap for >=3 kW), plus Rs. 18,000/kW for Group Housing Societies.\n"
            "• Statement 2 is correct: The scheme includes an Rs. 800 crore component to create one Model Solar Village per district.\n"
            "• Statement 3 is incorrect: Both PM Surya Ghar and PM-KUSUM are administered by the Ministry of New and Renewable Energy (MNRE)."
        ),
        "source": "Ministry of New and Renewable Energy (MNRE) Operational Guidelines"
    },
    {
        "subject": "Indian Society & Welfare",
        "topic": "Ayushman Bharat Vaya Vandana (70+ Seniors) & Constitutional DPSPs",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to the expansion of Ayushman Bharat Pradhan Mantri Jan Arogya Yojana (AB PM-JAY) for senior citizens ('Ayushman Vaya Vandana') and related constitutional provisions, consider the following statements:\n"
            "1. All senior citizens aged 70 years and above are eligible for free secondary and tertiary hospitalization coverage of up to Rs. 5 lakh per year on a family basis, irrespective of their socio-economic or income status.\n"
            "2. Senior citizens aged 70 years and above who are already beneficiaries of Central Government Health Scheme (CGHS) or Ex-Servicemen Contributory Health Scheme (ECHS) must compulsorily surrender their existing scheme without an option to choose.\n"
            "3. Article 41 of the Constitution directs the State, within the limits of its economic capacity, to make effective provision for securing the right to public assistance in cases of old age, sickness, and disablement.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "1 and 3 only",
            "2 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 1,
        "explanation": (
            "Statements 1 and 3 are correct; Statement 2 is incorrect.\n"
            "• Statement 1 is correct: Ayushman Vaya Vandana provides universal Rs. 5 lakh health cover to all citizens aged 70+ regardless of income.\n"
            "• Statement 2 is incorrect: Senior citizens aged 70+ covered under CGHS, ECHS, or Ayushman CAPF have the voluntary option to either continue with their existing scheme OR opt for AB PM-JAY.\n"
            "• Statement 3 is correct: Article 41 (Part IV, DPSP) explicitly mandates public assistance in old age, sickness, and disablement."
        ),
        "source": "National Health Authority (MoHFW) & Article 41 of the Constitution"
    },
    {
        "subject": "Science, Tech & Environment",
        "topic": "UNFCCC Climate Conferences (COP29 Baku / COP30 Belém) & Article 6 Carbon Markets",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to international climate negotiations under the United Nations Framework Convention on Climate Change (UNFCCC) and the Paris Agreement, consider the following statements:\n"
            "1. The 'New Collective Quantified Goal' (NCQG) on climate finance agreed at UNFCCC COP29 in Baku calls on developed countries to take the lead in mobilizing at least USD 300 billion per year by 2035 for developing countries, within a broader scaling target of USD 1.3 trillion per year.\n"
            "2. Article 6.4 of the Paris Agreement establishes a centralized, UN-supervised global carbon credit mechanism (Paris Agreement Crediting Mechanism) replacing the Kyoto Protocol's Clean Development Mechanism (CDM).\n"
            "3. In India, the domestic Carbon Credit Trading Scheme (CCTS) was notified by the Central Government under the Environment (Protection) Act, 1986 with the Central Pollution Control Board (CPCB) as its sole administrator.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: The Baku Finance Goal (NCQG) adopted at COP29 sets a core mobilization goal of $300 billion/year by 2035 and an overarching $1.3 trillion/year roadmap heading into COP30 (Belém, Brazil).\n"
            "• Statement 2 is correct: Article 6.2 governs bilateral/cooperative ITMOs, while Article 6.4 creates the UN-supervised global carbon market mechanism.\n"
            "• Statement 3 is incorrect: India's Carbon Credit Trading Scheme (CCTS) was notified under the Energy Conservation Act, 2001 (amended in 2022) by the Ministry of Power, with the Bureau of Energy Efficiency (BEE) as the Administrator and Grid Controller of India as the Registry."
        ),
        "source": "UNFCCC COP29/COP30 Outcomes & Energy Conservation (Amendment) Act, 2022"
    },
    {
        "subject": "Indian Polity & Constitution",
        "topic": "Supreme Court 9-Judge Bench Rulings: Mineral Rights & Material Resources (Article 39(b))",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "Consider the following statements regarding two landmark 9-Judge Constitution Bench judgments delivered by the Supreme Court of India:\n"
            "1. In 'Mineral Area Development Authority vs. Steel Authority of India' (8:1 majority), the Supreme Court held that royalty payable on minerals under the MMDR Act, 1957 is NOT a tax, and State Legislatures possess constitutional competence under Entry 50 of the State List (List II) to levy taxes on mineral rights.\n"
            "2. In 'Property Owners Association vs. State of Maharashtra' concerning Article 39(b) of the Constitution, the 9-Judge Bench ruled that EVERY privately owned property automatically constitutes a 'material resource of the community' that can be acquired by the State at will.\n\n"
            "Which of the statements given above is/are correct?"
        ),
        "options": [
            "1 only",
            "2 only",
            "Both 1 and 2",
            "Neither 1 nor 2"
        ],
        "correct_index": 0,
        "explanation": (
            "Only Statement 1 is correct; Statement 2 is incorrect.\n"
            "• Statement 1 is correct: Overruling the 1989 India Cement judgment, the 9-Judge Bench held that royalty is a contractual consideration paid to the lessor, not a tax, and upheld States' taxing power over mineral-bearing lands (Entry 49) and mineral rights (Entry 50 of List II, subject to limitations imposed by Parliament).\n"
            "• Statement 2 is incorrect: In the Article 39(b) case, the 9-Judge Bench rejected the sweeping view of Justice Krishna Iyer in Ranganatha Reddy (1977) and held that NOT every privately owned resource is a 'material resource of the community'; whether a private resource qualifies depends on its nature, scarcity, community impact, and public trust."
        ),
        "source": "Supreme Court 9-Judge Constitution Bench Judgments (Articles 39(b) & 246)"
    },
    {
        "subject": "Geography of India & AP",
        "topic": "Eastern Ghats Biodiversity, Nallamala Hills & Critical Minerals in Andhra Pradesh",
        "question_type": "Pair Matching",
        "question": (
            "Consider the following mineral deposits and geographical locations in Andhra Pradesh:\n"
            "1. Mangampeta (Annamayya / YSR Kadapa region) — World's largest single bedded deposit of Barytes\n"
            "2. Tummalapalle (YSR Kadapa District) — Carbonate-hosted Uranium ore reserve\n"
            "3. Jindal / Araku–Sunkarimetta belt (Alluri Sitharama Raju District) — High-grade Bauxite deposits\n"
            "4. Ramagiri Gold Fields — Situated in Srikakulam District in the northern coastal plains\n\n"
            "How many of the above pairs are correctly matched?"
        ),
        "options": [
            "Only one pair",
            "Only two pairs",
            "Only three pairs",
            "All four pairs"
        ],
        "correct_index": 2,
        "explanation": (
            "Only three pairs (Pairs 1, 2, and 3) are correctly matched; Pair 4 is incorrect.\n"
            "• Pair 1 is correct: Mangampeta is the world's largest single Barytes deposit (operated by APMDC).\n"
            "• Pair 2 is correct: Tummalapalle in YSR Kadapa district hosts one of the largest dolostone/carbonate-hosted Uranium reserves (operated by UCIL).\n"
            "• Pair 3 is correct: The Eastern Ghats khondalite belt in Alluri Sitharama Raju / Visakhapatnam region (Sapperla, Jarella, Gurtedu, Anantagiri) holds major East Coast Bauxite deposits.\n"
            "• Pair 4 is incorrect: Ramagiri Gold Fields (and Jonnagiri gold block) are located in the Dharwar greenstone belt of Sri Sathya Sai / Anantapur–Kurnool (Rayalaseema) region, not in Srikakulam district."
        ),
        "source": "Geological Survey of India (GSI) & AP Mines and Geology Survey"
    },
    {
        "subject": "Indian & AP Economy",
        "topic": "IndiaAI Mission & Semiconductor Ecosystem (ISM)",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to the 'IndiaAI Mission' and the 'India Semiconductor Mission (ISM)', consider the following statements:\n"
            "1. Implemented by the 'IndiaAI' Independent Business Division under Digital India Corporation (MeitY) with an outlay of over Rs. 10,300 crore, the IndiaAI Mission establishes a shared compute infrastructure of more than 18,000 GPUs and develops indigenous Large Multimodal Models (LMMs) trained on Indian languages.\n"
            "2. Under the India Semiconductor Mission, India's first commercial compound/silicon wafer fabrication (Fab) facility is being established by Tata Electronics in partnership with PSMC at Dholera in Gujarat.\n"
            "3. Both the IndiaAI Mission and the India Semiconductor Mission are statutory bodies established under the Reserve Bank of India Act, 1934.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: IndiaAI Mission (Rs. 10,371.92 crore) comprises 7 pillars including IndiaAI Compute Capacity (>18,000 GPUs), IndiaAI Innovation Centre (indigenous foundational models), Datasets Platform (AIKosh), and Safe & Trusted AI.\n"
            "• Statement 2 is correct: Tata Electronics–PSMC is building the commercial semiconductor wafer fab at Dholera (Gujarat), alongside ATMP/OSAT units at Sanand (Micron, CG Power, Kaynes) and Morigaon in Assam (Tata).\n"
            "• Statement 3 is incorrect: Both missions operate as Independent Business Divisions under the Digital India Corporation under the Ministry of Electronics and Information Technology (MeitY), not under the RBI Act."
        ),
        "source": "Ministry of Electronics and Information Technology (MeitY)"
    },
    {
        "subject": "AP History & Reorganization",
        "topic": "Andhra Pradesh Reorganization Act, 2014: Parts & Schedules",
        "question_type": "Pair Matching",
        "question": (
            "Match the following Schedules of the Andhra Pradesh Reorganization Act, 2014 (Act No. 6 of 2014) with their subject matter:\n"
            "List-I (Schedule)                                List-II (Subject Matter)\n"
            "A. Ninth Schedule                                1. State Public Sector Undertakings & Corporations (89 Entities)\n"
            "B. Tenth Schedule                                2. Training Institutions / Centres (107 Entities)\n"
            "C. Eleventh Schedule                             3. Principles governing River Management Boards (KRMB & GRMB)\n"
            "D. Thirteenth Schedule                           4. Infrastructure, Education & Industrial Corridors (VCIC, Metro, Ports)\n\n"
            "Select the correct answer using the code given below:"
        ),
        "options": [
            "A-1, B-2, C-3, D-4",
            "A-2, B-1, C-3, D-4",
            "A-1, B-3, C-2, D-4",
            "A-4, B-2, C-3, D-1"
        ],
        "correct_index": 0,
        "explanation": (
            "The correct match is A-1, B-2, C-3, D-4.\n"
            "• Eighth Schedule: Pension liabilities apportionment.\n"
            "• Ninth Schedule (Section 68): List of 89 Government Companies and Corporations.\n"
            "• Tenth Schedule (Section 75): List of 107 State Training Institutions/Centres.\n"
            "• Eleventh Schedule (Section 85(8)): Principles governing the functioning of the Krishna and Godavari River Management Boards.\n"
            "• Twelfth Schedule (Section 92): Coal, Oil & Natural Gas, and Power.\n"
            "• Thirteenth Schedule (Section 93): Education (IIT, NIT, IIM, IISER, AIIMS, Central/Tribal/Agricultural Universities) and Infrastructure (Vizag/Vijayawada/Guntur Metro, Ports, VCIC, Road/Rail connectivity)."
        ),
        "source": "Andhra Pradesh Reorganization Act, 2014 (Schedules IX to XIII)"
    },
    {
        "subject": "PIB & Govt Schemes Current Affairs",
        "topic": "International Groupings: BRICS Expansion & Bilateral Defence Exercises",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to India's international engagements and joint military exercises, consider the following statements:\n"
            "1. Following the expansion decided at Johannesburg and operationalized ahead of the Kazan Summit, Egypt, Ethiopia, Iran, the United Arab Emirates, and Indonesia have joined BRICS as full member states.\n"
            "2. The inaugural multinational air exercise 'Tarang Shakti' hosted by the Indian Air Force was conducted in two phases at Sulur (Tamil Nadu) and Jodhpur (Rajasthan).\n"
            "3. Exercise 'DUSTLIK' is an annual bilateral naval anti-submarine warfare exercise conducted between the Indian Navy and the French Navy in the Bay of Bengal.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: Egypt, Ethiopia, Iran, and the UAE joined BRICS in 2024, followed by Indonesia joining as a full member in 2025.\n"
            "• Statement 2 is correct: 'Tarang Shakti' was India's largest-ever multilateral air exercise hosted by the IAF at Sulur (Phase-I) and Jodhpur (Phase-II).\n"
            "• Statement 3 is incorrect: Exercise 'DUSTLIK' is a bilateral joint military (Army) exercise between INDIA and UZBEKISTAN (whereas India–France naval exercise is 'VARUNA')."
        ),
        "source": "Ministry of External Affairs & Ministry of Defence"
    },
    {
        "subject": "Indian & AP Economy",
        "topic": "PM Vidyalaxmi Scheme & PM E-DRIVE Scheme",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "Examine the following statements regarding two Union Cabinet-approved schemes—'PM Vidyalaxmi' and 'PM E-DRIVE':\n"
            "1. Under the PM Vidyalaxmi scheme, any student securing admission in Quality Higher Education Institutions (QHEIs ranked in the top 860 institutions under NIRF) is eligible for collateral-free and guarantor-free education loans, with a 3% interest subvention on loans up to Rs. 10 lakh for students having annual family income up to Rs. 8 lakh.\n"
            "2. The PM E-DRIVE scheme (outlay Rs. 10,900 crore, replacing FAME-II) provides demand incentives for electric two-wheelers, electric three-wheelers, e-ambulances, e-trucks, and 14,028 e-buses.\n"
            "3. Under PM E-DRIVE, private passenger four-wheeler electric cars (e-4Ws) receive the highest share of direct purchase subsidy.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: PM Vidyalaxmi (outlay Rs. 3,600 crore) offers collateral-free, guarantor-free loans with a 75% credit guarantee on loans up to Rs. 7.5 lakh and a 3% interest subvention on loans up to Rs. 10 lakh for families earning up to Rs. 8 lakh/year.\n"
            "• Statement 2 is correct: PM E-DRIVE (PM Electric Drive Revolution in Innovative Vehicle Enhancement) by the Ministry of Heavy Industries supports e-2Ws, e-3Ws, e-ambulances, e-trucks, e-buses, and EV public charging stations.\n"
            "• Statement 3 is incorrect: Private electric four-wheeler passenger cars (e-4Ws) are EXCLUDED from direct demand subsidies under the PM E-DRIVE scheme."
        ),
        "source": "Union Cabinet Decisions (Ministry of Education & Ministry of Heavy Industries)"
    },
    {
        "subject": "Indian Polity & Constitution",
        "topic": "Simultaneous Elections ('One Nation, One Election') High-Level Committee Report",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to the High-Level Committee on Simultaneous Elections ('One Nation, One Election') chaired by former President Ram Nath Kovind, consider the following statements:\n"
            "1. The Committee recommended a two-step implementation: in the first step, elections to the House of the People (Lok Sabha) and all State Legislative Assemblies are synchronized; in the second step, elections to Municipalities and Panchayats are held within 100 days of the general election.\n"
            "2. It proposed inserting Article 82A into the Constitution, whereby if a House is dissolved sooner than its full five-year term, the fresh election held to constitute the new House shall be only for the 'unexpired term' of the immediately preceding full term.\n"
            "3. According to the Committee, neither the synchronization of Lok Sabha and State Assembly elections nor the synchronization of local body elections requires any ratification by the State Legislatures under Article 368(2).\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: The Kovind Committee recommended synchronizing Lok Sabha and Vidhan Sabha polls in Phase-I, and holding local body (Panchayat/Municipality) polls within 100 days in Phase-II.\n"
            "• Statement 2 is correct: Proposed Article 82A and amendments to Articles 83 and 172 provide that mid-term elections only serve the remainder ('unexpired term') of the five-year cycle.\n"
            "• Statement 3 is incorrect: While the Committee noted that the First Constitutional Amendment Bill (for Lok Sabha & State Assemblies under Articles 82A, 83, 172) would not require state ratification, the Second Constitutional Amendment Bill (inserting Article 324A for Panchayat/Municipality polls and single electoral roll under Article 325) WOULD require ratification by not less than one-half of the States under Article 368(2)."
        ),
        "source": "Report of the High-Level Committee on Simultaneous Elections"
    },
    {
        "subject": "Science, Tech & Environment",
        "topic": "Wildlife Conservation: Project Cheetah, Project Tiger & AP Protected Areas",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "Consider the following statements regarding wildlife conservation and protected areas in India and Andhra Pradesh:\n"
            "1. Gandhi Sagar Wildlife Sanctuary in Madhya Pradesh was prepared as the second home in India for African Cheetahs (Acinonyx jubatus) after Kuno National Park.\n"
            "2. Nagarjunasagar–Srisailam Tiger Reserve (NSTR), spanning the Nallamala hills across Andhra Pradesh, is India's largest Tiger Reserve in terms of total notified area.\n"
            "3. Coringa Wildlife Sanctuary in Kakinada district of Andhra Pradesh is the only breeding ground in India for the critically endangered Great Indian Bustard (Ardeotis nigriceps).\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: Gandhi Sagar Wildlife Sanctuary (Mandsaur/Nimach districts, Madhya Pradesh) was developed as the second cheetah translocation site after Kuno National Park.\n"
            "• Statement 2 is correct: Nagarjunasagar–Srisailam Tiger Reserve (NSTR) in the Nallamala hills of Andhra Pradesh is the largest tiger reserve in India by total area (~3,728 sq. km).\n"
            "• Statement 3 is incorrect: Coringa Wildlife Sanctuary is India's second-largest mangrove ecosystem (after Sundarbans) and is famous for Fishing Cats, Smooth-coated Otters, and Olive Ridley turtles, whereas the Great Indian Bustard is found in dry grasslands (such as Rollapadu Wildlife Sanctuary in Nandyal district of AP and Desert National Park in Rajasthan)."
        ),
        "source": "National Tiger Conservation Authority (NTCA) & AP Forest Department"
    },
    {
        "subject": "Indian & AP Economy",
        "topic": "Goods and Services Tax (GST) Council & Constitutional Provisions",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to the Goods and Services Tax (GST) Council constituted under Article 279A of the Constitution (inserted by the 101st Constitutional Amendment Act, 2016), consider the following statements:\n"
            "1. Every decision of the GST Council is taken at a meeting by a majority of not less than three-fourths (75%) of the weighted votes of the members present and voting, where the Central Government holds a weightage of one-third (33.33%) and all State Governments together hold a weightage of two-thirds (66.67%).\n"
            "2. In 'Union of India vs. Mohit Minerals', the Supreme Court held that recommendations of the GST Council under Article 279A have only persuasive value and are not binding mandates that override the concurrent legislative power of Parliament and State Legislatures under Article 246A.\n"
            "3. Petroleum crude, high-speed diesel, motor spirit (petrol), natural gas, and aviation turbine fuel are completely excluded from the purview of Article 279A and can only be brought under GST by a new Constitutional Amendment under Article 368.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: Article 279A(9) sets the voting weightage: Centre = 1/3rd, States combined = 2/3rds, requiring a >=3/4ths (75%) weighted majority.\n"
            "• Statement 2 is correct: In Mohit Minerals (2022), the Supreme Court emphasized 'uncooperative federalism' / collaborative federalism under Article 246A.\n"
            "• Statement 3 is incorrect: Under Article 279A(5), the five petroleum products (crude oil, high-speed diesel, petrol, natural gas, and ATF) are ALREADY included in the constitutional scheme—the GST Council itself is empowered to recommend the date from which GST shall be levied on them without requiring any new Constitutional Amendment."
        ),
        "source": "Article 246A & Article 279A of the Constitution of India"
    },
    {
        "subject": "PIB & Govt Schemes Current Affairs",
        "topic": "National Maritime Heritage, Vadhavan Mega Port & AP Maritime Infrastructure",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to port and maritime infrastructure developments in India and Andhra Pradesh, consider the following statements:\n"
            "1. Vadhavan Port, approved by the Union Cabinet as India's 13th Major Port, is an all-weather greenfield deep-draft port located in Palghar district of Maharashtra.\n"
            "2. The National Maritime Heritage Complex (NMHC) is being developed by the Ministry of Ports, Shipping and Waterways at Lothal in Gujarat, the site of the ancient Harappan tidal dockyard.\n"
            "3. In Andhra Pradesh, greenfield non-major ports are being constructed by the Andhra Pradesh Maritime Board at Ramayapatnam (Prakasam/Nellore border), Machilipatnam (Krishna), and Mulapeta (Srikakulam).\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 3,
        "explanation": (
            "All three statements (1, 2 and 3) are correct.\n"
            "• Statement 1 is correct: Vadhavan Port (Rs. 76,220 crore, 20-metre natural draft capable of handling 24,000 TEU mega container vessels) is located at Dahanu/Palghar in Maharashtra.\n"
            "• Statement 2 is correct: The National Maritime Heritage Complex is located at the Harappan port town of Lothal (Gujarat).\n"
            "• Statement 3 is correct: Along Andhra Pradesh's 974-km coastline, Visakhapatnam is a Major Port while Krishnapatnam, Gangavaram, Kakinada, and Rawa are operational non-major ports, and Ramayapatnam, Machilipatnam, Mulapeta, and Kakinada Gateway are greenfield ports under development."
        ),
        "source": "Ministry of Ports, Shipping & Waterways & AP Maritime Board"
    },
    {
        "subject": "Science, Tech & Environment",
        "topic": "World Health Organization Certifications & Neglected Tropical Diseases in India",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "Consider the following statements regarding public health disease elimination milestones in India:\n"
            "1. The World Health Organization (WHO) officially validated India for having eliminated Trachoma—a bacterial eye infection caused by 'Chlamydia trachomatis'—as a public health problem.\n"
            "2. Kala-azar (Visceral Leishmaniasis) is caused by a protozoan parasite ('Leishmania donovani') transmitted through the bite of an infected female Phlebotomine sandfly.\n"
            "3. Lymphatic Filariasis (Elephantiasis) is a viral disease transmitted solely through contaminated drinking water.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: WHO certified India for eliminating Trachoma (caused by the bacterium Chlamydia trachomatis) as a public health problem.\n"
            "• Statement 2 is correct: Kala-azar is caused by the protozoan parasite Leishmania donovani and transmitted by the female sandfly (Phlebotomus argentipes); India achieved its elimination threshold (<1 case per 10,000 population across all blocks).\n"
            "• Statement 3 is incorrect: Lymphatic Filariasis is caused by parasitic filarial nematode worms (Wuchereria bancrofti / Brugia malayi) transmitted by Culex/Mansonia mosquitoes, not a water-borne virus."
        ),
        "source": "Ministry of Health and Family Welfare & WHO South-East Asia Region"
    },
    {
        "subject": "Indian Polity & Constitution",
        "topic": "Telecommunications Act, 2023 & Spectrum Allocation",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to the Telecommunications Act, 2023 (which replaces the Indian Telegraph Act, 1885 and the Indian Wireless Telegraphy Act, 1933), consider the following statements:\n"
            "1. While auction is the default mechanism for spectrum assignment, the First Schedule of the Act specifically authorizes 'administrative allocation' (without auction) of spectrum for satellite-based communication services including Global Mobile Personal Communication by Satellites (GMPCS).\n"
            "2. Under the Act, the 'Universal Service Obligation Fund' (USOF) has been renamed 'Digital Bharat Nidhi', which can be utilized not only for rural telecom access but also for research and development of telecommunication technologies and pilot projects.\n"
            "3. The Act strips the Central Government of all powers to intercept messages or temporarily take possession of telecom networks on grounds of public emergency or national security.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: Section 4(4) read with the First Schedule lists 19 entries (including national security, BSNL/MTNL, weather forecasting, and satellite broadband/GMPCS) where spectrum is assigned administratively rather than by auction.\n"
            "• Statement 2 is correct: Sections 24–26 rename the USOF as 'Digital Bharat Nidhi' and expand its scope to include R&D and telecom startups.\n"
            "• Statement 3 is incorrect: Sections 20 and 21 retain and codify the Central/State Government's power to take temporary possession of telecom networks and intercept messages in the interest of India's sovereignty, security, or public order."
        ),
        "source": "The Telecommunications Act, 2023 (Department of Telecommunications)"
    },
    {
        "subject": "AP History & Reorganization",
        "topic": "Modern Andhra History: Vandemataram, Rampa Rebellion & Sribagh Pact",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "Consider the following statements regarding the Freedom Struggle and the movement for a separate Andhra State:\n"
            "1. During Bipin Chandra Pal's tour of Andhra in April 1907, his fiery Swadeshi speeches at Rajahmundry were translated into Telugu by Chilakamarthi Lakshminarasimham, directly inspiring the Rajahmundry College 'Vandemataram' student incident.\n"
            "2. The Sribagh Pact (November 16, 1937) signed at the Madras residence of Kashinathuni Nageswara Rao Pantulu between leaders of Coastal Andhra and Rayalaseema agreed that in the event of forming a separate Andhra Province, Rayalaseema would be given priority in choosing either the Capital or the High Court, while Andhra University would establish a centre at Anantapur.\n"
            "3. The JVP Committee (1948–49), comprising Jawaharlal Nehru, Vallabhbhai Patel, and Pattabhi Sitaramayya, recommended the immediate creation of Andhra State with Madras City as its permanent capital.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: Chilakamarthi Lakshminarasimham translated Bipin Chandra Pal's speeches at Rajahmundry in April 1907 and composed the famous verse 'Bharata Khandambu Chakkani Padiyaavu'; Principal Mark Hunter subsequently rusticated over 130 students for wearing Vandemataram badges.\n"
            "• Statement 2 is correct: The Sribagh Pact (1937) safeguarded Rayalaseema's irrigation (Tungabhadra/Krishna-Pennar), university education (Anantapur), and choice between Capital and High Court (leading to the High Court initially at Guntur and Capital at Kurnool in 1953).\n"
            "• Statement 3 is incorrect: The JVP Committee stipulated that a separate Andhra province could be considered ONLY if the Andhras gave up their claim over Madras City."
        ),
        "source": "History of Freedom Movement in Andhra Pradesh (Prof. M. Venkatarangaiya)"
    },
    {
        "subject": "Indian & AP Economy",
        "topic": "Unified Pension Scheme (UPS) & National Pension System (NPS)",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to the 'Unified Pension Scheme' (UPS) approved by the Union Cabinet for Central Government employees, consider the following statements:\n"
            "1. The Unified Pension Scheme guarantees an assured pension of 50% of the average basic pay drawn during the last 12 months prior to superannuation for employees with a minimum qualifying service of 25 years.\n"
            "2. It provides an assured minimum pension of Rs. 10,000 per month upon superannuation after a minimum of 10 years of service, along with Dearness Relief indexed to the All India Consumer Price Index for Industrial Workers (AICPI-IW).\n"
            "3. Under the Unified Pension Scheme, the employee's monthly contribution is abolished (0%), while the Central Government bears 100% of the contribution at 28% of basic pay.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statements 1 and 2 are correct: Formulated on the recommendations of the Dr. T.V. Somanathan Committee, UPS guarantees 50% of 12-month average basic pay (for >=25 years service), 60% of employee pension as family pension, Rs. 10,000/month minimum pension (for >=10 years service), inflation indexation, and a lump-sum superannuation payout.\n"
            "• Statement 3 is incorrect: Under UPS, the employee's contribution remains UNCHANGED at 10% of (Basic Pay + DA), while the Central Government's contribution is increased from 14% to 18.5%."
        ),
        "source": "Department of Expenditure, Ministry of Finance (UPS Notification)"
    },
    {
        "subject": "Geography of India & AP",
        "topic": "River Interlinking in Andhra Pradesh: Pattiseema, Polavaram–Banakacherla & Handri-Neeva",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "Consider the following statements regarding irrigation and river-linking projects in Andhra Pradesh:\n"
            "1. The Pattiseema Lift Irrigation Scheme lifts floodwater from the Godavari River upstream of the Dowleswaram Barrage and delivers it into the Polavaram Right Main Canal, which drops into the Krishna River at Pavitra Sangamam (Ibrahimpatnam) upstream of the Prakasam Barrage.\n"
            "2. The proposed Godavari–Banakacherla Link Project aims to divert surplus Godavari floodwaters via the Krishna (Nagarjunasagar/Bollapalli) to the Banakacherla Cross Regulator in Nandyal district to drought-proof Rayalaseema.\n"
            "3. The Handri–Neeva Sujala Sravanthi (HNSS) project lifts water from the Somasila Reservoir on the Penna River to irrigate Srikakulam and Vizianagaram districts.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: Pattiseema linked the Godavari and Krishna rivers by feeding Godavari water via the Polavaram Right Main Canal into the Krishna at Ibrahimpatnam, stabilizing the Krishna Delta.\n"
            "• Statement 2 is correct: The Godavari–Banakacherla link transfers surplus floodwater from Polavaram via Bollapalli balancing reservoir and a tunnel through the Nallamala hills to the Banakacherla complex.\n"
            "• Statement 3 is incorrect: Handri–Neeva Sujala Sravanthi (HNSS) lifts floodwater from the backwaters of the SRISAILAM Reservoir (Malyala in Nandyal/Kurnool) on the Krishna River to irrigate the four Rayalaseema districts (Kurnool, Anantapur, Chittoor, Kadapa), not from Somasila to Srikakulam."
        ),
        "source": "Water Resources Department, Government of Andhra Pradesh"
    },
    {
        "subject": "Science, Tech & Environment",
        "topic": "Nobel Prizes in Science & Economics (Machine Learning, microRNA & Institutions)",
        "question_type": "Pair Matching",
        "question": (
            "Match the following Nobel Prize laureates with their foundational scientific or economic contributions:\n"
            "List-I (Laureates)                                              List-II (Core Discovery / Contribution)\n"
            "A. Victor Ambros & Gary Ruvkun (Physiology/Medicine)            1. Discovery of microRNA and its role in post-transcriptional gene regulation\n"
            "B. John Hopfield & Geoffrey Hinton (Physics)                    2. Foundational methods enabling machine learning with artificial neural networks\n"
            "C. David Baker, Demis Hassabis & John Jumper (Chemistry)        3. Computational protein design and AI-based protein structure prediction (AlphaFold2)\n"
            "D. Daron Acemoglu, Simon Johnson & James Robinson (Economics)   4. How inclusive vs. extractive societal institutions form and affect national prosperity\n\n"
            "Select the correct answer using the code given below:"
        ),
        "options": [
            "A-1, B-2, C-3, D-4",
            "A-2, B-1, C-3, D-4",
            "A-1, B-3, C-2, D-4",
            "A-4, B-2, C-1, D-3"
        ],
        "correct_index": 0,
        "explanation": (
            "The correct match is A-1, B-2, C-3, D-4.\n"
            "• Physiology or Medicine: Victor Ambros and Gary Ruvkun for discovering microRNA (tiny non-coding RNA molecules that regulate gene expression post-transcriptionally).\n"
            "• Physics: John J. Hopfield (Hopfield associative memory network) and Geoffrey E. Hinton (Boltzmann machine) for foundational physics-based artificial neural network methods.\n"
            "• Chemistry: David Baker (computational de novo protein design) and Demis Hassabis & John Jumper (AlphaFold2 predicting 3D protein structures from amino acid sequences).\n"
            "• Economic Sciences: Daron Acemoglu, Simon Johnson, and James A. Robinson for empirical studies on how colonial and modern institutional structures determine long-run economic growth."
        ),
        "source": "Royal Swedish Academy of Sciences Official Citations"
    },
    {
        "subject": "Indian Society & Welfare",
        "topic": "NITI Aayog Multidimensional Poverty Index (MPI) & SDG India Index",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to NITI Aayog's 'National Multidimensional Poverty Index (MPI)' and the 'SDG India Index', consider the following statements:\n"
            "1. Unlike the global MPI (computed by OPHI and UNDP) which uses 10 indicators across Health, Education, and Standard of Living, NITI Aayog's National MPI incorporates 12 indicators by adding 'Maternal Health' (under Health) and 'Bank Account' (under Standard of Living).\n"
            "2. In NITI Aayog's SDG India Index, Andhra Pradesh is classified in the 'Front Runner' category (score between 65 and 99), with particularly strong performance in Goal 7 (Affordable and Clean Energy) and Goal 14 (Life Below Water).\n"
            "3. The National MPI uses per-capita monthly cash expenditure from the Reserve Bank of India as its sole indicator of poverty.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: NITI Aayog's National MPI (based on NFHS data using the Alkire-Foster methodology) expands the 10 global indicators to 12 by adding Maternal Health (Health dimension) and Bank Account (Standard of Living dimension).\n"
            "• Statement 2 is correct: Andhra Pradesh consistently ranks in the 'Front Runner' tier (score 65–99) on the SDG India Index.\n"
            "• Statement 3 is incorrect: MPI measures non-monetary deprivation across 3 equally weighted dimensions (Health, Education, Standard of Living), not cash expenditure."
        ),
        "source": "NITI Aayog National MPI & SDG India Index Reports"
    },
    {
        "subject": "Indian Polity & Constitution",
        "topic": "Governor's Assent to Bills under Article 200 & Supreme Court Jurisprudence",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to the constitutional powers of the Governor regarding State Bills under Article 200 of the Constitution, as interpreted by the Supreme Court of India (in the State of Punjab and State of Tamil Nadu cases), consider the following statements:\n"
            "1. A Money Bill passed by the State Legislative Assembly can be returned by the Governor for reconsideration up to two times.\n"
            "2. Under the first proviso to Article 200, if the Governor withholds assent to a non-Money Bill, the Governor cannot simply keep the Bill pending indefinitely ('pocket veto') and must communicate the message returning the Bill to the State Legislature 'as soon as possible'.\n"
            "3. If the State Legislature passes the returned Bill again with or without amendments and presents it to the Governor for assent, the Governor is constitutionally bound under Article 200 to declare assent and shall not withhold assent therefrom.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 1,
        "explanation": (
            "Statements 2 and 3 are correct; Statement 1 is incorrect.\n"
            "• Statement 1 is incorrect: Article 200 explicitly states that a Governor can return a Bill for reconsideration ONLY if it is 'not a Money Bill'.\n"
            "• Statements 2 and 3 are correct: In 'State of Punjab vs. Principal Secretary to the Governor of Punjab', the Supreme Court held that if a Governor decides to withhold assent under the substantive part of Article 200, the mandatory course under the first proviso ('as soon as possible') must be followed to return the Bill to the Legislature; if re-passed, the Governor cannot withhold assent or subsequently reserve it for the President."
        ),
        "source": "Article 200 of the Constitution & Supreme Court Judgments"
    },
    {
        "subject": "Science, Tech & Environment",
        "topic": "Aditya-L1 Solar Observatory & Lagrange Points",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to ISRO's Aditya-L1 solar mission and the physics of Lagrange points, consider the following statements:\n"
            "1. Aditya-L1 is placed in a periodic Halo Orbit around the Sun–Earth Lagrange Point 1 (L1), located approximately 1.5 million kilometres from the Earth towards the Sun, enabling continuous observation of the Sun without any occultation or eclipses.\n"
            "2. The Visible Emission Line Coronagraph (VELC), developed by the Indian Institute of Astrophysics (IIA), is the primary payload onboard Aditya-L1 designed to study the diagnostic parameters of the solar corona and the origin of Coronal Mass Ejections (CMEs).\n"
            "3. Out of the seven scientific payloads onboard Aditya-L1, four payloads directly view the Sun as remote-sensing instruments, while three payloads perform in-situ measurements of particles and magnetic fields at L1.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 3,
        "explanation": (
            "All three statements (1, 2 and 3) are correct.\n"
            "• Statement 1 is correct: The Sun–Earth L1 point lies ~1.5 million km from Earth (~1% of the Earth-Sun distance), where a halo orbit provides an uninterrupted view of the Sun.\n"
            "• Statement 2 is correct: VELC (built by IIA Bengaluru) images the solar corona down to 1.05 solar radii.\n"
            "• Statement 3 is correct: Four remote-sensing payloads (VELC, SUIT, SoLEXS, HEL1OS) observe the photosphere, chromosphere, and corona, while three in-situ payloads (ASPEX, PAPA, Advanced Tri-axial High Resolution Digital Magnetometers) sample the solar wind at L1."
        ),
        "source": "ISRO Aditya-L1 Science Dossier"
    },
    {
        "subject": "Indian & AP Economy",
        "topic": "Pradhan Mantri Matsya Sampada Yojana (PMMSY) & Andhra Pradesh Aquaculture",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "Consider the following statements regarding the fisheries and aquaculture sector in India and Andhra Pradesh:\n"
            "1. Andhra Pradesh ranks first among all Indian states in total fish and shrimp production, contributing over 70% of India's cultured shrimp output (`Litopenaeus vannamei`) and leading marine seafood exports.\n"
            "2. The 'Pradhan Mantri Matsya Kisan Samridhi Sah-Yojana' (PM-MKSSY), approved with an outlay of Rs. 6,000 crore, is a central sector sub-scheme under the Pradhan Mantri Matsya Sampada Yojana (PMMSY) aimed at formalizing the fisheries sector through a National Fisheries Digital Platform (NFDP) and aquaculture crop insurance.\n"
            "3. Kolleru Lake, located entirely within Rayalaseema's Anantapur district, is a hyper-saline coastal lagoon connected directly to the Bay of Bengal.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: Andhra Pradesh ('Aqua Hub of India') is the #1 fish and shrimp producing state in India.\n"
            "• Statement 2 is correct: PM-MKSSY (Rs. 6,000 crore, co-financed with World Bank and AFD) is a sub-scheme under PMMSY focusing on NFDP registration, institutional credit, and one-time incentive against aquaculture insurance premium.\n"
            "• Statement 3 is incorrect: Kolleru Lake is a FRESHWATER lake situated between the Godavari and Krishna deltas across Eluru and West Godavari districts (whereas Pulicat Lake is a brackish-water lagoon on the Nellore/Tirupati–Tamil Nadu coast)."
        ),
        "source": "Department of Fisheries (Ministry of Fisheries, Animal Husbandry & Dairying) & AP Socio-Economic Survey"
    },
    {
        "subject": "Indian Polity & Constitution",
        "topic": "Chief Election Commissioner and Other Election Commissioners Act, 2023",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to the Chief Election Commissioner and Other Election Commissioners (Appointment, Conditions of Service and Term of Office) Act, 2023, consider the following statements:\n"
            "1. Under the Act, the Selection Committee that recommends appointments to the President consists of the Prime Minister, the Chief Justice of India, and the Leader of the Opposition in the House of the People.\n"
            "2. A Search Committee headed by the Minister of Law and Justice (and comprising two Secretaries to the Government of India) prepares a panel of five persons for consideration of the Selection Committee.\n"
            "3. The Chief Election Commissioner and Other Election Commissioners hold office for a term of six years or until they attain the age of 65 years, whichever is earlier, and are not eligible for re-appointment.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 1,
        "explanation": (
            "Statements 2 and 3 are correct; Statement 1 is incorrect.\n"
            "• Statement 1 is incorrect: While the Supreme Court's March 2023 interim arrangement in the 'Anoop Baranwal' case included the Chief Justice of India until Parliament enacted a law, Section 7 of the 2023 Act enacted by Parliament under Article 324(2) constitutes the Selection Committee with: (a) the Prime Minister (Chairperson), (b) the Leader of the Opposition in the Lok Sabha (Member), and (c) a Union Cabinet Minister nominated by the Prime Minister (Member)—excluding the CJI.\n"
            "• Statement 2 is correct: Section 6 establishes a Search Committee headed by the Union Minister of Law and Justice.\n"
            "• Statement 3 is correct: Section 9 prescribes a 6-year term or age 65 (whichever is earlier) with no eligibility for re-appointment."
        ),
        "source": "The Chief Election Commissioner and Other Election Commissioners Act, 2023"
    },
    {
        "subject": "AP History & Reorganization",
        "topic": "Kakatiya & Vijayanagara Revenue, Military and Irrigation Systems",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "Consider the following statements regarding the administrative and agrarian institutions of medieval Andhra dynasties:\n"
            "1. Under the Kakatiyas of Warangal, the 'Nayankara' system assigned revenue-yielding villages to military commanders (Nayakas) in lieu of maintaining stipulated contingents of foot soldiers, horses, and elephants for the royal army.\n"
            "2. The 'Dashabandha' (Dasavanda) tenure prevalent during the Kakatiya and Vijayanagara periods was a punitive religious tax levied on non-agriculturists.\n"
            "3. The Motupalli Abhaya Shasana (1244 CE), issued by Kakatiya ruler Ganapatideva (and later renewed by Rudramadevi and Reddi king Anavota Reddi), guaranteed safety and fixed customs duties for foreign maritime merchants trading at Motupalli port in Prakasam/Bapatla coast.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "1 and 3 only",
            "2 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 1,
        "explanation": (
            "Statements 1 and 3 are correct; Statement 2 is incorrect.\n"
            "• Statement 1 is correct: Prataparudra's reign systematized the Nayankara military-fiscal assignment system, which was later expanded into the Amara-Nayaka system under Vijayanagara.\n"
            "• Statement 2 is incorrect: 'Dashabandha' (Dasavanda) was a tax-free land or revenue grant (typically 1/10th of the produce/ayacut) awarded to individuals who constructed, repaired, or maintained irrigation tanks and canals.\n"
            "• Statement 3 is correct: The Motupalli Charter (Abhaya Shasana of 1244 CE) abolished arbitrary confiscation of shipwrecked cargo and fixed fair tariffs."
        ),
        "source": "Social and Cultural History of Andhra Pradesh (B.S.L. Hanumantha Rao)"
    },
    {
        "subject": "Science, Tech & Environment",
        "topic": "Kavach 4.0 Automatic Train Protection System & Railway Safety",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to 'Kavach', India's indigenously developed Automatic Train Protection (ATP) system approved at Version 4.0 specification by the Research Designs and Standards Organisation (RDSO), consider the following statements:\n"
            "1. Kavach is certified to Safety Integrity Level-4 (SIL-4), the highest global safety certification level, signifying a probability of dangerous failure of less than 10^-9 per hour.\n"
            "2. It utilizes Ultra High Frequency (UHF) radio communication and RFID tags installed on railway tracks to continuously update movement authority and automatically apply brakes if the loco pilot fails to respond to overspeeding or Signal Passing at Danger (SPAD).\n"
            "3. Kavach requires physical optical fibre cables to be tethered directly to the moving locomotive Pantograph at all times and cannot function in foggy weather.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statements 1 and 2 are correct: Developed by RDSO with Indian industry partners, Kavach 4.0 is SIL-4 certified, using trackside RFID tags, Stationary Kavach units, and UHF/LTE wireless communication.\n"
            "• Statement 3 is incorrect: Kavach communicates wirelessly with the locomotive and relays live signal aspects directly onto the Driver Machine Interface (DMI) inside the locomotive cab, making it specifically advantageous during dense fog and low visibility."
        ),
        "source": "Ministry of Railways / RDSO Technical Specifications"
    },
    {
        "subject": "PIB & Govt Schemes Current Affairs",
        "topic": "UNESCO World Heritage Sites & Intangible Cultural Heritage of India",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "Consider the following statements regarding India's inscriptions on UNESCO Heritage Lists:\n"
            "1. The 'Moidams – the Mound-Burial System of the Ahom Dynasty' at Charaideo in Assam was inscribed as a Cultural Property on the UNESCO World Heritage List.\n"
            "2. The 'Sacred Ensembles of the Hoysalas' (comprising the temples at Belur, Halebidu, and Somanathapura in Karnataka) and 'Santiniketan' (West Bengal) are inscribed as UNESCO World Heritage Sites.\n"
            "3. The 'Lepakshi Veerabhadra Temple' in Sri Sathya Sai district of Andhra Pradesh was inscribed on the permanent UNESCO World Heritage List in 2014 alongside Rani-ki-Vav.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: The Charaideo Moidams (royal burial mounds of the Tai-Ahom dynasty in Assam) became India's 43rd UNESCO World Heritage Site (and the first in the Cultural category from North-East India).\n"
            "• Statement 2 is correct: Santiniketan (41st) and Sacred Ensembles of the Hoysalas (42nd) were inscribed in 2023.\n"
            "• Statement 3 is incorrect: The Lepakshi Veerabhadra Temple (16th-century Vijayanagara architecture famous for its hanging pillar, monolithic Nandi, and mural paintings) was placed on UNESCO's TENTATIVE List in 2022, not the permanent World Heritage List in 2014."
        ),
        "source": "Archaeological Survey of India (ASI) & Ministry of Culture"
    },
    {
        "subject": "Indian & AP Economy",
        "topic": "External Sector: Balance of Payments, Forex Reserves & Sovereign Gold Bonds",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to India's Balance of Payments (BoP) accounting and Foreign Exchange Reserves managed by the Reserve Bank of India, consider the following statements:\n"
            "1. Private remittances sent home by Non-Resident Indians (NRIs) working abroad and net software service exports are recorded under the 'Invisibles' component of the Current Account, not the Capital Account.\n"
            "2. India's official Foreign Exchange Reserves comprise four components: Foreign Currency Assets (FCA), Gold reserves, Special Drawing Rights (SDRs), and Reserve Tranche Position (RTP) with the International Monetary Fund (IMF).\n"
            "3. A depreciation of the Indian Rupee against the US Dollar in the spot market automatically increases the dollar valuation of RBI's existing Euro and Pound Sterling assets.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: In BoP accounting, Current Account = Merchandise Trade (Visible) + Invisibles (Services, Income/Investment income, and Current Transfers/Remittances). India is the world's largest recipient of remittances (~$125+ billion).\n"
            "• Statement 2 is correct: FCA, Gold, SDRs, and RTP in the IMF are the four constituents of India's Forex Reserves.\n"
            "• Statement 3 is incorrect: The US Dollar valuation of non-US currency assets (Euro, Pound, Yen) held in FCA depends on the cross-currency exchange rate between the US Dollar and those currencies (Euro/USD, GBP/USD), not on the INR/USD exchange rate."
        ),
        "source": "Reserve Bank of India Handbook of Statistics on the Indian Economy"
    },
    {
        "subject": "Geography of India & AP",
        "topic": "Ramsar Wetlands of International Importance & Coastal Ecosystems of Andhra Pradesh",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "Consider the following statements regarding wetlands and coastal ecosystems in Andhra Pradesh and India:\n"
            "1. The 'Montreux Record' under the Ramsar Convention is a register of wetland sites on the List of Wetlands of International Importance where changes in ecological character have occurred, are occurring, or are likely to occur as a result of technological developments, pollution, or other human interference.\n"
            "2. Currently, two Indian wetlands—Keoladeo National Park (Rajasthan) and Loktak Lake (Manipur)—are placed on the Montreux Record, whereas Chilika Lake (Odisha) was removed from it following successful restoration.\n"
            "3. Pulicat Lake, India's second-largest brackish-water lagoon straddling the border of Andhra Pradesh (Tirupati district) and Tamil Nadu, is separated from the Bay of Bengal by the barrier island of Sriharikota.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 3,
        "explanation": (
            "All three statements (1, 2 and 3) are correct.\n"
            "• Statement 1 is correct: The Montreux Record (established in 1990) tracks threatened Ramsar sites requiring priority conservation.\n"
            "• Statement 2 is correct: Keoladeo National Park (1990) and Loktak Lake (1993) remain on the Montreux Record; Chilika Lake was placed on it in 1993 due to siltation and removed in 2002 (winning the Ramsar Wetland Conservation Award).\n"
            "• Statement 3 is correct: Pulicat Lake lies on the AP–TN coast, separated from the Bay of Bengal by the barrier spindle island of Sriharikota (which houses ISRO's Satish Dhawan Space Centre)."
        ),
        "source": "Ministry of Environment, Forest and Climate Change (Wetlands Division)"
    },
    {
        "subject": "Indian Society & Welfare",
        "topic": "106th Constitutional Amendment Act (Nari Shakti Vandan Adhiniyam) & Women's Reservation",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "With reference to the Constitution (One Hundred and Sixth Amendment) Act, 2023 ('Nari Shakti Vandan Adhiniyam'), consider the following statements:\n"
            "1. The Act inserts Articles 330A and 332A into the Constitution to reserve one-third (33%) of all seats for women in the House of the People (Lok Sabha) and in the Legislative Assemblies of all States, including the Legislative Assembly of the NCT of Delhi (under Article 239AA).\n"
            "2. It provides for a horizontal one-third reservation for women within the seats already reserved for Scheduled Castes (SCs) and Scheduled Tribes (STs) in the Lok Sabha and State Legislative Assemblies.\n"
            "3. The Act also mandates a one-third reservation of seats for women in the Council of States (Rajya Sabha) and in State Legislative Councils (Vidhan Parishads).\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statements 1 and 2 are correct: The 106th Constitutional Amendment Act, 2023 inserts Article 239AA(2)(ba) (NCT of Delhi), Article 330A (Lok Sabha), Article 332A (State Assemblies), and Article 334A (commencement after the first Census and subsequent delimitation exercise, with a 15-year sunset clause extendable by Parliament), including 1/3rd quota within SC/ST reserved seats.\n"
            "• Statement 3 is incorrect: There is NO reservation for women in the Rajya Sabha or State Legislative Councils under the 106th Amendment Act."
        ),
        "source": "The Constitution (One Hundred and Sixth Amendment) Act, 2023"
    },
    {
        "subject": "PIB & Govt Schemes Current Affairs",
        "topic": "National Critical Mineral Mission & Offshore Mineral Blocks",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "Consider the following statements regarding the 'National Critical Mineral Mission' and recent reforms under the Mines and Minerals (Development and Regulation) Amendment Act:\n"
            "1. The MMDR Amendment Act removed six atomic/strategic minerals—including Lithium, Beryllium, Niobium, Titanium, Tantalum, and Zirconium—from the list of atomic minerals in Part B of the First Schedule, thereby opening their exploration and mining to the private sector.\n"
            "2. The Central Government has been exclusively empowered to auction mining leases and composite licences for 24 identified 'Critical and Strategic Minerals' listed in Part D of the First Schedule (such as Lithium, Cobalt, Nickel, Rare Earth Elements, Graphite, and Vanadium), while the royalty accrued continues to be paid to the respective State Governments.\n"
            "3. Under the Offshore Areas Mineral (Development and Regulation) Act, State Governments have exclusive jurisdiction to auction mineral blocks up to 200 nautical miles in the Exclusive Economic Zone (EEZ).\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statement 1 is correct: Six minerals (Lithium, Beryllium, Titanium, Niobium, Tantalum, Zirconium) were delisted from the atomic minerals list to allow private participation.\n"
            "• Statement 2 is correct: While the Union Ministry of Mines conducts the e-auction of the 24 critical minerals in Part D of the First Schedule, all auction premium and statutory royalty accrue directly to the State Governments where the mines are located.\n"
            "• Statement 3 is incorrect: Under Article 297 of the Constitution and the OAMDR Act, all minerals in the territorial waters, continental shelf, and Exclusive Economic Zone (EEZ) vest exclusively in the UNION Government, which conducts offshore mineral block auctions."
        ),
        "source": "Ministry of Mines & MMDR Amendment Act"
    },
    {
        "subject": "AP History & Reorganization",
        "topic": "Buddhist Sites of Andhra Pradesh: Amaravati, Nagarjunakonda, Bhattiprolu & Salihundam",
        "question_type": "Pair Matching",
        "question": (
            "Consider the following ancient Buddhist sites in Andhra Pradesh and their distinctive archaeological features:\n"
            "1. Bhattiprolu (Bapatla District) — Yielded early Brahmi inscriptions on crystal/stone reliquaries (c. 3rd century BCE) mentioning King Kuberaka and the 'Gosthi' (guild/committee) system.\n"
            "2. Nagarjunakonda / Vijayapuri (Palnadu District) — Capital of the Ikshvaku dynasty featuring apsidal chaityagrihas, an amphitheatre with acoustic properties, and a Mahachaitya whose relics were salvaged onto an island museum before submergence by the Nagarjunasagar Dam.\n"
            "3. Salihundam (Srikakulam District) — Located on the southern bank of the Vamsadhara River, showing continuity from Theravada to Vajrayana Buddhism (with sculptures of Tara and Marichi).\n"
            "4. Thotlakonda and Bavikonda — Rock-cut cave sites located in Kurnool district on the banks of the Tungabhadra River.\n\n"
            "How many of the above pairs are correctly matched?"
        ),
        "options": [
            "Only one pair",
            "Only two pairs",
            "Only three pairs",
            "All four pairs"
        ],
        "correct_index": 2,
        "explanation": (
            "Only three pairs (Pairs 1, 2, and 3) are correctly matched; Pair 4 is incorrect.\n"
            "• Pairs 1, 2, and 3 are correct: Bhattiprolu (Pratipalapura) yielded pre-Ashokan/Ashokan-era southern Brahmi caskets mentioning King Kuberaka; Nagarjunakonda (Vijayapuri) was the Ikshvaku capital; Salihundam on the Vamsadhara river in Srikakulam was a major port-monastery site.\n"
            "• Pair 4 is incorrect: Thotlakonda and Bavikonda are coastal hilltop Buddhist monastic complexes overlooking the Bay of Bengal in VISAKHAPATNAM district (not Kurnool district)."
        ),
        "source": "Archaeological Survey of India & Ancient History of Andhra Pradesh"
    },
    {
        "subject": "Indian Polity & Constitution",
        "topic": "Tenth Schedule (Anti-Defection Law) & Parliamentary Privileges (Sita Soren Case)",
        "question_type": "Multi-Statement Analysis",
        "question": (
            "Consider the following statements regarding recent constitutional rulings on legislative immunity and the Tenth Schedule:\n"
            "1. In 'Sita Soren vs. Union of India' (2024), a 7-Judge Constitution Bench of the Supreme Court overruled the 1998 'P.V. Narasimha Rao' judgment and held that MPs and MLAs do NOT enjoy immunity under Articles 105(2) and 194(2) from criminal prosecution for accepting bribes to cast a vote or ask a question in the Legislature.\n"
            "2. According to the Supreme Court, the offence of bribery under the Prevention of Corruption Act is complete the moment an legislator accepts the illegal gratification, regardless of whether they subsequently vote or speak in the House as agreed.\n"
            "3. Under the Tenth Schedule of the Constitution, an independent member of a House becomes disqualified only if they join a political party AFTER the expiry of six months from the date of taking their seat.\n\n"
            "Which of the statements given above are correct?"
        ),
        "options": [
            "1 and 2 only",
            "2 and 3 only",
            "1 and 3 only",
            "1, 2 and 3"
        ],
        "correct_index": 0,
        "explanation": (
            "Statements 1 and 2 are correct; Statement 3 is incorrect.\n"
            "• Statements 1 and 2 are correct: The unanimous 7-Judge Constitution Bench in Sita Soren (2024) overruled the 5-Judge P.V. Narasimha Rao (JMM Bribery) ruling and held that legislative privilege under Articles 105(2)/194(2) is tied to collective deliberative functioning and does not shield bribery.\n"
            "• Statement 3 is incorrect: Under Paragraph 2(2) of the Tenth Schedule, an elected INDEPENDENT member becomes disqualified IMMEDIATELY upon joining any political party after the election; the 6-month window applies only to NOMINATED members under Paragraph 2(3)."
        ),
        "source": "Supreme Court 7-Judge Constitution Bench (Sita Soren vs. Union of India) & Tenth Schedule"
    }
]


def run_compiler(question_count=40, save_to_db=True):
    print("[1/2] Compiling Authentic APPSC Group-I & Group-II Current Affairs + Static GS Exam...")
    questions = []
    for idx in range(question_count):
        base = dict(AUTHENTIC_CA_EXAM_QUESTIONS[idx % len(AUTHENTIC_CA_EXAM_QUESTIONS)])
        base["q_no"] = idx + 1
        base["id"] = f"APPSC-CA-Q{idx + 1:03d}"
        questions.append(base)

    new_test = {
        "test_id": "APPSC-JAN2027-CA-STATIC",
        "title": f"Current Affairs & Static GS Special Full Mock Exam ({question_count} Qs)",
        "exam_group": "Group 1 & 2",
        "category": "Current Affairs & Static GS",
        "duration_minutes": 45 if question_count == 40 else question_count,
        "question_count": len(questions),
        "total_marks": float(len(questions)),
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": [
            "PIB & Govt Schemes Current Affairs",
            "Indian & AP Economy",
            "Indian Polity & Constitution",
            "Geography of India & AP",
            "Science, Tech & Environment",
            "AP History & Reorganization",
            "Indian Society & Welfare"
        ],
        "description": "Authentic APPSC Group-I & Group-II exam-grade questions integrating National, International, Science & Tech, Economic Survey/Budget, Supreme Court Judgments, and Andhra Pradesh State Current Affairs with Static GS.",
        "source_portal": "Union & AP Budget, Economic Survey, PIB, PRS Legislative Research & Supreme Court Judgments",
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "questions": questions
    }

    if save_to_db and os.path.exists(DB_PATH):
        with open(DB_PATH, "r", encoding="utf-8") as f:
            db = json.load(f)
        db["tests"] = [
            t for t in db["tests"]
            if not str(t.get("test_id", "")).startswith("APPSC-PIB-LIVE-")
            and t.get("test_id") != "APPSC-JAN2027-CA-STATIC"
        ]
        insert_pos = 8 if len(db["tests"]) >= 8 else 0
        db["tests"].insert(insert_pos, new_test)
        db["total_tests"] = len(db["tests"])
        db["generated_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(DB_PATH, "w", encoding="utf-8") as f:
            json.dump(db, f, indent=2, ensure_ascii=False)
        print(f"[2/2] Added '{new_test['test_id']}' ({len(questions)} Qs) to database! Total tests now: {db['total_tests']}")
    else:
        out_single = os.path.join(DATA_DIR, "latest_pib_test.json")
        with open(out_single, "w", encoding="utf-8") as f:
            json.dump(new_test, f, indent=2, ensure_ascii=False)
        print(f"[2/2] Saved Current Affairs + Static Test to {out_single}")

    return new_test


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="APPSC Authentic Current Affairs + Static GS Compiler")
    parser.add_argument("--questions", type=int, default=40, help="Number of questions to generate in the test")
    parser.add_argument("--no-save-db", action="store_true", help="Save only to latest_pib_test.json without modifying tests_db.json")
    args = parser.parse_args()
    run_compiler(question_count=args.questions, save_to_db=not args.no_save_db)
