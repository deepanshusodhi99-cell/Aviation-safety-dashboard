# Boeing Aircraft Safety Trends Dashboard

Aggregate safety-trend analysis of **real** National Transportation Safety
Board (NTSB) accident/incident records for Boeing aircraft.

## About the data

- **Source**: NTSB Aviation Accident Database & Synopses — a public-domain
  U.S. government dataset covering civil aviation accidents/incidents, 1948
  onward. Downloaded from a public GitHub mirror of the same CSV widely used
  in data-analysis coursework
  ([pyamin1878/Airline_DS_Project](https://github.com/pyamin1878/Airline_DS_Project),
  originally distributed via [Kaggle](https://www.kaggle.com/datasets/khsamaha/aviation-accident-database-synopses)).
- **Scope**: every record where `Make == BOEING` — 2,745 records spanning
  1982–2022. This is **all Boeing models** in the database, not only the
  737, and includes everything from minor incidents to fatal accidents as
  classified by the NTSB itself.
- **What's shown**: aggregate counts and rates only — by decade, injury
  severity classification, phase of flight, weather condition, aircraft
  damage, and engine type. No individual event narratives, aircraft
  registration numbers, or other identifying details are surfaced.
- **What this is not**: this is not investigative journalism or an
  incident-by-incident review of specific crashes, and it should not be
  described as such. It's a real, public, aggregate dataset analysis — the
  same kind of exercise commonly done in data-analytics coursework — used
  here to demonstrate data cleaning, aggregation, and visualization skills.

## Tech stack

- **Python (pandas)** — loading, cleaning, and aggregating the raw NTSB CSV
  (`generate_data.py`)
- **JavaScript + Chart.js** — bar and doughnut charts
- **HTML/CSS** — static, no framework

## Structure

```
.
├── Aviation_Data_raw.csv   # real NTSB dataset (full, all makes)
├── generate_data.py         # filters to Boeing, aggregates, writes data.json
├── data.json                 # aggregated output consumed by the dashboard
├── index.html
└── README.md
```

## Running locally

```bash
python generate_data.py     # re-aggregate from the raw CSV
python -m http.server 8000
# open http://localhost:8000
```

## Live demo

Enable GitHub Pages (Settings → Pages → deploy from `main`, root):
`https://<your-username>.github.io/aviation-safety-dashboard/`
