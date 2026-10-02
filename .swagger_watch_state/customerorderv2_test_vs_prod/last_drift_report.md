# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-02T11:25:00Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c7c7d40659bdc1384c1de624217bf12bcae2ae5b91ad72a5c5d1da22f66a222c`
- PROD hash: `12b5f95018f945572aa77f7c2ed3081864c56d000d26d8a14fffad2ccc0ed0d8`

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
