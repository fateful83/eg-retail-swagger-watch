# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-26T19:50:13Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a13e6d2e2d2054c2c6ed61fab1aaa71aafcfdf7454cb54f0339639cc911092ce`
- PROD hash: `bf92290e76cf1c8c345573d9ee45dd1dadd711abd1f0c5755b1c5b45cc20b247`

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
