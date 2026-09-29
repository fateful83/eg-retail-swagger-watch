# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-29T11:38:02Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `19c1cf15def5a23cc92dfccd43fc14fc529f642f8473e8ff4388112c3b63e76f`
- PROD hash: `90b2ce68e6f1970fd0d7b9c4798fd259b655ce8fcbf9995c2795b18be67f3a02`

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
