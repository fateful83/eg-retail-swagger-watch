# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-22T02:13:16Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `418319f31401289248a9415d76ba291755c4926a1fa30c875021f37eb187c98c`
- PROD hash: `5c0797ff20108777a46aea27b53aecaf1c3c3adfd323d051b893fe04c00b90b5`

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
