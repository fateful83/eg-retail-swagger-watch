# TEST vs PROD drift detected: POS API

- Time: 2026-07-22T18:52:16Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `056f0a2f879aa8f36bb969a578d01d1f6627e4a18268cf77326959ef9cd9caaa`
- PROD hash: `da461183a7ae843e2c8fb5f79a91fcd15b5c537a0f06bb9a2ba2e2cd1189a180`

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
