# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-07T22:19:37Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0cc9006a17e6d58f952299255c98d92df9f47cce85efb8327743c50b9a69a39b`
- PROD hash: `990d79f828b6b8466ef0d9547a951cbcf1f91b003fa86d3f9484566a4c389eeb`

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
