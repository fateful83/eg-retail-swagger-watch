# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-21T08:01:22Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `77ce85c0b63ca954ea860c094910580e204e8bdac0e8b2c5ed7e6ebb168959c2`
- PROD hash: `b40e3227bdbe7d09c83300657d392f886772ef73490d9faeb346d38fb1b610d8`

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
