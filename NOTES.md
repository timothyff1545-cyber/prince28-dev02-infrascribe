# Engineering notes: InfraScribe

## D03 · PostgreSQL

### Migrations (upgrade, downgrade, upgrade)

```text
55404245c0e5 -> 35b3293dfd29 (head), add gin index on metadata
<base> -> 55404245c0e5, create documents and pages
```

### The loader is idempotent

```text
run 1: paste here
run 2: paste here
run 3 (after editing one record): paste here
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

When would it switch to the GIN index? (1 line)
