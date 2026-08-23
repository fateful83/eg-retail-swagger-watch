# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-23T00:28:16Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1624d6dfe7119373ac640ffe3dd014bf92f82e806d512d885faf38d05ed5c376`
- PROD hash: `43df3c2155fb2e5c933889fd946c4420d5ef262c432d4a873e0647bdd1e28aec`

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
