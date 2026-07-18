# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-18T01:09:03Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b10b74b9cf12f440d7e4af65c6332cb4241aa503ad614e19e5bc6faff96123cf`
- PROD hash: `577d7b155ceb691f3caa505697987f41cba16a92a93dbaa7dd9799e0b3ae8aec`

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
