# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-17T01:17:14Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9ace475938956e3eea896e45fb97f4b297a327da2770854723de48443413c873`
- PROD hash: `aadae9f27248c592a3c110eef7a5748398104bbcf6133acc50111b0c4d14403d`

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
