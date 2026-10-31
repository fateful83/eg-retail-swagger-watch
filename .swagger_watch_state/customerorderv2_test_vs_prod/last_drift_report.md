# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-31T02:50:14Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a719788ffeda4f0424bc7050b7e5ae2cca89c2f19b47d6e2b6cda77d9f1c1923`
- PROD hash: `8236f7532433a693094a9d4def27a0afa34a35d26e6bb0227d81fe7e7fcc0c10`

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
