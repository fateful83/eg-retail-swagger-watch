# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-20T15:52:36Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `69760c88a3085b3e382374e5ae8ac4835ddeb469cb9f0de0db5c265ab1311ca3`
- PROD hash: `26d3851fbc2274647770ab1ee9d4b42e3ba2a1e5f46e1183c42b65db16f96ef3`

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
