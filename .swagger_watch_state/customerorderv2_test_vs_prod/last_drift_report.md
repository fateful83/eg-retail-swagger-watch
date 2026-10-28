# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-28T17:28:34Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `97a5a70e4096cd486e7f0707ed4d56190c9c125c24082c348c165411f25fa646`
- PROD hash: `9dba7bca13f652f4850d4fb06320da6473bd5b2892016baf95b1f998c0877df5`

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
