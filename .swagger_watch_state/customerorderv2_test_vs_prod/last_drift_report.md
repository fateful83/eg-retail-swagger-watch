# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-02T20:10:41Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `82db2e896b8a8d3aec95dd422b2ba9ef39c60d31fad2ddecf41fe11a6ab64d58`
- PROD hash: `653f56cb57e6879c03f18ffe525d9928ee37c341ce2473f71c52255df6453139`

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
