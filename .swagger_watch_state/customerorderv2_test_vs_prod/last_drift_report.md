# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-09T12:09:28Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `75ff7a1cb7309ffc4c01275e48326926c0e16777c3bdf0b9d9e99ac24b93adca`
- PROD hash: `fffd167122d2964cf846bf14a57f17a4ccf4a648ce4356edbd4b85abfaa968f0`

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
