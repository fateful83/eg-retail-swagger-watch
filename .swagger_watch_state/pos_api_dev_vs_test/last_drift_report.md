# DEV vs TEST drift detected: POS API

- Time: 2026-07-15T07:44:48Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `1ac88579983d691e4aa4921e85c8a7a06af44d0120405efa6d03ba810fe9512e`
- TEST hash: `108f566296a8ad6079549bfe6ca0b891a3dcbdc25f0420c3a987d8a71c5d19d3`

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
