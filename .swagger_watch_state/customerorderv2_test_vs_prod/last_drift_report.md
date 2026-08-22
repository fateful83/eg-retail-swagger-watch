# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-22T00:27:05Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `61e7d43a3029dfd1c61f13d6a48ac26e8aec239dff10c64fb2bd40dea6fbc871`
- PROD hash: `b4b6fe099284ea516144da9fd466ea3f54bda14b0503aff6bfdc9b96f3c26230`

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
