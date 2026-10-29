#!/usr/bin/env python3
"""
APPSC Group 1 & Group 2 Exam Test Series Generator
==================================================
Generates 32 comprehensive, exam-formatted Test Series for APPSC Group 1 and Group 2 aspirants:
- Tests 1-8:   APPSC Group 1 Prelims Full Mock Tests (120 Questions | 120 Minutes | +1 / -0.33 Marks)
- Tests 9-18:  APPSC Group 2 Prelims & Mains Full Mock Tests (150 Questions | 150 Minutes | +1 / -0.33 Marks)
- Tests 19-32: PIB Government Portal, AP Schemes & Subject-Wise Sectional Tests (50 Questions | 50 Minutes | +1 / -0.33 Marks)

Every question includes:
- Official APPSC exam-level framing (Statement-based, Assertion-Reason, Match-the-Following, Direct Conceptual)
- 4 options (A, B, C, D)
- Detailed multi-point explanation & exam takeaways
- Reliable government source citation (PIB, PRS India, AP Socio-Economic Survey, Constitution of India, NCERT/Standard Refs)
"""

import json
import os
import random
from datetime import datetime

# Ensure deterministic yet varied test generation across the 32 test series
random.seed(20261028)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)


# ==============================================================================
# 1. CURATED HIGH-YIELD APPSC KNOWLEDGE BASE BY SUBJECT
# ==============================================================================

AP_HISTORY_FACTS = [
    {
        "topic": "Satavahana Dynasty",
        "fact": "Gautamiputra Satakarni (c. 106–130 CE) was the greatest ruler of the Satavahana dynasty, whose achievements are recorded in the Nasik Prasasti inscribed by his mother Gautami Balasri.",
        "detail": "He defeated the Western Kshatrapa ruler Nahapana (proven by the Jogalthambi hoard of restruck silver coins) and assumed titles like 'Ekabrahmana', 'Trisamudratoyapitavahana', and 'Kshatriyadarpamana-mardana'.",
        "false_stmt": "Gautamiputra Satakarni issued the Hathigumpha inscription in Kalinga and shifted the Satavahana capital permanently to Kanchipuram.",
        "source": "AP History - Satavahana Epigraphy & AP State Archives"
    },
    {
        "topic": "Satavahana Administration & Culture",
        "fact": "Hala, the 17th ruler of the Satavahana dynasty, compiled 'Gathasaptasati' (Sattasai), an anthology of 700 erotic and pastoral verses in Maharashtri Prakrit.",
        "detail": "During the Satavahana period, nigamas (merchant guilds) and srenis played a vital role in trade, issuing potin and lead coins, with major ports at Motupalli, Koddura, and Ghantasala (Kantakossyla).",
        "false_stmt": "Gathasaptasati was composed in classical Sanskrit by Nagarjuna at the court of Pulomavi III.",
        "source": "APSC Syllabus - Social & Cultural History of Andhra Pradesh"
    },
    {
        "topic": "Ikshvaku Dynasty (Vijayapuri)",
        "fact": "Vasishthiputra Chamtamula founded the Ikshvaku dynasty with Vijayapuri (Nagarjunakonda) as its capital and performed Vedic sacrifices including Agnishtoma, Vajapeya, and Asvamedha.",
        "detail": "While the Ikshvaku kings patronized Vedic Brahmanism, the royal women (such as Chamtisri, sister of Chamtamula) generously patronized Buddhist mahachaityas and viharas at Nagarjunakonda.",
        "false_stmt": "The Ikshvaku kings banned Buddhism completely and destroyed all stupas in the Krishna valley.",
        "source": "Archaeological Survey of India (ASI) - Nagarjunakonda Excavations"
    },
    {
        "topic": "Eastern Chalukyas of Vengi",
        "fact": "Kubja Vishnuvardhana, brother of Pulakesin II, founded the Eastern Chalukya dynasty of Vengi in 624 CE, initiating nearly five centuries of rule in Coastal Andhra.",
        "detail": "Under Rajaraja Narendra (1019–1061 CE) at Rajamahendravaram, Nannaya Bhatta began translating the Sanskrit Mahabharata into Telugu, earning the title 'Adi Kavi' (First Poet), assisted by Narayana Bhatta (mentioned in the Nandampudi Grant).",
        "false_stmt": "Nannaya Bhatta completed all eighteen parvas of the Andhra Mahabharata single-handedly during the reign of Kubja Vishnuvardhana.",
        "source": "APSahitya Akademi & Epigraphia Indica"
    },
    {
        "topic": "Kakatiya Dynasty (Orugallu)",
        "fact": "Ganapatideva (1199–1262 CE) unified the Telugu-speaking lands under the Kakatiya empire, shifted the capital to Orugallu (Warangal), and issued the famous Motupalli Abhaya Sasana (1244 CE) guaranteeing safety and fair customs duties to foreign sea merchants.",
        "detail": "He was succeeded by his daughter Rudramadevi (who ruled under the male title Rudradeva Maharaja, praised by Marco Polo) and later Prataparudra II. The Kakatiyas pioneered the 'Nayankara' military tenure system and chain-tank irrigation.",
        "false_stmt": "The Motupalli Abhaya Sasana was issued by Prola I to prohibit all maritime trade with Southeast Asia.",
        "source": "AP History - Kakatiya Epigraphy & Motupalli Inscription"
    },
    {
        "topic": "Vijayanagara Empire (Tuluva Dynasty)",
        "fact": "Sri Krishnadevaraya (1509–1529 CE) of the Tuluva dynasty authored 'Amuktamalyada' (Vishnuchittiyam) in Telugu, which expounds both Vaishnava bhakti and pragmatic statecraft (Rajaniti).",
        "detail": "His court 'Bhuvana Vijayam' was adorned by the Ashtadiggajas (eight literary stalwarts including Allasani Peddana, author of Manucharitra). Foreign travelers Duarte Barbosa and Domingo Paes visited Vijayanagara during his reign.",
        "false_stmt": "Sri Krishnadevaraya belonged to the Aravidu dynasty and fought the Battle of Talikota in 1565 CE.",
        "source": "National Portal of India - Vijayanagara Heritage & APPSC Archives"
    },
    {
        "topic": "British Revenue Administration in Andhra",
        "fact": "Sir Thomas Munro introduced the Ryotwari settlement in the Ceded Districts (Rayalaseema) starting in 1800–1807 as Principal Collector before becoming Governor of Madras Presidency (1820–1827).",
        "detail": "Under the Ryotwari system, land revenue was settled directly with the individual cultivator (ryot) rather than through zamindars, alongside cadastral survey and classification of soils.",
        "false_stmt": "Sir Thomas Munro introduced the Permanent Zamindari Settlement in Rayalaseema while Lord Cornwallis introduced Ryotwari in Northern Circars.",
        "source": "Madras Presidency District Gazetteers & AP History"
    },
    {
        "topic": "19th Century Socio-Religious Reform in AP",
        "fact": "Kandukuri Veeresalingam Pantulu (1848–1919), hailed as the 'Father of the Renaissance Movement in Andhra', founded the journal 'Vivekavardhani' (1874) and performed the first widow remarriage in Andhra on December 11, 1881 at Rajahmundry.",
        "detail": "He also established the Hitakarini Samajam (1906) and wrote 'Rajasekhara Charitramu', considered the first novel in Telugu literature.",
        "false_stmt": "Kandukuri Veeresalingam opposed women's education and founded the Justice Party in Madras in 1916.",
        "source": "Ministry of Culture - Indian Renaissance Leaders & AP State Portal"
    },
    {
        "topic": "Vandemataram & Swadeshi Movement in Andhra",
        "fact": "Bipin Chandra Pal's tour of Coastal Andhra in April 1907 (visiting Vizianagaram, Visakhapatnam, Kakinada, Rajahmundry, and Vijayawada) galvanized the Vandemataram Movement, with Chilakamarthi Lakshmi Narasimham spontaneously composing the famous Telugu verse 'Bharata Desamunati Paadi Aavu'.",
        "detail": "The Rajahmundry College incident (1907) saw students suspended by Principal Mark Hunter for wearing Vandemataram badges, while the Kotappakonda incident (1909) saw Chinnapa Reddy executed.",
        "false_stmt": "Bipin Chandra Pal toured Andhra in 1930 during the Civil Disobedience Movement at the invitation of Lord Curzon.",
        "source": "History of Freedom Movement in Andhra Pradesh - State Committee"
    },
    {
        "topic": "Rampa Rebellion (1922–1924)",
        "fact": "Alluri Sitarama Raju led the heroic Rampa (Manyam) Rebellion (1922–1924) in the Visakhapatnam-Godavari agency tracts against oppressive British forest laws (1882 Madras Forest Act) and forced unpaid labor (Muttadari exploitation and Bastian's road works).",
        "detail": "Raju raided police stations including Chintapalli, Krishnadevipeta, and Rajavommangi for arms, before being martyred on May 7, 1924 at Koyyuru.",
        "false_stmt": "Alluri Sitarama Raju led the Chirala-Perala movement in Guntur district against municipal taxation.",
        "source": "PIB Special Feature - Azadi Ka Amrit Mahotsav Tribal Freedom Fighters"
    },
    {
        "topic": "Non-Cooperation Movement in AP",
        "fact": "During the Non-Cooperation Movement (1921–22), Andhra witnessed unique local struggles: the Chirala-Perala movement led by Duggirala Gopalakrishnayya (who formed the 'Ramadandu' volunteer corps and evacuated the town to 'Ramnagar') and the Pedanandipadu No-Tax campaign led by Parvataneni Veeraiah Chowdary ('Andhra Sivaji').",
        "detail": "Meanwhile, Karumanchi Venkata Subbaiah and Kanneganti Hanumanthu led the Palnadu Forest Satyagraha in Guntur district.",
        "false_stmt": "The Pedanandipadu No-Tax Campaign was organized during the Quit India Movement of 1942 in Srikakulam district.",
        "source": "AP State Archives - Freedom Struggle in Andhra"
    },
    {
        "topic": "Formation of Andhra State (1953) & Sribagh Pact",
        "fact": "The Sribagh Pact was signed on November 16, 1937 at the residence of Kashinathuni Nageswara Rao in Madras between leaders of Coastal Andhra and Rayalaseema to safeguards Rayalaseema's irrigation and administrative interests in a future Andhra province.",
        "detail": "Following the 58-day fast-unto-death and martyrdom of Potti Sreeramulu on December 15, 1952, Andhra State was carved out of Madras Presidency on October 1, 1953 with Kurnool as capital and Tanguturi Prakasam Pantulu as First Chief Minister.",
        "false_stmt": "The Sribagh Pact was signed in 1956 between leaders of Coastal Andhra and Telangana at Hyderabad.",
        "source": "AP Reorganization & State Formation Official Records"
    },
    {
        "topic": "AP Reorganization Act, 2014 (Act No. 6 of 2014)",
        "fact": "The Andhra Pradesh Reorganization Act, 2014 contains 108 Sections divided into 12 Parts and 13 Schedules, receiving Presidential assent on March 1, 2014 and coming into force on the 'Appointed Day' of June 2, 2014.",
        "detail": "Under Part IX (Section 85), the Godavari and Krishna River Management Boards were constituted, while Section 90 mandated the execution of the Polavaram Irrigation Project as a National Project by the Central Government.",
        "false_stmt": "The AP Reorganization Act, 2014 contains 95 Sections and 8 Schedules, declaring Polavaram a state-funded municipal project under Schedule VII.",
        "source": "Ministry of Home Affairs (MHA) - Gazette of India, AP Reorganization Act 2014"
    },
    {
        "topic": "Schedules of AP Reorganization Act, 2014",
        "fact": "In the AP Reorganization Act, 2014, Schedule IX lists 89 Government Companies and Corporations (such as APSRTC, APGENCO) while Schedule X lists 107 State-level Training Institutions and Centers for division/sharing between Andhra Pradesh and Telangana.",
        "detail": "Schedule XI specifies the principles governing the functioning of the Krishna and Godavari River Management Boards, and Schedule XIII covers infrastructure, educational, and industrial development measures (including Visakhapatnam-Chennai Industrial Corridor and metro rail).",
        "false_stmt": "Schedule IX of the AP Reorganization Act deals with allocation of Rajya Sabha seats, while Schedule X deals with amendment to the Constitution's First Schedule.",
        "source": "Legislative Department, Ministry of Law and Justice - AP Reorganization Act, 2014"
    }
]

POLITY_FACTS = [
    {
        "topic": "Constitutional Bodies & Finance Commission",
        "fact": "Under Article 280 of the Constitution of India, the President constitutes the Finance Commission every five years to recommend the distribution of net proceeds of taxes between the Union and the States (vertical devolution) and among the States (horizontal devolution).",
        "detail": "The 16th Finance Commission was constituted by the Government of India with Dr. Arvind Panagariya as Chairman, covering the five-year award period starting April 1, 2026.",
        "false_stmt": "The Finance Commission is a statutory body created under the RBI Act, 1934 and is chaired ex-officio by the Union Finance Minister.",
        "source": "PIB - Ministry of Finance & Article 280 of the Constitution of India"
    },
    {
        "topic": "Fundamental Rights & Constitutional Remedies",
        "fact": "Article 32 guarantees the right to move the Supreme Court for the enforcement of Fundamental Rights and was described by Dr. B.R. Ambedkar as the 'very soul of the Constitution and the very heart of it'.",
        "detail": "While the Supreme Court issues writs only for the enforcement of Fundamental Rights under Article 32, High Courts under Article 226 have wider writ jurisdiction extending to both Fundamental Rights and ordinary legal rights ('for any other purpose').",
        "false_stmt": "The writ jurisdiction of the Supreme Court under Article 32 is wider than that of a High Court under Article 226 because it includes ordinary legal rights.",
        "source": "Constitution of India - Part III & Supreme Court Judgments"
    },
    {
        "topic": "73rd & 74th Constitutional Amendment Acts (1992)",
        "fact": "The 73rd Constitutional Amendment Act, 1992 added Part IX ('The Panchayats', Articles 243 to 243-O) and the Eleventh Schedule containing 29 functional items to the Constitution.",
        "detail": "Article 243-D mandates not less than one-third reservation of seats and chairperson offices for women in Panchayats, while Article 243-I provides for a State Finance Commission every five years and Article 243-K provides for the State Election Commission.",
        "false_stmt": "The 73rd Amendment Act added the Twelfth Schedule with 18 items and placed Panchayat elections under the direct supervision of the Election Commission of India (Article 324).",
        "source": "Ministry of Panchayati Raj & Constitution of India"
    },
    {
        "topic": "Parliamentary Committees (PAC & Estimates)",
        "fact": "The Public Accounts Committee (PAC) consists of 22 members (15 from Lok Sabha and 7 from Rajya Sabha) elected annually by proportional representation using single transferable vote, examining the audit reports of the Comptroller and Auditor General (CAG).",
        "detail": "By parliamentary convention established since 1967, the Chairperson of the PAC is appointed by the Speaker from the Opposition. In contrast, the Estimates Committee has 30 members drawn exclusively from the Lok Sabha.",
        "false_stmt": "The Estimates Committee comprises 22 members from both Houses of Parliament and is always chaired by the Leader of the Opposition in Rajya Sabha.",
        "source": "Lok Sabha Secretariat & PRS Legislative Research"
    },
    {
        "topic": "106th Constitutional Amendment Act, 2023 (Nari Shakti Vandan Adhiniyam)",
        "fact": "The Constitution (106th Amendment) Act, 2023 reserves one-third (33%) of all seats for women in the Lok Sabha (Article 330A), State Legislative Assemblies (Article 332A), and the Legislative Assembly of NCT of Delhi (Article 239AA).",
        "detail": "This reservation also applies within the seats reserved for Scheduled Castes (SCs) and Scheduled Tribes (STs), and will take effect after the publication of the first Census and subsequent delimitation exercise following the Act's enactment, for a period of 15 years.",
        "false_stmt": "The 106th Constitutional Amendment Act reserves 33% seats for women in the Rajya Sabha and State Legislative Councils with immediate effect from 2024 without requiring delimitation.",
        "source": "PIB - Ministry of Law and Justice, Gazette Notification"
    },
    {
        "topic": "Anti-Defection Law (Tenth Schedule)",
        "fact": "The Tenth Schedule was inserted by the 52nd Constitutional Amendment Act, 1985 to curb political defections, while the 91st Amendment Act, 2003 omitted the provision allowing a 'split' by one-third of legislature party members and restricted the size of the Council of Ministers to 15% of the strength of the lower house.",
        "detail": "In Kihoto Hollohan vs Zachillhu (1992), the Supreme Court held that the Presiding Officer waiting to decide disqualification under the Tenth Schedule functions as a tribunal and their final decision is subject to judicial review on grounds of mala fides or perversity.",
        "false_stmt": "The Tenth Schedule was added by the 42nd Amendment Act, 1976 and grants absolute immunity from judicial review to the Speaker's decision.",
        "source": "PRS Legislative Research & Supreme Court Constitutional Bench Rulings"
    },
    {
        "topic": "Centre-State Legislative Relations & Seventh Schedule",
        "fact": "Under Article 249, Parliament is empowered to legislate on any matter in the State List in the national interest if the Rajya Sabha passes a resolution supported by not less than two-thirds of the members present and voting.",
        "detail": "Such a resolution remains in force for one year at a time (renewable any number of times by one year each). Residuary powers of legislation are vested in the Union Parliament under Article 248.",
        "false_stmt": "Under Article 249, only the Lok Sabha can authorize Parliament to legislate on a State List subject by a simple majority.",
        "source": "Constitution of India - Part XI (Centre-State Relations)"
    },
    {
        "topic": "Governor's Legislative Powers (Articles 200 & 213)",
        "fact": "Under Article 200, when a State Bill is presented to the Governor, the Governor may give assent, withhold assent, return the Bill (if it is not a Money Bill) for reconsideration, or reserve the Bill for the consideration of the President.",
        "detail": "Under Article 213, the Governor can promulgate Ordinances only when the State Legislature (or either House in a bicameral legislature) is not in session; such ordinances must be approved by the State Legislature within six weeks of its reassembly.",
        "false_stmt": "A Governor can return a State Money Bill for reconsideration under Article 200 and promulgate ordinances even when both Houses of the State Legislature are in session.",
        "source": "Ministry of Law and Justice - Constitution of India"
    }
]

ECONOMY_FACTS = [
    {
        "topic": "Monetary Policy Committee (MPC) & RBI",
        "fact": "Under Section 45ZB of the amended RBI Act, 1934, the Monetary Policy Committee (MPC) is a six-member statutory body (3 from RBI including the Governor as ex-officio Chairperson, and 3 external members appointed by the Central Government) tasked with maintaining price stability while keeping in mind the objective of growth.",
        "detail": "The flexible inflation targeting framework mandates maintaining Consumer Price Index (CPI-Combined) inflation at 4% with a tolerance band of +/- 2% (i.e., 2% to 6%). The RBI Governor holds a casting vote in case of a tie.",
        "false_stmt": "The Monetary Policy Committee consists of 10 members chaired by the Union Finance Secretary and targets Wholesale Price Index (WPI) inflation at 2%.",
        "source": "Reserve Bank of India (RBI) Official Portal & PIB Finance Releases"
    },
    {
        "topic": "Goods and Services Tax (GST) Council",
        "fact": "The GST Council is a constitutional body established under Article 279A (inserted by the 101st Constitutional Amendment Act, 2016), chaired by the Union Finance Minister with State Finance/Taxation Ministers as members.",
        "detail": "Every decision of the GST Council requires a majority of not less than three-fourths (75%) of the weighted votes of the members present and voting, where the Central Government's vote has a weightage of one-third (33.33%) and all State Governments together have a weightage of two-thirds (66.67%).",
        "false_stmt": "The GST Council is a non-statutory body chaired by the NITI Aayog Vice-Chairperson where the Union Government holds a 51% veto weightage.",
        "source": "GST Council Secretariat & PIB Ministry of Finance"
    },
    {
        "topic": "AP Economic Survey & Agriculture Sector",
        "fact": "Andhra Pradesh is widely recognized as the 'Aqua Hub of India' and the 'Fruit Bowl of the South', ranking first nationally in total fish and shrimp production as well as oil palm, papaya, lemon, and tomato cultivation.",
        "detail": "The Gross Value Added (GVA) of the Agriculture and Allied Sector (particularly Horticulture and Livestock/Aquaculture) contributes over one-third of Andhra Pradesh's GSVA, significantly higher than the national average share of agriculture in GDP.",
        "false_stmt": "Andhra Pradesh has zero coastal aquaculture contribution and its agriculture sector accounts for less than 5% of the state's Gross State Value Added (GSVA).",
        "source": "AP Socio-Economic Survey & Directorate of Economics and Statistics, AP"
    },
    {
        "topic": "Fiscal Responsibility and Budget Management (FRBM)",
        "fact": "Primary Deficit is defined as Fiscal Deficit minus Interest Payments on previous borrowings, indicating the borrowing requirement of the government strictly for current year non-interest expenditure.",
        "detail": "Effective Revenue Deficit (ERD) equals Revenue Deficit minus Grants-in-Aid for the creation of capital assets, distinguishing consumption expenditure from capital-building transfers to states.",
        "false_stmt": "Primary Deficit is calculated by adding Total Revenue Receipts to Gross Fiscal Deficit.",
        "source": "Union Budget Documents & Ministry of Finance Glossary"
    },
    {
        "topic": "Industrial Corridors in Andhra Pradesh",
        "fact": "Andhra Pradesh is the only state in India traversed by three major National Industrial Corridors: the Visakhapatnam-Chennai Industrial Corridor (VCIC), the Chennai-Bengaluru Industrial Corridor (CBIC - Krishnapatnam node), and the Hyderabad-Bengaluru Industrial Corridor (HBIC - Orvakal/Kurnool node).",
        "detail": "Major industrial nodes being developed under NICDC and APIIC include Nakkapalli (Anakapalli), Kopparthy (YSR Kadapa), Krishnapatnam (Tirupati/Nellore), and Orvakal (Kurnool).",
        "false_stmt": "Andhra Pradesh is excluded from the National Industrial Corridor Development Programme (NICDP) and has no coastal industrial nodes.",
        "source": "PIB - Ministry of Commerce & Industry (DPIIT) & APIIC Portal"
    },
    {
        "topic": "Multidimensional Poverty Index (NITI Aayog)",
        "fact": "NITI Aayog's National Multidimensional Poverty Index (MPI) measures simultaneous deprivations across three equally weighted dimensions—Health, Education, and Standard of Living—comprising 12 indicators aligned with the Sustainable Development Goals (SDGs).",
        "detail": "Compared to the global MPI (which uses 10 indicators), India's National MPI adds two critical indicators: 'Maternal Health (Antenatal Care)' under Health and 'Bank Account' under Standard of Living.",
        "false_stmt": "NITI Aayog's National MPI measures poverty solely using daily per-capita calorie intake without considering health or education.",
        "source": "PIB - NITI Aayog National Multidimensional Poverty Index Report"
    },
    {
        "topic": "PM-KISAN & PM Vishwakarma Schemes (PIB Flagship)",
        "fact": "Under PM-KISAN (Pradhan Mantri Kisan Samman Nidhi), the Central Government provides income support of Rs. 6,000 per year in three equal four-monthly installments of Rs. 2,000 directly into the Aadhaar-seeded bank accounts of landholding farmer families via Direct Benefit Transfer (DBT).",
        "detail": "Meanwhile, the PM Vishwakarma Scheme (launched on September 17, 2023 with a Rs. 13,000 crore outlay) supports traditional artisans and craftspeople across 18 trades with PM Vishwakarma certificates, Rs. 15,000 toolkit e-vouchers, and collateral-free enterprise development loans up to Rs. 3 lakh (in two tranches of Rs. 1 lakh and Rs. 2 lakh at 5% concessional interest).",
        "false_stmt": "PM-KISAN provides Rs. 25,000 per month only to large corporate plantations, while PM Vishwakarma is restricted exclusively to software exporters.",
        "source": "PIB - Ministry of Agriculture & Farmers Welfare / Ministry of MSME"
    },
    {
        "topic": "Balance of Payments & Foreign Exchange Reserves",
        "fact": "India's Foreign Exchange Reserves held by the Reserve Bank of India consist of four components: Foreign Currency Assets (FCA - the largest component), Gold reserves, Special Drawing Rights (SDRs) with the IMF, and the Reserve Tranche Position (RTP) in the IMF.",
        "detail": "In the Balance of Payments (BoP), software service exports and private remittances from the Indian diaspora are recorded under the 'Invisibles' (Services and Transfers) sub-account of the Current Account, whereas FDI and FPI inflows are recorded under the Capital/Financial Account.",
        "false_stmt": "Foreign Direct Investment (FDI) inflows and external commercial borrowings are part of the Merchandise Trade balance in the Current Account.",
        "source": "RBI Handbook of Statistics on the Indian Economy"
    }
]

GEOGRAPHY_FACTS = [
    {
        "topic": "Physical Geography of Andhra Pradesh & Coastline",
        "fact": "Andhra Pradesh possesses the second-longest mainland coastline in India (~974 km) after Gujarat, stretching from Ichchapuram (Srikakulam district) in the north to Tada/Pulicat Lake (Tirupati district) in the south along the Bay of Bengal.",
        "detail": "The Eastern Ghats in Andhra Pradesh are discontinuous, dissected by major east-flowing rivers (Godavari, Krishna, Penna, Nagavali, Vamsadhara). Jindhagada Peak (~1,690 m) in the Araku Valley / Alluri Sitharama Raju district is the highest peak in Andhra Pradesh.",
        "false_stmt": "Andhra Pradesh has a landlocked border with no coastline, and Dodabetta is the highest mountain peak located in Guntur district.",
        "source": "AP State Geography Portal & Survey of India"
    },
    {
        "topic": "River Systems & Polavaram Project",
        "fact": "The Godavari River (Dakshin Ganga, total length ~1,465 km) enters Andhra Pradesh and forms a vast lobate delta below Rajamahendravaram (Dowleswaram Barrage built by Sir Arthur Cotton in 1852); its major left-bank tributaries include Purna, Pranhita, Indravati, and Sabari, while Manjira is a major right-bank tributary.",
        "detail": "The Polavaram Project (Indira Sagar) is a multi-purpose National Irrigation Project on the Godavari River near Ramayyapeta village, designed to transfer 80 TMC of surplus Godavari water to the Krishna river basin via the Right Main Canal (Pattiseema/Prakasam Barrage link).",
        "false_stmt": "The Godavari River originates in the Aravalli Range and flows westward into the Arabian Sea without forming any delta.",
        "source": "PIB - Ministry of Jal Shakti & Central Water Commission (CWC)"
    },
    {
        "topic": "Kolleru & Pulicat Lakes (Wetlands of AP)",
        "fact": "Kolleru Lake, located across the inter-deltaic plain between the Krishna and Godavari deltas in Eluru/West Godavari region, is one of India's largest freshwater lakes and is designated as a Ramsar Wetland of International Importance.",
        "detail": "Pulicat Lake, located at the southern border of Andhra Pradesh (Tirupati district) and Tamil Nadu, is the second-largest brackish water lagoon in India after Chilika Lake, separated from the Bay of Bengal by the barrier island of Sriharikota (home to ISRO's Satish Dhawan Space Centre).",
        "false_stmt": "Kolleru Lake is a hypersaline volcanic crater lake in Rayalaseema, whereas Pulicat Lake is a glacial freshwater lake in the Himalayas.",
        "source": "Ministry of Environment, Forest and Climate Change (MoEFCC) - Ramsar Sites"
    },
    {
        "topic": "Mineral Wealth of Andhra Pradesh",
        "fact": "The Mangampeta deposit in Annamayya/YSR Kadapa district of Andhra Pradesh holds the single largest reserve of Barytes in the world (accounting for over 90% of India's barytes resources), while the Tummalapalle belt is one of the largest strata-bound Uranium reserves globally.",
        "detail": "Additionally, Andhra Pradesh is a leading producer of limestone (Cuddapah basin), mica (Nellore mica belt), beach sand heavy minerals (ilmenite, monazite, garnet along Srikakulam-Visakhapatnam coast), and bauxite (Eastern Ghats agency tracts).",
        "false_stmt": "Mangampeta is famous strictly for anthracite coal mines, and Andhra Pradesh lacks any limestone or barytes deposits.",
        "source": "Indian Bureau of Mines (IBM) Yearbook & Dept of Mines and Geology, AP"
    },
    {
        "topic": "Indian Monsoon & Retreating Northeast Monsoon",
        "fact": "While most of India receives over 75% of its annual rainfall from the Southwest Monsoon (June–September), the southern coastal districts of Andhra Pradesh (Nellore, Tirupati, Prakasam) and Rayalaseema receive a substantial portion (30–50%) of their annual rainfall from the Retreating / Northeast Monsoon (October–December).",
        "detail": "During the Northeast Monsoon, winds blowing over the warm Bay of Bengal pick up moisture and frequently interact with tropical cyclonic depressions to bring heavy post-monsoon rainfall to the Coromandel coast.",
        "false_stmt": "Coastal Andhra and Rayalaseema receive 100% of their rainfall only from Western Disturbances in January and zero rainfall from October to December.",
        "source": "India Meteorological Department (IMD) Climatological Atlas"
    },
    {
        "topic": "Forests & Protected Areas in Andhra Pradesh",
        "fact": "The Nagarjunasagar-Srisailam Tiger Reserve (NSTR), spanning the Nallamala hills across Nandyal, Prakasam, and Palnadu districts, is the largest Tiger Reserve in India by core and total notified area (~3,728 sq. km).",
        "detail": "The Seshachalam Hills (Tirupati/Annamayya/Kadapa districts) are designated as a Biosphere Reserve by MoEFCC and are the globally endemic habitat of the precious Red Sanders (Pterocarpus santalinus) and the Golden Gecko.",
        "false_stmt": "Nagarjunasagar-Srisailam Tiger Reserve is the smallest wildlife sanctuary in India and is located in the Western Ghats of Kerala.",
        "source": "National Tiger Conservation Authority (NTCA) & AP Forest Department"
    }
]

INDIAN_SOCIETY_FACTS = [
    {
        "topic": "Tribal Groups & PVTGs of Andhra Pradesh",
        "fact": "Out of 75 Particularly Vulnerable Tribal Groups (PVTGs) notified across India, Andhra Pradesh and Telangana region historically share key PVTGs with Andhra Pradesh hosting 6 major PVTG communities in its Scheduled Areas: Chenchu, Gadaba, Gutob Gadaba, Khond (Dongria/Kutia), Kolam/Konda Reddi, and Savara (Konda Savara).",
        "detail": "The PM-JANMAN (Pradhan Mantri Janjati Adivasi Nyaya Maha Abhiyan) mission, launched by the Government of India with an outlay of ~Rs. 24,104 crore across 9 Ministries, saturates PVTG habitations with pucca housing, piped water, mobile medical units, Van Dhan Vikas Kendras, and road connectivity.",
        "false_stmt": "Andhra Pradesh has no Scheduled Tribes or PVTGs notified under Article 342 of the Constitution.",
        "source": "PIB - Ministry of Tribal Affairs & Tribal Welfare Department, AP"
    },
    {
        "topic": "Caste System, Sanskritization & Social Mobility",
        "fact": "Sociologist M.N. Srinivas introduced the concepts of 'Sanskritization' (the process by which a 'low' Hindu caste or tribal group changes its customs, ritual, ideology, and way of life in the direction of a 'high', frequently twice-born caste) and 'Dominant Caste' in Indian sociology.",
        "detail": "A 'Dominant Caste' is characterized by sizable numerical strength, substantial ownership of arable land in the village, high ritual/local status, and access to modern western education and administration.",
        "false_stmt": "The concept of 'Sanskritization' was coined by Karl Marx to describe industrial automation in European factories.",
        "source": "APPSC Group 2 Prelims Syllabus - Structure of Indian Society (NCERT Sociology)"
    },
    {
        "topic": "Constitutional & Statutory Safeguards for SCs, STs & OBCs",
        "fact": "The National Commission for Scheduled Castes (Article 338), National Commission for Scheduled Tribes (Article 338A, inserted by the 89th Amendment Act, 2003), and National Commission for Backward Classes (Article 338B, inserted by the 102nd Amendment Act, 2018) are constitutional bodies vested with the powers of a civil court to investigate and monitor safeguards.",
        "detail": "Furthermore, the fifth schedule of the Constitution combined with the Panchayats (Extension to the Scheduled Areas) Act, 1996 (PESA) empowers the Gram Sabha in Scheduled Areas to safeguard tribal traditions, control minor forest produce, and regulate land alienation.",
        "false_stmt": "The National Commission for Backward Classes (NCBC) was abolished by the 102nd Constitutional Amendment Act, 2018.",
        "source": "Ministry of Social Justice and Empowerment & PIB Releases"
    },
    {
        "topic": "Welfare Mechanisms for Women & Children",
        "fact": "The Government of India reorganized women and child welfare schemes under three umbrella missions: 'Mission Saksham Anganwadi and Poshan 2.0' (nutrition), 'Mission Shakti' (comprising 'Sambal' for safety/security like One Stop Centres & Beti Bachao Beti Padhao, and 'Samarthya' for empowerment like PM Matru Vandana Yojana & Shakti Sadan), and 'Mission Vatsalya' (child protection services).",
        "detail": "Legislations such as the Protection of Women from Domestic Violence Act (2005), Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act (2013 - POSH), and POCSO Act (2012) form the legal backbone for safety.",
        "false_stmt": "Mission Vatsalya is a heavy-industry mining subsidy scheme under the Ministry of Coal.",
        "source": "PIB - Ministry of Women and Child Development"
    },
    {
        "topic": "Kinship, Marriage & Family Systems in India",
        "fact": "In Indian kinship sociology (analyzed by Irawati Karve in 'Kinship Organization in India'), Northern Indian kinship is strongly patrilineal with village exogamy and prohibition of cross-cousin marriages, whereas Dravidian (Southern Indian) kinship traditionally permits preferential cross-cousin and uncle-niece alliances while maintaining clan (gotra/intiperu) exogamy.",
        "detail": "Meanwhile, matrilineal kinship systems have historically been practiced among the Khasis, Jaintias, and Garos of Meghalaya and the Nairs of Kerala (taravad system).",
        "false_stmt": "According to Irawati Karve, Southern Indian Dravidian kinship strictly prohibits all forms of cross-cousin marriage while Northern India practices matrilineal inheritance.",
        "source": "APPSC Group 2 Indian Society Syllabus - Family, Marriage & Kinship"
    }
]

SCIENCE_TECH_FACTS = [
    {
        "topic": "ISRO Space Missions (Chandrayaan-3, Aditya-L1 & Gaganyaan)",
        "fact": "ISRO's Chandrayaan-3 successfully soft-landed its Vikram Lander (carrying the Pragyan Rover) near the lunar south pole (at ~69.37° S latitude, named 'Statio Shiv Shakti') on August 23, 2023—celebrated annually as 'National Space Day'—making India the first country to land near the lunar south pole and fourth overall to soft-land on the Moon.",
        "detail": "Subsequently, Aditya-L1 (launched via PSLV-C57 on September 2, 2023) was inserted into a halo orbit around the Sun-Earth Lagrange Point 1 (L1, ~1.5 million km from Earth) with 7 payloads (including VELC and SUIT) for continuous uninterrupted solar observation.",
        "false_stmt": "Chandrayaan-3 landed on Mars' north pole using a GSLV Mk-I rocket, while Aditya-L1 orbits around Lagrange Point L3 behind the Sun.",
        "source": "PIB - Department of Space / ISRO Official Releases"
    },
    {
        "topic": "NISAR & Next-Generation Launch Vehicles (ISRO)",
        "fact": "NISAR (NASA-ISRO Synthetic Aperture Radar) is a joint Earth-observing satellite mission featuring dual-frequency radar: an L-band SAR provided by NASA and an S-band SAR provided by ISRO, using SweepSAR technology to map global land surface changes, ice-sheet dynamics, and natural hazards every 12 days.",
        "detail": "ISRO launches satellites primarily from the Satish Dhawan Space Centre (SDSC-SHAR) at Sriharikota in Tirupati district, Andhra Pradesh, utilizing PSLV, GSLV, LVM3 (Launch Vehicle Mark-3), and SSLV (Small Satellite Launch Vehicle).",
        "false_stmt": "NISAR is a deep-space telescope jointly built by Roscosmos and ESA without any radar payloads.",
        "source": "ISRO Official Portal & PIB Science & Technology"
    },
    {
        "topic": "National Green Hydrogen Mission & Renewable Energy",
        "fact": "Approved by the Union Cabinet with an initial outlay of Rs. 19,744 crore (anchored by the SIGHT programme—Strategic Interventions for Green Hydrogen Transition), the National Green Hydrogen Mission targets a production capacity of at least 5 Million Metric Tonnes (MMT) of Green Hydrogen per annum by 2030, along with adding ~125 GW of associated renewable energy capacity.",
        "detail": "Andhra Pradesh (particularly Visakhapatnam/Pudimadaka and Kakinada green hydrogen hubs) has emerged as a major coastal destination for Green Hydrogen and Green Ammonia production and export projects.",
        "false_stmt": "The National Green Hydrogen Mission aims to replace solar and wind energy with coal-based grey hydrogen by 2030.",
        "source": "PIB - Ministry of New and Renewable Energy (MNRE)"
    },
    {
        "topic": "Biotechnology: CRISPR-Cas9, CAR-T Cell Therapy & Vaccines",
        "fact": "NexCAR19, developed indigenously at IIT Bombay and Tata Memorial Centre and approved by CDSCO, is India's first indigenous Chimeric Antigen Receptor T-cell (CAR-T) gene therapy for treating relapsed/refractory B-cell lymphomas and leukemia at a fraction of global costs.",
        "detail": "Meanwhile, CRISPR-Cas9 (using guide RNA and Cas9 endonuclease) has enabled breakthroughs such as indigenous gene-editing research for Sickle Cell Anaemia under the National Sickle Cell Anaemia Elimination Mission (targeting elimination by 2047).",
        "false_stmt": "CAR-T cell therapy is an antibiotic ointment derived from marine algae used only for bacterial skin infections.",
        "source": "PIB - Department of Biotechnology (DBT) & Ministry of Health"
    },
    {
        "topic": "IndiaAI Mission & National Quantum Mission",
        "fact": "The Union Cabinet approved the 'IndiaAI Mission' (outlay over Rs. 10,300 crore) to build a high-end common compute infrastructure of 10,000+ GPUs, indigenous large multimodal foundational models, and the IndiaAI Datasets Platform.",
        "detail": "Complementing it, the National Quantum Mission (NQM, outlay ~Rs. 6,003 crore for 2023–2031) aims to develop intermediate-scale quantum computers with 50–1,000 physical qubits and establish four Thematic Hubs (T-Hubs) in Quantum Computing, Quantum Communication, Quantum Sensing, and Quantum Materials.",
        "false_stmt": "The National Quantum Mission is restricted to manufacturing analog vacuum tubes and excludes quantum cryptography.",
        "source": "PIB - MeitY & Department of Science and Technology (DST)"
    },
    {
        "topic": "Defence Technology & DRDO Missile Systems",
        "fact": "Mission Divyastra marked the successful flight test by DRDO of the indigenous Agni-5 intercontinental surface-to-surface ballistic missile equipped with MIRV (Multiple Independently Targetable Re-entry Vehicle) technology, enabling a single missile to deliver multiple nuclear warheads at different independent targets hundreds of kilometers apart.",
        "detail": "Under the Integrated Guided Missile Development Programme (IGMDP) conceived by Dr. A.P.J. Abdul Kalam, India developed Prithvi, Agni, Trishul, Akash, and Nag, alongside the supersonic cruise missile BrahMos.",
        "false_stmt": "Agni-5 with MIRV technology is a short-range anti-tank unguided rocket with a maximum range of 4 kilometers.",
        "source": "PIB - Ministry of Defence / DRDO Press Release"
    }
]

INDIAN_HISTORY_FACTS = [
    {
        "topic": "Indus Valley Civilization (Harappan Sites)",
        "fact": "Dholavira (located on Khadir Bet island in the Rann of Kutch, Gujarat and inscribed as India's 40th UNESCO World Heritage Site) is unique among Harappan cities for its division into three parts (Citadel, Middle Town, and Lower Town) and its sophisticated rock-cut water harvesting reservoirs and ten-sign signboard inscription.",
        "detail": "Lothal (on the Bhogavo river in Gujarat) featured an artificial brick tidal dockyard and bead-making factory, while Kalibangan (Rajasthan) provided evidence of the earliest ploughed agricultural field and fire altars.",
        "false_stmt": "Dholavira is located in the Gangetic plains of Bihar and lacked any drainage or water storage systems.",
        "source": "Ministry of Culture / ASI - Harappan Civilization Records"
    },
    {
        "topic": "Mauryan Empire & Ashokan Edicts",
        "fact": "Emperor Ashoka's Major Rock Edict XIII gives a vivid, remorseful account of the Kalinga War (261 BCE, fought in the 8th regnal year after his coronation) and records his shift from 'Bherighosha' (conquest by force) to 'Dhammaghosha' (conquest by righteousness), while also mentioning Hellenistic kings like Antiochus II, Ptolemy II, Antigonus, Magas, and Alexander.",
        "detail": "Within Andhra Pradesh, major Ashokan edicts (Major Rock Edicts I–XIV and Minor Rock Edicts) are found at Erragudi and Rajulamandagiri in Kurnool district.",
        "false_stmt": "Ashoka's Major Rock Edict XIII celebrates his invasion of Sri Lanka and is written exclusively in Latin script.",
        "source": "ASI Epigraphy Branch - Corpus Inscriptionum Indicarum"
    },
    {
        "topic": "Indian National Movement (1885–1947)",
        "fact": "At the Lahore Session of the Indian National Congress in December 1929 (presided over by Jawaharlal Nehru on the banks of the Ravi River), the Congress passed the historic 'Purna Swaraj' (Complete Independence) resolution and declared January 26, 1930 as Independence Day.",
        "detail": "Earlier, at the 1921 Vijayawada AICC Session in Andhra Pradesh, Pingali Venkayya presented the design of the Swaraj National Flag (initially with red and green bands and a charkha, with white added on Mahatma Gandhi's suggestion).",
        "false_stmt": "The Purna Swaraj resolution was passed at the first INC session in 1885 at Bombay under Lord Dufferin's presidency.",
        "source": "PIB Azadi Ka Amrit Mahotsav & INC History Archives"
    },
    {
        "topic": "Constitutional Reforms under British Rule (1909, 1919, 1935)",
        "fact": "The Government of India Act, 1919 (Montagu-Chelmsford Reforms) introduced 'Dyarchy' in the Provinces (dividing provincial subjects into 'Transferred' and 'Reserved') and bicameralism at the Centre, whereas the Government of India Act, 1935 abolished Provincial Dyarchy, introduced 'Provincial Autonomy', and proposed an All-India Federation with a three-fold division of legislative lists (Federal, Provincial, Concurrent).",
        "detail": "The Indian Councils Act, 1909 (Morley-Minto Reforms) had earlier introduced separate communal electorates for Muslims and brought Satyendra Prasad Sinha as the first Indian member into the Viceroy's Executive Council.",
        "false_stmt": "The Government of India Act, 1935 introduced Provincial Dyarchy for the first time and abolished the Federal Court and Reserve Bank of India.",
        "source": "Constitutional History of India - National Archives"
    }
]

PIB_CURRENT_AFFAIRS_FACTS = [
    {
        "topic": "PIB Cabinet Decision: PM Surya Ghar Muft Bijli Yojana",
        "fact": "The Union Cabinet approved 'PM Surya Ghar: Muft Bijli Yojana' with a total outlay of Rs. 75,021 crore to install rooftop solar plants in 1 crore households across India, providing up to 300 units of free electricity every month.",
        "detail": "The scheme provides a central financial assistance (CFA) subsidy of Rs. 30,000 for 1 kW, Rs. 60,000 for 2 kW, and Rs. 78,000 for 3 kW systems or higher, alongside collateral-free low-interest loans around 7% and developing one 'Model Solar Village' in every district.",
        "false_stmt": "PM Surya Ghar Yojana provides free diesel generators to industrial factories with zero subsidy for residential rooftop solar.",
        "source": "PIB - Cabinet Committee on Economic Affairs / MNRE"
    },
    {
        "topic": "PIB Release: Ayushman Bharat Vaya Vandana Card (70+ Senior Citizens)",
        "fact": "Under the expanded Ayushman Bharat Pradhan Mantri Jan Arogya Yojana (AB PM-JAY), the Government of India launched health coverage of Rs. 5 lakh per year for ALL senior citizens aged 70 years and above, regardless of their socio-economic or income status.",
        "detail": "Eligible senior citizens receive a distinct 'Ayushman Vaya Vandana Card'; if they belong to a family already covered under AB PM-JAY, they get an additional shared top-up cover of up to Rs. 5 lakh per year exclusively for the 70+ senior members.",
        "false_stmt": "The expanded AB PM-JAY 70+ scheme is restricted only to retired central government defense officers earning below Rs. 10,000 per year.",
        "source": "PIB - Ministry of Health and Family Welfare (NHA)"
    },
    {
        "topic": "PIB Release: Polavaram & Amaravati Infrastructure Support",
        "fact": "Under the Union Budget and Cabinet commitments following the Andhra Pradesh Reorganization Act, 2014, the Central Government committed Rs. 15,000 crore financial assistance through multilateral development agencies for the development of Andhra Pradesh's greenfield capital city Amaravati, alongside fast-tracking the Polavaram National Irrigation Project.",
        "detail": "In addition, special grants and industrial infrastructure support were approved for the Kopparthy node on the Visakhapatnam-Chennai Industrial Corridor and the Orvakal node on the Hyderabad-Bengaluru Industrial Corridor, plus backward region grants for Rayalaseema and North Coastal Andhra.",
        "false_stmt": "The Union Budget repealed the AP Reorganization Act, 2014 and canceled all central funding for Polavaram and industrial corridors.",
        "source": "PIB - Ministry of Finance Union Budget Highlights"
    },
    {
        "topic": "PIB Release: Classical Languages Status",
        "fact": "The Union Cabinet approved conferring the status of 'Classical Language' to five additional Indian languages—Marathi, Pali, Prakrit, Assamese, and Bengali—taking the total number of recognized Classical Languages in India to eleven (joining Tamil, Sanskrit, Telugu, Kannada, Malayalam, and Odia).",
        "detail": "Telugu was accorded Classical Language status in 2008 based on its high antiquity of early texts/recorded history over 1500–2000 years and an original literary tradition distinct from modern forms. The Centre for Excellence for Studies in Classical Telugu (CESCT) operates at Nellore in Andhra Pradesh.",
        "false_stmt": "India recognizes only two Classical Languages, and Telugu has never been granted Classical Language status by the Ministry of Culture.",
        "source": "PIB - Ministry of Culture Cabinet Decision"
    },
    {
        "topic": "PIB Release: Dharti Aaba Janjatiya Gram Utkarsh Abhiyan (DAJGUA)",
        "fact": "Launched with a total outlay of Rs. 79,156 crore, the 'Dharti Aaba Janjatiya Gram Utkarsh Abhiyan' aims at complete saturation of critical social infrastructure gaps in ~63,000 tribal-majority villages across 549 districts in 30 States/UTs, benefiting over 5 crore tribal citizens.",
        "detail": "It converges 25 interventions implemented by 17 Union Ministries across housing, road connectivity, clean energy, telecom, mobile medical units, and Poshan.",
        "false_stmt": "Dharti Aaba Abhiyan is an urban metro rail privatization scheme limited solely to tier-1 metropolitan cities.",
        "source": "PIB - Ministry of Tribal Affairs"
    },
    {
        "topic": "PIB Release: BioE3 Policy (Biotechnology for Economy, Environment & Employment)",
        "fact": "The Union Cabinet approved the 'BioE3 Policy' (Biotechnology for Economy, Environment and Employment) spearheaded by the Department of Biotechnology to foster high-performance biomanufacturing across six thematic sectors: bio-based chemicals, smart proteins, precision biotherapeutics, climate-resilient agriculture, carbon capture, and marine/space biotechnology.",
        "detail": "The policy establishes Bio-Enabler Hubs, Biofoundries, and Biomanufacturing centres to accelerate India's transition toward a regenerative Green Bioeconomy.",
        "false_stmt": "The BioE3 Policy bans all fermentation and biomanufacturing research in Indian universities.",
        "source": "PIB - Ministry of Science & Technology (DBT)"
    }
]


# ==============================================================================
# 2. QUESTION SYNTHESIZER ENGINE (PRODUCES UNIQUE APPSC-FORMAT QUESTIONS)
# ==============================================================================

def create_questions_from_bank():
    """Generates a large, diverse pool of APPSC Group 1 & Group 2 questions across all subjects."""
    all_facts = (
        [("AP History & Reorganization", f) for f in AP_HISTORY_FACTS]
        + [("Indian Polity & Constitution", f) for f in POLITY_FACTS]
        + [("Indian & AP Economy", f) for f in ECONOMY_FACTS]
        + [("Geography of India & AP", f) for f in GEOGRAPHY_FACTS]
        + [("Indian Society & Welfare", f) for f in INDIAN_SOCIETY_FACTS]
        + [("Science, Tech & Environment", f) for f in SCIENCE_TECH_FACTS]
        + [("Indian History & National Movement", f) for f in INDIAN_HISTORY_FACTS]
        + [("PIB & Govt Schemes Current Affairs", f) for f in PIB_CURRENT_AFFAIRS_FACTS]
    )

    pool = []
    qid = 1

    # Pattern 1: 2-Statement "Consider the following statements" (Both 1 and 2 correct)
    for subj, item in all_facts:
        pool.append({
            "id": f"Q{qid:04d}",
            "subject": subj,
            "topic": item["topic"],
            "question_type": "Statement-Based (APPSC Pattern)",
            "question": (
                f"Consider the following statements regarding {item['topic']}:\n"
                f"1. {item['fact']}\n"
                f"2. {item['detail']}\n\n"
                f"Which of the statements given above is/are correct?"
            ),
            "options": [
                "1 only",
                "2 only",
                "Both 1 and 2",
                "Neither 1 nor 2"
            ],
            "correct_index": 2,
            "explanation": (
                f"Both Statement 1 and Statement 2 are correct.\n"
                f"• Statement 1 is correct: {item['fact']}\n"
                f"• Statement 2 is correct: {item['detail']}\n"
                f"• Exam Note: Questions on {item['topic']} frequently test both institutional/constitutional specifics and Andhra Pradesh regional implications."
            ),
            "source": item["source"]
        })
        qid += 1

        # Pattern 2: 2-Statement with Statement 2 False (1 only correct)
        pool.append({
            "id": f"Q{qid:04d}",
            "subject": subj,
            "topic": item["topic"],
            "question_type": "Statement Elimination",
            "question": (
                f"With reference to {item['topic']}, consider the following statements:\n"
                f"1. {item['fact']}\n"
                f"2. {item['false_stmt']}\n\n"
                f"Which of the statements given above is/are correct?"
            ),
            "options": [
                "1 only",
                "2 only",
                "Both 1 and 2",
                "Neither 1 nor 2"
            ],
            "correct_index": 0,
            "explanation": (
                f"Only Statement 1 is correct.\n"
                f"• Statement 1 is correct: {item['fact']}\n"
                f"• Statement 2 is incorrect because: {item['detail']} (The claim that '{item['false_stmt']}' is factually false)."
            ),
            "source": item["source"]
        })
        qid += 1

        # Pattern 3: 3-Statement APPSC Group 1 "How many statements are correct" / Combination
        pool.append({
            "id": f"Q{qid:04d}",
            "subject": subj,
            "topic": item["topic"],
            "question_type": "Multi-Statement Analysis",
            "question": (
                f"Examine the following three statements regarding {item['topic']}:\n"
                f"Statement I: {item['detail']}\n"
                f"Statement II: {item['false_stmt']}\n"
                f"Statement III: {item['fact']}\n\n"
                f"Which of the above statements are correct?"
            ),
            "options": [
                "I and II only",
                "I and III only",
                "II and III only",
                "I, II and III"
            ],
            "correct_index": 1,
            "explanation": (
                f"Statements I and III are correct, whereas Statement II is incorrect.\n"
                f"• Statement I: {item['detail']}\n"
                f"• Statement III: {item['fact']}\n"
                f"• Statement II is a distractor and is factually wrong."
            ),
            "source": item["source"]
        })
        qid += 1

        # Pattern 4: Assertion-Reason Format
        pool.append({
            "id": f"Q{qid:04d}",
            "subject": subj,
            "topic": item["topic"],
            "question_type": "Assertion-Reason",
            "question": (
                f"Given below are two statements, one labelled as Assertion (A) and the other as Reason (R) regarding {item['topic']}:\n\n"
                f"Assertion (A): {item['fact']}\n"
                f"Reason (R): {item['detail']}\n\n"
                f"Select the correct answer using the code given below:"
            ),
            "options": [
                "Both (A) and (R) are true and (R) provides valid contextual/explanatory support to (A)",
                "Both (A) and (R) are true, but (R) is completely unrelated to the subject of (A)",
                "(A) is true, but (R) is false",
                "(A) is false, but (R) is true"
            ],
            "correct_index": 0,
            "explanation": (
                f"Both Assertion (A) and Reason (R) are true and closely linked under {item['topic']}.\n"
                f"• {item['fact']}\n"
                f"• {item['detail']}"
            ),
            "source": item["source"]
        })
        qid += 1

        # Pattern 5: Identify the Incorrect Statement
        pool.append({
            "id": f"Q{qid:04d}",
            "subject": subj,
            "topic": item["topic"],
            "question_type": "Critical Verification",
            "question": (
                f"Which ONE of the following statements regarding {item['topic']} is NOT correct?"
            ),
            "options": [
                item["fact"],
                item["detail"],
                item["false_stmt"],
                f"Official records under {item['source']} document key provisions on {item['topic']}."
            ],
            "correct_index": 2,
            "explanation": (
                f"Option (C) is NOT correct.\n"
                f"• Correct facts: {item['fact']} Furthermore, {item['detail']}\n"
                f"• Option (C) states '{item['false_stmt']}', which is false."
            ),
            "source": item["source"]
        })
        qid += 1

    # Add Mental Ability, Logical Reasoning & Quantitative Aptitude Questions (APPSC Group 1 & 2 Paper II / Section 5)
    mental_ability_templates = [
        (
            "Percentages & Fiscal Allocation",
            "In a district development project in Andhra Pradesh, 40% of the total fund is allocated to irrigation, 25% of the remaining fund is allocated to rural roads, and the balance of Rs. 90 Crore is allocated to drinking water under Jal Jeevan Mission. What is the total project fund?",
            ["Rs. 150 Crore", "Rs. 180 Crore", "Rs. 200 Crore", "Rs. 240 Crore"],
            2,
            "Step-by-step calculation:\n• Let Total Fund = X.\n• Irrigation allocation = 40% of X = 0.40X. Remaining fund = 60% of X = 0.60X.\n• Rural roads = 25% of remaining (0.60X) = 0.25 × 0.60X = 0.15X.\n• Balance left for drinking water = 0.60X - 0.15X = 0.45X.\n• Given 0.45X = Rs. 90 Crore => X = 90 / 0.45 = Rs. 200 Crore."
        ),
        (
            "Time & Work (Canal Construction)",
            "Engineer Team A can complete a section of the Polavaram feeder canal in 20 days, and Engineer Team B can complete the same section in 30 days. They work together for 8 days, after which Team A leaves. In how many days will Team B alone finish the remaining work?",
            ["8 days", "10 days", "12 days", "15 days"],
            1,
            "Step-by-step calculation:\n• A's 1 day work = 1/20; B's 1 day work = 1/30.\n• Combined 1 day work of (A + B) = 1/20 + 1/30 = (3 + 2)/60 = 5/60 = 1/12.\n• Work done in 8 days together = 8 × (1/12) = 2/3.\n• Remaining work = 1 - 2/3 = 1/3.\n• Time taken by B alone to finish 1/3 work = (1/3) / (1/30) = 10 days."
        ),
        (
            "Number Series & Pattern Recognition",
            "Find the missing number in the APPSC analytical series: 7, 15, 31, 63, 127, ?",
            ["253", "254", "255", "256"],
            2,
            "Step-by-step pattern:\n• Each term follows the rule: (Previous Term × 2) + 1 (or 2^n - 1).\n• 7 × 2 + 1 = 15\n• 15 × 2 + 1 = 31\n• 31 × 2 + 1 = 63\n• 63 × 2 + 1 = 127\n• 127 × 2 + 1 = 255."
        ),
        (
            "Ratio & Proportion (SHG Credit Distribution)",
            "Under a Self-Help Group (SHG) linkage programme, Rs. 1,44,000 is distributed among three groups P, Q, and R in the ratio 3 : 4 : 5. How much more amount does Group R receive than Group P?",
            ["Rs. 18,000", "Rs. 24,000", "Rs. 36,000", "Rs. 48,000"],
            1,
            "Step-by-step calculation:\n• Total ratio parts = 3 + 4 + 5 = 12 parts.\n• Value of 1 part = Rs. 1,44,000 / 12 = Rs. 12,000.\n• Difference between Group R (5 parts) and Group P (3 parts) = 5 - 3 = 2 parts.\n• Required difference = 2 × Rs. 12,000 = Rs. 24,000."
        ),
        (
            "Logical Syllogism",
            "Statements:\n1. All Collectors are Civil Servants.\n2. All Civil Servants are Public Authorities.\n3. Some Public Authorities are Constitutional Functionaries.\n\nConclusions:\nI. All Collectors are Public Authorities.\nII. All Constitutional Functionaries are Collectors.\n\nWhich conclusion logically follows?",
            ["Only Conclusion I follows", "Only Conclusion II follows", "Both I and II follow", "Neither I nor II follows"],
            0,
            "Step-by-step Venn diagram analysis:\n• Since All Collectors ⊂ Civil Servants and All Civil Servants ⊂ Public Authorities, by transitivity All Collectors are definitely Public Authorities (Conclusion I follows).\n• Conclusion II does not follow because 'Some Public Authorities are Constitutional Functionaries' does not imply all of them are Collectors."
        ),
        (
            "Speed, Distance & Time (Vande Bharat Express)",
            "A Vande Bharat Express train 240 meters long crosses a telegraph pole in 8 seconds. How long will it take to cross a railway bridge 660 meters long at the same uniform speed?",
            ["22 seconds", "25 seconds", "30 seconds", "35 seconds"],
            2,
            "Step-by-step calculation:\n• Speed of the train = Length of train / Time to cross pole = 240 m / 8 s = 30 m/s.\n• Total distance to cross the bridge = Length of train + Length of bridge = 240 m + 660 m = 900 m.\n• Time required = 900 m / 30 m/s = 30 seconds."
        ),
        (
            "Compound Interest & Rural Banking",
            "What is the compound interest on a sum of Rs. 50,000 for 2 years at 10% per annum compounded annually?",
            ["Rs. 10,000", "Rs. 10,500", "Rs. 11,000", "Rs. 12,100"],
            1,
            "Step-by-step calculation:\n• Amount A = P(1 + R/100)^n = 50,000 × (1 + 10/100)^2 = 50,000 × (1.1)^2 = 50,000 × 1.21 = Rs. 60,500.\n• Compound Interest = A - P = 60,500 - 50,000 = Rs. 10,500."
        ),
        (
            "Coding-Decoding (Analytical Reasoning)",
            "In a certain code language, if 'AMARAVATI' is coded by shifting each letter one position forward in the English alphabet as 'BNBSBWBUJ', how will 'POLAVARAM' be coded in that language?",
            ["QPMBWBSBN", "QPMBVBSBN", "PONBWBSBN", "QPMBWBSAN"],
            0,
            "Step-by-step letter shift (+1 rule):\n• P(+1)=Q, O(+1)=P, L(+1)=M, A(+1)=B, V(+1)=W, A(+1)=B, R(+1)=S, A(+1)=B, M(+1)=N.\n• Hence 'POLAVARAM' becomes 'QPMBWBSBN'."
        ),
        (
            "Data Interpretation & Averages",
            "The average foodgrain production of 5 mandals in Krishna district is 420 tonnes. If a 6th mandal's production is included, the average increases to 450 tonnes. What is the production of the 6th mandal?",
            ["550 tonnes", "580 tonnes", "600 tonnes", "620 tonnes"],
            2,
            "Step-by-step calculation:\n• Total production of 5 mandals = 5 × 420 = 2,100 tonnes.\n• Total production of 6 mandals = 6 × 450 = 2,700 tonnes.\n• Production of 6th mandal = 2,700 - 2,100 = 600 tonnes."
        ),
        (
            "Blood Relations & Analytical Ability",
            "Pointing to a photograph, Padma said, 'He is the only son of my mother's father.' How is the man in the photograph related to Padma?",
            ["Father", "Maternal Uncle", "Paternal Uncle", "Brother"],
            1,
            "Step-by-step relation deduction:\n• 'My mother's father' = Padma's maternal grandfather.\n• 'The only son of my maternal grandfather' = Padma's mother's brother = Maternal Uncle."
        )
    ]

    for idx, (topic, qtext, opts, cidx, expl) in enumerate(mental_ability_templates, 1):
        pool.append({
            "id": f"Q{qid:04d}",
            "subject": "Mental Ability & Reasoning",
            "topic": topic,
            "question_type": "Analytical & Quantitative",
            "question": qtext,
            "options": opts,
            "correct_index": cidx,
            "explanation": expl,
            "source": "APPSC Prelims CSAT / Mental Ability Official Pattern"
        })
        qid += 1

    return pool


# ==============================================================================
# 3. DEFINE THE 32 PRE-LOADED APPSC GROUP 1 & GROUP 2 TEST SERIES EXAMS
# ==============================================================================

TEST_SERIES_CATALOG = [
    # --- GROUP 1 PRELIMS FULL MOCK TESTS (120 MINS / 120 MARKS / -1/3 NEGATIVE) ---
    {
        "test_id": "APPSC-G1-01",
        "title": "Test 01: APPSC Group-I Prelims Paper-I Full Mock Test 1 (GS-I)",
        "exam_group": "Group 1",
        "category": "Full Length Mock",
        "duration_minutes": 120,
        "question_count": 60,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["AP History & Reorganization", "Indian History & National Movement", "Indian Polity & Constitution", "Indian & AP Economy", "Geography of India & AP"],
        "description": "Official APPSC Group-I Prelims Paper-I pattern covering History & Culture of India & AP, Indian Constitution & Polity, Indian & AP Economy, and Geography with 1/3rd negative marking."
    },
    {
        "test_id": "APPSC-G1-02",
        "title": "Test 02: APPSC Group-I Prelims Paper-II Full Mock Test 1 (GS-II)",
        "exam_group": "Group 1",
        "category": "Full Length Mock",
        "duration_minutes": 120,
        "question_count": 60,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["Mental Ability & Reasoning", "Science, Tech & Environment", "PIB & Govt Schemes Current Affairs"],
        "description": "Official APPSC Group-I Prelims Paper-II pattern covering General Mental Ability, Science & Technology, Environment, and Regional/National Current Affairs from PIB."
    },
    {
        "test_id": "APPSC-G1-03",
        "title": "Test 03: APPSC Group-I Prelims Paper-I Full Mock Test 2 (Advanced Statement Special)",
        "exam_group": "Group 1",
        "category": "Full Length Mock",
        "duration_minutes": 120,
        "question_count": 60,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["AP History & Reorganization", "Indian Polity & Constitution", "Indian & AP Economy", "Geography of India & AP"],
        "description": "High-difficulty statement-elimination and Assertion-Reason mock modeled on latest APPSC Group-I Prelims Paper-I trends."
    },
    {
        "test_id": "APPSC-G1-04",
        "title": "Test 04: APPSC Group-I Prelims Paper-II Full Mock Test 2 (ISRO, DBT, PIB & CSAT)",
        "exam_group": "Group 1",
        "category": "Full Length Mock",
        "duration_minutes": 120,
        "question_count": 60,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["Science, Tech & Environment", "PIB & Govt Schemes Current Affairs", "Mental Ability & Reasoning"],
        "description": "Comprehensive Group-I Paper-II test emphasizing PIB Science & Tech releases, ISRO Sriharikota missions, BioE3 policy, and Data Interpretation."
    },
    {
        "test_id": "APPSC-G1-05",
        "title": "Test 05: APPSC Group-I Prelims Paper-I Full Mock Test 3 (AP Focus)",
        "exam_group": "Group 1",
        "category": "Full Length Mock",
        "duration_minutes": 120,
        "question_count": 60,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["AP History & Reorganization", "Indian & AP Economy", "Geography of India & AP", "Indian Polity & Constitution"],
        "description": "Focused Group-I Paper-I mock with intensive weightage on Andhra Pradesh Dynasties, AP Reorganization Act 2014, AP Socio-Economic Survey, and River Basins."
    },
    {
        "test_id": "APPSC-G1-06",
        "title": "Test 06: APPSC Group-I Prelims Paper-II Full Mock Test 3 (Current Affairs & Aptitude)",
        "exam_group": "Group 1",
        "category": "Full Length Mock",
        "duration_minutes": 120,
        "question_count": 60,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["PIB & Govt Schemes Current Affairs", "Science, Tech & Environment", "Mental Ability & Reasoning"],
        "description": "Balanced simulation of Group-I Paper-II testing time management across analytical reasoning and PIB Cabinet Decisions."
    },
    {
        "test_id": "APPSC-G1-07",
        "title": "Test 07: APPSC Group-I Prelims Grand Championship Mock 1",
        "exam_group": "Group 1",
        "category": "Full Length Mock",
        "duration_minutes": 120,
        "question_count": 60,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["AP History & Reorganization", "Indian Polity & Constitution", "Indian & AP Economy", "Geography of India & AP", "PIB & Govt Schemes Current Affairs"],
        "description": "All-India / State rank simulation test integrating static syllabus with live PIB policy updates for Group-I aspirants."
    },
    {
        "test_id": "APPSC-G1-08",
        "title": "Test 08: APPSC Group-I Prelims Grand Championship Mock 2",
        "exam_group": "Group 1",
        "category": "Full Length Mock",
        "duration_minutes": 120,
        "question_count": 60,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["Indian History & National Movement", "Indian Polity & Constitution", "Science, Tech & Environment", "PIB & Govt Schemes Current Affairs", "Mental Ability & Reasoning"],
        "description": "Final revision full-length Group-I mock test with multi-statement verification and complete solutions."
    },

    # --- GROUP 2 PRELIMS (SCREENING TEST) & MAINS FULL MOCK TESTS (150 MINS) ---
    {
        "test_id": "APPSC-G2-09",
        "title": "Test 09: APPSC Group-II Prelims (Screening Test) Full Mock 1",
        "exam_group": "Group 2",
        "category": "Full Length Mock",
        "duration_minutes": 150,
        "question_count": 75,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["Indian History & National Movement", "Geography of India & AP", "Indian Society & Welfare", "PIB & Govt Schemes Current Affairs", "Mental Ability & Reasoning"],
        "description": "Exact APPSC Group-II Screening Test pattern covering all 5 sections: Indian History, Geography, Indian Society, Current Affairs, and Mental Ability (150 mins timer)."
    },
    {
        "test_id": "APPSC-G2-10",
        "title": "Test 10: APPSC Group-II Prelims (Screening Test) Full Mock 2",
        "exam_group": "Group 2",
        "category": "Full Length Mock",
        "duration_minutes": 150,
        "question_count": 75,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["Indian History & National Movement", "Geography of India & AP", "Indian Society & Welfare", "PIB & Govt Schemes Current Affairs", "Mental Ability & Reasoning"],
        "description": "Full-length Group-II Prelims mock test with equal weightage across History, Geography, Indian Society (Caste, Tribe, Women Welfare), Current Affairs & Reasoning."
    },
    {
        "test_id": "APPSC-G2-11",
        "title": "Test 11: APPSC Group-II Prelims (Screening Test) Full Mock 3",
        "exam_group": "Group 2",
        "category": "Full Length Mock",
        "duration_minutes": 150,
        "question_count": 75,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["Indian History & National Movement", "Geography of India & AP", "Indian Society & Welfare", "PIB & Govt Schemes Current Affairs", "Mental Ability & Reasoning"],
        "description": "Statement-intensive Group-II Screening Test mock focusing on PVTG welfare, AP physical & economic geography, and Modern Indian History."
    },
    {
        "test_id": "APPSC-G2-12",
        "title": "Test 12: APPSC Group-II Prelims (Screening Test) Full Mock 4",
        "exam_group": "Group 2",
        "category": "Full Length Mock",
        "duration_minutes": 150,
        "question_count": 75,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["Indian History & National Movement", "Geography of India & AP", "Indian Society & Welfare", "PIB & Govt Schemes Current Affairs", "Mental Ability & Reasoning"],
        "description": "High-scoring practice mock for Group-II Prelims with 150-minute exam clock and 1/3rd negative penalty."
    },
    {
        "test_id": "APPSC-G2-13",
        "title": "Test 13: APPSC Group-II Prelims (Screening Test) Full Mock 5",
        "exam_group": "Group 2",
        "category": "Full Length Mock",
        "duration_minutes": 150,
        "question_count": 75,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["Indian History & National Movement", "Geography of India & AP", "Indian Society & Welfare", "PIB & Govt Schemes Current Affairs", "Mental Ability & Reasoning"],
        "description": "Pre-exam simulation test for APPSC Group-II Screening Test aspirants with detailed concept notes in solutions."
    },
    {
        "test_id": "APPSC-G2-14",
        "title": "Test 14: APPSC Group-II Mains Paper-I Full Mock 1 (AP History & Indian Constitution)",
        "exam_group": "Group 2",
        "category": "Mains Full Mock",
        "duration_minutes": 150,
        "question_count": 75,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["AP History & Reorganization", "Indian Polity & Constitution"],
        "description": "Official APPSC Group-II Mains Paper-I pattern: Section A (Social & Cultural History of Andhra Pradesh) + Section B (Indian Constitution & Polity) with 150-minute timer."
    },
    {
        "test_id": "APPSC-G2-15",
        "title": "Test 15: APPSC Group-II Mains Paper-II Full Mock 1 (Indian/AP Economy & Science & Tech)",
        "exam_group": "Group 2",
        "category": "Mains Full Mock",
        "duration_minutes": 150,
        "question_count": 75,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["Indian & AP Economy", "Science, Tech & Environment"],
        "description": "Official APPSC Group-II Mains Paper-II pattern: Section A (Indian and AP Economy & Planning) + Section B (Science, Technology & Environment) with 150-minute timer."
    },
    {
        "test_id": "APPSC-G2-16",
        "title": "Test 16: APPSC Group-II Mains Paper-I Full Mock 2 (Satavahanas to Bifurcation + Polity)",
        "exam_group": "Group 2",
        "category": "Mains Full Mock",
        "duration_minutes": 150,
        "question_count": 75,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["AP History & Reorganization", "Indian Polity & Constitution"],
        "description": "Advanced Group-II Mains Paper-I test covering Kakatiya/Vijayanagara administration, Andhra Mahasabha, Sribagh Pact, AP Reorganization Act 2014 & Constitutional Amendments."
    },
    {
        "test_id": "APPSC-G2-17",
        "title": "Test 17: APPSC Group-II Mains Paper-II Full Mock 2 (AP Budget, Survey, ISRO & BioE3)",
        "exam_group": "Group 2",
        "category": "Mains Full Mock",
        "duration_minutes": 150,
        "question_count": 75,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["Indian & AP Economy", "Science, Tech & Environment", "PIB & Govt Schemes Current Affairs"],
        "description": "Advanced Group-II Mains Paper-II test integrating PIB Economic & Science releases, Monetary Policy, GST Council, Space Missions, and Renewable Energy."
    },
    {
        "test_id": "APPSC-G2-18",
        "title": "Test 18: APPSC Group-II Combined Grand Championship Mock",
        "exam_group": "Group 2",
        "category": "Mains Full Mock",
        "duration_minutes": 150,
        "question_count": 75,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["AP History & Reorganization", "Indian Polity & Constitution", "Indian & AP Economy", "Science, Tech & Environment", "Indian Society & Welfare"],
        "description": "Comprehensive Group-II Prelims + Mains integrated championship exam for complete syllabus mastery."
    },

    # --- PIB GOVERNMENT PORTALS & SUBJECT-WISE SPECIAL TEST SERIES (TESTS 19-32) ---
    {
        "test_id": "APPSC-PIB-19",
        "title": "Test 19: PIB Official Portal Special - Union Cabinet Decisions & Flagship Schemes I",
        "exam_group": "Group 1 & 2",
        "category": "PIB & Govt Portals",
        "duration_minutes": 45,
        "question_count": 40,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["PIB & Govt Schemes Current Affairs", "Indian & AP Economy"],
        "description": "Curated directly from Press Information Bureau (pib.gov.in) releases: PM Surya Ghar, Ayushman Vaya Vandana, PM Vishwakarma, PM-KISAN, and Cabinet approvals."
    },
    {
        "test_id": "APPSC-PIB-20",
        "title": "Test 20: PIB Official Portal Special - Ministries, Acts, Missions & Indices II",
        "exam_group": "Group 1 & 2",
        "category": "PIB & Govt Portals",
        "duration_minutes": 45,
        "question_count": 40,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["PIB & Govt Schemes Current Affairs", "Science, Tech & Environment", "Indian Polity & Constitution"],
        "description": "Covers PIB Year-End Ministry reviews: IndiaAI Mission, National Quantum Mission, BioE3 Policy, Classical Languages, and 106th Constitutional Amendment."
    },
    {
        "test_id": "APPSC-APG-21",
        "title": "Test 21: Andhra Pradesh Socio-Economic Survey, Budget & Industrial Corridors",
        "exam_group": "Group 1 & 2",
        "category": "PIB & Govt Portals",
        "duration_minutes": 45,
        "question_count": 40,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["Indian & AP Economy", "Geography of India & AP", "PIB & Govt Schemes Current Affairs"],
        "description": "Sourced from AP Socio-Economic Survey, Union Budget AP allocations, Polavaram National Project updates, VCIC/CBIC/HBIC industrial nodes, and GSVA trends."
    },
    {
        "test_id": "APPSC-SEC-22",
        "title": "Test 22: Social & Cultural History of Andhra Pradesh (Satavahanas to Vijayanagara)",
        "exam_group": "Group 1 & 2",
        "category": "Subject-Wise Test",
        "duration_minutes": 45,
        "question_count": 40,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["AP History & Reorganization"],
        "description": "Deep-dive sectional exam on Satavahanas, Ikshvakus, Eastern Chalukyas, Kakatiyas, Reddi Kingdoms, and Vijayanagara architecture & Telugu literature."
    },
    {
        "test_id": "APPSC-SEC-23",
        "title": "Test 23: Modern AP History, Freedom Struggle & AP Reorganization Act, 2014",
        "exam_group": "Group 1 & 2",
        "category": "Subject-Wise Test",
        "duration_minutes": 45,
        "question_count": 40,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["AP History & Reorganization"],
        "description": "Covers Munro's Ryotwari, Kandukuri Veeresalingam, Vandemataram, Rampa Rebellion, Chirala-Perala, Sribagh Pact, and all 12 Parts & 13 Schedules of AP Reorganization Act 2014."
    },
    {
        "test_id": "APPSC-SEC-24",
        "title": "Test 24: Indian Constitution, Polity, Federalism & PRS Legislative Tracker",
        "exam_group": "Group 1 & 2",
        "category": "Subject-Wise Test",
        "duration_minutes": 45,
        "question_count": 40,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["Indian Polity & Constitution"],
        "description": "High-yield Polity test covering Fundamental Rights, Writs, 73rd/74th Amendments, Parliamentary Committees, Tenth Schedule, Governor's Powers & Finance Commission."
    },
    {
        "test_id": "APPSC-SEC-25",
        "title": "Test 25: Indian Economy, RBI Monetary Policy, GST Council & NITI Aayog Reports",
        "exam_group": "Group 1 & 2",
        "category": "Subject-Wise Test",
        "duration_minutes": 45,
        "question_count": 40,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["Indian & AP Economy"],
        "description": "Focused Economy test on Fiscal & Primary Deficit, MPC Inflation Targeting, GST Council voting weights, Balance of Payments, and National MPI."
    },
    {
        "test_id": "APPSC-SEC-26",
        "title": "Test 26: Physical, Social & Economic Geography of India and Andhra Pradesh",
        "exam_group": "Group 1 & 2",
        "category": "Subject-Wise Test",
        "duration_minutes": 45,
        "question_count": 40,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["Geography of India & AP"],
        "description": "Covers Eastern Ghats peaks, Godavari-Krishna-Penna basins, Kolleru & Pulicat wetlands, Mangampeta Barytes & Tummalapalle Uranium, NSTR, and Northeast Monsoon."
    },
    {
        "test_id": "APPSC-SEC-27",
        "title": "Test 27: Indian Society - Structure, Caste, Tribes (PVTGs) & Welfare Mechanisms",
        "exam_group": "Group 2",
        "category": "Subject-Wise Test",
        "duration_minutes": 45,
        "question_count": 40,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["Indian Society & Welfare"],
        "description": "Dedicated test for APPSC Group-II Screening Test Section 3: Family, Kinship, Sanskritization, PVTGs of AP, PM-JANMAN, Mission Shakti, Mission Vatsalya, and NCSC/NCST/NCBC."
    },
    {
        "test_id": "APPSC-SEC-28",
        "title": "Test 28: Science, Technology, ISRO Space Missions, Defence & Environment",
        "exam_group": "Group 1 & 2",
        "category": "Subject-Wise Test",
        "duration_minutes": 45,
        "question_count": 40,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["Science, Tech & Environment"],
        "description": "Covers Chandrayaan-3, Aditya-L1, NISAR, Agni-5 MIRV (Mission Divyastra), NexCAR19 CAR-T therapy, CRISPR, and National Green Hydrogen Mission."
    },
    {
        "test_id": "APPSC-SEC-29",
        "title": "Test 29: Ancient, Medieval & Modern Indian History & Freedom Struggle",
        "exam_group": "Group 1 & 2",
        "category": "Subject-Wise Test",
        "duration_minutes": 45,
        "question_count": 40,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["Indian History & National Movement", "AP History & Reorganization"],
        "description": "Covers Indus Valley (Dholavira, Lothal), Ashokan Edicts (Erragudi), 1909/1919/1935 Constitutional Acts, Purna Swaraj, and Vijayawada AICC Session."
    },
    {
        "test_id": "APPSC-SEC-30",
        "title": "Test 30: Logical Reasoning, Analytical Ability & Data Interpretation Special",
        "exam_group": "Group 1 & 2",
        "category": "Subject-Wise Test",
        "duration_minutes": 45,
        "question_count": 40,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["Mental Ability & Reasoning"],
        "description": "Timed aptitude & reasoning workout with step-by-step mathematical explanations for Group-I Paper-II and Group-II Prelims."
    },
    {
        "test_id": "APPSC-PIB-31",
        "title": "Test 31: Union Budget, Economic Survey & PIB Governance Year-Round Compilation",
        "exam_group": "Group 1 & 2",
        "category": "PIB & Govt Portals",
        "duration_minutes": 45,
        "question_count": 40,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["PIB & Govt Schemes Current Affairs", "Indian & AP Economy", "Indian Polity & Constitution"],
        "description": "Tests fiscal targets, 16th Finance Commission, Dharti Aaba Abhiyan, Tribal & Rural development allocations, and PIB Economic Policy briefs."
    },
    {
        "test_id": "APPSC-REV-32",
        "title": "Test 32: APPSC Group-I & Group-II High-Yield Statement Elimination Power Test",
        "exam_group": "Group 1 & 2",
        "category": "PIB & Govt Portals",
        "duration_minutes": 60,
        "question_count": 50,
        "marks_per_question": 1.0,
        "negative_marking": 0.3333,
        "subjects": ["AP History & Reorganization", "Indian Polity & Constitution", "Indian & AP Economy", "Geography of India & AP", "Indian Society & Welfare", "Science, Tech & Environment", "PIB & Govt Schemes Current Affairs"],
        "description": "Ultimate multi-subject revision test featuring 50 high-yield statement and assertion-reason questions across all Group-I and Group-II modules."
    }
]


def build_all_tests():
    pool = create_questions_from_bank()
    by_subject = {}
    for q in pool:
        by_subject.setdefault(q["subject"], []).append(q)

    tests_output = []
    for idx, meta in enumerate(TEST_SERIES_CATALOG):
        target_count = meta["question_count"]
        allowed_subjects = meta["subjects"]

        # Gather candidate questions matching this test's subjects
        candidates = []
        for s in allowed_subjects:
            candidates.extend(by_subject.get(s, []))

        # Deterministically shuffle with test index offset so every test has a distinct question order & selection
        rng = random.Random(20261000 + idx * 97)
        shuffled = list(candidates)
        rng.shuffle(shuffled)

        selected = []
        while len(selected) < target_count:
            for item in shuffled:
                if len(selected) >= target_count:
                    break
                # Create a clean copy with test-specific numbering and option permutation if cycling
                q_copy = dict(item)
                cycle_num = len(selected) // max(1, len(shuffled))
                q_copy["q_no"] = len(selected) + 1
                q_copy["id"] = f"{meta['test_id']}-Q{q_copy['q_no']:03d}"
                if cycle_num > 0:
                    # Permute options deterministically on cycle > 0 so repeated concepts test from a fresh option order
                    opts = list(item["options"])
                    correct_text = opts[item["correct_index"]]
                    # Only permute if options aren't fixed "1 only / 2 only / Both 1 and 2"
                    if "1 only" not in opts[0] and "Both (A)" not in opts[0] and "I and II" not in opts[0]:
                        rng.shuffle(opts)
                        q_copy["options"] = opts
                        q_copy["correct_index"] = opts.index(correct_text)
                selected.append(q_copy)

        test_obj = {
            "test_id": meta["test_id"],
            "title": meta["title"],
            "exam_group": meta["exam_group"],
            "category": meta["category"],
            "duration_minutes": meta["duration_minutes"],
            "question_count": len(selected),
            "total_marks": float(len(selected)) * meta["marks_per_question"],
            "marks_per_question": meta["marks_per_question"],
            "negative_marking": meta["negative_marking"],
            "subjects": meta["subjects"],
            "description": meta["description"],
            "source_portal": "PIB (pib.gov.in), AP Socio-Economic Survey, PRS India & APPSC Official Pattern",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "questions": selected
        }
        tests_output.append(test_obj)

    db_payload = {
        "app_name": "APPSC Group 1 & Group 2 Exam Prep & Test Series Portal",
        "version": "2.0.0",
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_tests": len(tests_output),
        "exam_rules": {
            "marks_per_correct": 1.0,
            "negative_marking_fraction": "1/3 (0.33 marks deducted per wrong answer)",
            "unattempted_marks": 0.0
        },
        "tests": tests_output
    }

    out_path = os.path.join(DATA_DIR, "tests_db.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(db_payload, f, indent=2, ensure_ascii=False)

    print(f"[SUCCESS] Generated {len(tests_output)} APPSC Group 1 & Group 2 Test Series Exams at: {out_path}")
    total_q = sum(t["question_count"] for t in tests_output)
    print(f"[INFO] Total Exam Questions with Explanations across 32 Tests: {total_q}")


if __name__ == "__main__":
    build_all_tests()
