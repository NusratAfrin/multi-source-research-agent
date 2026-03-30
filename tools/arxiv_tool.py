import requests
import xml.etree.ElementTree as ET


def search(query: str, max_results: int = 2) -> list[dict]:
    try:
        resp = requests.get(
            "http://export.arxiv.org/api/query",
            params={"search_query": f"all:{query}", "max_results": max_results},
            timeout=8,
        )
        root = ET.fromstring(resp.text)
        ns = "{http://www.w3.org/2005/Atom}"
        results = []
        for entry in root.findall(f"{ns}entry"):
            title = entry.find(f"{ns}title").text.strip().replace("\n", " ")
            url = entry.find(f"{ns}id").text.strip()
            summary = entry.find(f"{ns}summary").text.strip()[:400]
            results.append({"title": title, "url": url, "snippet": summary, "source_type": "arxiv"})
        return results
    except Exception:
        return []
