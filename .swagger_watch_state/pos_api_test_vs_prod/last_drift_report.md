# TEST vs PROD drift detected: POS API

- Time: 2026-07-24T01:16:24Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f0d49370467f3c5bdae7bb4891f9e7701c0c72aec2b9fa03e4d463b1ed06c910`
- PROD hash: `34031ce12942b09b1bfb5f3390b1a9eb27ab2291ca2ce8c395499fb5a6d6ef8d`

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
