"""
generate_data.py

Generates an ILLUSTRATIVE, SYNTHETIC dataset for a generic aviation safety
risk-trend dashboard portfolio project.

IMPORTANT: This dataset does NOT represent, reference, or estimate any real
aircraft, airline, flight, incident, or fatality. It contains no dates,
locations, aircraft identifiers, or casualty figures tied to any real event.
It exists only to demonstrate a risk-category trend analysis and reporting
methodology (the kind used in aviation safety management systems), using
made-up category labels and counts.

Run: python generate_data.py
Output: data.json
"""

import json
import numpy as np

rng = np.random.default_rng(seed=7)

RISK_CATEGORIES = [
    "Mechanical / Systems",
    "Human Factors",
    "Weather / Environmental",
    "Maintenance Procedure",
    "Air Traffic Coordination",
    "Documentation / Compliance",
]

QUARTERS = [f"Q{q} Yr{y}" for y in range(1, 4) for q in range(1, 5)]

# ---- Reported safety events by category, per quarter (counts, illustrative) ----
category_trend = {}
for cat in RISK_CATEGORIES:
    base = rng.integers(8, 30)
    drift = rng.uniform(-0.03, 0.02)  # slow illustrative trend
    series = []
    for i in range(len(QUARTERS)):
        val = max(0, int(base * (1 + drift * i) + rng.normal(0, 2.5)))
        series.append(val)
    category_trend[cat] = series

# ---- Severity tier distribution (illustrative, no real fatality data) ----
severity_tiers = {
    "Tier 1 — Reportable, no operational impact": int(rng.integers(140, 210)),
    "Tier 2 — Minor operational impact": int(rng.integers(60, 100)),
    "Tier 3 — Significant, corrective action required": int(rng.integers(15, 35)),
}

# ---- Corrective action status (illustrative) ----
status_breakdown = {
    "Closed": int(rng.integers(180, 240)),
    "In Review": int(rng.integers(20, 45)),
    "Open": int(rng.integers(8, 20)),
}

# ---- Root cause tags (illustrative) ----
root_causes = [
    {"cause": "Procedural deviation", "count": int(rng.integers(30, 70))},
    {"cause": "Component wear/fatigue", "count": int(rng.integers(25, 60))},
    {"cause": "Communication gap", "count": int(rng.integers(15, 40))},
    {"cause": "Training gap", "count": int(rng.integers(10, 35))},
    {"cause": "Documentation error", "count": int(rng.integers(10, 30))},
]
root_causes = sorted(root_causes, key=lambda x: x["count"], reverse=True)

summary = {
    "total_events_logged": sum(severity_tiers.values()),
    "pct_closed": round(100 * status_breakdown["Closed"] / sum(status_breakdown.values()), 1),
    "avg_quarterly_events": round(
        sum(sum(v) for v in category_trend.values()) / len(QUARTERS), 1
    ),
}

output = {
    "meta": {
        "note": (
            "ILLUSTRATIVE SYNTHETIC DATA ONLY. Does not represent any real "
            "aircraft, airline, incident, or fatality. Category labels and "
            "counts are randomly generated to demonstrate a risk-trend "
            "reporting methodology, not to report on any real event."
        ),
    },
    "summary": summary,
    "quarters": QUARTERS,
    "category_trend": category_trend,
    "severity_tiers": severity_tiers,
    "status_breakdown": status_breakdown,
    "root_causes": root_causes,
}

with open("data.json", "w") as f:
    json.dump(output, f, indent=2)

print("Wrote data.json (illustrative synthetic data)")
