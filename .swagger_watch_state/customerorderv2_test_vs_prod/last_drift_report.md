# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-20T14:56:46Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `68eedb35bf74ef9406e351046e0497938dcc0ab0e2773fa4d982e3da4a646635`
- PROD hash: `db5120ba092c0ab2412d6908b54c93c4ac0745e7e0b86f7f4472e397809c6280`

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
