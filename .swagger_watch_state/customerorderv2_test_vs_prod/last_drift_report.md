# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-28T01:59:41Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `46d4cfa1bedb6458192ed44eff49b9fce9461d58e6226b0826231eae80a2e765`
- PROD hash: `7c7f0c2f94ef99e573a1e5ca1c42f57f76d227066263c8a5928b3ea9180b9a38`

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
