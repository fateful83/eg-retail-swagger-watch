# DEV vs TEST drift detected: POS API

- Time: 2026-06-29T10:15:14Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `67607cbd613592b3cf71489ed55da17d397088812dd840501835c95c0b024dd3`
- TEST hash: `7059a8edf989b367d5976ad151d9cfe8363bcbed0bdc5b2b6503bfc4d3ef3d54`

## Summary
- Only in DEV: 7
- Only in TEST: 0
- Present in both but different: 0

## Only in DEV
- POST /api/Order/queue/Basic
- POST /api/Order/queue/Complete
- POST /api/Order/queue/Delivery
- POST /api/Order/queue/ItemTransaction
- POST /api/Order/queue/OrderPayments
- POST /api/Order/queue/Payment
- POST /api/Order/queue/Sale

## Only in TEST
- None

## Different in DEV and TEST
- None
