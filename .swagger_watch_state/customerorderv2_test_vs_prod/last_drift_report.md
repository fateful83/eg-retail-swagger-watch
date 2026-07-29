# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-29T18:45:52Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `3b1e41a4fc67f14cf5d072b281831616c353e32b71517c9abb59d3ff024c3a61`
- PROD hash: `f5c7cae322356f320c2cce70934f19ac49f3c6123e1c31a5772db9f6c0de3403`

## Summary
- Only in TEST: 1
- Only in PROD: 0
- Present in both but different: 1

## Only in TEST
- PATCH /api/gateway/ServiceOrders/{orderNumber}/orderStatus

## Only in PROD
- None

## Different in TEST and PROD
- POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment
