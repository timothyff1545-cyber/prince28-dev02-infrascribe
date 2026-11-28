# Engineering notes: InfraScribe

## D03 · PostgreSQL

### Migrations (upgrade, downgrade, upgrade)

```text
55404245c0e5 -> 35b3293dfd29 (head), add gin index on metadata
<base> -> 55404245c0e5, create documents and pages
```

### The loader is idempotent

```text
records=3 inserted=3 updated=0 unchanged=0
records=3 inserted=0 updated=0 unchanged=3
records=3 inserted=0 updated=1 unchanged=2
```

### EXPLAIN for ?resource_type=VALUE

```text
-- 1) What the planner chooses on its own:
Seq Scan on documents  (cost=0.00..11.00 rows=1 width=36) (actual time=0.773..0.775 rows=2.00 loops=1)
  Filter: (metadata @> '{"resource_type": "aws_s3_bucket"}'::jsonb)
  Rows Removed by Filter: 1
  Buffers: shared read=1 dirtied=1
Planning:
  Buffers: shared hit=143 read=8 dirtied=1
Planning Time: 6.294 ms
Execution Time: 0.803 ms

-- 2) Seq scan switched off, to prove the index can be used:
Bitmap Heap Scan on documents  (cost=12.81..16.82 rows=1 width=36) (actual time=1.618..1.619 rows=2.00 loops=1)
  Recheck Cond: (metadata @> '{"resource_type": "aws_s3_bucket"}'::jsonb)
  Heap Blocks: exact=1
  Buffers: shared hit=2 read=2
  ->  Bitmap Index Scan on ix_documents_metadata_gin  (cost=0.00..12.81 rows=1 width=0) (actual time=1.577..1.577 rows=2.00 loops=1)
        Index Cond: (metadata @> '{"resource_type": "aws_s3_bucket"}'::jsonb)
        Index Searches: 1
        Buffers: shared hit=1 read=2
Planning:
  Buffers: shared hit=1
Planning Time: 0.078 ms
Execution Time: 1.666 ms
```

Why did the planner choose a Seq Scan on my table? (2 lines, your own words)

The table contains very few records, so PostgreSQL estimates that scanning the entire table is cheaper than using the GIN index.
Using an index also has additional lookup overhead, which is unnecessary for such a small table.

When would it switch to the GIN index? (1 line)
When the table grows and the query becomes selective enough that using the GIN index is estimated to be cheaper than scanning the entire table.


## D05 · CI/CD and going live

- Live URL: (paste)
- CI run for pull request 1: https://github.com/timothyff1545-cyber/prince28-dev02-infrascribe/actions (paste the run link)
- First deploy that ran by itself: (paste the CD run link)
- Merge clicked at __:__ → "Smoke test passed" at __:__ → lead time: ___ min

### Smoke test output from that CD run

```text
paste the last 4 lines of the "Smoke test the live URL" step
```

### Rollback drill

- Rolled back to sha daefe525aad9276f85217c317bc3b4b2688de2e7: started 12:00, smoke passed 12:04 (4 min)
- Rolled forward to sha 1ea1f9f4e52e7b935fbc4f8d5311792a487d9a29: 5 min
- During the rollback, the database stayed on the newer schema. Why is that safe here? (2 lines)
The rollback only changes the application version; it does not reverse database migrations. The older application can continue working because the newer schema retains the fields and tables it needs.

### Where my secrets live

- Neon string: GitHub Secret DATABASE_URL + Render environment. Not in Git, not in the image.
- Render deploy hook: GitHub Secret RENDER_DEPLOY_HOOK only.

### Monitoring

- UptimeRobot checks /health every 5 minutes; alerts go to my email.
- One thing that would make my live app faster on its first request: (1 line)
 Keep the application warm using a scheduled health check to reduce cold-start delays.


## D06 · Collecting the corpus

- Start target: 200 most-used resource pages
- Collected today: **735 files, 774 measured pages, 7.2 MB measured size** (707 files were measurable by `dataset_report.py`; 28 files were not measured)
- Doors used: **URL list, Git repository**

### Licence check

| Source | Licence or terms, in my words | May I show full text in answers? |
|---|---|---|
| HashiCorp AWS Terraform provider GitHub repository | MPL-2.0 applies to covered repository files. Preserve licence and copyright notices and verify file coverage. | Only where permitted by the applicable licence; verify coverage before displaying full text. |
| Terraform Registry | Registry Terms restrict automated crawling and certain copying or storage of content. | No, not without checking the applicable terms and obtaining permission where required. |

### robots.txt

- Site: **Terraform Registry**. Its robots.txt says:
  ```
  User-agent: *
  Disallow:
  ```
- Was anything blocked for my bot? **The Registry robots.txt did not disallow paths under this rule. However, its Terms still restrict scraping, so robots.txt permission alone does not authorize automated collection.**

### Kill and resume

- Run 1: I pressed Ctrl+C after **[10]** files.
- Run 2: downloaded=**[10]** skipped=**[0]**
- Run 3: downloaded=**0** skipped=**[10]**

### Capacity (from docs/CAPACITY.md)

- Tokens per page, measured: **750**
- Full corpus: **2.46 M tokens, 7,082 chunks, embedding about Rs 40, vectors 22 MB**
- The number that surprised me most, and why:
  The estimated embedding cost was only around Rs 40 for 3,000 files.
  This is affordable for the initial version of InfraScribe, even as the documentation corpus grows.

### One thing that went wrong today, and how I fixed it

The dataset report measured only 707 files, while 735 files were physically present in `data/raw/`. I checked the source folders and file extensions to investigate the difference. The report did not measure 28 files, so I distinguished the physical file count from the measurable file count instead of treating them as the same.

## D07 · Parser comparison

<!-- parsers:start -->
| File | Parsers (A / B) | Pages | A found | B found | Time (A / B) | Better, why |
|---|---|---|---|---|---|---|
| lambda-function-html-a2c107d6.html | trafilatura / strip tags | 12 | 31,441 chars, 0 headings, 1 tables | 35,361 chars, 33 headings, 0 tables | 0.23 s / 0.01 s | |
| db-instance-html-063b52f5.html | trafilatura / strip tags | 7 | 35,812 chars, 0 headings, 1 tables | 38,624 chars, 10 headings, 0 tables | 0.16 s / 0.01 s | |
| instance-html-b589d836.html | trafilatura / strip tags | 12 | 34,909 chars, 0 headings, 1 tables | 37,385 chars, 1 headings, 0 tables | 0.14 s / 0.01 s | |
| s3-bucket-html-dc92e79b.html | trafilatura / strip tags | 10 | 29,524 chars, 0 headings, 1 tables | 32,137 chars, 1 headings, 0 tables | 0.11 s / 0.01 s | |
| dynamodb-table-html-8df4ac4b.html | trafilatura / strip tags | 9 | 21,233 chars, 0 headings, 1 tables | 24,195 chars, 3 headings, 0 tables | 0.15 s / 0.01 s | |
| security-group-html-d88c84fc.html | trafilatura / strip tags | 8 | 16,778 chars, 7 headings, 1 tables | 19,636 chars, 13 headings, 0 tables | 0.11 s / 0.01 s | |
| iam-role-html-c7a4fd86.html | trafilatura / strip tags | 5 | 10,220 chars, 0 headings, 1 tables | 13,162 chars, 3 headings, 0 tables | 0.09 s / 0.01 s | |
| subnet-html-c67f55b4.html | trafilatura / strip tags | 4 | 9,025 chars, 0 headings, 1 tables | 11,864 chars, 1 headings, 0 tables | 0.08 s / 0.01 s | |
| vpc-html-ab2ba283.html | trafilatura / strip tags | 3 | 7,390 chars, 0 headings, 1 tables | 10,072 chars, 1 headings, 0 tables | 0.07 s / 0.00 s | |
| ebs-volume-html-427fc811.html | trafilatura / strip tags | 2 | 3,636 chars, 0 headings, 1 tables | 6,322 chars, 0 headings, 0 tables | 0.06 s / 0.00 s | |
<!-- parsers:end -->

### D07 · Parsing my corpus

- Files in the raw corpus: **735 · measurable by dataset report: 707 · parsed: parsing summary not yet recorded · failed: parsing summary not yet recorded · pages in Postgres: not yet verified**
- Parsing coverage: **Not yet measured; requires the parsing summary.**

### Failures by reason

| Reason | Files | What I did |
|---|---:|---|
| no_text_layer | Not yet counted | Scanned PDFs require OCR |
| corrupt | Not yet counted | Record the failure for investigation or replacement |
| unsupported_type | Not yet counted | Identify unsupported formats and skip or convert them |
| empty | Not yet counted | Check whether the source file contains readable content |

- The one I fixed: file *models.py*, reason *Ruff formatting error*, fix: *ran `uv run ruff format .` and verified using `uv run poe lint`.*

### What I saw when I read my parsed pages

- A page where the heading path is right (document, page, path): **Fever Guidelines, page 2, [Fever Guidelines, Dengue] (verified by the parser unit test).**
- Something that came out wrong (document, page, what): **HTML extraction can include extra characters or unwanted content when using simple HTML tag stripping.**
- A table: Markdown grid or loose text? (document, page): **Markdown grid (verified by the PDF parser unit test).**

### My parser choice

- For PDFs I use *PyMuPDF* because it detects font sizes and can identify headings and tables. The unit tests also confirm that PyMuPDF and pypdf agree on the page count of a three-page test PDF.
- For HTML documents, I prefer *Trafilatura* over simple tag stripping because it extracts main article content and removes navigation, scripts and footer content. In my comparison, it detected tables in all 10 tested documents, while simple tag stripping detected none.
- A kind of document in my corpus that neither parser handles well: **Scanned PDFs without a text layer; they require OCR.**

### One thing that went wrong today, and how I fixed it

Ruff reported a formatting issue in `src/infrascribe/db/models.py` after adding the headings column and ParseFailure model. I fixed it using `uv run ruff format .` and confirmed that `uv run poe lint` passed.


# D08 · LLM gateway

- **Primary:** `gemini-3.8-flash` (Gemini)
- **Fallback:** `openai/gpt-oss-20b` (Groq)
- **Gateway:** `LLMGateway` handles retries, fallback, circuit breaking, token tracking, latency and cost recording.

### First questions on my laptop

| Test | Provider / model | Total time | Tokens in | Tokens out | Cost (Rs) | Fallback |
|---|---|---:|---:|---:|---:|---|
| Hello! How can I help you with Terraform for AWS today? | Groq / `openai/gpt-oss-20b` | 16.35 s | 226 | 59 | 0.003292 | Yes |
| Refund definition | Groq / `openai/gpt-oss-20b` | 28.79 s | 234 | 66 | 0.003548 | Yes |
| Off-topic question | Groq / `openai/gpt-oss-20b` | 13.98 s | 248 | 87 | 0.004246 | Yes |

- **First words after:** Not recorded in these outputs.
- **Same question on live URL:** Not recorded yet. Day 1 target: under 1.5 s.

### Tokens: English against Tamil

| Message | Tokens in |
|---|---:|
| "Hi" (baseline: mostly my system prompt) | ___ |
| The English sentence | ___ |
| The same sentence in Tamil | ___ |

- The Tamil message needs about ___ times the tokens of the English one.
- The three measurements above are different questions, so they cannot establish an English-versus-Tamil token ratio.

### What the model does without my documents

- **Question 6 ("How much is our AWS bill this month?"):** Not tested yet.
- **Exact words:** ___
- **A detail it got wrong or invented:** The refund question received a general definition of a refund, despite being outside the Terraform assistant's intended scope.
- **Off-topic question:** Yes, it declined in one sentence.

Exact response:

> I’m sorry, but that question is outside the scope of this Terraform assistant.

### Fallback and circuit breaker

- **With the primary broken:** Gemini → Groq.
- **Fallback model:** `openai/gpt-oss-20b`.
- **Observed:** All three supplied requests used Groq with `fallback=YES`.
- **First words after:** Not recorded.
- **The question at which "llm call gemini … error" stopped appearing in the log:** Number ___

### The bill

- **Three observed calls:** 3
- **Total observed cost:** Rs 0.011086
- **Average cost per answered question:** Rs 0.003695 (approximately)
- **Day 1 target:** Under Rs 0.50 per answered question.
- **Actual `/v1/usage` totals:** Calls ___, errors ___, fallbacks ___, cost Rs ___

### One thing that went wrong today, and how I fixed it

**Problem:** Four unit tests failed when running `uv run poe test`:
- Three chat API tests returned HTTP 503 instead of HTTP 200.
- The usage API test returned HTTP 500 because it attempted a real PostgreSQL connection.

**Root cause:** `tests/unit/conftest.py` contained its own `client` fixture. It took precedence over the parent fixture in `tests/conftest.py`, but did not override `get_gateway` and `get_usage_repo`.

**Fix:** Updated `tests/unit/conftest.py` to include:
- A `FakeLLM` fixture and `get_gateway` dependency override.
- A `FakeUsage` class and `get_usage_repo` dependency override.

**Additional lint and formatting fixes:**
- Fixed Ruff import ordering using `uv run ruff check tests/unit/conftest.py --fix`.
- Three files needed formatting: `config.py`, `models.py` and `tests/unit/conftest.py`.
- Formatting command: `uv run ruff format .`

**Verification:** Ruff lint passed (`All checks passed!`). Formatting verification was pending in the last shared output.

## D09 · Prompt versions compared

<!-- prompts:start -->

| Prompt version | Correct | Accuracy | Invalid replies | Avg tokens in |
|---|---|---|---|---|
| classify_v1 | 14/21 | 67% | 0 | 114 |
| classify_v2 | 20/21 | 95% | 0 | 265 |
| classify_v3 | 21/21 | 100% | 0 | 385 |
| classify_v4 | 21/21 | 100% | 0 | 558 |

<!-- prompts:end -->
# D09 · Prompts and structured output

## Router prompt evaluation

- **My best router prompt:** `classify_v3` and `classify_v4` — both achieved **21/21 (100%)**.
- **What I changed in v4, and what happened to the score:**
  I added more challenging examples covering multi-resource Terraform configurations, provider version changes, migration questions, live AWS infrastructure information, security configuration and prompt injection. V4 maintained the perfect 21/21 score achieved by V3. There was no measurable accuracy improvement, but V4 tested a wider range of question types.
- **The question my best version still gets wrong (line, wanted, got), and why I think so:**
  None. Both V3 and V4 classified all 21 evaluation questions correctly.
- **A label in my test set that I changed after seeing the results:** None recorded.
- **Input tokens per question:** V1 — not recorded; best version — not recorded. The extra accuracy cannot be calculated from token measurements. V4 maintained the same accuracy as V3 while testing more varied examples.

### Router evaluation results

| Prompt version | Correct | Accuracy |
|---|---:|---:|
| classify_v1 | 14/21 | 67% |
| classify_v2 | 20/21 | 95% |
| classify_v3 | 21/21 | 100% |
| classify_v4 | 21/21 | 100% |

**Classification errors observed:**

- V1 incorrectly classified the IAM permissions question as `docs` instead of `personal`.
- V1 incorrectly classified pet names, bicycle repair, Baahubali and jokes as Terraform-related or personal questions.
- V1 treated a prompt-injection question as a documentation question.
- V1 classified a live AWS security-group inspection request as `off_topic`.
- V2 still incorrectly classified the AWS account cost question as `off_topic` instead of `personal`.

**Model calls:** 42 calls were made for the current evaluation; the remaining results came from the cache. The detailed call breakdown is to be recorded in the table in `NOTES.md`.

## My contract (DocMeta)

- **Fields I kept from my project card:** Not recorded in the shared code/output. Need to verify the actual `DocMeta` schema.
- **Fields I deleted, and why they make no sense per document:** Not recorded.
- **The field I tightened, and how:** Not recorded.

The purpose of `DocMeta` is to produce a validated metadata record for each parsed document, so metadata can be stored consistently in PostgreSQL and used by InfraScribe.

## Extraction run

- **Prompt version:** `extract_v1`
- **Documents:** 3 successfully processed, 0 repaired, 0 failed. The command was run with `--limit 5`.
- **Terminal summary:** `pending=5`, `ok=3`, `repaired=0`, `failed=0`.
- **Not finished? Why, and how many are left:** The run stopped because Gemini returned HTTP 429 — current API quota exceeded. The terminal reported 5 pending records. Three were successfully processed. The exact remaining count should be confirmed from the extraction checkpoint/database before the next run.
- **Most common failure reason, and what I did about it:** Gemini API quota exhaustion (HTTP 429). I checked Google AI Studio Usage and Rate Limits. The displayed Gemini 3.8 Flash usage was below the displayed limits, so the precise quota responsible still needs investigation.
- **A record that was valid but wrong (document, field, what it said, what is true):** Not identified yet.
- **Cost at list price:** Rs 0.1156 total for this run. Approximately Rs 0.0385 per successfully processed document (Rs 0.1156 / 3). This is an estimate based on the reported run cost.

### Extraction usage

| Metric | Result |
|---|---:|
| Input tokens | 6,765 |
| Output tokens | 2,364 |
| Estimated cost | Rs 0.1156 |
| Execution time | 186 seconds |
| Successfully processed | 3 |
| Repaired | 0 |
| Failed | 0 |
| Pending reported | 5 |

### Provider issue

Gemini returned HTTP 429 with the message:

`You exceeded your current quota, please check your plan and billing details.`

The script waited 60 seconds and stopped because no model could answer.

I investigated switching the extraction model to Groq. The extraction script uses `build_gateway()` and the shared LLM gateway, which currently configures Gemini as primary and Groq as fallback. The exact handling of HTTP 429 still needs to be checked in `gateway.py`.

The Groq connectivity test succeeded with `openai/gpt-oss-20b`, responding with `pong` in 899 ms.

The extraction script supports resuming unfinished work. I should verify its saved progress before rerunning it to ensure completed records are skipped.

## One thing that went wrong today, and how I fixed it

Gemini's free-tier API quota was exceeded while running metadata extraction.

The command was:

`uv run python scripts/extract_metadata.py --limit 5`

Three documents were processed successfully, but the extraction stopped when Gemini returned HTTP 429. Waiting 60 seconds did not resolve the quota error.

I checked Google AI Studio's Usage and Rate Limit pages. The displayed request, token and daily limits were not exhausted, so the exact quota issue remains under investigation.

I also tested Groq independently. It responded successfully, proving that the Groq provider was reachable.

**Next action:** Inspect the gateway's fallback handling for HTTP 429 and configure metadata extraction to use Groq without changing the primary model used by the normal chat application.


# D10 · Queue and worker

- **First run:** 10 documents queued, finished in **53 s**. Done **10**, skipped **0**, failed **0**.
- **Pace:** **5.3 s per document** (INGEST_RPM = not recorded, INGEST_CONCURRENCY = not confirmed; observed up to 2 running jobs simultaneously).

### Kill test

- Queued: 20. At the kill: queued **not recorded**, running **not recorded**, done **not recorded**, failed **not recorded**.
- After the new worker: done **not recorded** + skipped **not recorded** + failed **not recorded** = **not verified (20 expected)**.
- Documents in the database: **not recorded**, different IDs: **not recorded** (must be equal).
- The interrupted items came back after **not measured**. Why that long: ARQ uses its job retry/recovery mechanism to recover unfinished jobs; the exact recovery time depends on the configured timeout and polling/retry settings.
- Why nothing was doubled (one sentence, in my own words): **Not verified by a kill-test result yet.**

### Dead-letter list

| Stage (parse / extract / download / gave up) | Items | What I did |
|---|---:|---|
| No dead-letter results recorded | — | Needs verification |

### Live ingestion

- InfraScribe on Render: **Not recorded** of 5 documents done, **not recorded** failed. The reasons: External Redis traffic was initially blocked by Render's Networking restrictions.
- A request without the token gets status **not tested / not recorded**.

### Week 2 against Monday's estimate

- docs/CAPACITY.md said: **not recorded** pages, **not recorded** tokens. docs/INGEST_REPORT.md says: **not recorded** pages, **not recorded** tokens.
- The difference, and why: **Pending comparison of the two reports.**

### One thing that went wrong today, and how I fixed it

The ARQ worker could not connect to Render Key Value, resulting in a Redis connection timeout. The ingestion endpoint consequently returned HTTP 503 because it could not enqueue jobs. I identified that Render was blocking external traffic and that my laptop needed an allowed IP address and the external Redis connection URL. The local ingestion run subsequently returned HTTP 202 and completed all 10 queued documents successfully.
