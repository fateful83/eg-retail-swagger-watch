# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-20T18:18:42Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `fff53c32a1592adacc189b860123fcd0217339d847f317c0befc27bc0d41932f`
- PROD hash: `bfb29b080f15965494bb56e43ff92ad54f7ecec19577f61293c84baf084ea612`

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
