# Hi, I'm Khaled

Backend engineer. I build services that stay correct when things go wrong: duplicate requests, crashed workers, hung endpoints, bad input.

**Stack:** Go · Python (Django, DRF, Celery) · Node.js (Express) · Postgres · MongoDB · Redis · Docker

## Featured projects

### [multi-tenant-billing-system](https://github.com/SupeeerMario/multi-tenant-billing-system)
**A billing API that never double-charges.** Django, DRF, Postgres, Celery.
- Idempotent payments enforced by a database constraint, proven under 8-thread concurrency
- Double-entry, append-only ledger with asserted balance invariants
- Per-tenant isolation via API keys, scheduled invoicing with Celery beat
- **Live:** [Swagger docs](https://multi-tenant-billing-app.duckdns.org/api/docs/)

### [bulk-data-import-pipeline](https://github.com/SupeeerMario/bulk-data-import-pipeline)
**Streaming import of huge CSV/Excel files into MongoDB.** Node.js, Express, MinIO (S3), Redis Streams.
- Upload streams straight to object storage; API answers `202 {jobId}` immediately
- 500,000 rows imported with memory flat at ~120–130 MB
- Each 1000-row chunk and its checkpoint commit in one transaction, so a killed worker resumes with no lost or duplicated rows
- Retries, dead-letter stream, and a streamed CSV report of every rejected row

### [uptime-monitor](https://github.com/SupeeerMario/uptime-monitor)
**Concurrent HTTP uptime monitor.** Go, Gin, pgx, Postgres.
- Scheduler asks Postgres which monitors are due; a worker-pool of goroutines probes them
- One hung endpoint cannot stall the others, and a test fails if that stops being true
- Every probe (status, latency, error) stored; uptime computed in one SQL query
- Graceful shutdown: workers drain and every result is written before the pool closes

## Also

- [learn-hub](https://github.com/SupeeerMario/learn-hub): full-stack learning platform with real-time chat (React, Node.js, MongoDB, Socket.IO). Graduation project, 2024.
