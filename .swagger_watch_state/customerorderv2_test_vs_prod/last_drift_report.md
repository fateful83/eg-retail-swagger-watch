# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-20T01:17:47Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9a2ffa302cf9e30fa16e1caf499ac82d99f6ba225cafb99087ca6c8d225754e6`
- PROD hash: `677c872a506b4efd3ad514c319b8d6597969abce47a70eff7238a0a44d13ea15`

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
