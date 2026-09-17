# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-17T01:52:35Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9d82d5f6486b32a6ad70efef12c0e444156b99ad8c9f2025daacbbc2ca10014a`
- PROD hash: `d791dbf14e5f2465d830640ea7016a51a29f6c744d9b9212a039f3a0d20efec1`

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
