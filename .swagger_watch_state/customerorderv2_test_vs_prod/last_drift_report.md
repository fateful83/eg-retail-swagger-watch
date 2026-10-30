# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-30T21:43:12Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `be91b8a7414175f3f0e279ff029cec641d5e77ef4e008eade4bf10ad87d320a6`
- PROD hash: `48db764254aba3d77aa6496c1b519ed7f6a1e4d74572d8d1f3522919036d8f91`

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
