# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-13T01:57:25Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `210157a26e295d30cc432f8f39f56f368e7e67a7a945308a5248b89503d3d011`
- PROD hash: `38972a8988d38c648b17c7ee73ba69e9f93579d36b9149d46f2d0f5747af1f12`

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
