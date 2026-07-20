# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-20T19:19:01Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1fd663ca13345eaec37293172a73cfde627dc72ffacd035c435638d10b0f740b`
- PROD hash: `94c2385fbe3468db93351fef4e7ee2c55997a7a277f09e7aa0c7abdb72f2fdc4`

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
