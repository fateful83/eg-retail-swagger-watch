# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-10T07:01:02Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8459cdb262b0e4cbdc61eedd39a318609dc0e160ce6b0e116d48cf9321aa105a`
- PROD hash: `9357cfea477091f0e5fec6f287b6f407a5f87cd5fd9feaac006076164da47297`

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
