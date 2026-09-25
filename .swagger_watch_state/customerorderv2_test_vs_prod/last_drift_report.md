# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-25T10:37:14Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1b607992e3b3e6e3b79f274786e7bd5cda0e5abdaa8875e5f5dac2aac5ffd815`
- PROD hash: `6c727e61ca2ed8511916f04e8dce0b77ba12e47fb3400ac86c4851eb827e01ec`

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
