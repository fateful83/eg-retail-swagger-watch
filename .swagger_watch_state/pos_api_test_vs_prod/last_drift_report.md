# TEST vs PROD drift detected: POS API

- Time: 2026-06-30T08:50:04Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `5edf471c8a6ff0443692c32baffb5cf1b95cab3cb48f43da40030df3cf80ced9`
- PROD hash: `e5182b744cabbeb7129f50eb367c2f648e69cffd3c663c007f515367f256240c`

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
