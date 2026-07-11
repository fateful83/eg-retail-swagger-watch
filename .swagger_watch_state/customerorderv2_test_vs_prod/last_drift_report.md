# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-11T12:43:22Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8432b2e28dec7815204585a1a2e44cd5dbddb456871542946d5dbfe07a078f48`
- PROD hash: `e87ff93372ddf59c654fe8f9aafa1b5dc889e8937b80ffffea6c83aad5331faa`

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
