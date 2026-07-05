# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-05T18:53:50Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a717d8b190bd3f9748e2b9169042f03adbc9680c4d67ccd7a5faf67650f30fe5`
- PROD hash: `1f195b9e62da814e9a282fdcec38bce6a44652af234d7245119bfdba3b952893`

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
