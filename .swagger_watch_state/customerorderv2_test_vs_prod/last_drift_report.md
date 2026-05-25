# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-25T09:41:26Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8e6aa996e15e204d2edcf094295516907dd4f205aeefe88308bb544063235b59`
- PROD hash: `31f6394e804183cc2b74144fef56dda6dbcf22131635a7d5b3011dae6c8dcd8f`

## Summary
- Only in TEST: 1
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- GET /api/gateway/ServiceOrders/{storeNumber}

## Only in PROD
- None

## Different in TEST and PROD
- None
