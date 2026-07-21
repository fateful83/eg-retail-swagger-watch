# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-21T18:59:20Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9c18160f2b6c0609efa24a9a71544d58209841ba396f04192470dd557df663e9`
- PROD hash: `4783d7bd323d4e2fa34f84eb93806e51a374912d618bf63b6acb98f64aedab32`

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
