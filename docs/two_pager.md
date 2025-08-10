# Smart Fan — Share of Voice (SoV) — Two-pager

## Page 1 — Tech stack & Setup 
**Objective:** Compute Share of Voice (SoV) for brand *Atomberg* for the query "smart fan" across online sources.

**Tech stack**
- Python 3.11+ (Codespaces)
- Data collection: Google Custom Search API (used here)
- Sentiment: `vaderSentiment`
- Dev: GitHub Codespaces
- Output: JSON & CSV files in `samples/`

**How to reproduce**
1. Open repo in Codespaces.
2. Create `.env` (copy `.env.example`) and filling in:
3. In the terminal, install dependencies:
```bash
pip install -r requirements.txt
4. Run the SoV analysis: python main.py
5. Output files generated:

samples/results_all.json — all collected results with sentiment

samples/results_all.csv — CSV export for easy review

samples/summary.json — summary with SoV and sentiment scores

Page 2 — Findings, insights & recommendations
Analysis date (UTC): 2025-08-10T09:27:11.895293

Platforms analyzed: Google (Top 50 results)

Key metrics

n_results: 50

Presence SoV (Google): 0.94 (94% of results mention Atomberg)

Combined Presence SoV: 0.94

Average Sentiment (all results): 0.8634

Average Sentiment (brand mentions): 0.8613

Engagement SoV: Not available for Google search results

Interpretation & Insights

Atomberg appears in the vast majority of results for the query "smart fan Atomberg", showing strong brand coverage for brand-specific searches.

Sentiment is strongly positive both for all results and for brand mentions (~0.86), suggesting favorable public perception.

Lack of engagement metrics from Google means social media sources are required for engagement-weighted SoV.

Recommendations

Expand to Generic Keywords — For "smart fan" without brand name, monitor SoV to track market share against competitors.

Add More Platforms — Include X/Twitter and YouTube to capture engagement data.

SEO Optimization — Maintain high visibility for both brand-specific and generic queries through targeted content and backlinks.

Continuous Monitoring — Run this analysis regularly (e.g., weekly) and investigate any drop in SoV or sentiment.

Example Snippets
Positive:

“Atomberg’s smart fans are energy-efficient and stylish, making them a top choice for modern homes.”

“The Atomberg Renesa is one of the best smart fans available in the market today.”

Neutral:

“List of smart fans including brands like Atomberg, Orient, and Crompton.”

yaml
Copy
Edit

---

### How to add this file
In Codespaces:
1. Right-click your repo root → **New Folder** → name it `docs`.
2. Right-click `docs` → **New File** → name it `two_pager.md`.
3. Paste the above content.
4. Save (`Ctrl+S`).
5. Commit:
   ```bash
   git add docs/two_pager.md
   git commit -m "Add two_pager.md report"
   git push origin main
If you want, I can also auto-generate docs/examples.md from your current JSON results so you have richer examples for the “Example Snippets” section. That’ll make your submission more impressive.
Do you want me to do that?







You said:
should i paste everything what you gave in the markdown


ChatGPT said:
Yes — paste everything I gave inside the triple backticks markdown … into your new file docs/two_pager.md.

That means in the file, it should start with:

bash
Copy
Edit
# Smart Fan — Share of Voice (SoV) — Two-pager
…and end with:

yaml
Copy
Edit
---