# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-27T01:57:38Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `498a936950f2317e55f284e905ec7b9825275bce9446e8153eaff4a1d7eee364`
- PROD hash: `291714d1456887cda146235b30bde36c7a2bdeddb21a2bbe1cb275c30c0fce8e`

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
