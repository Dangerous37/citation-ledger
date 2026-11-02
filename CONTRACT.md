# Evidence contract
Input has sources mapping stable source IDs to Unicode text and citations containing source, quote and optional lowercase sha256 of UTF-8 source bytes. Verify verbatim quotations. Emit zero-based Unicode code-point offsets, end exclusive. Optional start disambiguates repeated passages. Return a status per citation, preserving input order.
