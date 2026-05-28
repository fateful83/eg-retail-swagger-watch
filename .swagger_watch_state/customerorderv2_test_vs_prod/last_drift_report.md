# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-28T01:29:21Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `296760b9a205b19820091fb0dde92061cbc8cf03e96c48e1ca36a415a5b2d1e8`
- PROD hash: `c112e8b5a5ca478e7bdeed20c6fca5c281c6fcc3338e5d3fb90e69b3c405c1e5`

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
