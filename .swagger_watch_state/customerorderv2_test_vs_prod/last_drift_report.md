# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-19T01:44:17Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `392d7b5275b04d493310a6ad4959d0bf50bbdfe1302a9bbda822ed7e7d2fe18b`
- PROD hash: `a1fca60170918f4c4381b7073bafcd56571bf0c740f9655603caef4ba2fef043`

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
