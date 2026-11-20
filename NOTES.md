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

- Rolled back to sha ________ : started __:__, smoke passed __:__ (___ min)
- Rolled forward to sha ________ : ___ min
- During the rollback, the database stayed on the newer schema. Why is that safe here? (2 lines)

### Where my secrets live

- Neon string: GitHub Secret DATABASE_URL + Render environment. Not in Git, not in the image.
- Render deploy hook: GitHub Secret RENDER_DEPLOY_HOOK only.

### Monitoring

- UptimeRobot checks /health every 5 minutes; alerts go to my email.
- One thing that would make my live app faster on its first request: (1 line)
