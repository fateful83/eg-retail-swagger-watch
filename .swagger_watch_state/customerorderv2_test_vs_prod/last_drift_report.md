# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-04T11:22:52Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6560b11fa2314734cbdf630c146795dc7366f6216b1cbce10a51d5f7e6f21ef5`
- PROD hash: `0df42a1e0ad93529d191f3040ad8d1649df84c71d3f32b5b0a5d3ada7f152cd7`

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
