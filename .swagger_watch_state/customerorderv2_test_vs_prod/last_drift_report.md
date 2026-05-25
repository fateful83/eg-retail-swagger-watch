# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-25T14:25:49Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `bcf05e4b7b698c40c3427c4d36f5ffa62f80a22f25ed53ca484ec5614e577382`
- PROD hash: `a1aaa8e5a81bd478bbe244b67c636ce6bb6b6ec9162817f5cc031ab779968352`

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
