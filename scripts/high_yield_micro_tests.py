#!/usr/bin/env python3
"""
APPSC Group 1 & Group 2 — High-Yield Micro-Test Database
=========================================================
Contains 4 dedicated, focused micro-tests (20 questions each, 15-20 min CBT drills)
on the most heavily tested APPSC core traps:
1. AP Reorganisation Act, 2014 (Sections, Schedules, Assets & River Boards)
2. AP Socio-Economic Survey & State Budget 2026–27 (Tables, GSDP, Growth, Schemes)
3. AP River Systems, Irrigation Projects & District Reorganisation Geography
4. 73rd & 74th Constitutional Amendments, Schedules, Articles & Local Governance
"""

HIGH_YIELD_MICRO_TESTS = [
    {
        "test_id": "APPSC-MICRO-01",
        "title": "⚡ Micro-Drill 1: AP Reorganisation Act, 2014 (Sections & Schedules)",
        "exam_group": "Group 1 & 2",
        "category": "High-Yield Micro-Test",
        "duration_minutes": 20,
        "question_count": 20,
        "total_marks": 20.0,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["AP History & Reorganization", "Indian Polity & Constitution"],
        "description": "High-yield 20-minute drill on Andhra Pradesh Reorganisation Act, 2014 (Act 6 of 2014): Sections 3 to 108, Schedules I to XIII, Apex Council, KRMB/GRMB, Polavaram Section 90, and asset division principles.",
        "questions": [
            {
                "q_no": 1,
                "id": "APPSC-MICRO-01-Q01",
                "subject": "AP History & Reorganization",
                "topic": "AP Reorganisation Act, 2014 Structure & Enactment",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "Consider the following statements regarding the structural framework of the Andhra Pradesh Reorganisation Act, 2014 (Act No. 6 of 2014):\n"
                    "1. The Act contains 108 Sections arranged across 12 Parts and 13 Schedules.\n"
                    "2. The Act received Presidential assent on March 1, 2014, and the 'Appointed Day' for the bifurcation of Andhra Pradesh was notified as June 2, 2014.\n"
                    "3. Under Section 3 of the Act, Hyderabad was declared the permanent sole capital of Telangana with immediate effect from the Appointed Day, with no transition period.\n\n"
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
                    "• Statement 1 & 2: The AP Reorganisation Act, 2014 has 108 Sections, 12 Parts, and 13 Schedules. Presidential assent was received on March 1, 2014; Appointed Day was June 2, 2014.\n"
                    "• Statement 3 is incorrect: Under Section 5 of the Act, Hyderabad was designated as the common capital for both Telangana and Andhra Pradesh for a period not exceeding 10 years (ending June 2, 2024)."
                ),
                "source": "AP Reorganisation Act, 2014 (Sections 3, 5 & Gazette of India)"
            },
            {
                "q_no": 2,
                "id": "APPSC-MICRO-01-Q02",
                "subject": "AP History & Reorganization",
                "topic": "Polavaram National Project under Section 90",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Under which Section of the Andhra Pradesh Reorganisation Act, 2014 is the Polavaram Irrigation Project declared a 'National Project' whose execution, environmental clearance, and cost of execution are assumed by the Central Government?"
                ),
                "options": [
                    "Section 85",
                    "Section 90",
                    "Section 94",
                    "Section 108"
                ],
                "correct_index": 1,
                "explanation": (
                    "Section 90(1) of the AP Reorganisation Act, 2014 declares the Polavaram Irrigation Project to be a National Project.\n"
                    "Under Section 90(2), the Central Government assumed the responsibility of executing the project, obtaining all necessary environmental and forest clearances, and financing the irrigation component."
                ),
                "source": "AP Reorganisation Act, 2014 - Part IX (Water Resources Development, Section 90)"
            },
            {
                "q_no": 3,
                "id": "APPSC-MICRO-01-Q03",
                "subject": "AP History & Reorganization",
                "topic": "Schedules IX and X of AP Reorganisation Act, 2014",
                "question_type": "Pair Matching MCQ",
                "question": (
                    "Match List-I (Schedule of AP Reorganisation Act, 2014) with List-II (Subject Matter):\n\n"
                    "List-I (Schedule):\n"
                    "A. Schedule IX\n"
                    "B. Schedule X\n"
                    "C. Schedule XII\n"
                    "D. Schedule XIII\n\n"
                    "List-II (Subject Matter):\n"
                    "1. Infrastructure and Special Economic Measures (Ports, Steel Plant, AIIMS, IIT)\n"
                    "2. 89 Government Companies and Corporations (APSRTC, APGENCO, APTRANSCO)\n"
                    "3. 107 State-level Training Institutions and Centers (AP Police Academy, etc.)\n"
                    "4. Principles for Coal, Power, Oil & Gas allocation (Singareni, APGENCO)\n\n"
                    "Select the correct code:"
                ),
                "options": [
                    "A-2, B-3, C-4, D-1",
                    "A-3, B-2, C-1, D-4",
                    "A-2, B-3, C-1, D-4",
                    "A-4, B-1, C-2, D-3"
                ],
                "correct_index": 0,
                "explanation": (
                    "Correct Matching:\n"
                    "• Schedule IX (Section 68): Lists 89 Government Companies & Corporations to be apportioned.\n"
                    "• Schedule X (Section 75): Lists 107 State Training & Research Institutions where common facilities continue.\n"
                    "• Schedule XII: Governs Power, Coal (Singareni Collieries), and Petroleum allocation.\n"
                    "• Schedule XIII (Section 93): Mandates Central infrastructure measures (New Capital, Vizag Metro, Kadapa Steel Plant, VCIC Industrial Corridor)."
                ),
                "source": "AP Reorganisation Act, 2014 (Schedules IX, X, XII, XIII)"
            },
            {
                "q_no": 4,
                "id": "APPSC-MICRO-01-Q04",
                "subject": "AP History & Reorganization",
                "topic": "Apex Council & River Management Boards (KRMB & GRMB)",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "Regarding the River Management Boards and Apex Council constituted under the Andhra Pradesh Reorganisation Act, 2014, consider the following statements:\n"
                    "1. Under Section 85 of the Act, two separate boards—the Krishna River Management Board (KRMB) and the Godavari River Management Board (GRMB)—were constituted by the Central Government.\n"
                    "2. The Apex Council for Godavari and Krishna river water disputes is chaired by the Union Minister of Jal Shakti, with the Chief Ministers of Andhra Pradesh and Telangana as members.\n"
                    "3. The headquarters of KRMB was permanently mandated in Hyderabad, while GRMB was located in Vijayawada under the First Schedule.\n\n"
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
                    "• Statements 1 & 2: Under Section 85, KRMB and GRMB were established as autonomous corporate bodies. Under Section 84, the Apex Council is chaired by the Union Jal Shakti Minister with both CMs as members.\n"
                    "• Statement 3 is incorrect: Under Section 85(2), the headquarters of KRMB was specified to be located in Andhra Pradesh (subsequently shifted/notified to Visakhapatnam/Vijayawada), while GRMB is in Telangana (Hyderabad)."
                ),
                "source": "AP Reorganisation Act, 2014 (Part IX, Sections 84, 85, 87)"
            },
            {
                "q_no": 5,
                "id": "APPSC-MICRO-01-Q05",
                "subject": "AP History & Reorganization",
                "topic": "Division of Assets, Liabilities & Public Debt (Sections 47–67)",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Under Section 48 and Section 52 of the AP Reorganisation Act, 2014, what is the fundamental criterion adopted for the apportionment of land, immovable assets, and cash balances between Andhra Pradesh and Telangana?"
                ),
                "options": [
                    "Land and immovable property are divided strictly on population ratio, while cash balances follow location ratio",
                    "Land and immovable assets belong to the successor State in which they are physically situated ('location basis'), while cash balances, public debt, and loans are divided on the basis of population ratio (58.32 : 41.68)",
                    "All assets and liabilities are divided strictly in a 50:50 equal ratio between both states",
                    "All immovable assets outside Hyderabad are divided on geographic area ratio"
                ],
                "correct_index": 1,
                "explanation": (
                    "Under Part VI of the Act (Sections 47 to 67):\n"
                    "• Immovable assets (land, buildings, offices) vest in the successor state where they are physically located.\n"
                    "• Cash balances, public debt, and financial liabilities are apportioned on the basis of the 2011 Census population ratio of Andhra Pradesh (58.32%) and Telangana (41.68%)."
                ),
                "source": "AP Reorganisation Act, 2014 (Part VI, Sections 47, 48, 52, 59)"
            },
            {
                "q_no": 6,
                "id": "APPSC-MICRO-01-Q06",
                "subject": "AP History & Reorganization",
                "topic": "Legislative Assembly & Legislative Council Seats (Part III)",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "With reference to the legislative allocation under Part III of the Andhra Pradesh Reorganisation Act, 2014, consider the following:\n"
                    "1. The number of elected seats in the Legislative Assembly of the successor State of Andhra Pradesh was fixed at 175, while Telangana received 119 seats.\n"
                    "2. The strength of the Andhra Pradesh Legislative Council was fixed at 58 seats, while Telangana Legislative Council was allocated 40 seats.\n"
                    "3. Section 26 of the Act provides for future delimitation and increase of assembly seats up to 225 for Andhra Pradesh and 153 for Telangana, subject to Article 170 provisions.\n\n"
                    "Which of the statements given above are correct?"
                ),
                "options": [
                    "1 and 2 only",
                    "2 and 3 only",
                    "1, 2 and 3",
                    "1 and 3 only"
                ],
                "correct_index": 2,
                "explanation": (
                    "All three statements (1, 2, and 3) are correct.\n"
                    "• Assembly Seats: AP = 175, Telangana = 119 (Section 15 & 17).\n"
                    "• Council Seats: AP = 58, Telangana = 40 (Section 22).\n"
                    "• Section 26: Contemplates increasing AP Assembly seats from 175 to 225 and Telangana from 119 to 153."
                ),
                "source": "AP Reorganisation Act, 2014 (Sections 15, 17, 22, 26)"
            },
            {
                "q_no": 7,
                "id": "APPSC-MICRO-01-Q07",
                "subject": "AP History & Reorganization",
                "topic": "High Court Jurisdiction & Establishment (Part IV)",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Under Section 30 and Section 31 of the AP Reorganisation Act, 2014, what provision was made regarding the High Court for Andhra Pradesh?"
                ),
                "options": [
                    "The High Court of Judicature at Hyderabad served as the common High Court until a separate High Court for Andhra Pradesh was constituted under Article 214 with principal seat at Amaravati (operationalized on January 1, 2019)",
                    "Madras High Court was assigned immediate jurisdiction over Coastal Andhra districts",
                    "A bench of the Supreme Court was established at Visakhapatnam to hear AP civil appeals",
                    "The High Court for Andhra Pradesh was immediately operational on June 2, 2014 at Kurnool"
                ],
                "correct_index": 0,
                "explanation": (
                    "Under Section 30, the High Court of Judicature at Hyderabad served as the Common High Court. Under Section 31, a separate High Court for Andhra Pradesh was constituted by Presidential Order with effect from January 1, 2019, with its principal seat at Amaravati."
                ),
                "source": "AP Reorganisation Act, 2014 (Part IV, Sections 30 & 31) & Ministry of Law Notification (2018)"
            },
            {
                "q_no": 8,
                "id": "APPSC-MICRO-01-Q08",
                "subject": "AP History & Reorganization",
                "topic": "Lok Sabha and Rajya Sabha Seat Allocation (Part II)",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "In the Andhra Pradesh Reorganisation Act, 2014, how were the 42 Lok Sabha seats and 18 Rajya Sabha seats of combined Andhra Pradesh apportioned between Andhra Pradesh and Telangana?"
                ),
                "options": [
                    "Lok Sabha: AP 25, Telangana 17 | Rajya Sabha: AP 11, Telangana 7",
                    "Lok Sabha: AP 28, Telangana 14 | Rajya Sabha: AP 12, Telangana 6",
                    "Lok Sabha: AP 21, Telangana 21 | Rajya Sabha: AP 9, Telangana 9",
                    "Lok Sabha: AP 24, Telangana 18 | Rajya Sabha: AP 10, Telangana 8"
                ],
                "correct_index": 0,
                "explanation": (
                    "Under First & Second Schedules:\n"
                    "• Lok Sabha (42 seats total): Andhra Pradesh = 25 seats; Telangana = 17 seats.\n"
                    "• Rajya Sabha (18 seats total): Andhra Pradesh = 11 seats; Telangana = 7 seats."
                ),
                "source": "AP Reorganisation Act, 2014 (Sections 6, 9 & First/Second Schedules)"
            },
            {
                "q_no": 9,
                "id": "APPSC-MICRO-01-Q09",
                "subject": "AP History & Reorganization",
                "topic": "Section 94 Central Financial Support & Capital Development",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "Consider the following provisions under Section 94 of the Andhra Pradesh Reorganisation Act, 2014:\n"
                    "1. Section 94(1) mandates that the Central Government shall provide appropriate fiscal incentives, including tax concessions, to promote industrialization and economic growth in both successor States.\n"
                    "2. Section 94(3) mandates that the Central Government shall provide special financial support for the creation of essential facilities for the new capital of Andhra Pradesh, including Raj Bhavan, High Court, Secretariat, and Legislative Assembly.\n"
                    "3. Section 94(4) mandates the Central Government to fund the establishment of a petroleum refinery and petrochemical complex in Rayalaseema.\n\n"
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
                    "• Statements 1 & 2: Section 94(1) covers tax incentives; Section 94(3) specifically mandates Central funding for capital infrastructure (Raj Bhavan, High Court, Assembly, Secretariat).\n"
                    "• Statement 3 is incorrect: The crude oil refinery and petrochemical complex (HPCL expansion/new complex) is mentioned under Schedule XIII item 3 for Coastal Andhra (Kakinada/Visakhapatnam), not Rayalaseema."
                ),
                "source": "AP Reorganisation Act, 2014 (Section 94 & Schedule XIII)"
            },
            {
                "q_no": 10,
                "id": "APPSC-MICRO-01-Q10",
                "subject": "AP History & Reorganization",
                "topic": "Schedule XIII Educational & Infrastructure Institutions",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "Which of the following National Premier Institutions were mandated to be established in Andhra Pradesh under Schedule XIII of the AP Reorganisation Act, 2014?\n"
                    "1. Indian Institute of Technology (IIT) at Tirupati\n"
                    "2. Indian Institute of Management (IIM) at Visakhapatnam\n"
                    "3. All India Institute of Medical Sciences (AIIMS) at Mangalagiri\n"
                    "4. National Institute of Technology (NIT) at Tadepalligudem\n\n"
                    "Select the correct answer using the code given below:"
                ),
                "options": [
                    "1, 2, 3 and 4",
                    "1 and 2 only",
                    "2, 3 and 4 only",
                    "1, 3 and 4 only"
                ],
                "correct_index": 0,
                "explanation": (
                    "All 4 institutions were established under Schedule XIII of the Act:\n"
                    "• IIT Tirupati\n"
                    "• IIM Visakhapatnam\n"
                    "• AIIMS Mangalagiri\n"
                    "• NIT Tadepalligudem (West Godavari)\n"
                    "Other institutions include IISER Tirupati, IIIT Kurnool, Central University of AP (Anantapur), and Tribal University (Salur/Vizianagaram)."
                ),
                "source": "AP Reorganisation Act, 2014 (Schedule XIII Education Provisions)"
            },
            {
                "q_no": 11,
                "id": "APPSC-MICRO-01-Q11",
                "subject": "AP History & Reorganization",
                "topic": "Section 8 – Special Responsibilities of Governor for Common Capital",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "What special responsibility was vested in the Governor under Section 8 of the AP Reorganisation Act, 2014 during the period when Hyderabad functioned as the common capital?"
                ),
                "options": [
                    "Responsibility for the security of life, liberty and property of all citizens residing in the common capital area of Hyderabad",
                    "Sole power to allocate municipal taxes of Greater Hyderabad Municipal Corporation (GHMC)",
                    "Power to dissolve the Telangana Assembly without aid and advice",
                    "Direct command over the armed forces deployed in Andhra Pradesh"
                ],
                "correct_index": 0,
                "explanation": (
                    "Section 8 of the Act provided that the Governor of Telangana (acting as common Governor) had special responsibility for the security of life, liberty and property, and the allocation of government buildings in the common capital area of Hyderabad."
                ),
                "source": "AP Reorganisation Act, 2014 (Section 8)"
            },
            {
                "q_no": 12,
                "id": "APPSC-MICRO-01-Q12",
                "subject": "AP History & Reorganization",
                "topic": "Section 46 – Apportionment of Expenditure and Taxes",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Under Section 46 of the AP Reorganisation Act, 2014, how is the financial liability for pension payments to retired employees of the erstwhile undivided State of Andhra Pradesh apportioned?"
                ),
                "options": [
                    "On the basis of the population ratio of Andhra Pradesh (58.32%) and Telangana (41.68%)",
                    "On the basis of the birthplace of the pensioner",
                    "Borne 100% by the Union Ministry of Finance",
                    "Borne exclusively by Telangana where the pension treasury is located"
                ],
                "correct_index": 0,
                "explanation": (
                    "Under Section 59 and Eighth Schedule of the Act, pension liabilities for employees who retired prior to the Appointed Day are shared between Andhra Pradesh and Telangana strictly in proportion to their population ratio (58.32% : 41.68%)."
                ),
                "source": "AP Reorganisation Act, 2014 (Section 59 & Eighth Schedule)"
            },
            {
                "q_no": 13,
                "id": "APPSC-MICRO-01-Q13",
                "subject": "AP History & Reorganization",
                "topic": "Section 7 – Common Governor",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Under Section 7 of the AP Reorganisation Act, 2014, what provision was made regarding the office of the Governor?"
                ),
                "options": [
                    "The Governor of the existing State of Andhra Pradesh became the common Governor for both the successor States for such period as may be determined by the President",
                    "Two separate Governors were mandatory from day one (June 2, 2014)",
                    "The Chief Justice of the High Court acted as Administrator for Andhra Pradesh",
                    "The President assumed direct administration of Andhra Pradesh under Article 356"
                ],
                "correct_index": 0,
                "explanation": (
                    "Section 7 provided that on and from the Appointed Day, the Governor of the existing State of Andhra Pradesh (E.S.L. Narasimhan) was to be the Governor for both Andhra Pradesh and Telangana for a period determined by the President (served until 2019)."
                ),
                "source": "AP Reorganisation Act, 2014 (Section 7)"
            },
            {
                "q_no": 14,
                "id": "APPSC-MICRO-01-Q14",
                "subject": "AP History & Reorganization",
                "topic": "Section 92 & Schedule XII – Power Generation & PPA Sharing",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "Regarding power allocation and Power Purchase Agreements (PPAs) under Section 92 and Schedule XII of the AP Reorganisation Act, 2014, consider the following:\n"
                    "1. Power generated from APGENCO thermal and hydel power stations was apportioned between AP and Telangana based on historical power consumption ratios (46.11% to AP and 53.89% to Telangana).\n"
                    "2. All unallocated power from Central Generating Stations (NTPC Ramagundam, Simhadri, etc.) was allocated exclusively to Andhra Pradesh.\n\n"
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
                    "Statement 1 is correct; Statement 2 is incorrect.\n"
                    "• Statement 1: Power from existing APGENCO stations was divided based on the 4-year average historical consumption of DISCOMs (AP: 46.11%, Telangana: 53.89%).\n"
                    "• Statement 2: Central Generating Stations power was allocated in the same ratio of 46.11 : 53.89, with a dedicated 4,000 MW thermal power plant mandated for Telangana under NTPC."
                ),
                "source": "AP Reorganisation Act, 2014 (Schedule XII Power Sector Principles)"
            },
            {
                "q_no": 15,
                "id": "APPSC-MICRO-01-Q15",
                "subject": "AP History & Reorganization",
                "topic": "Part VII – State Public Service Commissions",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Under Section 83 of the AP Reorganisation Act, 2014, what provision was made regarding the Public Service Commission?"
                ),
                "options": [
                    "The Public Service Commission for the existing State of Andhra Pradesh became the PSC for the successor State of Andhra Pradesh (APPSC), while Telangana constituted TSPSC under Article 315",
                    "A single Joint Public Service Commission (JSPSC) was permanently established for both states",
                    "UPSC was mandated to conduct all state civil service exams for 10 years",
                    "APPSC was dissolved and reconstituted as a municipal board"
                ],
                "correct_index": 0,
                "explanation": (
                    "Section 83 provided that the existing APPSC became the Public Service Commission for the successor State of Andhra Pradesh, while Telangana constituted its own State Public Service Commission (TSPSC) under Article 315."
                ),
                "source": "AP Reorganisation Act, 2014 (Part VIII, Section 83)"
            },
            {
                "q_no": 16,
                "id": "APPSC-MICRO-01-Q16",
                "subject": "AP History & Reorganization",
                "topic": "Section 93 & Schedule XIII – Port and Industrial Infrastructure",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "Which of the following infrastructure projects are specifically mandated for Andhra Pradesh under Schedule XIII of the AP Reorganisation Act, 2014?\n"
                    "1. Development of a major port at Dugarajapatnam / Ramayapatnam in Coastal Andhra\n"
                    "2. Feasibility study for a steel plant in YSR Kadapa district by SAIL\n"
                    "3. Visakhapatnam-Chennai Industrial Corridor (VCIC) development with ADB support\n\n"
                    "Select the correct answer using the code given below:"
                ),
                "options": [
                    "1, 2 and 3",
                    "1 and 2 only",
                    "2 and 3 only",
                    "1 and 3 only"
                ],
                "correct_index": 0,
                "explanation": (
                    "All three projects are explicitly listed in Schedule XIII (Infrastructure) of the Act:\n"
                    "• Item 1: Development of a new Major Port at Dugarajapatnam / alternate port.\n"
                    "• Item 2: Steel plant feasibility in YSR Kadapa district.\n"
                    "• Item 3: Visakhapatnam-Chennai Industrial Corridor (VCIC)."
                ),
                "source": "AP Reorganisation Act, 2014 (Schedule XIII Infrastructure)"
            },
            {
                "q_no": 17,
                "id": "APPSC-MICRO-01-Q17",
                "subject": "AP History & Reorganization",
                "topic": "Section 108 – Power to Remove Difficulties",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Under Section 108 of the Andhra Pradesh Reorganisation Act, 2014, who is empowered to make orders to remove any difficulty arising in giving effect to the provisions of the Act within a period of three years from the Appointed Day?"
                ),
                "options": [
                    "The President of India",
                    "The Chief Justice of India",
                    "The Governor of Andhra Pradesh",
                    "The Speaker of Lok Sabha"
                ],
                "correct_index": 0,
                "explanation": (
                    "Section 108 (Power to remove difficulties) empowers the President of India to make orders, not inconsistent with the provisions of the Act, to remove difficulties within three years of the Appointed Day."
                ),
                "source": "AP Reorganisation Act, 2014 (Part XII, Section 108)"
            },
            {
                "q_no": 18,
                "id": "APPSC-MICRO-01-Q18",
                "subject": "AP History & Reorganization",
                "topic": "Sivaramakrishnan Committee on AP Capital City",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "In pursuance of Section 6 of the AP Reorganisation Act, 2014, the Expert Committee constituted by the Ministry of Home Affairs to study alternatives for a new capital city for Andhra Pradesh was chaired by:\n"
                    "1. K.C. Sivaramakrishnan\n"
                    "2. Justice B.N. Srikrishna\n"
                    "3. Dr. C. Rangarajan\n"
                    "4. Justice G.T. Nanavati\n\n"
                    "Select the correct answer:"
                ),
                "options": [
                    "1 only",
                    "2 only",
                    "3 only",
                    "4 only"
                ],
                "correct_index": 0,
                "explanation": (
                    "Under Section 6 of the Act, the Central Government constituted the 5-member Expert Committee chaired by former Union Urban Development Secretary K.C. Sivaramakrishnan to study capital alternatives for Andhra Pradesh (submitted report in August 2014)."
                ),
                "source": "MHA Notification & Sivaramakrishnan Committee Report (2014)"
            },
            {
                "q_no": 19,
                "id": "APPSC-MICRO-01-Q19",
                "subject": "AP History & Reorganization",
                "topic": "Part VIII – Employee Allocation & Kamalanathan Committee",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Which Committee was appointed by the Government of India under Section 77 of the AP Reorganisation Act, 2014 for the final allocation of state cadre employees between Andhra Pradesh and Telangana?"
                ),
                "options": [
                    "C.R. Kamalanathan Committee",
                    "S.K. Dhar Committee",
                    "Fazal Ali Commission",
                    "J.M. Lyngdoh Committee"
                ],
                "correct_index": 0,
                "explanation": (
                    "The C.R. Kamalanathan Committee was appointed under Section 77(2) to determine the principles and carry out the division of ~52,000 state-cadre employees between Andhra Pradesh and Telangana."
                ),
                "source": "DoPT Notification & Kamalanathan Committee Guidelines"
            },
            {
                "q_no": 20,
                "id": "APPSC-MICRO-01-Q20",
                "subject": "AP History & Reorganization",
                "topic": "Section 89 – Water Dispute Tribunal Reference",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "Under Section 89 of the Andhra Pradesh Reorganisation Act, 2014, the Krishna Water Disputes Tribunal (KWDT-II, Justice Brijesh Kumar Tribunal) term was extended for which specific mandate?\n"
                    "1. Project-wise allocation of water among the successor States of Andhra Pradesh and Telangana.\n"
                    "2. Determining operational protocols for project-wise releases of water in times of deficit.\n"
                    "3. Reallocating the water shares of upper riparian states Maharashtra and Karnataka.\n\n"
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
                    "• Under Section 89, KWDT-II was mandated strictly to make project-wise allocations and operational deficit protocols between Andhra Pradesh and Telangana without altering the overall state-wise allocations of Maharashtra or Karnataka."
                ),
                "source": "AP Reorganisation Act, 2014 (Part IX, Section 89)"
            }
        ]
    },
    {
        "test_id": "APPSC-MICRO-02",
        "title": "⚡ Micro-Drill 2: AP Socio-Economic Survey & Budget 2026–27 (Tables & Schemes)",
        "exam_group": "Group 1 & 2",
        "category": "High-Yield Micro-Test",
        "duration_minutes": 20,
        "question_count": 20,
        "total_marks": 20.0,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["Indian & AP Economy", "PIB & Govt Schemes Current Affairs"],
        "description": "High-yield 20-minute drill on Andhra Pradesh Socio-Economic Survey & State Budget 2026–27: GSVA sectoral shares, GSDP growth, Swarna Andhra @ 2047, P4 model, Annadata Sukhibhava, Deepam-2.0, Talliki Vandanam, and NTR Bharosa pensions.",
        "questions": [
            {
                "q_no": 1,
                "id": "APPSC-MICRO-02-Q01",
                "subject": "Indian & AP Economy",
                "topic": "Gross State Value Added (GSVA) Sectoral Composition",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "According to the Andhra Pradesh Socio-Economic Survey, consider the following statements regarding the sectoral composition of Andhra Pradesh's Gross State Value Added (GSVA) at current prices:\n"
                    "1. The Agriculture and Allied Sector contributes over 34% to the GSVA of Andhra Pradesh, which is roughly double the national average share of agriculture in India's GDP.\n"
                    "2. Within the Agriculture and Allied Sector, the Livestock and Fisheries/Aquaculture sub-sectors together contribute more than 60% of the total agricultural GSVA.\n"
                    "3. The Industrial Sector in Andhra Pradesh accounts for over 50% of the state's GSVA.\n\n"
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
                    "• Statement 1 & 2: Agriculture & Allied contributes ~34–35% to AP's GSVA (national ~18%). Livestock (~28% of agri) and Fisheries (~32% of agri) form over 60% of agri GSVA.\n"
                    "• Statement 3 is incorrect: The Industrial sector contributes ~22–24% of GSVA, while Services contributes ~41–43%."
                ),
                "source": "Directorate of Economics & Statistics, AP Socio-Economic Survey"
            },
            {
                "q_no": 2,
                "id": "APPSC-MICRO-02-Q02",
                "subject": "Indian & AP Economy",
                "topic": "Swarna Andhra @ 2047 Vision Targets & Growth Rate",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Under the 'Swarna Andhra @ 2047' Vision Document adopted by the Government of Andhra Pradesh, what are the targeted GSDP economy size and Per Capita Income (PCI) milestones by the centenary year 2047?"
                ),
                "options": [
                    "$2.4 Trillion GSDP and Per Capita Income exceeding $42,000 (targeting >15% annual compound growth rate)",
                    "$500 Billion GSDP and Per Capita Income of $5,000",
                    "$1.0 Trillion GSDP and Per Capita Income of $10,000",
                    "$5.0 Trillion GSDP and Per Capita Income of $100,000"
                ],
                "correct_index": 0,
                "explanation": (
                    "Swarna Andhra @ 2047 sets the vision of making Andhra Pradesh a $2.4 Trillion economy with a Per Capita Income of over $42,000 by 2047, driven by sustained >15% annual GSDP growth."
                ),
                "source": "Planning Department, Govt of AP — Swarna Andhra @ 2047 Vision Document"
            },
            {
                "q_no": 3,
                "id": "APPSC-MICRO-02-Q03",
                "subject": "Indian & AP Economy",
                "topic": "P4 Model of Zero-Poverty Governance",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "In the Andhra Pradesh State Budget and Governance Framework, what does the 'P4' initiative stand for?"
                ),
                "options": [
                    "Public-Private-People Partnership (mentoring and empowering bottom 20% households to eradicate poverty)",
                    "Panchayat-Prakasam-Polavaram Plan",
                    "Public Procurement Price Policy",
                    "Petroleum-Port-Power Platform"
                ],
                "correct_index": 0,
                "explanation": (
                    "P4 stands for 'Public-Private-People Partnership', a poverty-eradication model connecting top corporates, mentors, and government welfare to uplift the bottom 20% economically vulnerable families in AP."
                ),
                "source": "AP State Budget Speech & Swarna Andhra @ 2047 Document"
            },
            {
                "q_no": 4,
                "id": "APPSC-MICRO-02-Q04",
                "subject": "PIB & Govt Schemes Current Affairs",
                "topic": "Annadata Sukhibhava Scheme Financial Outlay",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Under the 'Annadata Sukhibhava - PM KISAN' scheme implemented in Andhra Pradesh, what is the total annual direct financial assistance provided per eligible farmer family?"
                ),
                "options": [
                    "Rs. 20,000 per year (comprising Rs. 6,000 from Central PM-KISAN and Rs. 14,000 from State Government)",
                    "Rs. 10,000 per year (Rs. 6,000 PM-KISAN + Rs. 4,000 State)",
                    "Rs. 15,000 per year (Rs. 6,000 PM-KISAN + Rs. 9,000 State)",
                    "Rs. 25,000 per year paid in 5 monthly instalments"
                ],
                "correct_index": 0,
                "explanation": (
                    "Under Annadata Sukhibhava, farmers receive Rs. 20,000 annually per family (Rs. 6,000 via PM-KISAN + Rs. 14,000 via AP State Government DBT)."
                ),
                "source": "Department of Agriculture, AP Budget & Welfare Schemes"
            },
            {
                "q_no": 5,
                "id": "APPSC-MICRO-02-Q05",
                "subject": "PIB & Govt Schemes Current Affairs",
                "topic": "Deepam-2.0 Free LPG Cylinder Scheme",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Under the 'Deepam-2.0' scheme launched by the Government of Andhra Pradesh, eligible BPL/white ration card households are entitled to how many free domestic LPG cooking gas refills per year?"
                ),
                "options": [
                    "3 free LPG cooking gas cylinder refills per year (one every 4-month block)",
                    "1 free LPG refill per year",
                    "6 free LPG refills per year",
                    "12 free LPG refills per year"
                ],
                "correct_index": 0,
                "explanation": (
                    "Deepam-2.0 provides 3 free domestic LPG gas cylinder refills every financial year to eligible white ration card holders, with subsidy credited via Direct Benefit Transfer."
                ),
                "source": "Civil Supplies Department, Govt of AP & State Budget Releases"
            },
            {
                "q_no": 6,
                "id": "APPSC-MICRO-02-Q06",
                "subject": "PIB & Govt Schemes Current Affairs",
                "topic": "NTR Bharosa Social Security Pension Slabs",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "Consider the following enhanced monthly pension amounts under the 'NTR Bharosa Social Security Pensions' in Andhra Pradesh:\n"
                    "1. Old Age Persons, Widows, Weavers, Toddy Tappers, Fishermen, and Single Women: Rs. 4,000 per month.\n"
                    "2. Severely Disabled Persons (PwDs with high disability): Rs. 6,000 to Rs. 15,000 per month (depending on disability category).\n"
                    "3. Fully Bedridden / Chronic Kidney Disease patients undergoing dialysis: Rs. 10,000 per month.\n\n"
                    "Which of the statements given above are correct?"
                ),
                "options": [
                    "1, 2 and 3",
                    "1 and 2 only",
                    "2 and 3 only",
                    "1 and 3 only"
                ],
                "correct_index": 0,
                "explanation": (
                    "All three statements (1, 2, and 3) are correct:\n"
                    "• General OAP/Widow/Single Women pension was enhanced to Rs. 4,000/month.\n"
                    "• PwD pensions were raised to Rs. 6,000/month (and up to Rs. 15,000 for severe disability).\n"
                    "• Dialysis / Bedridden patients receive Rs. 10,000/month."
                ),
                "source": "Panchayat Raj & Rural Development Department, AP (NTR Bharosa Guidelines)"
            },
            {
                "q_no": 7,
                "id": "APPSC-MICRO-02-Q07",
                "subject": "Indian & AP Economy",
                "topic": "Talliki Vandanam Educational Scheme",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Under the 'Talliki Vandanam' scheme in Andhra Pradesh, what financial incentive is provided to eligible mothers for sending their children to school?"
                ),
                "options": [
                    "Rs. 15,000 per annum per school-going child deposited into the mother's bank account",
                    "Rs. 5,000 per family regardless of child count",
                    "Rs. 20,000 one-time voucher redeemable only at bookshops",
                    "Rs. 1,000 monthly food stipend"
                ],
                "correct_index": 0,
                "explanation": (
                    "Talliki Vandanam provides Rs. 15,000 per year per school-going child to eligible mothers, encouraging 100% school enrollment and eliminating child dropout rates."
                ),
                "source": "School Education Department, Govt of AP & State Budget"
            },
            {
                "q_no": 8,
                "id": "APPSC-MICRO-02-Q08",
                "subject": "Indian & AP Economy",
                "topic": "Andhra Pradesh Community-Managed Natural Farming (APCNF)",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "Regarding Andhra Pradesh Community-Managed Natural Farming (APCNF / ZBNF), consider the following statements:\n"
                    "1. APCNF is implemented by Rythu Sadhikara Samstha (RySS), a not-for-profit company owned by the Government of Andhra Pradesh.\n"
                    "2. It relies on four core biological inputs: Bijamrit (seed treatment), Jiwamrit (soil inoculant), Acchadana (mulching), and Waaphasa (soil aeration/moisture).\n"
                    "3. APCNF received the prestigious Gulbenkian Prize for Humanity in recognition of its global leadership in climate-resilient agriculture.\n\n"
                    "Which of the statements given above are correct?"
                ),
                "options": [
                    "1, 2 and 3",
                    "1 and 2 only",
                    "2 and 3 only",
                    "1 and 3 only"
                ],
                "correct_index": 0,
                "explanation": (
                    "All three statements (1, 2, and 3) are correct:\n"
                    "• Implemented by RySS covering over 1 million farmers.\n"
                    "• Uses 4 natural pillars: Bijamrit, Jiwamrit, Mulching, Waaphasa.\n"
                    "• APCNF won the international Gulbenkian Prize for Humanity in 2024."
                ),
                "source": "RySS Portal & AP Socio-Economic Survey (Agriculture Chapter)"
            },
            {
                "q_no": 9,
                "id": "APPSC-MICRO-02-Q09",
                "subject": "Indian & AP Economy",
                "topic": "National Rankings of AP in Agriculture & Horticulture",
                "question_type": "Pair Matching MCQ",
                "question": (
                    "According to the AP Socio-Economic Survey, in which of the following agricultural and horticultural commodities does Andhra Pradesh rank First (1st) in India in production?\n"
                    "1. Brackish-water Cultured Shrimp and Total Marine Fish\n"
                    "2. Oil Palm\n"
                    "3. Papaya and Lime (Citrus)\n"
                    "4. Cocoa and Tomato\n\n"
                    "Select the correct answer using the code given below:"
                ),
                "options": [
                    "1, 2, 3 and 4",
                    "1 and 2 only",
                    "2 and 3 only",
                    "1, 3 and 4 only"
                ],
                "correct_index": 0,
                "explanation": (
                    "Andhra Pradesh holds the 1st national rank in:\n"
                    "• Cultured Shrimp (~70% of India) and Total Fish\n"
                    "• Oil Palm (~50% of national production)\n"
                    "• Papaya, Lime, Cocoa, and Tomato\n"
                    "• Also 1st in Egg production (Poultry)."
                ),
                "source": "Directorate of Economics and Statistics, AP & Dept of Horticulture"
            },
            {
                "q_no": 10,
                "id": "APPSC-MICRO-02-Q10",
                "subject": "Indian & AP Economy",
                "topic": "Major Industrial Corridors & Smart Nodes in AP",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "Match the Industrial Nodes in Andhra Pradesh with their corresponding National Industrial Corridor:\n\n"
                    "1. Kopparthy Industrial Node — VCIC (Visakhapatnam-Chennai Corridor) / YSR Kadapa\n"
                    "2. Orvakal Industrial Node — HBIC (Hyderabad-Bengaluru Corridor) / Kurnool\n"
                    "3. Krishnapatnam Industrial Node — CBIC (Chennai-Bengaluru Corridor) / Tirupati-Nellore\n"
                    "4. Nakkapalli Bulk Drug & Industrial Node — VCIC / Anakapalli\n\n"
                    "Which of the pairs given above are correctly matched?"
                ),
                "options": [
                    "1, 2, 3 and 4",
                    "1 and 2 only",
                    "2, 3 and 4 only",
                    "1, 3 and 4 only"
                ],
                "correct_index": 0,
                "explanation": (
                    "All four pairs are correctly matched:\n"
                    "• Kopparthy: YSR Kadapa (VCIC node)\n"
                    "• Orvakal: Kurnool (HBIC node)\n"
                    "• Krishnapatnam: Tirupati/Nellore (CBIC node)\n"
                    "• Nakkapalli: Anakapalli (VCIC Bulk Drug node)."
                ),
                "source": "APIIC & National Industrial Corridor Development Corporation (NICDC)"
            },
            {
                "q_no": 11,
                "id": "APPSC-MICRO-02-Q11",
                "subject": "Indian & AP Economy",
                "topic": "AP State Revenue Receipts Structure",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "In the Andhra Pradesh State Budget Revenue Receipts, which of the following constitutes the largest single source of Own Tax Revenue (SOTR) for the state?"
                ),
                "options": [
                    "State Goods and Services Tax (SGST) followed by Sales Tax/VAT on Petroleum and Motor Spirit",
                    "Land Revenue collected from agricultural lands",
                    "Stamp Duty and Registration Fees from software exports",
                    "Taxes on Agricultural Income"
                ],
                "correct_index": 0,
                "explanation": (
                    "In AP's State Own Tax Revenue (SOTR), SGST forms the largest component (~40%), followed closely by VAT on Petroleum/Liquor and State Excise Duties."
                ),
                "source": "AP State Budget Explanatory Memorandum & Finance Department"
            },
            {
                "q_no": 12,
                "id": "APPSC-MICRO-02-Q12",
                "subject": "Indian & AP Economy",
                "topic": "Fiscal Deficit & FRBM Norms for AP",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Under the Union Finance Ministry's FRBM guidelines following the 15th/16th Finance Commission, what is the standard net borrowing ceiling (Fiscal Deficit to GSDP ratio) allowed for Andhra Pradesh?"
                ),
                "options": [
                    "3.0% of GSDP (with an extra 0.5% performance-linked borrowing for Power Sector Reforms under Section 15 of FRBM)",
                    "10.0% of GSDP without any conditions",
                    "1.0% of GSDP",
                    "Zero deficit (strictly balanced budget mandate)"
                ],
                "correct_index": 0,
                "explanation": (
                    "States are allowed a base Fiscal Deficit of 3.0% of GSDP, plus an additional 0.5% of GSDP upon completing power sector distribution and loss-reduction reforms."
                ),
                "source": "Ministry of Finance, Department of Expenditure & 15th/16th Finance Commission"
            },
            {
                "q_no": 13,
                "id": "APPSC-MICRO-02-Q13",
                "subject": "PIB & Govt Schemes Current Affairs",
                "topic": "Dr. NTR Vaidya Seva Healthcare Scheme",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Under the enhanced Dr. NTR Vaidya Seva health insurance scheme in Andhra Pradesh, what is the maximum cashless medical treatment coverage per eligible family per year?"
                ),
                "options": [
                    "Cashless coverage up to Rs. 25 Lakh per family covering over 3,250 medical/surgical procedures in empaneled network hospitals",
                    "Rs. 2 Lakh per family for emergency trauma only",
                    "Rs. 50,000 per family",
                    "Reimbursement of Rs. 10 Lakh only at government medical colleges"
                ],
                "correct_index": 0,
                "explanation": (
                    "Dr. NTR Vaidya Seva provides universal free cashless treatment up to Rs. 25 Lakh per family covering 3,250+ surgical and clinical procedures across empaneled hospitals."
                ),
                "source": "Dr. NTR Vaidya Seva Trust & Health Department, Govt of AP"
            },
            {
                "q_no": 14,
                "id": "APPSC-MICRO-02-Q14",
                "subject": "Indian & AP Economy",
                "topic": "Per Capita Income Comparison (AP vs National)",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "According to recent AP Socio-Economic Survey estimates, how does the Per Capita Income (PCI) of Andhra Pradesh at current prices compare with the All-India average?"
                ),
                "options": [
                    "Andhra Pradesh's Per Capita Income is approximately 30–35% higher than the All-India National average Per Capita Income",
                    "Andhra Pradesh's Per Capita Income is less than half of the national average",
                    "Andhra Pradesh has the lowest Per Capita Income among all Indian states",
                    "Andhra Pradesh and India have identical Per Capita Income of exactly Rs. 50,000"
                ],
                "correct_index": 0,
                "explanation": (
                    "AP's Per Capita Income at current prices stands at ~Rs. 2.42 Lakh per annum, which is ~30–35% higher than the All-India average of ~Rs. 1.83 Lakh."
                ),
                "source": "AP Socio-Economic Survey & MoSPI State-wise Per Capita Income Tables"
            },
            {
                "q_no": 15,
                "id": "APPSC-MICRO-02-Q15",
                "subject": "Indian & AP Economy",
                "topic": "AP Ports Development & Coastline Infrastructure",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "With reference to Port Infrastructure in Andhra Pradesh, consider the following statements:\n"
                    "1. Visakhapatnam Port is the only Major Port in Andhra Pradesh administered by the Central Government under the Major Port Authorities Act, 2021.\n"
                    "2. Non-major (Minor) ports developed or under construction by AP Maritime Board include Gangavaram, Krishnapatnam, Kakinada Deep Water, Ramayapatnam, Machilipatnam, and Bhavanapadu (Mulapeta).\n"
                    "3. Andhra Pradesh handles the second-largest cargo traffic in India after Gujarat.\n\n"
                    "Which of the statements given above are correct?"
                ),
                "options": [
                    "1, 2 and 3",
                    "1 and 2 only",
                    "2 and 3 only",
                    "1 and 3 only"
                ],
                "correct_index": 0,
                "explanation": (
                    "All three statements (1, 2, and 3) are correct:\n"
                    "• Visakhapatnam is the sole Major Port under Union control.\n"
                    "• Non-major ports: Krishnapatnam, Gangavaram, Ramayapatnam, Machilipatnam, Mulapeta.\n"
                    "• AP handles ~180+ MMT cargo, ranking 2nd nationally after Gujarat."
                ),
                "source": "AP Maritime Board & Ministry of Ports, Shipping and Waterways"
            },
            {
                "q_no": 16,
                "id": "APPSC-MICRO-02-Q16",
                "subject": "PIB & Govt Schemes Current Affairs",
                "topic": "Skill Census & AP Skill Development Corporation",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "The Government of Andhra Pradesh launched the country's first comprehensive 'Skill Census' (Nipunata Ganana) with the objective of:"
                ),
                "options": [
                    "Mapping the exact skills, educational qualifications, and employability gaps of every youth across all 26 districts to provide industry-aligned skilling and job placement",
                    "Registering civil servants for overseas training",
                    "Counting the number of primary school teachers in rural mandals",
                    "Conducting a census of all software engineers working in Hyderabad"
                ],
                "correct_index": 0,
                "explanation": (
                    "AP Skill Census is a pioneering digital survey mapping individual skill levels and training requirements across 18–59 age groups to link youth with certified industry jobs."
                ),
                "source": "AP State Skill Development Corporation (APSSDC) & Planning Dept"
            },
            {
                "q_no": 17,
                "id": "APPSC-MICRO-02-Q17",
                "subject": "Indian & AP Economy",
                "topic": "Renewable Energy & Pumped Hydro Storage Projects (PSPs)",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Which region of Andhra Pradesh is emerging as India's premier hub for Integrated Renewable Energy Projects (combining Solar, Wind, and Pumped Hydro Energy Storage Systems - PSPs) including the Pinnapuram project?"
                ),
                "options": [
                    "Kurnool and Nandyal districts (Rayalaseema plateau)",
                    "Srikakulam coastal belt",
                    "West Godavari delta",
                    "Krishna delta plain"
                ],
                "correct_index": 0,
                "explanation": (
                    "Kurnool/Nandyal (Pinnapuram 5,230 MW Integrated Renewable Project by Greenko) features India's largest co-located solar, wind, and pumped-hydro closed-loop storage system."
                ),
                "source": "New and Renewable Energy Development Corporation of AP (NREDCAP)"
            },
            {
                "q_no": 18,
                "id": "APPSC-MICRO-02-Q18",
                "subject": "Indian & AP Economy",
                "topic": "Micro, Small & Medium Enterprises (MSMEs) Policy of AP",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Under Andhra Pradesh's 'One Mandal One Product' (OMOP) and MSME Industrial Development Policy, what single-desk clearance mechanism facilitates industrial approvals within 21 days?"
                ),
                "options": [
                    "Single Desk Portal (AP Single Window Act)",
                    "SEBI Clearance Cell",
                    "RBI Industrial Window",
                    "Panchayat NOC Committee"
                ],
                "correct_index": 0,
                "explanation": (
                    "AP Single Desk Portal integrates approvals from 19 departments, granting time-bound statutory industrial clearances and green-channel incentives within 21 working days."
                ),
                "source": "Industries & Commerce Department, Govt of AP"
            },
            {
                "q_no": 19,
                "id": "APPSC-MICRO-02-Q19",
                "subject": "Indian & AP Economy",
                "topic": "Livestock Sector Contribution in AP",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "In the livestock sector of Andhra Pradesh, which of the following statements represents the state's national standing?"
                ),
                "options": [
                    "AP ranks 1st in Egg production (~20% of national supply) and 2nd in Meat production",
                    "AP produces zero milk and ranks last in poultry",
                    "AP has no livestock and imports all poultry from northern states",
                    "AP is restricted solely to camel rearing"
                ],
                "correct_index": 0,
                "explanation": (
                    "Andhra Pradesh produces over 2,500 crore eggs annually (ranking 1st in India) and ranks 2nd in meat production, making livestock a major engine of rural wealth."
                ),
                "source": "Basic Animal Husbandry Statistics & AP Socio-Economic Survey"
            },
            {
                "q_no": 20,
                "id": "APPSC-MICRO-02-Q20",
                "subject": "Indian & AP Economy",
                "topic": "Multidimensional Poverty Index (NITI Aayog AP Performance)",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "According to NITI Aayog's National Multidimensional Poverty Index (MPI) Report, what has been the trend of multidimensional poverty in Andhra Pradesh?"
                ),
                "options": [
                    "Multidimensional poverty in AP dropped significantly from over 11.7% to below 4.2%, with districts like Alluri Sitharama Raju and Parvathipuram Manyam showing highest reduction under saturation welfare schemes",
                    "Poverty increased to over 80% across all coastal districts",
                    "There was no change in poverty indicators since 1991",
                    "AP was excluded from the NITI Aayog MPI ranking"
                ],
                "correct_index": 0,
                "explanation": (
                    "NITI Aayog's National MPI Report highlights that Andhra Pradesh reduced its multidimensional poverty headcount ratio from 11.77% to 4.19%, lifting over 4 million people out of multidimensional deprivation."
                ),
                "source": "NITI Aayog National Multidimensional Poverty Index Baseline & Progress Reports"
            }
        ]
    },
    {
        "test_id": "APPSC-MICRO-03",
        "title": "⚡ Micro-Drill 3: AP Rivers, Irrigation Projects & District Reorganisation Geography",
        "exam_group": "Group 1 & 2",
        "category": "High-Yield Micro-Test",
        "duration_minutes": 20,
        "question_count": 20,
        "total_marks": 20.0,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["Geography of India & AP", "AP History & Reorganization"],
        "description": "High-yield 20-minute drill on Andhra Pradesh Geography: Godavari-Krishna-Penna-Nagavali-Vamsadhara river basins, Pattiseema, Veligonda, Handri-Neeva, Galeru-Nagari, 26 Reorganised Districts, Eastern Ghats peaks, and mineral deposits.",
        "questions": [
            {
                "q_no": 1,
                "id": "APPSC-MICRO-03-Q01",
                "subject": "Geography of India & AP",
                "topic": "26 Reorganised Districts of Andhra Pradesh",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "On April 4, 2022, the Government of Andhra Pradesh reorganised the state's 13 erstwhile districts into 26 districts. Which of the following are the two newly carved Scheduled Agency / Tribal districts in Andhra Pradesh?"
                ),
                "options": [
                    "Alluri Sitharama Raju (HQ: Paderu) and Parvathipuram Manyam (HQ: Parvathipuram)",
                    "Annamayya and Sri Sathya Sai",
                    "Konaseema and Kakinada",
                    "Palnadu and Bapatla"
                ],
                "correct_index": 0,
                "explanation": (
                    "The two exclusive tribal/agency districts are:\n"
                    "• Alluri Sitharama Raju district (Headquarters: Paderu)\n"
                    "• Parvathipuram Manyam district (Headquarters: Parvathipuram)."
                ),
                "source": "AP Gazette Notification on District Reorganisation (April 2022)"
            },
            {
                "q_no": 2,
                "id": "Geography of India & AP",
                "subject": "Geography of India & AP",
                "topic": "Godavari River Left and Right Bank Tributaries in AP",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "Consider the following statements regarding the Godavari river basin in Andhra Pradesh:\n"
                    "1. The Godavari river splits into two principal branches at Sir Arthur Cotton Barrage (Dowleswaram): Gautami Godavari (eastern) and Vasishta Godavari (western).\n"
                    "2. The Vasishta Godavari further branches into the Vainateya Godavari near Razole in Dr. B.R. Ambedkar Konaseema district.\n"
                    "3. Sabari and Sileru are major right-bank tributaries of the Godavari originating in Rayalaseema.\n\n"
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
                    "• Statements 1 & 2: Below Rajahmundry, Godavari splits into Gautami and Vasishta; Vasishta splits into Vainateya.\n"
                    "• Statement 3 is incorrect: Sabari (and its tributary Sileru) are left-bank tributaries originating in Odisha/Eastern Ghats, not Rayalaseema."
                ),
                "source": "Central Water Commission (CWC) & AP Irrigation Atlas"
            },
            {
                "q_no": 3,
                "id": "APPSC-MICRO-03-Q03",
                "subject": "Geography of India & AP",
                "topic": "Pattiseema Lift Irrigation Scheme & River Interlinking",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "What makes the Pattiseema Lift Irrigation Project historic in Indian river interlinking?"
                ),
                "options": [
                    "It achieved the first formal interlinking of two major peninsular rivers—transferring surplus Godavari water into the Krishna river basin upstream of Prakasam Barrage through the Polavaram Right Main Canal",
                    "It linked the Ganges with the Brahmaputra in West Bengal",
                    "It connected the Narmada with the Mahanadi",
                    "It transferred water from Cauvery into Kolleru lake"
                ],
                "correct_index": 0,
                "explanation": (
                    "Pattiseema Lift Irrigation Scheme (completed in record time in West Godavari) lifted 80 TMC of floodwaters from Godavari into Krishna via Polavaram Right Main Canal, stabilizing the Krishna Delta and saving water for Rayalaseema."
                ),
                "source": "Water Resources Department, AP & Limca Book of Records Entry"
            },
            {
                "q_no": 4,
                "id": "APPSC-MICRO-03-Q04",
                "subject": "Geography of India & AP",
                "topic": "Major Rayalaseema Irrigation Projects",
                "question_type": "Pair Matching MCQ",
                "question": (
                    "Match the major irrigation project in Andhra Pradesh with its source reservoir/river:\n\n"
                    "1. Handri-Neeva Sujala Sravanthi (HNSS) — Srisailam Reservoir (Krishna River)\n"
                    "2. Galeru Nagari Sujala Sravanthi (GNSS) — Srisailam / Gorakallu (Krishna River)\n"
                    "3. Poola Subbaiah Veligonda Project — Srisailam Reservoir (Nallamala Tunnel) to Prakasam/Nellore/Kadapa\n"
                    "4. Thotapalli Barrage — Nagavali River (Vizianagaram)\n\n"
                    "Which of the pairs given above are correctly matched?"
                ),
                "options": [
                    "1, 2, 3 and 4",
                    "1 and 2 only",
                    "2, 3 and 4 only",
                    "1, 3 and 4 only"
                ],
                "correct_index": 0,
                "explanation": (
                    "All four pairs are correctly matched:\n"
                    "• HNSS: Lifts from Srisailam foreshore (Malyala) for Kurnool, Anantapur, Chittoor.\n"
                    "• GNSS: Srisailam flood flow to Kadapa and Chittoor.\n"
                    "• Veligonda: Twin tunnels through Nallamala hills to Eastern Prakasam/Nellore/Kadapa.\n"
                    "• Thotapalli: Barrage on Nagavali river in Vizianagaram."
                ),
                "source": "AP Water Resources Department & Major Projects Handbook"
            },
            {
                "q_no": 5,
                "id": "APPSC-MICRO-03-Q05",
                "subject": "Geography of India & AP",
                "topic": "Highest Peaks in Andhra Pradesh Eastern Ghats",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Which of the following is the highest mountain peak in the state of Andhra Pradesh?"
                ),
                "options": [
                    "Arma Konda / Jindhagada Peak (~1,690 meters, Araku Valley in Alluri Sitharama Raju district)",
                    "Mahendragiri (~1,501 meters)",
                    "Horsley Hills (~1,265 meters)",
                    "Nallamala Peak (~900 meters)"
                ],
                "correct_index": 0,
                "explanation": (
                    "Arma Konda (also known as Jindhagada Peak or Sitamma Konda) in the Eastern Ghats of Araku Valley (ASR district) stands at ~1,690 m, making it the highest peak in Andhra Pradesh."
                ),
                "source": "Survey of India & AP Forest Department Flora/Fauna Surveys"
            },
            {
                "q_no": 6,
                "id": "APPSC-MICRO-03-Q06",
                "subject": "Geography of India & AP",
                "topic": "Penna River Basin & Tributaries",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "With reference to the Penna (Pinakini) River system in Andhra Pradesh, consider the following statements:\n"
                    "1. The Penna river originates in the Nandi Hills (Chikkaballapur district of Karnataka) and flows through Anantapur, YSR Kadapa, and SPSR Nellore districts before emptying into the Bay of Bengal near Utukuru.\n"
                    "2. Somasila Dam and Gandikota Reservoir are major water storage structures constructed on the Penna River.\n"
                    "3. Major tributaries of Penna include Papagni, Chitravathi, Cheyyeru, and Kundu.\n\n"
                    "Which of the statements given above are correct?"
                ),
                "options": [
                    "1, 2 and 3",
                    "1 and 2 only",
                    "2 and 3 only",
                    "1 and 3 only"
                ],
                "correct_index": 0,
                "explanation": (
                    "All three statements (1, 2, and 3) are correct:\n"
                    "• Originates in Nandi Hills, Karnataka; flows through Rayalaseema & Nellore.\n"
                    "• Somasila and Gandikota (Grand Canyon of India gorge) are on Penna.\n"
                    "• Tributaries: Papagni, Chitravathi, Cheyyeru, Kundu, Sagileru, Boggeru."
                ),
                "source": "Central Water Commission & Penna Basin Report"
            },
            {
                "q_no": 7,
                "id": "APPSC-MICRO-03-Q07",
                "subject": "Geography of India & AP",
                "topic": "Vamsadhara and Nagavali Rivers (North Coastal AP)",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "Consider the following statements regarding the North Coastal rivers of Andhra Pradesh:\n"
                    "1. Both the Vamsadhara and Nagavali rivers originate in the Eastern Ghats of Odisha (Kalahandi/Rayagada region) and flow through Srikakulam/Vizianagaram districts into the Bay of Bengal.\n"
                    "2. The Vamsadhara Water Disputes Tribunal (VWDT) resolved the dispute between Andhra Pradesh and Odisha regarding the Neradi Barrage and Side Weir at Katragadda.\n\n"
                    "Which of the statements given above is/are correct?"
                ),
                "options": [
                    "Both 1 and 2",
                    "1 only",
                    "2 only",
                    "Neither 1 nor 2"
                ],
                "correct_index": 0,
                "explanation": (
                    "Both Statements 1 and 2 are correct:\n"
                    "• Vamsadhara and Nagavali rise in Odisha and discharge into Bay of Bengal near Kalingapatnam and Mofazbandar (Srikakulam).\n"
                    "• Neradi Barrage was adjudicated under the Inter-State River Water Disputes Act by VWDT."
                ),
                "source": "VWDT Award & Ministry of Jal Shakti River Basins Portal"
            },
            {
                "q_no": 8,
                "id": "APPSC-MICRO-03-Q08",
                "subject": "Geography of India & AP",
                "topic": "Strategic Minerals: Barytes, Uranium & Heavy Minerals",
                "question_type": "Pair Matching MCQ",
                "question": (
                    "Match the mineral deposit in Andhra Pradesh with its specific geographic location:\n\n"
                    "1. Mangampeta — World's largest single bedded deposit of Barytes (Annamayya/YSR Kadapa)\n"
                    "2. Tummalapalle — Large strata-bound Uranium reserve (Vemula Mandal, YSR Kadapa)\n"
                    "3. Srikakulam & Visakhapatnam Beach Sands — Heavy mineral placer deposits (Ilmenite, Rutile, Monazite, Garnet)\n"
                    "4. Mangalagiri & Piduguralla — Limestone belt of Palnadu (Cement manufacturing)\n\n"
                    "Which of the pairs given above are correctly matched?"
                ),
                "options": [
                    "1, 2, 3 and 4",
                    "1 and 2 only",
                    "2, 3 and 4 only",
                    "1, 3 and 4 only"
                ],
                "correct_index": 0,
                "explanation": (
                    "All four mineral locations are correctly matched:\n"
                    "• Mangampeta: Barytes (~94% of India).\n"
                    "• Tummalapalle: Uranium Corporation of India (UCIL) processing plant.\n"
                    "• Beach sands: IREL heavy minerals (Ilmenite, Monazite).\n"
                    "• Palnadu/Cuddapah Basin: High-grade limestone for cement."
                ),
                "source": "Indian Bureau of Mines (IBM) & Dept of Mines and Geology, AP"
            },
            {
                "q_no": 9,
                "id": "APPSC-MICRO-03-Q09",
                "subject": "Geography of India & AP",
                "topic": "Kolleru & Pulicat Wetland Ecosystems",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "Consider the following comparison between Kolleru Lake and Pulicat Lake in Andhra Pradesh:\n"
                    "1. Kolleru Lake is a natural freshwater wetland located between the Krishna and Godavari deltas, designated as a Ramsar Site and fed by the Budameru and Tammileru streams.\n"
                    "2. Pulicat Lake is a brackish water lagoon situated on the border of AP (Tirupati district) and Tamil Nadu, protected from the Bay of Bengal by the barrier island of Sriharikota.\n"
                    "3. Both Kolleru and Pulicat lakes are natural crater lakes formed by meteorite impact in Rayalaseema.\n\n"
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
                    "• Statements 1 & 2: Kolleru is an inter-deltaic freshwater Ramsar lake (fed by Budameru/Tammileru, drained by Upputeru). Pulicat is a marine-connected lagoon barrier system.\n"
                    "• Statement 3 is incorrect: Neither is a crater lake (Lonar Lake in Maharashtra is a crater lake)."
                ),
                "source": "MoEFCC Ramsar Wetland Factsheets & AP Wildlife Wing"
            },
            {
                "q_no": 10,
                "id": "APPSC-MICRO-03-Q10",
                "subject": "Geography of India & AP",
                "topic": "Nagarjunasagar-Srisailam Tiger Reserve (NSTR)",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Which of the following geographical features correctly describes the Nagarjunasagar-Srisailam Tiger Reserve (NSTR)?"
                ),
                "options": [
                    "It is the largest Tiger Reserve in India by total area, encompassing the Nallamala hill range through which the Krishna River carves deep gorges",
                    "It is a mangrove forest located entirely on the Godavari delta",
                    "It is situated on the Nilgiri plateau of the Western Ghats",
                    "It is a desert national park on the AP-Karnataka border"
                ],
                "correct_index": 0,
                "explanation": (
                    "NSTR is India's largest tiger reserve (~3,728 sq km total area across Nandyal, Prakasam, Palnadu districts), situated in the dry deciduous Nallamala forests along the Krishna River gorge."
                ),
                "source": "National Tiger Conservation Authority (NTCA) & AP Forest Dept"
            },
            {
                "q_no": 11,
                "id": "APPSC-MICRO-03-Q11",
                "subject": "Geography of India & AP",
                "topic": "District Headquarters of Newly Carved Districts",
                "question_type": "Pair Matching MCQ",
                "question": (
                    "Match the newly formed district of Andhra Pradesh with its designated District Headquarters:\n\n"
                    "1. Sri Sathya Sai District — Puttaparthi\n"
                    "2. Annamayya District — Rayachoti\n"
                    "3. Dr. B.R. Ambedkar Konaseema District — Amalapuram\n"
                    "4. NTR District — Vijayawada\n\n"
                    "Which of the pairs given above are correctly matched?"
                ),
                "options": [
                    "1, 2, 3 and 4",
                    "1 and 2 only",
                    "2, 3 and 4 only",
                    "1, 3 and 4 only"
                ],
                "correct_index": 0,
                "explanation": (
                    "All four headquarters are correctly matched:\n"
                    "• Sri Sathya Sai: Puttaparthi\n"
                    "• Annamayya: Rayachoti\n"
                    "• Dr. B.R. Ambedkar Konaseema: Amalapuram\n"
                    "• NTR: Vijayawada\n"
                    "Other key headquarters: Kakinada (Kakinada), Eluru (Eluru), Palnadu (Narasaraopet), Bapatla (Bapatla), Nandyal (Nandyal), Sri Balaji/Tirupati (Tirupati)."
                ),
                "source": "Government of Andhra Pradesh District Reorganisation Notifications"
            },
            {
                "q_no": 12,
                "id": "APPSC-MICRO-03-Q12",
                "subject": "Geography of India & AP",
                "topic": "Gandikota Gorge & Belum Caves (Karst Topography)",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "Consider the following unique geological wonders of Andhra Pradesh:\n"
                    "1. Gandikota Gorge (in YSR Kadapa district) is formed by the Penna River cutting through the Erramala hills and is famously called the 'Grand Canyon of India'.\n"
                    "2. Belum Caves and Borra Caves represent outstanding examples of Karst topography (limestone speleothems with stalactites and stalagmites).\n"
                    "3. Borra Caves (in ASR district / Ananthagiri hills) were carved by the subterranean flow of the Gosthani River.\n\n"
                    "Which of the statements given above are correct?"
                ),
                "options": [
                    "1, 2 and 3",
                    "1 and 2 only",
                    "2 and 3 only",
                    "1 and 3 only"
                ],
                "correct_index": 0,
                "explanation": (
                    "All three statements (1, 2, and 3) are correct:\n"
                    "• Gandikota: Penna river quartz gorge in Kadapa.\n"
                    "• Belum (Kurnool/Nandyal) & Borra (ASR district): Famous karst limestone caves.\n"
                    "• Borra Caves: Formed by the Gosthani River in Ananthagiri hills."
                ),
                "source": "Geological Survey of India (GSI) & AP Tourism Development Corporation"
            },
            {
                "q_no": 13,
                "id": "APPSC-MICRO-03-Q13",
                "subject": "Geography of India & AP",
                "topic": "Rayalaseema Drought & Rain Shadow Zone",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Why does the Rayalaseema region (Anantapur, Sri Sathya Sai, Kurnool, Kadapa) receive low rainfall during the Southwest Monsoon (June–September)?"
                ),
                "options": [
                    "It lies in the rain-shadow zone (leeward side) of the Western Ghats, causing descending dry air masses to yield scanty orographic precipitation",
                    "It is situated at the North Pole where cold blizzards block rain clouds",
                    "There are no rivers or water bodies in southern India",
                    "Southwest Monsoon winds do not blow across the Indian peninsula"
                ],
                "correct_index": 0,
                "explanation": (
                    "Rayalaseema (especially Anantapur, which receives <550 mm annual rain) lies in the rain-shadow region of the Western Ghats during the SW monsoon, making it the second-driest district in India after Jaisalmer."
                ),
                "source": "India Meteorological Department (IMD) & Climatology of Andhra Pradesh"
            },
            {
                "q_no": 14,
                "id": "APPSC-MICRO-03-Q14",
                "subject": "Geography of India & AP",
                "topic": "Seshachalam Biosphere Reserve & Red Sanders",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Which precious, endangered tree species is endemic strictly to the Seshachalam and Veligonda hill ranges of the Southern Eastern Ghats in Andhra Pradesh (Tirupati, Kadapa, Chittoor, Nellore)?"
                ),
                "options": [
                    "Red Sanders / Red Sandalwood (Pterocarpus santalinus)",
                    "Teak (Tectona grandis)",
                    "Deodar (Cedrus deodara)",
                    "Sal (Shorea robusta)"
                ],
                "correct_index": 0,
                "explanation": (
                    "Red Sanders (Pterocarpus santalinus), listed under CITES Appendix II, is globally endemic to the Seshachalam Biosphere Reserve and surrounding Cuddapah formation hills."
                ),
                "source": "AP Forest Department & MoEFCC Biosphere Reserves Registry"
            },
            {
                "q_no": 15,
                "id": "APPSC-MICRO-03-Q15",
                "subject": "Geography of India & AP",
                "topic": "Prakasam Barrage and Dowleswaram Barrage History",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Sir Arthur Cotton, revered as 'Apara Bhageeratha' in Andhra Pradesh, designed and constructed which two landmark delta irrigation systems in the 19th century?"
                ),
                "options": [
                    "Dowleswaram Barrage across Godavari River (1852) and Prakasam Barrage (Krishna Delta system at Vijayawada, 1855)",
                    "Srisailam Dam and Nagarjuna Sagar Dam",
                    "Bhakra Nangal Dam and Hirakud Dam",
                    "Mettur Dam and Mullaperiyar Dam"
                ],
                "correct_index": 0,
                "explanation": (
                    "Major Cotton engineered the Dowleswaram Barrage (Godavari Delta) and the original Krishna Anicut (modern Prakasam Barrage) at Vijayawada, transforming both deltas into the Rice Bowl of India."
                ),
                "source": "History of Irrigation in Andhra Pradesh & Cotton Museum, Dowleswaram"
            },
            {
                "q_no": 16,
                "id": "APPSC-MICRO-03-Q16",
                "subject": "Geography of India & AP",
                "topic": "Gundlakamma and Swarnamukhi Rivers",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "Consider the following local medium river systems of Andhra Pradesh:\n"
                    "1. Gundlakamma River originates in the Nallamala Hills (Prakasam/Palnadu border) and discharges into the Bay of Bengal near Devarampadu.\n"
                    "2. Swarnamukhi River flows past the holy temple towns of Chandragiri, Tirupati, and Srikalahasti before emptying into Pulicat/Bay of Bengal.\n\n"
                    "Which of the statements given above is/are correct?"
                ),
                "options": [
                    "Both 1 and 2",
                    "1 only",
                    "2 only",
                    "Neither 1 nor 2"
                ],
                "correct_index": 0,
                "explanation": (
                    "Both Statements 1 and 2 are correct:\n"
                    "• Gundlakamma: Nallamala origin; Gundlakamma Reservoir in Prakasam.\n"
                    "• Swarnamukhi: Rises in Chandragiri hills; flows through Tirupati and Srikalahasti (Vayu Lingam temple)."
                ),
                "source": "AP State Water Resources Portal & District Gazetteers"
            },
            {
                "q_no": 17,
                "id": "APPSC-MICRO-03-Q17",
                "subject": "Geography of India & AP",
                "topic": "Coringa Wildlife Sanctuary & Mangrove Wetlands",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Coringa Wildlife Sanctuary, situated at the mouth of the Gautami Godavari River in Kakinada district, is renowned for:"
                ),
                "options": [
                    "The second largest expanse of mangrove forests in mainland India after the Sundarbans, home to Fishing Cats and Olive Ridley turtles",
                    "High-altitude Alpine coniferous forests",
                    "Cold desert wildlife including Snow Leopards",
                    "Freshwater trout fisheries in Himalayan glaciers"
                ],
                "correct_index": 0,
                "explanation": (
                    "Coringa Wildlife Sanctuary covers ~235 sq km of dense mangroves in the Godavari estuary, hosting the world's largest population of Fishing Cats and nesting Olive Ridley sea turtles."
                ),
                "source": "AP Forest Department (Wildlife Wing) & MoEFCC Mangrove Atlas"
            },
            {
                "q_no": 18,
                "id": "APPSC-MICRO-03-Q18",
                "subject": "Geography of India & AP",
                "topic": "Cuddapah Geological Basin Structure",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "In Indian Stratigraphy and Geology, what is the shape and economic significance of the 'Cuddapah Basin' in Andhra Pradesh?"
                ),
                "options": [
                    "A crescent-shaped (crescentic) Proterozoic sedimentary basin rich in limestone, dolomite, barytes, asbestos, and uranium",
                    "A circular volcanic caldera with active basaltic magma",
                    "A modern sand dune desert with zero mineral resources",
                    "A glacial moraine valley formed in the Pleistocene epoch"
                ],
                "correct_index": 0,
                "explanation": (
                    "The Cuddapah Basin is a world-famous crescent-shaped Proterozoic basin (Papaghni, Chitravathi, Nallamalai, and Kurnool groups) packed with rich industrial minerals."
                ),
                "source": "Geological Survey of India (GSI Memoirs - Geology of Cuddapah Basin)"
            },
            {
                "q_no": 19,
                "id": "APPSC-MICRO-03-Q19",
                "subject": "Geography of India & AP",
                "topic": "Coastline Features: Hope Island & Barrier Spits",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "What is 'Hope Island' located off the coast of Kakinada in Andhra Pradesh?"
                ),
                "options": [
                    "A natural tadpole-shaped barrier sand spit formed by Godavari sediment drift that protects Kakinada Port from severe cyclonic waves and tidal surges",
                    "A volcanic island with active thermal springs",
                    "A coral atoll in the Arabian Sea",
                    "An artificial concrete breakwater built by the Dutch in 1602"
                ],
                "correct_index": 0,
                "explanation": (
                    "Hope Island is a natural 16-km long sand spit formed over the last two centuries by longshore drift of Godavari sand, making Kakinada a tranquil natural deep-water harbor."
                ),
                "source": "National Institute of Oceanography (NIO) & AP Maritime Board"
            },
            {
                "q_no": 20,
                "id": "APPSC-MICRO-03-Q20",
                "subject": "Geography of India & AP",
                "topic": "Srisailam Left and Right Bank Hydroelectric Stations",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "At the Srisailam Hydroelectric Project across the Krishna River, how are the power houses divided between Andhra Pradesh and Telangana?"
                ),
                "options": [
                    "Srisailam Right Bank Power House (7 x 110 = 770 MW) is operated by APGENCO (Andhra Pradesh), while the Left Bank Underground Power House (6 x 150 = 900 MW, reversible pumped storage) is operated by TGGENCO (Telangana)",
                    "Both power houses are operated by Karnataka Power Corporation",
                    "APGENCO operates 100% of both left and right power houses",
                    "NTPC owns and operates the entire reservoir without state involvement"
                ],
                "correct_index": 0,
                "explanation": (
                    "Under inter-state sharing conventions:\n"
                    "• AP operates Right Bank Power House (770 MW).\n"
                    "• Telangana operates Left Bank Underground Power House (900 MW reversible turbine station)."
                ),
                "source": "KRMB & Central Electricity Authority (CEA) Hydroelectric Stations Directory"
            }
        ]
    },
    {
        "test_id": "APPSC-MICRO-04",
        "title": "⚡ Micro-Drill 4: 73rd & 74th Constitutional Amendments, Schedules & Articles",
        "exam_group": "Group 1 & 2",
        "category": "High-Yield Micro-Test",
        "duration_minutes": 20,
        "question_count": 20,
        "total_marks": 20.0,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["Indian Polity & Constitution", "Indian Society & Welfare"],
        "description": "High-yield 20-minute drill on 73rd and 74th Constitutional Amendment Acts: Articles 243 to 243ZG, Eleventh Schedule (29 subjects), Twelfth Schedule (18 subjects), Gram Sabha, State Election Commission (243K), State Finance Commission (243-I/243Y), PESA Act 1996, and DPC (243ZD).",
        "questions": [
            {
                "q_no": 1,
                "id": "APPSC-MICRO-04-Q01",
                "subject": "Indian Polity & Constitution",
                "topic": "73rd and 74th Amendment Act Parts & Schedules",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "Consider the following statements regarding the 73rd and 74th Constitutional Amendment Acts, 1992:\n"
                    "1. The 73rd Amendment Act inserted Part IX ('The Panchayats', Articles 243 to 243-O) and the Eleventh Schedule containing 29 functional subjects.\n"
                    "2. The 74th Amendment Act inserted Part IX-A ('The Municipalities', Articles 243-P to 243-ZG) and the Twelfth Schedule containing 18 functional subjects.\n"
                    "3. Both Amendment Acts came into force on the exact same date of January 26, 1950.\n\n"
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
                    "• Statements 1 & 2: 73rd Act = Part IX (243 to 243-O, 11th Schedule 29 subjects). 74th Act = Part IX-A (243-P to 243-ZG, 12th Schedule 18 subjects).\n"
                    "• Statement 3 is incorrect: 73rd Amendment came into force on April 24, 1993 (celebrated as National Panchayati Raj Day); 74th Amendment came into force on June 1, 1993."
                ),
                "source": "Constitution of India (Parts IX & IX-A) & Ministry of Panchayati Raj"
            },
            {
                "q_no": 2,
                "id": "APPSC-MICRO-04-Q02",
                "subject": "Indian Polity & Constitution",
                "topic": "Constitutional Articles Mapping: 243A to 243K",
                "question_type": "Pair Matching MCQ",
                "question": (
                    "Match List-I (Article of the Constitution) with List-II (Panchayati Raj Provision):\n\n"
                    "List-I (Article):\n"
                    "A. Article 243-A\n"
                    "B. Article 243-D\n"
                    "C. Article 243-I\n"
                    "D. Article 243-K\n\n"
                    "List-II (Provision):\n"
                    "1. State Finance Commission (Finance review & tax devolution)\n"
                    "2. Gram Sabha (Powers and functions at village level)\n"
                    "3. Elections to the Panchayats (State Election Commission)\n"
                    "4. Reservation of Seats for SCs, STs and Women\n\n"
                    "Select the correct code:"
                ),
                "options": [
                    "A-2, B-4, C-1, D-3",
                    "A-1, B-3, C-2, D-4",
                    "A-2, B-1, C-4, D-3",
                    "A-3, B-4, C-1, D-2"
                ],
                "correct_index": 0,
                "explanation": (
                    "Correct Matching:\n"
                    "• 243-A: Gram Sabha\n"
                    "• 243-D: Reservation of seats (SCs, STs, and min 1/3rd for Women)\n"
                    "• 243-I: State Finance Commission\n"
                    "• 243-K: Elections to Panchayats (State Election Commissioner)."
                ),
                "source": "Constitution of India — Part IX (Articles 243 to 243-O)"
            },
            {
                "q_no": 3,
                "id": "APPSC-MICRO-04-Q03",
                "subject": "Indian Polity & Constitution",
                "topic": "Compulsory vs Voluntary Provisions of 73rd Amendment",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "Which of the following are 'Compulsory (Mandatory)' provisions under the 73rd Constitutional Amendment Act that every State Legislature must implement?\n"
                    "1. Organization of Gram Sabha in a village or group of villages (Article 243-A)\n"
                    "2. Establishment of a 3-tier Panchayati Raj system at Village, Intermediate, and District levels (except in States with population < 20 Lakh where intermediate tier is optional)\n"
                    "3. Minimum 21 years of age for contesting Panchayat elections (Article 243-F)\n"
                    "4. Reserving seats and offices of Chairpersons for Backward Classes (BCs/OBCs)\n\n"
                    "Select the correct answer using the code given below:"
                ),
                "options": [
                    "1, 2 and 3 only",
                    "1, 2, 3 and 4",
                    "2, 3 and 4 only",
                    "1 and 4 only"
                ],
                "correct_index": 0,
                "explanation": (
                    "Statements 1, 2, and 3 are Compulsory provisions.\n"
                    "• Statement 4 is a Voluntary provision: Providing reservation for Other Backward Classes (OBCs) is left to the discretion of individual State Legislatures under Article 243-D(6)."
                ),
                "source": "Ministry of Panchayati Raj Compulsory/Voluntary Guidelines & Constitution"
            },
            {
                "q_no": 4,
                "id": "APPSC-MICRO-04-Q04",
                "subject": "Indian Polity & Constitution",
                "topic": "State Election Commissioner (Article 243-K & 243-ZA)",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "Consider the following statements regarding the State Election Commissioner (SEC) appointed under Article 243-K of the Constitution:\n"
                    "1. The SEC is appointed by the Governor of the State.\n"
                    "2. The SEC can be removed from office only in like manner and on the like grounds as a Judge of a High Court.\n"
                    "3. The conditions of service and tenure of office of the SEC cannot be varied to their disadvantage after appointment.\n\n"
                    "Which of the statements given above are correct?"
                ),
                "options": [
                    "1, 2 and 3",
                    "1 and 2 only",
                    "2 and 3 only",
                    "1 and 3 only"
                ],
                "correct_index": 0,
                "explanation": (
                    "All three statements (1, 2, and 3) are correct:\n"
                    "• Article 243-K(1): Appointed by the Governor.\n"
                    "• Article 243-K(2): Has constitutional protection equivalent to a High Court Judge (removal by Parliament via proved misbehavior/incapacity) and conditions cannot be varied to disadvantage."
                ),
                "source": "Constitution of India (Article 243-K) & Supreme Court in Aparmita Prasad Case"
            },
            {
                "q_no": 5,
                "id": "APPSC-MICRO-04-Q05",
                "subject": "Indian Polity & Constitution",
                "topic": "PESA Act, 1996 (Extension to Scheduled Areas)",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "Regarding the Panchayats (Extension to the Scheduled Areas) Act, 1996 (PESA Act, 1996), which extends Part IX to Fifth Schedule Areas in 10 states (including Andhra Pradesh), consider the following:\n"
                    "1. PESA was enacted on the recommendations of the Dileep Singh Bhuria Committee.\n"
                    "2. Every Gram Sabha in PESA areas is endowed with mandatory ownership of Minor Forest Produce (MFP).\n"
                    "3. Mandatory prior consultation with the Gram Sabha / Panchayats is required before acquiring land for development projects and rehabilitating affected persons.\n\n"
                    "Which of the statements given above are correct?"
                ),
                "options": [
                    "1, 2 and 3",
                    "1 and 2 only",
                    "2 and 3 only",
                    "1 and 3 only"
                ],
                "correct_index": 0,
                "explanation": (
                    "All three statements (1, 2, and 3) are correct:\n"
                    "• Enacted following Bhuria Committee (1995).\n"
                    "• Endows Gram Sabha with minor forest produce ownership, land alienation control, minor water body management, and liquor licensing power."
                ),
                "source": "Ministry of Tribal Affairs / Ministry of Panchayati Raj — PESA Act, 1996"
            },
            {
                "q_no": 6,
                "id": "APPSC-MICRO-04-Q06",
                "subject": "Indian Polity & Constitution",
                "topic": "District Planning Committee (Article 243-ZD)",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Under Article 243-ZD of the Constitution, what proportion of the members of the District Planning Committee (DPC) must be elected by and from among the elected members of the Zilla Praja Parishad (Panchayat at district level) and Municipalities in the district?"
                ),
                "options": [
                    "Not less than four-fifths (4/5ths or 80%) in proportion to the rural and urban population of the district",
                    "Exactly one-half (50%)",
                    "100% appointed by the District Collector",
                    "Not less than one-third (33%)"
                ],
                "correct_index": 0,
                "explanation": (
                    "Under Article 243-ZD(2)(b), not less than four-fifths (4/5) of the total members of the DPC shall be elected by, and from amongst, the elected members of the district Panchayat and Municipalities in proportion to rural/urban population."
                ),
                "source": "Constitution of India — Article 243-ZD (District Planning Committee)"
            },
            {
                "q_no": 7,
                "id": "APPSC-MICRO-04-Q07",
                "subject": "Indian Polity & Constitution",
                "topic": "Metropolitan Planning Committee (Article 243-ZE)",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Under Article 243-ZE of the Constitution, a Metropolitan Planning Committee (MPC) is constituted for metropolitan areas having a population of:"
                ),
                "options": [
                    "10 Lakh (1 Million) or more",
                    "5 Lakh or more",
                    "50 Lakh or more",
                    "1 Crore or more"
                ],
                "correct_index": 0,
                "explanation": (
                    "Article 243-P(c) defines a Metropolitan area as an area having a population of 10 Lakh (1 Million) or more. Article 243-ZE mandates a Metropolitan Planning Committee where not less than 2/3rds members are elected by municipal councillors and panchayat chairpersons."
                ),
                "source": "Constitution of India — Article 243-ZE & 243-P"
            },
            {
                "q_no": 8,
                "id": "APPSC-MICRO-04-Q08",
                "subject": "Indian Polity & Constitution",
                "topic": "Eleventh Schedule Subjects Count & Examples",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "Which of the following functional items are included in the Eleventh Schedule (29 subjects under Article 243-G) devolved to Panchayats?\n"
                    "1. Agriculture, including agricultural extension\n"
                    "2. Minor irrigation, water management, and watershed development\n"
                    "3. Drinking water and Rural housing\n"
                    "4. Atomic Energy and Defence Communications\n\n"
                    "Select the correct answer using the code given below:"
                ),
                "options": [
                    "1, 2 and 3 only",
                    "1, 2, 3 and 4",
                    "2 and 3 only",
                    "1 and 4 only"
                ],
                "correct_index": 0,
                "explanation": (
                    "Items 1, 2, and 3 are part of the 29 subjects in the Eleventh Schedule.\n"
                    "• Item 4 (Atomic Energy & Defence) is under Union List (List I, Seventh Schedule) and has no relation to Panchayats."
                ),
                "source": "Eleventh Schedule of the Constitution (Article 243-G)"
            },
            {
                "q_no": 9,
                "id": "APPSC-MICRO-04-Q09",
                "subject": "Indian Polity & Constitution",
                "topic": "Twelfth Schedule Subjects Count & Examples",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "How many functional subjects are listed in the Twelfth Schedule of the Constitution (Article 243-W) for Municipalities, and which of the following is an example?"
                ),
                "options": [
                    "18 subjects; including Urban planning, Regulation of land-use, Roads and bridges, Water supply, and Fire services",
                    "29 subjects; including Railways and Space research",
                    "10 subjects; including Income tax assessment",
                    "22 subjects; including Passport issuance"
                ],
                "correct_index": 0,
                "explanation": (
                    "The Twelfth Schedule contains 18 items governing municipal administration (urban planning, solid waste management, fire services, public amenities, burial grounds, slum improvement)."
                ),
                "source": "Twelfth Schedule of the Constitution (Article 243-W)"
            },
            {
                "q_no": 10,
                "id": "APPSC-MICRO-04-Q10",
                "subject": "Indian Polity & Constitution",
                "topic": "Committees on Panchayati Raj Evolution",
                "question_type": "Pair Matching MCQ",
                "question": (
                    "Arrange the following landmark Committees on Panchayati Raj in chronological order of their constitution:\n"
                    "1. Balwant Rai Mehta Committee\n"
                    "2. Ashok Mehta Committee\n"
                    "3. G.V.K. Rao Committee\n"
                    "4. L.M. Singhvi Committee\n\n"
                    "Select the correct chronological sequence:"
                ),
                "options": [
                    "1 — 2 — 3 — 4",
                    "2 — 1 — 3 — 4",
                    "1 — 3 — 2 — 4",
                    "4 — 3 — 2 — 1"
                ],
                "correct_index": 0,
                "explanation": (
                    "Chronological Order:\n"
                    "1. Balwant Rai Mehta Committee (1957) — recommended 3-tier Panchayati Raj\n"
                    "2. Ashok Mehta Committee (1977–78) — recommended 2-tier system (Mandal Panchayat & Zilla Parishad)\n"
                    "3. G.V.K. Rao Committee (1985) — recommended making ZP the principal development body\n"
                    "4. L.M. Singhvi Committee (1986) — first recommended constitutional recognition for Panchayats."
                ),
                "source": "Ministry of Panchayati Raj Evolution Reports & NCERT Indian Polity"
            },
            {
                "q_no": 11,
                "id": "APPSC-MICRO-04-Q11",
                "subject": "Indian Polity & Constitution",
                "topic": "Article 243-E Duration and Dissolution Rules",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "Under Article 243-E of the Constitution regarding the duration of Panchayats, consider the following statements:\n"
                    "1. Every Panchayat shall continue for five years from the date appointed for its first meeting and no longer.\n"
                    "2. If a Panchayat is dissolved prematurely before the expiration of its 5-year duration, elections to constitute the new Panchayat must be completed within six months of dissolution.\n"
                    "3. A Panchayat reconstituted after premature dissolution serves for a fresh full term of 5 years.\n\n"
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
                    "• Under Article 243-E(4), a Panchayat constituted upon the dissolution of a Panchayat before the expiration of its duration shall continue only for the remainder of the period for which the dissolved Panchayat would have continued."
                ),
                "source": "Constitution of India — Article 243-E (Duration of Panchayats)"
            },
            {
                "q_no": 12,
                "id": "APPSC-MICRO-04-Q12",
                "subject": "Indian Polity & Constitution",
                "topic": "Article 243-O Bar to Interference by Courts",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Under Article 243-O of the Constitution, what bar is imposed on the jurisdiction of courts in electoral matters concerning Panchayats?"
                ),
                "options": [
                    "The validity of any law relating to the delimitation of constituencies or allotment of seats cannot be called in question in any court, and no election to any Panchayat shall be called in question except by an election petition presented to such authority as provided by State law",
                    "Courts can stay all Panchayat elections across India at will",
                    "Panchayat disputes must be tried directly by the International Court of Justice",
                    "High Courts can abolish the State Election Commission"
                ],
                "correct_index": 0,
                "explanation": (
                    "Article 243-O bars courts from interfering in delimitation and provides that Panchayat elections can only be questioned via election petitions before prescribed tribunals."
                ),
                "source": "Constitution of India — Article 243-O"
            },
            {
                "q_no": 13,
                "id": "APPSC-MICRO-04-Q13",
                "subject": "Indian Polity & Constitution",
                "topic": "Types of Municipalities under Article 243-Q",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Article 243-Q of the Constitution provides for the constitution of three types of Municipalities based on demographic and economic factors. What are they?"
                ),
                "options": [
                    "Nagar Panchayat (for transitional areas from rural to urban), Municipal Council (for smaller urban areas), and Municipal Corporation (for larger urban areas)",
                    "Gram Panchayat, Mandal Parishad, and Zilla Parishad",
                    "Cantonment Board, Port Trust, and Notified Area Committee",
                    "Town Area Committee, Census Town, and Smart City"
                ],
                "correct_index": 0,
                "explanation": (
                    "Article 243-Q(1) specifies:\n"
                    "• (a) Nagar Panchayat: transitional area\n"
                    "• (b) Municipal Council (Nagara Palika): smaller urban area\n"
                    "• (c) Municipal Corporation (Maha Nagara Palika): larger urban area."
                ),
                "source": "Constitution of India — Article 243-Q"
            },
            {
                "q_no": 14,
                "id": "APPSC-MICRO-04-Q14",
                "subject": "Indian Polity & Constitution",
                "topic": "Wards Committees under Article 243-S",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Under Article 243-S of the Constitution, the constitution of Wards Committees is mandatory within the territorial area of a Municipality having a population of:"
                ),
                "options": [
                    "3 Lakh or more",
                    "1 Lakh or more",
                    "50,000 or more",
                    "10 Lakh or more"
                ],
                "correct_index": 0,
                "explanation": (
                    "Article 243-S mandates the constitution of Wards Committees (consisting of one or more wards) within the territorial area of a Municipality having a population of 3 Lakh (300,000) or more."
                ),
                "source": "Constitution of India — Article 243-S"
            },
            {
                "q_no": 15,
                "id": "APPSC-MICRO-04-Q15",
                "subject": "Indian Polity & Constitution",
                "topic": "Women Reservation in Panchayats (Article 243-D & State Acts)",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "Regarding reservation for women under Article 243-D of the Constitution and Andhra Pradesh Panchayat Raj Act, 1994, consider the following:\n"
                    "1. Article 243-D(3) mandates that not less than one-third (33.33%) of the total number of seats to be filled by direct election in every Panchayat shall be reserved for women.\n"
                    "2. Article 243-D(4) mandates that not less than one-third of the total number of offices of Chairpersons in Panchayats at each level shall be reserved for women.\n"
                    "3. Andhra Pradesh has legally enhanced women's reservation in local bodies (Panchayats and Municipalities) to 50%.\n\n"
                    "Which of the statements given above are correct?"
                ),
                "options": [
                    "1, 2 and 3",
                    "1 and 2 only",
                    "2 and 3 only",
                    "1 and 3 only"
                ],
                "correct_index": 0,
                "explanation": (
                    "All three statements (1, 2, and 3) are correct:\n"
                    "• The Constitution sets a floor of 1/3rd (33.33%).\n"
                    "• Andhra Pradesh (along with 20 other states) enacted legislation enhancing women's reservation to 50% in local bodies."
                ),
                "source": "Article 243-D & AP Panchayat Raj (Amendment) Act"
            },
            {
                "q_no": 16,
                "id": "APPSC-MICRO-04-Q16",
                "subject": "Indian Polity & Constitution",
                "topic": "Article 243-M Areas Exempted from Part IX",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Under Article 243-M of the Constitution, which of the following areas/states are exempted from the application of Part IX (Panchayats) unless extended by law?"
                ),
                "options": [
                    "The States of Nagaland, Meghalaya, and Mizoram, Hill areas in Manipur with District Councils, and Darjeeling Gorkha Hill Council areas",
                    "All coastal districts of Andhra Pradesh and Tamil Nadu",
                    "The entire states of Punjab, Haryana, and Gujarat",
                    "Only Union Territories with Legislative Assemblies"
                ],
                "correct_index": 0,
                "explanation": (
                    "Article 243-M exempts Nagaland, Meghalaya, Mizoram (traditional tribal councils exist), Scheduled/Tribal areas under Article 244 (extended via PESA), and Darjeeling/Manipur hill councils."
                ),
                "source": "Constitution of India — Article 243-M"
            },
            {
                "q_no": 17,
                "id": "APPSC-MICRO-04-Q17",
                "subject": "Indian Polity & Constitution",
                "topic": "Audit of Accounts of Panchayats (Article 243-J)",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Under Article 243-J and Article 243-Z of the Constitution, who is empowered to make provisions with respect to the maintenance of accounts and auditing of such accounts of Panchayats and Municipalities?"
                ),
                "options": [
                    "The Legislature of a State by law",
                    "The Comptroller and Auditor General (CAG) acting solely without state law",
                    "The World Bank",
                    "The Union Finance Minister"
                ],
                "correct_index": 0,
                "explanation": (
                    "Articles 243-J and 243-Z empower the State Legislature by law to make provisions regarding maintenance and auditing of accounts of local bodies (often audited by State Local Fund Audit Dept / CAG Technical Guidance)."
                ),
                "source": "Constitution of India — Article 243-J & 243-Z"
            },
            {
                "q_no": 18,
                "id": "APPSC-MICRO-04-Q18",
                "subject": "Indian Polity & Constitution",
                "topic": "G.V.K. Rao Committee 'Grass without Roots' Phrase",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "Which Committee appointed by the Planning Commission in 1985 observed that development administration was becoming increasingly bureaucratized and divorced from local participation, describing Panchayati Raj as 'Grass without Roots'?"
                ),
                "options": [
                    "G.V.K. Rao Committee",
                    "Sarkaria Commission",
                    "Thungon Committee",
                    "Kothari Commission"
                ],
                "correct_index": 0,
                "explanation": (
                    "The G.V.K. Rao Committee (1985) coined the famous critique 'Grass without Roots' to describe how bureaucratic control had weakened Panchayati Raj institutions."
                ),
                "source": "Planning Commission Committee on Administrative Arrangements for Rural Development (1985)"
            },
            {
                "q_no": 19,
                "id": "APPSC-MICRO-04-Q19",
                "subject": "Indian Polity & Constitution",
                "topic": "Gram Sabha Definition under Article 243(b)",
                "question_type": "Direct Concept MCQ",
                "question": (
                    "How is 'Gram Sabha' constitutionally defined under Article 243(b) of the Constitution of India?"
                ),
                "options": [
                    "A body consisting of all persons registered in the electoral rolls relating to a village comprised within the area of Panchayat at the village level",
                    "An elected council of 5 village elders appointed by the Tehsildar",
                    "A meeting exclusively of landowning farmers and taxpayers",
                    "The executive committee of the Gram Panchayat"
                ],
                "correct_index": 0,
                "explanation": (
                    "Article 243(b) defines Gram Sabha as a constitutional body consisting of all registered voters (persons registered in the electoral rolls) of the village."
                ),
                "source": "Constitution of India — Article 243(b)"
            },
            {
                "q_no": 20,
                "id": "APPSC-MICRO-04-Q20",
                "subject": "Indian Polity & Constitution",
                "topic": "Andhra Pradesh Panchayat Raj Act, 1994 Structure",
                "question_type": "Multi-Statement Analysis",
                "question": (
                    "In conformity with the 73rd Constitutional Amendment Act, the Andhra Pradesh Panchayat Raj Act, 1994 established a 3-tier Panchayati Raj structure comprising:\n"
                    "1. Gram Panchayat at the Village level (headed by Sarpanch)\n"
                    "2. Mandal Praja Parishad (MPP) at the Mandal / Intermediate level (headed by MPP President)\n"
                    "3. Zilla Praja Parishad (ZPP) at the District level (headed by ZPP Chairperson)\n\n"
                    "Which of the statements given above are correct?"
                ),
                "options": [
                    "1, 2 and 3",
                    "1 and 2 only",
                    "2 and 3 only",
                    "1 and 3 only"
                ],
                "correct_index": 0,
                "explanation": (
                    "All three statements (1, 2, and 3) are correct:\n"
                    "• Andhra Pradesh follows the 3-tier system: Gram Panchayat (Village), Mandal Praja Parishad (Mandal), and Zilla Praja Parishad (District)."
                ),
                "source": "Andhra Pradesh Panchayat Raj Act, 1994 (Act No. 13 of 1994)"
            }
        ]
    }
]
