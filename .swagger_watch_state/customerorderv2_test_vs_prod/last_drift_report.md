# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-27T21:31:04Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9d12f191f22900b7f6d7cda3641ef5b284443617d5c1c41638de240e8424c241`
- PROD hash: `9ff7e0fff73576b6c4f229ed0190c6d1859e490c5fc03bbb4747e59b55420e44`

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
