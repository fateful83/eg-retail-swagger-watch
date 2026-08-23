# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-23T12:12:52Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ca11d4adfaaa729a80855b0382251d1f468a4f6ebf05998e368114f72e0bd2e0`
- PROD hash: `676ad882331a5074b032c249de0b72765b47c1800d180587dfdaf2bb447396d0`

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
