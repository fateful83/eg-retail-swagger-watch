# TEST vs PROD drift detected: POS API

- Time: 2026-08-04T13:29:37Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b94a7490946873fd3acc0f34c10a9977084dd94ba43d11ca676b6c21d8c56b0e`
- PROD hash: `ced4b37a7448c42261fc2a552e6eef1f3fff8345f31d241bc230f5d7c5851a6d`

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
