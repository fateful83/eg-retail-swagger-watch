# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-07T02:47:13Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d1bfb07fc367aa1991425073ce583b3c1dbf247b5c0b8e895a2fbf382df99234`
- PROD hash: `b61c15d99f46c7cf5c5b6992ea60e78f7d589588ed218c71307dc3ddf3228d4c`

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
