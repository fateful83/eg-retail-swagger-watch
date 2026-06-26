# TEST vs PROD drift detected: POS API

- Time: 2026-06-26T19:24:46Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f96b5a3bdb78255c6aef9e6e056ee07ca5328864122da8b43050ac6d61f10894`
- PROD hash: `f5de04fd648a4f9bf45e697357d95cdffd793fe7d9307f087a7bdfb10f5dc1a8`

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
