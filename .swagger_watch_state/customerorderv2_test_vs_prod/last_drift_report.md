# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-27T05:11:10Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `22a28ff8f69d9f59b3daff89f3498219032ab43e9b3ae2ab78174d457e848640`
- PROD hash: `5ac19962e2f16d04a1bcd80e3053c9fe04ec91f946bd49763c370199b8fcfc7e`

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
