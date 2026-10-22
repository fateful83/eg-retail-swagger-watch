# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-22T16:08:08Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `81b7fbcf069235de06c946d5a5ec95d1614555c745722a706f1cec6c415697f6`
- PROD hash: `d7d5e8eb2babcc25ee4f57136f099961e0de1e2b56e4b77888e722fd4f16f965`

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
