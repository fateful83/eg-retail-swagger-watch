# DEV vs TEST drift detected: POS API

- Time: 2026-07-14T18:55:33Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `01b4b148642c4ef491db53b6306287355905cccf2b3c3a63118c3aee107b3883`
- TEST hash: `56195cb645bf579b3bcd6d3ecd232f820d9ab4bb7425c9d68dbb30b11faa35ea`

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
