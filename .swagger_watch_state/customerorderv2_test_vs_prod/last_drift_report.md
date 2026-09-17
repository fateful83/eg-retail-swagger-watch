# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-17T10:30:02Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c3a7dd5a8d48efde6c234eb065f7129e6572693d66358f6778124bf843338b99`
- PROD hash: `949c7a665d766832c6aba94ff7520dc0c7b1d8f30efe2d67e7c85b38bb262c03`

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
