# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-05T12:45:01Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `4db874f21e543320bc2783b5974c11dc4913d3ee99b92512af50d70803c27f97`
- PROD hash: `a074108629f1030ff475739b69be5dd1580d86cfa594f3562c25b8d1b2433cd4`

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
