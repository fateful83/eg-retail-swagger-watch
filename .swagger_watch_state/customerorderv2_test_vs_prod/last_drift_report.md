# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-24T12:52:06Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ee2ba026d844ceab2bf0016125d95328e4c157dc7942040e0b831e19ee09d068`
- PROD hash: `8bc63741674c0b360908320a3fee195b2af285f227b67a00bd6a0b199f9c7ae2`

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
