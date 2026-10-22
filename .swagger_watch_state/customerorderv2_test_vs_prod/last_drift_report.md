# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-22T20:52:57Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `91294ee002e44e05a5b97ead0684d0350cc5b8ba4e8bef76c537f4de84c5f37e`
- PROD hash: `68a4d5c271c46621f686c168802b0932801fb2ab451982a27370995f1bbeeceb`

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
