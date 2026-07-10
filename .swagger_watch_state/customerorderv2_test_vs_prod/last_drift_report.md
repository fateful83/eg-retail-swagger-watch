# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-10T13:47:15Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ea0042cb88ef2e57f35667b8173057789e5d446e1533c5222af2a3a713448a99`
- PROD hash: `18ed4e29dad330922a39811828b587e20714cbdbd981b3f9176bd05a14259f8a`

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
