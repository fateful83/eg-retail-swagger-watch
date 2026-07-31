# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-31T13:22:15Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0f7cdf53ae80a0ec40a7161898ce9238a54a11fd0510ee1d690611cbd0318638`
- PROD hash: `f3ab23129cf9950ec1d68fa271de9320f524d6e0463e4ca63f5f0a753a17979a`

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
