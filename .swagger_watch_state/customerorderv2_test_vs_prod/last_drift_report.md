# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-28T17:45:26Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `997ef58d350265e2a05c3cca6abc0d1f4662a7336e82e11cf4b2d6c5da239b74`
- PROD hash: `9e9e010632b50bfeb2899c83888cbcae53e4bb62483683660088b815c04d5fd8`

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
