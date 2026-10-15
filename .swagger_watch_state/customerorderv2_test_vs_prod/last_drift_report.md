# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-15T01:56:40Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e4af16adc53bde244eff7f37d6d8e866de2fb3253ae9509b167f0937bb899020`
- PROD hash: `0089db1142e4ea06c66f51522f5d85d99652c300ab11a46fcada4ecca1760ff6`

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
