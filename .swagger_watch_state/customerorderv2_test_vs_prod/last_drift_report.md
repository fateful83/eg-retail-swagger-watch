# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-09T01:39:54Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ccdf27b842fed54ffa066658ae957cb9cee1feff01a4ec468fffa2bcead399ef`
- PROD hash: `ae46b85caec8051f596787fb7f3a127fb5be33a105402e8013a28f86e414a02a`

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
