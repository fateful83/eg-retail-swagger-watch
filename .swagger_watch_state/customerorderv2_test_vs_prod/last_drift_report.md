# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-09T15:22:23Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a7a838417ee3edd7dda3eff5e13711b056ba1f3827cf82a887853b6ce642935c`
- PROD hash: `4acebe7e5f91bd7467044365bad84a89309c692c9524e270b6715d0f35af4ccf`

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
