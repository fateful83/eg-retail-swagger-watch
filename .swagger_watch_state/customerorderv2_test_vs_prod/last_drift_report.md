# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-23T01:52:24Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f70ea02e783574394dc5a9cd100d4e9ad7cb1f8b836fe3f7d4d19775a25c7664`
- PROD hash: `118ce2a7ee522f98de840d73d74e0f348ff19f6a22cec17774456c635b8093a6`

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
