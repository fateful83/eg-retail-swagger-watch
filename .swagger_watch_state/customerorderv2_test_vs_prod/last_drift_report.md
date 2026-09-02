# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-02T10:00:01Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `343c35c8246911d687bc31adc078f1bd672e04fa627889c284bb091faf7b7bb1`
- PROD hash: `a943d1349d6bdabee546e111e80ac24a468179b75ab4fa9b218603c81f39e535`

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
