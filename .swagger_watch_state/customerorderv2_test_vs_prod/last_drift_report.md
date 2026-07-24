# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-24T01:16:15Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `3a58c1ffcc35cc4c8bdc598f07c80acb00400e627fb56d20fd50b6648089691c`
- PROD hash: `0b4fa780a4728eeb392dfac43fcb254ebaf98e9445e44ad654aa030e7fbb19d0`

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
