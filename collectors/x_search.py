# collectors/x_search.py
from datetime import datetime, timezone, timedelta
import snscrape.modules.twitter as sntwitter

def x_search(query, top_n=100, since_days=90):
    """
    Returns list of dicts with fields:
    source, id, content, user, date (ISO), likes, retweets, replies, rank
    """
    cutoff = datetime.now(timezone.utc) - timedelta(days=since_days)
    out = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= top_n:
            break
        # skip older than cutoff
        if tweet.date < cutoff:
            continue
        out.append({
            "source": "x",
            "id": tweet.id,
            "content": tweet.content,
            "user": tweet.user.username,
            "date": tweet.date.isoformat(),
            "likes": getattr(tweet, "likeCount", 0) or 0,
            "retweets": getattr(tweet, "retweetCount", 0) or 0,
            "replies": getattr(tweet, "replyCount", 0) or 0,
            "rank": i + 1
        })
    return out
