# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-19T12:42:37Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a522f25a6f8667c3b4ac4f29ca46ed82731819bb0d6dc954cf3a11d2f1139e50`
- PROD hash: `928f8c02cda3bebd33fd613c9020b418f2e93e060df5fbd1a13de30947112787`

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
