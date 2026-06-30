# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-30T08:49:55Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `fca49b05eb68245432b6bd915e63b61bbaa313f60baf77196e03442563895a99`
- PROD hash: `be86188861f38297cfe60247030cd45ccc834bb1b77db486b8857f2e3867080a`

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
