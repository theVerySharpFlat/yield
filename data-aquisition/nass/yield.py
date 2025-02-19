import urllib3
import os

KEY = os.environ.get("NASS_KEY")
MIN_YEAR = 2012
MAX_YEAR = 2025

STATES = ["IA", "IL", "MO", "KY", "SD", "ND", "IN"]

for state in STATES:
    resp = urllib3.request(
        "GET",
        f"https://quickstats.nass.usda.gov/api/api_GET/?key={KEY}&commodity_desc=CORN&year__GE={MIN_YEAR}&year__LE={MAX_YEAR}&statisticcat_desc=YIELD&unit_desc=BU / ACRE&state_alpha={state}&agg_level_desc=COUNTY&format=CSV",
    )

    with open(f"{state}_{MIN_YEAR}-{MAX_YEAR}_yield.csv", "w", encoding="utf-8") as f:
        f.write(str(resp.data, "utf-8"))

# resp = urllib3.request(
#     "GET",
#     f"https://quickstats.nass.usda.gov/api/get_param_values/?key={KEY}&param=location_desc",
# )
