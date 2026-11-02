import hashlib


def inspect(citation, sources):
    key, quote = citation["source"], citation["quote"]
    if not isinstance(key, str) or not isinstance(quote, str) or not quote.strip():
        raise ValueError("supply source ID and nonblank quotation")
    if key not in sources:
        return {"status": "unknown_source"}
    text = sources[key]
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    if "sha256" in citation and citation["sha256"] != digest:
        return {"status": "stale_revision", "sha256": digest}
    if "start" in citation:
        start = citation["start"]
        if type(start) is not int or start < 0:
            raise ValueError("invalid start offset")
        if not text.startswith(quote, start):
            return {"status": "offset_mismatch"}
    else:
        start = text.find(quote)
        if start < 0:
            return {"status": "quote_missing"}
        if text.find(quote, start + 1) >= 0:
            return {"status": "ambiguous"}
    return {"status": "verified", "start": start, "end": start + len(quote), "sha256": digest}


def evaluate(data):
    sources = data["sources"]
    if not isinstance(sources, dict) or not all(isinstance(s, str) for s in sources.values()):
        raise ValueError("sources must map IDs to text")
    report = [dict(source=item["source"], **inspect(item, sources)) for item in data["citations"]]
    return {"review_required": any(row["status"] != "verified" for row in report), "citations": report}
