# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-22T20:26:53Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b26252e7957c4779d32c0f85d23429106ee7ae97a24f395af44ec083c7f6d64c`
- PROD hash: `d3990ec0844936ce9cf930c24a07049782865896df1257a4efdc71da5a630884`

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
