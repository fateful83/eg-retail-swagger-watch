# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-03T08:53:03Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9fcef7f6d34f03cdbad75b61507566ca0d981eea34012fced0491d6ebfa056a3`
- PROD hash: `b2fe51b1ad7daaf091b5917c11a3730b41d19da75520a5de34c93732b9a60fcc`

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
