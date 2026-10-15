# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-15T20:35:27Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a0c5192f3a5913353b23b2a5a68a0f9ea7b283843634f0610baa09c2c71aaacb`
- PROD hash: `209a582bb3e39b9f4ec1b7ff9d6be4b33994f6206302c2b881e32fa021fb7d28`

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
