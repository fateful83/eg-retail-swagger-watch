# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-12T13:36:47Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `4e36c70014cb2479213d18282a0717026050e492765fce7920a1d63e04d88cb6`
- PROD hash: `16e7e321093e0327d7b5da9077f9ff885973077a769c0d282572e5a3ec76b0d4`

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
