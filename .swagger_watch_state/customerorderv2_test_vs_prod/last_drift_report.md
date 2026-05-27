# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-27T08:54:42Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d593c11d6dad1980432b4694a0077654ad5e49a5bcb5386d345001c97648c2c6`
- PROD hash: `83e424f6472a126425d214cf084125971dde7fbe08684b9f0d578a94a04b9886`

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
