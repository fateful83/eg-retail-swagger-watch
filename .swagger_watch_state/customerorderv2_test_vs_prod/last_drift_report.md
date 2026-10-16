# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-16T01:46:29Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `457fd9d8cc09229e81314410eceb8ea876161399422b6acac7f39659c7d3acb9`
- PROD hash: `801be55eaddc0cf817901bc305d57ece09d63b727801c0c1014781f6ccef28d4`

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
