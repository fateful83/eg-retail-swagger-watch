# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-20T13:40:06Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `bd728645af40dddc068fcd4b4bf02d2b0fd9b5d9f9e74c56d342f2426b150521`
- PROD hash: `0c5d54f759068c0631e59f9a681aa2d91094b189630a1fe6d39482cea4e1b9a4`

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
