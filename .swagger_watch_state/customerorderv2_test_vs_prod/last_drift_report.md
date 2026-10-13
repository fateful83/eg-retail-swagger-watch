# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-13T22:00:32Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2f5693e0f062e109a8f414f64b5fc1a08b37ebb170fd1118eb216a0e11b811f8`
- PROD hash: `d6eeb6d7e8e6432ae5100f6ec5b58f3df86f3cc4553b22cf8123bbdfc23305a3`

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
