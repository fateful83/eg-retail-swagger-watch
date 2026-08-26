# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-26T12:21:45Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `93de189ea8996d704b57407ffb82c714deac971141d5d499a62e3873744bb903`
- PROD hash: `7fa987a8756a50903c453ba80cf818d19ef3efe69cfc24b96c9f42d2d8296934`

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
