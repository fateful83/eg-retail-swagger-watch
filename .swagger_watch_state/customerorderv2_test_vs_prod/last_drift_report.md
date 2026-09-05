# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-05T14:02:23Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a396e1ed2de5adcab3b8a8a0fb424843d918d0340fb3eeef6dddfa0c2601a412`
- PROD hash: `f6bb7a262de6c5c1152f38f55bb38fb5306f68dfc5de5e160358f955e39d17d3`

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
