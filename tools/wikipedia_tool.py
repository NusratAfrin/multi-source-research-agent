import requests


def search(query: str) -> dict:
    try:
        resp = requests.get(
            "https://en.wikipedia.org/api/rest_v1/page/summary/" + query.replace(" ", "_"),
            timeout=6,
        )
        if resp.status_code == 200:
            data = resp.json()
            return {
                "title": data.get("title", query),
                "url": data.get("content_urls", {}).get("desktop", {}).get("page", ""),
                "snippet": data.get("extract", "")[:600],
                "source_type": "wikipedia",
            }
    except Exception:
        pass
    return {"title": query, "url": "", "snippet": "No result found.", "source_type": "wikipedia"}
