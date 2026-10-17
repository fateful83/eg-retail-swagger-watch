# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-17T09:46:12Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `84101f0cbdfbfb60413c84f1c515d56c8f7dd0cbb558623f9cdc36ece7c06c6c`
- PROD hash: `f9e5c4e6c1bc536914a46d2ec37704294069fbf94de9ebe40fedd8ab1f1344a1`

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
