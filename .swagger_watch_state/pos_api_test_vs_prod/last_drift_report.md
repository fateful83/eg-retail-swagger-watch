# TEST vs PROD drift detected: POS API

- Time: 2026-07-14T18:55:33Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `56195cb645bf579b3bcd6d3ecd232f820d9ab4bb7425c9d68dbb30b11faa35ea`
- PROD hash: `7677c9fc12908fd0756c37fd206f2305238b74494d77e75ac8cb7dc0d88d9d2c`

## Summary
- Only in TEST: 0
- Only in PROD: 7
- Present in both but different: 0

## Only in TEST
- None

## Only in PROD
- POST /api/Order/queue/Basic
- POST /api/Order/queue/Complete
- POST /api/Order/queue/Delivery
- POST /api/Order/queue/ItemTransaction
- POST /api/Order/queue/OrderPayments
- POST /api/Order/queue/Payment
- POST /api/Order/queue/Sale

## Different in TEST and PROD
- None
