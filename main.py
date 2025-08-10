# main.py
import os, json
from config import CONFIG
from collectors.google_search import google_search  # your existing google collector
#from collectors.x_search import x_search
from processors.sentiment import sentiment_score
from processors.scorer import presence_sov, engagement_sov, avg_sentiment
from datetime import datetime

BRAND_KEYWORDS = ["Atomberg", "atomberg", "Atomberg Technologies", "Atomberg Fan"]
QUERY = '"smart fan" Atomberg'

OUT_DIR = "samples"
os.makedirs(OUT_DIR, exist_ok=True)

def gather(platforms, query, top_n):
    results_by_platform = {}
    if "google" in platforms:
        results_by_platform["google"] = google_search(query, top_n=top_n)
    if "x" in platforms:
        # search X for the brand+keyword and also the keyword alone for comparison
        results_by_platform["x"] = x_search(query, top_n=top_n, since_days=CONFIG.get("date_range_days", 90))
    return results_by_platform

def annotate(results_by_platform):
    for plat, items in results_by_platform.items():
        for it in items:
            text = (it.get("title","") or "") + " " + (it.get("snippet","") or "") + " " + (it.get("content","") or "")
            it["sentiment"] = sentiment_score(text)
    return results_by_platform

def analyze(results_by_platform, brand_keywords):
    summary = {"timestamp": datetime.utcnow().isoformat(), "by_platform": {}}
    all_results = []
    for plat, items in results_by_platform.items():
        p_sov = presence_sov(items, brand_keywords)
        e_sov = engagement_sov(items, brand_keywords)
        avg_all, avg_brand = avg_sentiment(items, brand_keywords)
        summary["by_platform"][plat] = {
            "n_results": len(items),
            "presence_sov": p_sov,
            "engagement_sov": e_sov,
            "avg_sentiment_all": avg_all,
            "avg_sentiment_brand": avg_brand
        }
        all_results.extend(items)
    # combined presence across all platforms
    combined_presence = presence_sov(all_results, brand_keywords)
    summary["combined_presence_sov"] = combined_presence
    return summary, all_results

if __name__ == "__main__":
    platforms = CONFIG.get("platforms", ["google", "x"])
    top_n = CONFIG.get("N", 20)
    print("Gathering:", platforms, "top_n=", top_n)
    results_by_platform = gather(platforms, QUERY, top_n)
    results_by_platform = annotate(results_by_platform)
    summary, all_results = analyze(results_by_platform, BRAND_KEYWORDS)

    # save outputs
    with open(os.path.join(OUT_DIR, "results_all.json"), "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    with open(os.path.join(OUT_DIR, "summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print("Summary:")
    print(json.dumps(summary, indent=2))
    print("Saved files in", OUT_DIR)
