# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-24T08:47:41Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `08e8965efef86272921f67e8649aed5ace0287b3ba8c52fe16bfcaf9775ac95c`
- PROD hash: `eec1e65999e96031c0533082ece94bff5554da1c116bbc6fb6d04157aa500b71`

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
