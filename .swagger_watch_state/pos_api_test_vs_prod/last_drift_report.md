# TEST vs PROD drift detected: POS API

- Time: 2026-07-12T07:52:06Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `06d3de083cdb9dc8b5591a3897d3156cc25d4b9ed95d9432151f0b1ef6a514bd`
- PROD hash: `fd5a1d34fcf99fb6eb1ce6b3beef0114d76c36aceda3efd356caf226f07306b7`

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
