# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-07T20:50:09Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9443f5b3cf2918b7d173cfdb60f390ad2fd872e65205d454c6ca481831655e54`
- PROD hash: `4d8e9ffb749f9296ee49d7e9bb0f56f3981e5ab88496d9f4b32488dcc88ba04c`

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
