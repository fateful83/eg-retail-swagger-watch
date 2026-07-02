# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-02T01:54:43Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6f228af2c6aab41875e103236cb0e361ff40e984c99c572ccb461be0d3f87fe2`
- PROD hash: `811ebc651912946f2e2535431d1794fc9a9b31e0bbe0d7bf22695c8fbb1a53db`

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
