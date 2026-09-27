# Aviation Safety Risk-Trend Dashboard (Illustrative)

A risk-category trend and corrective-action tracking dashboard demonstrating
a safety management system (SMS)-style reporting methodology.

## ⚠️ About the data — read this before sharing this project anywhere

**This project uses entirely illustrative, synthetic data.** It does **not**
represent, reference, or estimate any real aircraft, airline, flight,
incident, or fatality. There are no real dates, locations, aircraft
identifiers, or casualty figures anywhere in this repository — only made-up
category labels and randomly generated counts, built to demonstrate a
reporting and root-cause-tracking methodology.

This is a deliberate choice: real aviation safety incidents involve real
people and real consequences, and it would be inappropriate to fabricate
statistics that could be mistaken for actual incident data. If you want to
extend this project with real analysis, the appropriate path is to pull
anonymized, aggregate statistics from a public source like the NTSB or ASN
aviation safety databases — not to generate placeholder numbers that look
like real incident counts.

**When you talk about this project (resume, interview, README) say plainly
that it uses illustrative synthetic data for demonstrating methodology** —
not "aviation safety analysis" phrased in a way that implies real incident
data was analyzed.

## Tech stack

- **Python (numpy)** — synthetic data generation (`generate_data.py`)
- **JavaScript + Chart.js** — trend line, doughnut, and bar visualizations
- **HTML/CSS** — static, no framework

## Structure

```
.
├── generate_data.py   # generates data.json (illustrative data only)
├── data.json
├── index.html
└── README.md
```

## Running locally

```bash
python generate_data.py
python -m http.server 8000
# open http://localhost:8000
```

## Live demo

Enable GitHub Pages (Settings → Pages → deploy from `main`, root):
`https://<your-username>.github.io/aviation-safety-dashboard/`
