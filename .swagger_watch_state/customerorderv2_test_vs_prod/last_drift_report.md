# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-23T18:10:30Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9c311cf89fbc1d2335fc11fb67ca0e3cbd1d5b180b586458dcd855ef6955af1b`
- PROD hash: `1bbc24f325392d0f5019149725ef0842c0d12c350bf9d43d44e759b459cdb192`

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
