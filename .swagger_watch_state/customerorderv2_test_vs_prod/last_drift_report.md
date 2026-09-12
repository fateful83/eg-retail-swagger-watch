# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-12T09:40:02Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e9677f3dbe2700204a2de2c85088900d817c4aa08406a6cdac2f3c3969c6b274`
- PROD hash: `226d5441e007838083074edf2146f8de4943c519cce2e4e887f91109dc191c93`

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
