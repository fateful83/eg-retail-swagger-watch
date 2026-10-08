# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-08T12:17:36Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `5ef083080cda9c4191f8e090e0094dfc5d5a010c7db62b9ee87add0afb970e37`
- PROD hash: `f61ac172e5562eea23eb757a4fbf5197259efd7fb4b3440277ea8f303077a531`

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
