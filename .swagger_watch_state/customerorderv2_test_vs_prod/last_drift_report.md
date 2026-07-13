# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-13T13:53:00Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `de298a7728712cb6b6ededfb4a40c1d929ff60a49bd5f804efee2ed6e840ac10`
- PROD hash: `5d7fdeb9f2551f300aa4de005d40810e3e2d97d544801e0bbf745aba36640143`

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
