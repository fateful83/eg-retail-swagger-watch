# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-27T01:57:59Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f1fd4fed8f621edd63e1e93347342d3cd8c52428b75648b0801ea776afceb551`
- PROD hash: `00dd96f438b17b345ea51f33407610487cb2070d06d9c498a5258e4229909abb`

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
