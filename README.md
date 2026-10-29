# 🏛️ APPSC Group-I & Group-II Official CBT Test Series Website

**Live Website URL (once GitHub Pages is enabled):**
👉 **[https://chandu1123.github.io/APPSC-TEST-SERIES/](https://chandu1123.github.io/APPSC-TEST-SERIES/)**

An authentic **Computer Based Test (CBT) Web Portal** designed specifically for **Andhra Pradesh Public Service Commission (APPSC) Group-I and Group-II** aspirants. Hosted directly on **GitHub Pages** (no `.exe` installation required—works on Desktop, Laptop, Tablet, and Mobile browsers!).

---

## ✨ Key Features

1. **33+ Full-Length & Sectional Mock Exams (`1,830+` Questions Ready Instantly)**:
   - **10 Group-I Prelims Full Mock Tests** (Paper-I General Studies & Paper-II General Aptitude — **120 Questions, 120 Minutes**).
   - **12 Group-II Prelims Screening Mock Tests** (AP History, Indian Polity, Economy, Geography & Mental Ability — **150 Questions, 150 Minutes**).
   - **8 Group-II Mains Paper-I & Paper-II Full Tests** (Social & Cultural History of AP, Indian Constitution, AP & Indian Economy, Science & Technology — **150 Questions, 150 Minutes**).
   - **2 Exclusive PIB & AP Government Schemes Special Tests**.
   - **Live Dynamic PIB Current Affairs Exams** generated on-demand directly in your browser or via Python script.

2. **Real-Time PIB (`pib.gov.in`) & Government Portal Exam Generator**:
   - Click **"Fetch Live PIB & Create Test"** right on the website header to pull the latest Press Information Bureau (PIB) releases and immediately generate a fresh **30-Question Timed Current Affairs Mock Exam**.
   - Includes a **GitHub Actions workflow** (`.github/workflows/deploy-pages.yml`) that automatically scrapes PIB every morning and deploys updated exams to GitHub Pages.

3. **Exact Official APPSC Exam Hall Interface**:
   - Strict countdown timer (`120 mins` for Group-I, `150 mins` for Group-II) with auto-submit when time expires.
   - Official **`-1/3` (`-0.33`) negative marking** calculation.
   - TCS iON-style Question Palette: *Answered*, *Not Answered*, *Marked for Review*, *Answered & Marked*, and *Not Visited*.

4. **Comprehensive Post-Exam Analytics & Printable Explanations**:
   - Instant scorecard with **Net Score**, **Accuracy %**, **Cutoff Qualification Status**, and **Subject-wise Breakdown**.
   - Detailed **Step-by-Step Solutions & Official Source References** (`PIB`, `AP Socio-Economic Survey`, `Laxmikanth`, `AP Reorganisation Act 2014`) with filter tabs (*All*, *Incorrect Only*, *Unattempted*, *Correct*) and PDF/Print export.

---

## 🚀 How to Publish & Enable Your Website on GitHub Pages

1. Double-click **`PUSH_TO_GITHUB.bat`** (or push via GitHub Desktop / Git CLI) to upload this repository to `https://github.com/Chandu1123/APPSC-TEST-SERIES`.
2. Open your repository on GitHub: **[https://github.com/Chandu1123/APPSC-TEST-SERIES/settings/pages](https://github.com/Chandu1123/APPSC-TEST-SERIES/settings/pages)**
3. Under **Build and deployment** -> **Source**, select:
   - **Deploy from a branch** -> Branch: **`main`** -> Folder: **`/ (root)`** -> Click **Save** *(or select **GitHub Actions** to also enable automatic daily PIB scraping)*.
4. In ~60 seconds, your website will be live at:
   👉 **`https://chandu1123.github.io/APPSC-TEST-SERIES/`**

*(You can also open `index.html` directly on your computer anytime—it works 100% offline too!)*

---

## 📂 Project Structure

```text
APPSC-TEST-SERIES/
├── index.html                          # Main CBT Exam Portal Website (GitHub Pages Root)
├── manifest.json                       # Progressive Web App (PWA) Manifest (Installable on Mobile/Desktop)
├── sw.js                               # Offline Service Worker
├── data/
│   ├── tests_db.js                     # Pre-compiled 33+ Test Series bundle (1,830+ MCQs with explanations)
│   └── tests_db.json                   # Raw JSON Question Bank
├── scripts/
│   ├── generate_test_series.py         # Generates the 32 baseline APPSC Group 1 & 2 exams
│   ├── pib_scraper.py                  # Live PIB (pib.gov.in) RSS scraper & MCQ generator
│   └── build_site.py                   # Rebuilds data/tests_db.js and cleans the project
└── .github/workflows/
    └── deploy-pages.yml                # Automated GitHub Pages Deployment + Daily PIB Scraper
```
