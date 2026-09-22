# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-22T20:31:17Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f6b8589f9317653f9a7b7372f11fad0c71ae2432435ce4647f82901750097676`
- PROD hash: `17055d9170e5abe0c014154c6062c182ccdfbbc12f7256749fed893a9b5db051`

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
