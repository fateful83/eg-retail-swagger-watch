# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-22T15:46:57Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2d0c9e696cfb62d94c32a82a5a249ae52628b5ff22b163777ff9e10d809cc82f`
- PROD hash: `2989780c1a576262730331be347a74cf21035587b84c8a6b1928697992134727`

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
