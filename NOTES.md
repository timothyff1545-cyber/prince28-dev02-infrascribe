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
