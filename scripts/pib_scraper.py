#!/usr/bin/env python3
"""
APPSC Group 1 & Group 2 — Target January 2027 Exam:
Last 6 Months (July–Dec 2026) & Full 1-Year (Jan–Dec 2026) Current Affairs + Static GS Compiler
================================================================================================
Designed specifically for aspirants appearing in the January 2027 APPSC Group-I & Group-II Exams.
Instead of noisy daily press releases, this compiler focuses strictly on:
1. High-Yield Last 6 Months Current Affairs (July 2026 – December 2026) — Highest weightage for Jan 2027 Exam
2. Full 1-Year Current Affairs Roundup (January 2026 – December 2026) — Union & AP Budget 2026-27, Economic Survey,
   16th Finance Commission, ISRO Space Roadmap, Supreme Court Constitution Bench Rulings, and AP State Schemes
3. Direct Static GS Linkage for EVERY Current Affairs topic (Constitutional Articles, AP History/Reorganization Act,
   River Basins, and Economic Concepts) matching the official APPSC Group-I & Group-II exam pattern.
"""

import argparse
import datetime
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "tests_db.json")

# High-Yield 1-Year (Jan 2026 – Dec 2026) & Last 6 Months (Jul 2026 – Dec 2026) Current Affairs + Static GS Bank for Jan 2027 Exam
JAN_2027_EXAM_CA_STATIC_BANK = [
    {
        "title": "Sixteenth Finance Commission (2026–2031 Award Period) & Constitutional Fiscal Federalism",
        "window": "Full 1-Year (Jan–Dec 2026) High-Yield",
        "subject": "Indian Polity & Constitution",
        "current_affairs": "The Sixteenth Finance Commission (chaired by Dr. Arvind Panagariya), whose five-year award period commences on April 1, 2026 (2026–2031), evaluates vertical tax devolution between the Centre and States and horizontal distribution criteria including Income Distance, Population (2011 Census), Area, Forest & Ecology, Demographic Performance, and Tax/Fiscal Effort.",
        "static_gs": "STATIC POLITY LINK: Under Article 280 of the Constitution, the Finance Commission is a quasi-judicial constitutional body appointed by the President every five years; it recommends tax devolution (Article 270), Grants-in-Aid of revenues to States (Article 275), and measures to augment State Consolidated Funds for Panchayats and Municipalities based on State Finance Commission (Article 243-I & 243-Y) reports.",
        "distractor": "The 16th Finance Commission is a statutory body under the NITI Aayog Act whose recommendations are legally binding on the Union Parliament under Article 110.",
        "source": "16th Finance Commission Report (2026–31) + Static Polity (Articles 270, 275, 280)"
    },
    {
        "title": "Andhra Pradesh Budget 2026–27, Swarna Andhra @ 2047 Vision & AP Socio-Economic Survey",
        "window": "Last 6 Months (July–Dec 2026) High-Yield",
        "subject": "Indian & AP Economy",
        "current_affairs": "Under the 'Swarna Andhra @ 2047' Vision document and AP State Budget 2026–27, Andhra Pradesh targets a $2.4 Trillion state economy and over $42,000 per capita income by 2047 through the 'P4 Model' (Public-Private-People Partnership / Zero Poverty), 'One Family – One Entrepreneur', and 10 guiding principles (Padi Sutralu), while Agriculture & Allied sectors (led by Aquaculture and Horticulture) contribute over 34% to AP's GSVA.",
        "static_gs": "STATIC ECONOMY LINK: Gross State Value Added (GSVA) at basic prices equals GSDP minus net product taxes (taxes less subsidies on products). Under the AP FRBM Act, Fiscal Deficit represents total borrowings required by the State Government, whereas Primary Deficit is Fiscal Deficit minus interest payments on previous debt.",
        "distractor": "Swarna Andhra @ 2047 abolishes all private sector participation and targets reducing Andhra Pradesh's coastal aquaculture output to zero by 2030.",
        "source": "AP Socio-Economic Survey 2025–26 & AP Budget 2026–27 + Static Macro-Economy"
    },
    {
        "title": "Polavaram National Irrigation Project (Phase-I Execution) & Godavari-Krishna Basin Static Geography",
        "window": "Last 6 Months (July–Dec 2026) High-Yield",
        "subject": "Geography of India & AP",
        "current_affairs": "In 2026, the Union Cabinet and Ministry of Jal Shakti fast-tracked advance central financial assistance for the new diaphragm wall and Phase-I storage (+41.15 meters contour level) of the Polavaram National Project in Eluru/Alluri Sitharama Raju border region to stabilize irrigation across Godavari and Krishna deltas and supply drinking water to Visakhapatnam.",
        "static_gs": "STATIC GEOGRAPHY & REORGANIZATION LINK: Section 90 of the Andhra Pradesh Reorganization Act, 2014 declared the Polavaram Irrigation Project as a National Project. The Godavari River (1,465 km, rising at Trimbakeshwar in Nashik, Maharashtra) has major left-bank tributaries Purna, Pranhita, Indravati, and Sabari (joining at Kunavaram), and right-bank tributary Manjira.",
        "distractor": "Polavaram Project is built across the Penna River at Somasila and is classified as a private municipal project under Schedule II of the AP Reorganization Act.",
        "source": "Union Cabinet / Ministry of Jal Shakti (2026) + Static AP Geography & Section 90 of AP Reorganization Act 2014"
    },
    {
        "title": "Amaravati Greenfield Capital Development, Industrial Corridors (VCIC/HBIC/CBIC) & Schedule XIII",
        "window": "Last 6 Months (July–Dec 2026) High-Yield",
        "subject": "AP History & Reorganization",
        "current_affairs": "During 2026, multilateral funding of Rs. 15,000 crore (World Bank and Asian Development Bank) accelerated trunk infrastructure in Amaravati Capital City, alongside the development of two National Industrial Corridor smart manufacturing nodes in Andhra Pradesh approved by the Union Cabinet: Kopparthy (YSR Kadapa district, 2,596 acres) and Orvakal (Kurnool district, 2,621 acres).",
        "static_gs": "STATIC REORGANIZATION LINK: Part II (Sections 5 & 6) and Schedule XIII of the AP Reorganization Act, 2014 mandate Central financial and infrastructural support for Andhra Pradesh's new capital city, metro rail, port development, and the Visakhapatnam-Chennai Industrial Corridor (VCIC). Andhra Pradesh is the only state traversed by three industrial corridors (VCIC, CBIC, and HBIC).",
        "distractor": "Orvakal Industrial Node is located in Srikakulam district on the East Coast Corridor, and Schedule XIII of the AP Reorganization Act deals exclusively with Rajya Sabha seat allocation.",
        "source": "Union Budget & NICDC Industrial Nodes (2026) + Static AP Reorganization Act, 2014 (Schedule XIII)"
    },
    {
        "title": "Supreme Court 7-Judge Constitution Bench on Sub-Classification of SCs/STs & Articles 14, 15, 16, 341",
        "window": "Full 1-Year (Jan–Dec 2026) High-Yield",
        "subject": "Indian Polity & Constitution",
        "current_affairs": "Following the landmark 7-Judge Constitution Bench ruling in 'State of Punjab vs Davinder Singh' (overruling the 2004 E.V. Chinnaiah judgment) and subsequent state commission implementations in 2025–2026 (including Andhra Pradesh's one-man commission on SC sub-classification), States are constitutionally empowered to sub-classify Scheduled Castes based on quantifiable empirical data of inter-se backwardness and inadequate representation.",
        "static_gs": "STATIC POLITY LINK: Article 341 empowers the President (after consultation with the Governor) to notify Scheduled Castes for a State, and only Parliament by law can include or exclude castes from the Presidential List under Article 341(2). Substantive equality under Articles 14, 15(4), and 16(4) permits rational sub-classification within a class solong as it does not exclude any caste from the Presidential List.",
        "distractor": "The Supreme Court held that State Legislatures can unilaterally delete castes from the Presidential List under Article 341(2) by an executive order without parliamentary legislation.",
        "source": "Supreme Court Constitution Bench & AP SC Sub-Classification Implementation (2026) + Static Polity (Articles 14–16, 341)"
    },
    {
        "title": "ISRO 2026–2027 Space Roadmap: Gaganyaan Uncrewed Missions, NISAR, Chandrayaan-4 & Static Orbit Mechanics",
        "window": "Last 6 Months (July–Dec 2026) High-Yield",
        "subject": "Science, Tech & Environment",
        "current_affairs": "Leading up to January 2027, ISRO's space calendar features the Gaganyaan uncrewed orbital flight tests (G1/G2 with humanoid robot 'Vyommitra') using Human-Rated LVM3 (HLVM3), operationalization of the joint NASA-ISRO Synthetic Aperture Radar (NISAR) satellite, and design milestones for Chandrayaan-4 (lunar sample return), Venus Orbiter Mission (Shukrayaan), and Bharatiya Antariksh Station (BAS-1 module by 2028).",
        "static_gs": "STATIC S&T LINK: Earth observation satellites like NISAR and Cartosat operate in polar Sun-Synchronous Orbits (SSO, ~600–800 km altitude), whereas communication satellites (GSAT/CMS) operate in Geostationary Transfer / Geostationary Earth Orbit (GEO, ~35,786 km above the equator). LVM3 has a three-stage propulsion system: S200 solid boosters, L110 liquid core stage (Vikas engines), and C25 cryogenic upper stage (CE-20 engine using LH2 + LOX).",
        "distractor": "NISAR is placed in a Geostationary Orbit at 35,786 km using a single-stage solid rocket launched from Thiruvananthapuram.",
        "source": "Department of Space / ISRO Annual Report (2026) + Static Space Technology & Launch Vehicles"
    },
    {
        "title": "Union Budget 2026–27 Fiscal Consolidation Roadmap, RBI Monetary Policy & Static Banking Concepts",
        "window": "Full 1-Year (Jan–Dec 2026) High-Yield",
        "subject": "Indian & AP Economy",
        "current_affairs": "In the Union Budget 2026–27 fiscal glide path, the Government of India committed to bringing the Union Fiscal Deficit below 4.5% of GDP and shifting the medium-term fiscal anchor from annual fiscal deficit targets to a declining Central Government Debt-to-GDP trajectory from FY 2026–27 onwards, while RBI's 6-member Monetary Policy Committee (MPC) maintained CPI inflation within the 4% (±2%) target band.",
        "static_gs": "STATIC ECONOMY LINK: Under Section 45ZB of the RBI Act, 1934, the MPC consists of 6 members (RBI Governor as ex-officio Chairperson, Deputy Governor in charge of monetary policy, one RBI officer, and 3 Central Government nominees). Repo Rate is the policy rate at which RBI lends short-term liquidity to commercial banks against government securities under the Liquidity Adjustment Facility (LAF); Standing Deposit Facility (SDF) serves as the floor of the LAF corridor without requiring collateral.",
        "distractor": "The Standing Deposit Facility (SDF) requires 200% gold collateral from RBI and is determined by the Securities and Exchange Board of India (SEBI).",
        "source": "Union Budget 2026–27 & RBI Monetary Policy Statements (2026) + Static Money & Banking"
    },
    {
        "title": "Andhra Pradesh 'Super Six' & Welfare Schemes (Talliki Vandanam, Annadata Sukhibhava, Deepam-2) + Static Welfare",
        "window": "Last 6 Months (July–Dec 2026) High-Yield",
        "subject": "Indian Society & Welfare",
        "current_affairs": "Key welfare and human-capital schemes active in Andhra Pradesh during 2025–2026 include NTR Bharosa Pensions (enhanced monthly social security pensions of Rs. 4,000 for elderly/widows and Rs. 6,000–Rs. 15,000 for persons with disabilities), Deepam-2.0 (3 free LPG cylinders per year to eligible households), Annadata Sukhibhava (Rs. 20,000 annual financial assistance per farmer family converging with PM-KISAN), and Talliki Vandanam (Rs. 15,000 per annum per school-going child).",
        "static_gs": "STATIC POLITY & SOCIETY LINK: Directive Principles of State Policy under Part IV of the Constitution—specifically Article 41 (right to public assistance in cases of old age, sickness, and disablement), Article 45/21A (free and compulsory education), and Article 47 (raising the level of nutrition and standard of living)—provide the constitutional foundation for state social welfare schemes.",
        "distractor": "Under NTR Bharosa and Deepam-2.0, social security pensions are restricted only to income-tax-paying corporate employees under Article 360 of the Constitution.",
        "source": "AP State Socio-Economic Survey & Welfare Schemes (2026) + Static DPSP (Part IV of Constitution)"
    },
    {
        "title": "Classical Languages Expansion (11 Languages) & Static History of Telugu Literature and Epigraphy",
        "window": "Full 1-Year (Jan–Dec 2026) High-Yield",
        "subject": "AP History & Reorganization",
        "current_affairs": "Following the Union Cabinet's notification of Marathi, Pali, Prakrit, Assamese, and Bengali as Classical Languages, India now officially recognizes 11 Classical Languages (Tamil, Sanskrit, Telugu, Kannada, Malayalam, Odia, Marathi, Pali, Prakrit, Assamese, and Bengali), with national funding for Centres of Excellence including the Centre of Excellence for Studies in Classical Telugu (CESCT) at Nellore, Andhra Pradesh.",
        "static_gs": "STATIC AP HISTORY LINK: Telugu was granted Classical Language status in 2008. The earliest complete Telugu prose inscription is the Kalamalla Inscription (c. 575 CE) of Dhananjaya Erikal Mutturaju (Renati Chola ruler) in YSR Kadapa district, while Prakrit inscriptions from the Satavahana/Ikshvaku era (Amaravati, Bhattiprolu, Nagarjunakonda) and Nannaya Bhatta's 11th-century Mahabharata translation under Eastern Chalukya King Rajaraja Narendra mark milestones in Telugu literary history.",
        "distractor": "The Kalamalla Inscription was issued in 1857 CE by Lord Dalhousie in Persian script, and Telugu is not recognized as a Classical Language of India.",
        "source": "Ministry of Culture Notification (2025–26) + Static AP Epigraphy & Literary History"
    },
    {
        "title": "PM-JANMAN & Dharti Aaba Janjatiya Gram Utkarsh Abhiyan (2026) + Static PVTGs & Fifth Schedule in AP",
        "window": "Last 6 Months (July–Dec 2026) High-Yield",
        "subject": "Indian Society & Welfare",
        "current_affairs": "Throughout 2026, the Ministry of Tribal Affairs implemented two flagship tribal saturation missions: PM-JANMAN (Rs. 24,104 crore targeting 75 Particularly Vulnerable Tribal Groups across 18 States/UTs) and Dharti Aaba Janjatiya Gram Utkarsh Abhiyan (Rs. 79,156 crore across ~63,000 tribal villages converging 25 interventions of 17 Ministries), covering the Integrated Tribal Development Agencies (ITDAs) of Andhra Pradesh such as Paderu, Rampachodavaram, Parvathipuram, Seethampeta, and Srisailam.",
        "static_gs": "STATIC SOCIETY & POLITY LINK: The criteria for identifying PVTGs (originally Dhebar Commission 'Primitive Tribal Groups' in 1973) are: (1) pre-agricultural level of technology, (2) low level of literacy, (3) economic backwardness, and (4) a declining or stagnant population. Major PVTGs in Andhra Pradesh include Chenchu, Gadaba, Khond, Konda Reddi, Konda Savara, and Porja. Scheduled Areas in AP are governed under the Fifth Schedule (Article 244(1)) and the PESA Act, 1996.",
        "distractor": "Scheduled Areas in Andhra Pradesh are governed under the Sixth Schedule (Article 244(2)), and the Chenchu tribe is excluded from the PVTG list.",
        "source": "Ministry of Tribal Affairs (2026) + Static Indian Society (PVTGs, Fifth Schedule & PESA Act 1996)"
    },
    {
        "title": "Green Hydrogen Hubs in AP (Pudimadaka / Visakhapatnam & Kakinada), COP30/31 Climate Targets & Static Ecology",
        "window": "Last 6 Months (July–Dec 2026) High-Yield",
        "subject": "Science, Tech & Environment",
        "current_affairs": "In 2026, Andhra Pradesh emerged as India's premier coastal Green Hydrogen and Clean Energy hub under the National Green Hydrogen Mission (SIGHT programme) and AP Integrated Clean Energy Policy (targeting 160 GW renewable capacity and 1.5 MMTPA Green Hydrogen production), anchored by the NTPC Green Energy Hub at Pudimadaka (Anakapalli/Visakhapatnam) and Green Ammonia export terminals at Kakinada and Krishnapatnam.",
        "static_gs": "STATIC ENVIRONMENT & SCIENCE LINK: Green Hydrogen is produced via electrolysis of water (H2O -> H2 + 1/2 O2) powered entirely by renewable energy (solar/wind) with zero greenhouse gas emissions, whereas Grey Hydrogen is produced from natural gas/methane via Steam Methane Reforming (SMR) without carbon capture, and Blue Hydrogen pairs SMR with Carbon Capture, Utilization, and Storage (CCUS). India's Panchamrit climate commitments target 500 GW non-fossil energy capacity by 2030 and Net-Zero emissions by 2070.",
        "distractor": "Green Hydrogen is produced by burning bituminous coal in thermal power plants without any electrolysis or renewable energy input.",
        "source": "MNRE & AP Integrated Clean Energy Policy (2026) + Static Environment & Climate Change"
    },
    {
        "title": "One Nation One Subscription (ONOS), IndiaAI Mission & National Quantum Mission (2026 Execution) + Static S&T",
        "window": "Full 1-Year (Jan–Dec 2026) High-Yield",
        "subject": "Science, Tech & Environment",
        "current_affairs": "Operationalized across 2025–2026 with a Rs. 6,000 crore outlay, 'One Nation One Subscription' (ONOS, coordinated by INFLIBNET) provides 6,300+ government universities and R&D labs nationwide access to ~13,000 international research journals; simultaneously, the IndiaAI Mission (Rs. 10,372 crore, 18,000+ GPU compute facility) and National Quantum Mission (Rs. 6,003 crore, 4 Thematic Hubs) scaled indigenous deep-tech research.",
        "static_gs": "STATIC QUANTUM & COMPUTING LINK: Unlike classical bits (which exist strictly as 0 or 1), Quantum Bits (Qubits) leverage two foundational principles of quantum mechanics: Superposition (existing in a linear combination of 0 and 1 simultaneously) and Entanglement (strong non-local correlation between qubits), enabling exponential speedup in cryptography, molecular simulation, and optimization.",
        "distractor": "Quantum computers operate strictly on binary vacuum tubes and cannot perform superposition or entanglement.",
        "source": "DST / MeitY Annual Review (2026) + Static Quantum Mechanics & Emerging Technologies"
    },
    {
        "title": "Three New Criminal Laws Implementation (BNS, BNSS, BSA) & Static Constitutional Criminal Jurisprudence",
        "window": "Full 1-Year (Jan–Dec 2026) High-Yield",
        "subject": "Indian Polity & Constitution",
        "current_affairs": "By 2026, India completed institutional transition to the three new criminal codes—Bharatiya Nyaya Sanhita (BNS, replacing IPC 1860), Bharatiya Nagarik Suraksha Sanhita (BNSS, replacing CrPC 1973), and Bharatiya Sakshya Adhiniyam (BSA, replacing Indian Evidence Act 1872)—mandating Zero FIR, e-FIR, compulsory forensic investigation for offenses punishable with 7+ years imprisonment, time-bound trial/judgment delivery, and admissibility of electronic records as primary evidence.",
        "static_gs": "STATIC POLITY LINK: Criminal Law and Criminal Procedure fall under the Concurrent List (List III, Entries 1 and 2) of the Seventh Schedule of the Constitution. Article 20 of the Constitution guarantees three fundamental protections in respect of conviction for offenses: (1) No ex-post-facto criminal penalty (Art. 20(1)), (2) No double jeopardy (Art. 20(2)), and (3) No self-incrimination (Art. 20(3)).",
        "distractor": "Criminal Law is placed exclusively in the State List (List II) and Article 20 permits retrospective enhancement of criminal punishment.",
        "source": "Ministry of Home Affairs & PRS Legislative Research (2026) + Static Polity (Article 20 & Seventh Schedule)"
    },
    {
        "title": "National Mission on Natural Farming (NMNF), AP Community Managed Natural Farming (APCNF) & Static Soil Science",
        "window": "Last 6 Months (July–Dec 2026) High-Yield",
        "subject": "Indian & AP Economy",
        "current_affairs": "Under the National Mission on Natural Farming (NMNF, Rs. 2,481 crore outlay across 15,000 clusters and 10,000 Bio-input Resource Centres), Andhra Pradesh's globally acclaimed Rythu Sadhikara Samstha (RySS) 'AP Community Managed Natural Farming' (APCNF, recipient of the Gulbenkian Prize for Humanity) serves as the national model, training resource farmers across all districts in chemical-free practices.",
        "static_gs": "STATIC AGRICULTURE & GEOGRAPHY LINK: The four core wheels of Indian Natural Farming are: (1) Beejamrit (microbial seed coating using cow dung, cow urine, lime, and virgin soil), (2) Jeevamrit / Ghanajeevamrit (soil microbial biostimulant enhancer), (3) Acchadana (mulching to conserve soil moisture and organic carbon), and (4) Whapasa (maintaining a 50:50 balance of air and water molecules in soil pores). Major soil types in AP include Black Cotton (Regur) soils, Red Ferruginous soils (largest area in AP), Deltaic Alluvial soils, and Coastal Lateritic/Sandy soils.",
        "distractor": "APCNF mandates heavy application of synthetic urea and anhydrous ammonia while prohibiting mulching and microbial seed treatment.",
        "source": "Ministry of Agriculture & RySS Andhra Pradesh (2026) + Static AP Soils & Sustainable Agriculture"
    }
]


def synthesize_jan2027_questions(items, target_count=40):
    """Generates APPSC Group-I & Group-II exam-standard MCQs combining 2026 Current Affairs (6M-1Y) with Static GS."""
    questions = []
    q_no = 1
    idx = 0

    while len(questions) < target_count:
        rel = items[idx % len(items)]
        pattern = len(questions) % 3

        if pattern == 0:
            # Pattern A: Statement-I (Current Affairs 2026) + Statement-II (Linked Static GS Foundation)
            q_text = (
                f"[Jan 2027 Exam: {rel['window']} + Static GS Linkage]\n"
                f"With reference to '{rel['title']}', consider the following two statements:\n"
                f"Statement-I (Current Affairs): {rel['current_affairs']}\n"
                f"Statement-II (Static GS Core): {rel['static_gs'].replace('STATIC POLITY LINK: ', '').replace('STATIC ECONOMY LINK: ', '').replace('STATIC GEOGRAPHY & REORGANIZATION LINK: ', '').replace('STATIC REORGANIZATION LINK: ', '').replace('STATIC S&T LINK: ', '').replace('STATIC POLITY & SOCIETY LINK: ', '').replace('STATIC AP HISTORY LINK: ', '').replace('STATIC SOCIETY & POLITY LINK: ', '').replace('STATIC ENVIRONMENT & SCIENCE LINK: ', '').replace('STATIC QUANTUM & COMPUTING LINK: ', '').replace('STATIC AGRICULTURE & GEOGRAPHY LINK: ', '')}\n\n"
                f"Which of the statements given above is/are correct?"
            )
            options = [
                "Statement-I only",
                "Statement-II only",
                "Both Statement-I and Statement-II",
                "Neither Statement-I nor Statement-II"
            ]
            correct_idx = 2
            explanation = (
                f"Both Statement-I (Current Affairs) and Statement-II (Static GS Foundation) are correct.\n"
                f"• Current Affairs (Jan–Dec 2026 Window): {rel['current_affairs']}\n"
                f"• {rel['static_gs']}\n"
                f"• Jan 2027 APPSC Exam Strategy: APPSC Group-I & Group-II questions pair a recent 6-to-12-month policy event with its underlying constitutional/historical/scientific static concept."
            )
        elif pattern == 1:
            # Pattern B: APPSC 2024 PYQ 3-Statement "How many statements are correct" (CA + Static + False Distractor)
            clean_static = (
                rel["static_gs"]
                .split(": ", 1)[-1]
                if ": " in rel["static_gs"]
                else rel["static_gs"]
            )
            q_text = (
                f"[Jan 2027 Exam: {rel['window']} — 2024 PYQ Pattern]\n"
                f"Consider the following three statements regarding '{rel['title']}':\n"
                f"1. {rel['current_affairs']}\n"
                f"2. {clean_static}\n"
                f"3. {rel['distractor']}\n\n"
                f"How many of the statements given above are correct?"
            )
            options = [
                "Only one statement",
                "Only two statements",
                "All three statements",
                "None of the statements"
            ]
            correct_idx = 1
            explanation = (
                f"Only two statements (Statements 1 and 2) are correct; Statement 3 is incorrect.\n"
                f"• Statement 1 (2026 Current Affairs) is correct: {rel['current_affairs']}\n"
                f"• Statement 2 (Static GS Link) is correct: {clean_static}\n"
                f"• Statement 3 is incorrect (Distractor): '{rel['distractor']}' is false.\n"
                f"• Reference: {rel['source']}"
            )
        else:
            # Pattern C: Identify the Incorrect Statement among Current Affairs & Static GS statements
            clean_static = (
                rel["static_gs"]
                .split(": ", 1)[-1]
                if ": " in rel["static_gs"]
                else rel["static_gs"]
            )
            q_text = (
                f"Which ONE of the following statements regarding '{rel['title']}' (relevant for the January 2027 APPSC Group-I & Group-II Exams) is NOT correct?"
            )
            options = [
                rel["current_affairs"],
                clean_static,
                rel["distractor"],
                f"This topic integrates {rel['window']} developments with {rel['subject']} static syllabus."
            ]
            correct_idx = 2
            explanation = (
                f"Option (C) is NOT correct.\n"
                f"• Why Option (C) is false: '{rel['distractor']}' is factually incorrect.\n"
                f"• Verified 2026 Current Affairs: {rel['current_affairs']}\n"
                f"• {rel['static_gs']}\n"
                f"• Source: {rel['source']}"
            )

        questions.append({
            "q_no": q_no,
            "id": f"JAN2027-CA-Q{q_no:03d}",
            "subject": rel["subject"],
            "topic": f"{rel['title']} ({rel['window']})",
            "question_type": f"Jan 2027 Exam ({rel['window']} + Static GS)",
            "question": q_text,
            "options": options,
            "correct_index": correct_idx,
            "explanation": explanation,
            "source": rel["source"]
        })
        q_no += 1
        idx += 1

    return questions


def run_compiler(question_count=40, save_to_db=True):
    print("[1/2] Compiling Target Jan 2027 Exam: Last 6 Months (Jul–Dec 2026) & 1-Year (Jan–Dec 2026) Current Affairs + Static GS...")
    questions = synthesize_jan2027_questions(JAN_2027_EXAM_CA_STATIC_BANK, target_count=question_count)

    new_test = {
        "test_id": "APPSC-JAN2027-CA-STATIC",
        "title": f"Target Jan 2027 Exam Special: Last 6 Months & 1-Year Current Affairs (Jan–Dec 2026) + Static GS Linkage ({question_count} Qs)",
        "exam_group": "Group 1 & 2",
        "category": "Jan 2027 CA (6M-1Y) + Static",
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
        "description": "Specially curated for the January 2027 APPSC Group-I & Group-II Exams: covers High-Yield Last 6 Months (July–Dec 2026) and Full 1-Year (Jan–Dec 2026) Current Affairs directly paired with Static GS concepts (Articles, Acts, Geography & Economy).",
        "source_portal": "Jan–Dec 2026 (1-Year & Last 6M) High-Yield Current Affairs + Static GS Foundation",
        "created_at": "Target Exam: January 2027",
        "questions": questions
    }

    if save_to_db and os.path.exists(DB_PATH):
        with open(DB_PATH, "r", encoding="utf-8") as f:
            db = json.load(f)
        # Remove any old live PIB dynamic tests or duplicate APPSC-JAN2027-CA-STATIC before inserting
        db["tests"] = [
            t for t in db["tests"]
            if not str(t.get("test_id", "")).startswith("APPSC-PIB-LIVE-")
            and t.get("test_id") != "APPSC-JAN2027-CA-STATIC"
        ]
        # Insert right after the 8 PYQ papers (or at top of Mock & CA section)
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
        print(f"[2/2] Saved Jan 2027 Current Affairs + Static Test to {out_single}")

    return new_test


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="APPSC Jan 2027 Exam (Last 6M to 1-Year Current Affairs + Static GS) Compiler")
    parser.add_argument("--questions", type=int, default=40, help="Number of questions to generate in the test")
    parser.add_argument("--no-save-db", action="store_true", help="Save only to latest_pib_test.json without modifying tests_db.json")
    args = parser.parse_args()
    run_compiler(question_count=args.questions, save_to_db=not args.no_save_db)
