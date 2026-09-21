# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-21T17:14:02Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6acd0c4e01b18176af1a5f0ff5e56f8562d40622ec5e88897338b9adece9c5fd`
- PROD hash: `a5b2e8711bc76bb896149d64444d9f98e0121e7824a7582b36116ac0dddf0bf8`

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
