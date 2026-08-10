# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-10T12:36:46Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1978c5a4878a56d0b1b60495d40aefa2b924bc30a57d3d3f93270342f7f92702`
- PROD hash: `f34ba46943f2d790011daf1b9698556767d13765dba0673b9f6b0fb9deb2d8d2`

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
