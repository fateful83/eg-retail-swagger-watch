# TEST vs PROD drift detected: POS API

- Time: 2026-08-04T19:14:24Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b94a7490946873fd3acc0f34c10a9977084dd94ba43d11ca676b6c21d8c56b0e`
- PROD hash: `700020cc1c9f32d77dd9c12c3f4f69a9e5eaf20adb05f9cd3c0de78ecc8a9e70`

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
