# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-21T19:31:24Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e174dac0e8b3597cd2dbe9078d0db8c9de81690b274310e9c46cb85fb3041c0e`
- PROD hash: `c1f87a0c04c1ad1d1e0bcb20cc6cf09d7271f52c176eb62409b05730888f034f`

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
