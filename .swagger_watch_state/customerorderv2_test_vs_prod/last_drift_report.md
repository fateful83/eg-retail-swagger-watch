# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-24T12:19:21Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a8ca9ce4918fd73a3fb91676b4acbf93ea3fe7974bbce0ecc9b24005b87e81d4`
- PROD hash: `0ec7a5fb86579bd68942813e83e4f9e8996c1fa1cf222eae0c864dc917aeec6f`

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
