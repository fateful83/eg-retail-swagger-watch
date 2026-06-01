# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-01T02:06:51Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `fe637169101aed289216643469f01de39f7f24b603d1d463a256a9f0ba5f9530`
- PROD hash: `b4ac57df90d5c356fc2689ccb3e0b2ab98b92b61706beff452e0cbf2aa3e35df`

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
