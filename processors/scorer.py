import math

def engagement_value(item):
    # Generic engagement formula:
    # likes + 2*replies + 3*retweets  (adjust weights as you like)
    likes = item.get("likes", 0) or 0
    replies = item.get("replies", 0) or 0
    retweets = item.get("retweets", 0) or item.get("shares", 0) or 0
    return likes + 2 * replies + 3 * retweets

def presence_sov(results, brand_keywords):
    total = len(results)
    if total == 0: return 0.0
    brand_mentions = 0
    for it in results:
        text = (it.get("title","") + " " + it.get("snippet","") + " " + it.get("content","")).lower()
        if any(k.lower() in text for k in brand_keywords):
            brand_mentions += 1
    return brand_mentions / total

def engagement_sov(results, brand_keywords):
    # Works only if engagement fields are present
    total_eng = 0.0
    brand_eng = 0.0
    for it in results:
        eng = engagement_value(it)
        total_eng += eng
        text = (it.get("title","") + " " + it.get("snippet","") + " " + it.get("content","")).lower()
        if any(k.lower() in text for k in brand_keywords):
            brand_eng += eng
    if total_eng == 0: 
        return None  # no engagement data
    return brand_eng / total_eng

def avg_sentiment(results, brand_keywords=None):
    # returns (avg_all, avg_brand) where avg_brand may be None if no brand results
    total_s = 0.0
    total_n = 0
    brand_s = 0.0
    brand_n = 0
    for it in results:
        s = it.get("sentiment", 0.0) or 0.0
        total_s += s
        total_n += 1
        if brand_keywords:
            text = (it.get("title","") + " " + it.get("snippet","") + " " + it.get("content","")).lower()
            if any(k.lower() in text for k in brand_keywords):
                brand_s += s
                brand_n += 1
    avg_all = (total_s / total_n) if total_n else None
    avg_brand = (brand_s / brand_n) if brand_n else None
    return avg_all, avg_brand
