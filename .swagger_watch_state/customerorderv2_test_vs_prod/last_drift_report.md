# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-25T18:19:48Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6e9dd8fc9e2410ebb5ea557053257e47a7a5cacff2f42966238f71af0a82b388`
- PROD hash: `f5cfbc6307015ac9634d7b8fad41f5fe742370edd43e39e7f64dbf0bb277e46b`

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
