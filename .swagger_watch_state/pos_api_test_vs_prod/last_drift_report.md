# TEST vs PROD drift detected: POS API

- Time: 2026-07-01T09:23:18Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9bc99f1c7ffc24a7be40269c6a471c3c270da63e0966093a9bc81b447dd89554`
- PROD hash: `be517db2018b5b2cd06d66a3dd726d53f47d248475b9a26fb5d73cdfe6454a10`

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
