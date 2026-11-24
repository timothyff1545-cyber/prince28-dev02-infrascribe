# Capacity plan: InfraScribe

Full corpus target: All resource and data-source pages + upgrade guides + CHANGELOG (3,000+ files)

<!-- generated:start -->
## Measured on my start corpus (2026-11-24 22:19 UTC)

| What | Value |
|---|---|
| Files | 707 |
| Size on disk | 7.2 MB |
| Pages (PDF pages + 1 per 3,000 characters of text/HTML) | 774 |
| Characters of text | 2,321,928 |
| Estimated tokens (characters / 4) | 580,482 |
| Tokens per page | 750 |
| PDFs with almost no text (scanned? OCR is Day 7) | 0 |
| Files not measured (zip, xlsx, unreadable) | 0 |

## Estimate for the full corpus (target: 3,000 files)

| What | How | Value |
|---|---|---|
| Scale factor | target / measured | x 4.2 |
| Tokens | measured tokens x scale | 2.46 M |
| Raw files | measured MB x scale | 31 MB |
| Chunks | tokens / 400 x 1.15 overlap | 7,082 |
| Embedding cost, one time | tokens x 1.15 x $0.15 per 1M | $0.42 = Rs 40 |
| Vector storage | chunks x 768 numbers x 4 bytes | 22 MB |
| Text in Postgres | characters x scale x 1.2 | 12 MB |

Assumptions: 4 characters per token, 400-token chunks, 768-dimension embeddings at $0.15 per 1M tokens, Rs 95 per US dollar.
<!-- generated:end -->

## What I conclude

1. **Is embedding cost a problem for this product?**

   No. The estimated one-time embedding cost for the 3,000-file corpus is only about $0.42 (₹40), so it is affordable.

2. **Do the vectors and text fit in my free Postgres?**

   The estimated storage requirement is approximately 34 MB (22 MB for vectors + 12 MB for text). I need to compare this with the available storage limit in my PostgreSQL dashboard.

3. **Which number above am I least sure about, and how will I measure it better?**

   The estimated token count is uncertain because it uses characters divided by 4. I can measure actual tokens using the tokenizer of my chosen embedding model.

4. **What changes if the corpus grows 10 times?**

   The estimated token count increases to 24.6 million, with approximately 70,820 chunks.
   The one-time embedding cost increases to about $4.20 (₹400), and vector storage increases to approximately 220 MB. Text storage would be approximately 120 MB.
