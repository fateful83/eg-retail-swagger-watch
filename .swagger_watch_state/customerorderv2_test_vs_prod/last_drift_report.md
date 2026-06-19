# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-19T14:33:43Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `df80b392a9d27e588e2aece05e8b9e2b3404fd52a2cec1cac68384cdfd8dc667`
- PROD hash: `22531857cd338b028f7bae699ec51a675d160f42919b71af1f833fcebf6eb883`

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
