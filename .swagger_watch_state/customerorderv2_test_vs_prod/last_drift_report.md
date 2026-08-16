# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-16T06:17:02Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `73ddaee259d678892553d7562d5f816c335155a2f59866371402b1592f041fc6`
- PROD hash: `a4a222766537a20c36cb0c0d1b7181510c74c88a77f47d46c41b1de39c90216d`

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
