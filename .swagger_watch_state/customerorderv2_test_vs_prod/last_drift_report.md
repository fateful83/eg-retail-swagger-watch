# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-23T01:45:06Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `df87ba6d8f0990dc6c11d7fdd31b6cd488b2e8efa51d7c1958b7893f88b7b1f1`
- PROD hash: `ccf39974d314875112e7ba31a5884cfd7ccf41b35c8afd218ee11f9278e4ce20`

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
