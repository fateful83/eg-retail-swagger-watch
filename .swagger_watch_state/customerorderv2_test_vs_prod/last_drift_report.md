# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-16T00:27:16Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `5cb56cb691e1007ec3017579f09c25e6cdda6e4fcaa1c37a7f202f642062a60d`
- PROD hash: `e465bf72c9d83778ee75e238ebd3291abddd2ed03e60e133ab13b8f90442d684`

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
