# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-10T11:26:21Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1feed007827122b389d2585ca43054059ae12bff5c53c1806df18b6f14876b5b`
- PROD hash: `d51cef5fc38964d73c4f82a198e44f3d416b934b3f1dfe4244634af5ad361527`

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
