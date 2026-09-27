"""
generate_data.py

Uses the REAL National Transportation Safety Board (NTSB) civil aviation
accident/incident database (public domain, 1948-2023; ~90,000 records)
to analyze safety trends for Boeing aircraft.

Source: NTSB Aviation Accident Database & Synopses (public dataset,
downloaded from a public GitHub mirror of the Kaggle-hosted CSV:
https://github.com/pyamin1878/Airline_DS_Project).

IMPORTANT — what this is and isn't:
- This covers ALL Boeing aircraft models in the NTSB database (not just the
  737), across all eras (1948-2023), and includes everything from minor
  incidents to fatal accidents as separately classified by the NTSB.
- All figures shown are AGGREGATE counts and rates (by decade, phase of
  flight, weather, engine configuration) -- not individual crash narratives,
  names, or identifying details of any specific event.
- This is a real, publicly available dataset used widely in data-analysis
  coursework and portfolios; it is not a claim of specialized aviation-safety
  domain expertise beyond what the aggregate analysis itself demonstrates.

Run: python generate_data.py
Requires: Aviation_Data_raw.csv (in the same folder)
Output: data.json
"""

import json
import numpy as np
import pandas as pd

df = pd.read_csv("Aviation_Data_raw.csv", low_memory=False)
df["Make"] = df["Make"].astype(str).str.strip().str.upper()

boeing = df[df["Make"] == "BOEING"].copy()
boeing["Event.Date"] = pd.to_datetime(boeing["Event.Date"], errors="coerce")
boeing["Decade"] = (boeing["Event.Date"].dt.year // 10 * 10).astype("Int64")

for col in ["Total.Fatal.Injuries", "Total.Serious.Injuries", "Total.Minor.Injuries", "Total.Uninjured"]:
    boeing[col] = pd.to_numeric(boeing[col], errors="coerce").fillna(0)

# ---- Records by decade ----
by_decade = (
    boeing.dropna(subset=["Decade"])
    .groupby("Decade")
    .size()
    .reset_index(name="count")
    .sort_values("Decade")
)
decade_trend = [{"decade": f"{int(r['Decade'])}s", "count": int(r["count"])} for _, r in by_decade.iterrows()]

# ---- Injury severity breakdown ----
sev = boeing["Injury.Severity"].fillna("").astype(str).str.strip()
sev_clean = sev.apply(lambda s: "Fatal" if s.startswith("Fatal") else ("Non-Fatal" if s == "Non-Fatal" else ("Incident" if s == "Incident" else "Unknown/Other")))
severity_counts = sev_clean.value_counts().to_dict()

# ---- Broad phase of flight ----
phase_counts = (
    boeing["Broad.phase.of.flight"].astype(str).str.strip().replace({"nan": "Unknown"})
    .value_counts().head(8).to_dict()
)

# ---- Weather condition ----
weather_counts = (
    boeing["Weather.Condition"].astype(str).str.strip().replace({"nan": "Unknown", "UNK": "Unknown"})
    .value_counts().head(6).to_dict()
)

# ---- Aircraft damage ----
damage_counts = (
    boeing["Aircraft.damage"].astype(str).str.strip().replace({"nan": "Unknown"})
    .value_counts().to_dict()
)

# ---- Engine type ----
engine_counts = (
    boeing["Engine.Type"].astype(str).str.strip().replace({"nan": "Unknown"})
    .value_counts().head(6).to_dict()
)

summary = {
    "total_boeing_records": int(len(boeing)),
    "date_range": f"{int(boeing['Event.Date'].dt.year.min())}\u2013{int(boeing['Event.Date'].dt.year.max())}",
    "total_fatal_events": int((sev_clean == "Fatal").sum()),
    "pct_fatal": round(100 * (sev_clean == "Fatal").sum() / len(boeing), 1),
    "total_fatalities_recorded": int(boeing["Total.Fatal.Injuries"].sum()),
}

output = {
    "meta": {
        "source": "NTSB Aviation Accident Database & Synopses (public dataset, 1948\u20132023)",
        "note": (
            "Real NTSB records for all Boeing aircraft models in the database, aggregated "
            "by decade, phase of flight, weather, damage, and engine type. No individual "
            "event narratives, names, or identifying details are shown \u2014 aggregate "
            "counts only."
        ),
    },
    "summary": summary,
    "decade_trend": decade_trend,
    "severity_counts": severity_counts,
    "phase_counts": phase_counts,
    "weather_counts": weather_counts,
    "damage_counts": damage_counts,
    "engine_counts": engine_counts,
}

with open("data.json", "w") as f:
    json.dump(output, f, indent=2)

print(f"Boeing records: {len(boeing)}  |  Fatal events: {summary['total_fatal_events']} ({summary['pct_fatal']}%)")
print("Wrote data.json")
