# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-19T09:47:32Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `114c07be8d3d86af26b46d384c2b3137db6a209ec1bb243c21c7ab253a69b90e`
- PROD hash: `d833928ef27d542705a7d61c15bc064d349d29828ab936e973a8c32a3c845098`

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
