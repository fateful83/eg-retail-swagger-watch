# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-28T13:06:10Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `5828698aa5abf3dc625446ddfe851a57d96758d902ceb2c62fe7bc7d27b38b1c`
- PROD hash: `0479cc280b839472f68a7396f1d930e36ebbd02ff2c5eaeb10a4af6048d3d279`

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
