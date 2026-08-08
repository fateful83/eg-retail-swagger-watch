# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-08T12:18:31Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0326fa85d3466eb349c5cf78b981a9149488624850f988e7f26c602f53b4d51e`
- PROD hash: `dd9ed980a8beacc49981e0c4134d34ca8c3064eca0df70771128b0253b9dbf31`

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
