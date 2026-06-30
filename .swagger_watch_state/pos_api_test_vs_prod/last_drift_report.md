# TEST vs PROD drift detected: POS API

- Time: 2026-06-30T13:47:55Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `5edf471c8a6ff0443692c32baffb5cf1b95cab3cb48f43da40030df3cf80ced9`
- PROD hash: `91b45770a88d3273ea0bdb4476ad6eabd794fa2fa2858bce7925e77706d78b6b`

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
