# TEST vs PROD drift detected: POS API

- Time: 2026-07-06T09:47:12Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c75edb95cf9902c70c96f00d6a94f0ee0e044ff1ac49af57eb053751f3ebe285`
- PROD hash: `29342f12838eb5fb75669c7dcb27eda8b512ccd50444650a41dd0ce9ba0cc6e0`

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
