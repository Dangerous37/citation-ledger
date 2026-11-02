# Citation Ledger

Check evidence supplied with generated answers before accepting quotations. Reports distinguish an unknown source, a changed source revision, a missing quotation and an ambiguous match.

## Run locally

Use Python 3.12. The project uses the standard library. From the repository root:

```sh
python cli.py example.json
python -m unittest -v
```

The included example is synthetic. Pass a different UTF-8 JSON file to inspect your own input. The command prints JSON to stdout. Invalid input returns status 2 and an explanation on stderr. See [CONTRACT.md](CONTRACT.md) for input fields and interpretation.

## Operational limits

Exact quotation checks on trusted local inputs. A verified quotation establishes provenance; semantic support for a claim requires separate review.

## Resumen en español

Audita citas de texto generadas contra una versión concreta del corpus. Localiza pasajes verificables y señala evidencia ausente o ambigua.
