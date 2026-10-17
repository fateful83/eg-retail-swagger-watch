# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-17T01:41:12Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ae4f5a932105e7d01ec55e97ce55315412ee9caad5a7ae8e035b02a7d7eadbeb`
- PROD hash: `e4a0eae9c677bb10583c9903bc7adb4b7df439c06252ed6de268efd3f62f752f`

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
