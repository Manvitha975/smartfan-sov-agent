from googleapiclient.discovery import build
from config import CONFIG

def google_search(query, top_n=20):
    api_key = CONFIG["google_api_key"]
    cse_id = CONFIG["google_cse_id"]
    service = build("customsearch", "v1", developerKey=api_key)
    results = []
    start = 1
    while len(results) < top_n:
        res = service.cse().list(
            q=query, cx=cse_id, start=start, num=min(10, top_n-len(results))
        ).execute()
        items = res.get("items", [])
        for it in items:
            results.append({
                "source": "google",
                "url": it.get("link"),
                "title": it.get("title"),
                "snippet": it.get("snippet"),
                "rank": start
            })
        start += len(items)
        if not items:
            break
    return results
