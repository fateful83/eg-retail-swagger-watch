# TEST vs PROD drift detected: POS API

- Time: 2026-07-05T12:59:45Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `4e73c45c60ed2807e7004415e37eab29582923ca26ef54607c8cba733c64a3f6`
- PROD hash: `859c6fae342b83a79de3077deb1ccd73fea64abc4f34ff2187c5aa8e39badc71`

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
