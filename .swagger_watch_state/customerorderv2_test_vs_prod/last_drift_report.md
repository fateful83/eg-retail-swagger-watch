# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-13T00:48:51Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ae963e3f60b3e4f45b85b42270301af3f82b90acda0354fd654295b9c9806ce3`
- PROD hash: `e906b43c5d0b62e7a096ddba6923f21356cc6da2399b93c4762f3413fdd2d666`

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
