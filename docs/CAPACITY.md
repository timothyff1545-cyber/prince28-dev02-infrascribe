# Capacity plan: InfraScribe

Full corpus target: All resource and data-source pages + upgrade guides + CHANGELOG (3,000+ files)

<!-- generated:start -->
## Measured on my start corpus (2026-11-24 09:53 UTC)

| What | Value |
|---|---|
| Files | 1,775 |
| Size on disk | 15.5 MB |
| Pages (PDF pages + 1 per 3,000 characters of text/HTML) | 3,491 |
| Characters of text | 10,473,570 |
| Estimated tokens (characters / 4) | 2,618,392 |
| Tokens per page | 750 |
| PDFs with almost no text (scanned? OCR is Day 7) | 0 |
| Files not measured (zip, xlsx, unreadable) | 0 |

## Estimate for the full corpus (target: 3,000 files)

| What | How | Value |
|---|---|---|
| Scale factor | target / measured | x 1.7 |
| Tokens | measured tokens x scale | 4.43 M |
| Raw files | measured MB x scale | 26 MB |
| Chunks | tokens / 400 x 1.15 overlap | 12,723 |
| Embedding cost, one time | tokens x 1.15 x $0.15 per 1M | $0.76 = Rs 73 |
| Vector storage | chunks x 768 numbers x 4 bytes | 39 MB |
| Text in Postgres | characters x scale x 1.2 | 21 MB |

Assumptions: 4 characters per token, 400-token chunks, 768-dimension embeddings at $0.15 per 1M tokens, Rs 95 per US dollar.
<!-- generated:end -->

## What I conclude

1. Is embedding cost a problem for this product? (1 line, with the number)
2. Do the vectors and text fit in my free Postgres? (1 line: compare with the storage limit on my database dashboard)
3. Which number above am I least sure about, and how will I measure it better? (1 line)
4. What changes if the corpus grows 10 times? (2 lines)
