# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-28T08:36:09Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a720aec45a8384b1662e779190fde6f868a3c7dea55496c942034cf3cc2a0ef1`
- PROD hash: `ee2e215784a13048e24b1537891b1896f9ffdd72e549d710ddbda15097f200a1`

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
