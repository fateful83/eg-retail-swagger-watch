# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-12T12:36:35Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `4487fa1a1a8087d25009898fd1ac7cf31b12a87108c63a7ab1aa638a6aaadc46`
- PROD hash: `3769c005a2c350b55f894fc9e0037cefc1ced2b467cd1d9db26d5f431368dec6`

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
