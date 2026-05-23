# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-23T07:59:51Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e68b683fc5a742d09588085b7f3c8134f12518cbd267311096ee445b42aaa488`
- PROD hash: `ef6968cffc94e81729575211219f926c6112559c685c70643bcefc35076d4f30`

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
