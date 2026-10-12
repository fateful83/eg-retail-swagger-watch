# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-12T23:52:05Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0de3e37ac4ef7ad2f6427d6dad5c7f7a73a5f91cbfacd4a140ac2e0c57b007b7`
- PROD hash: `e32228d1947b155eb6656a4d491a0730b23eea14e4ca34e1efea24aae414013e`

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
