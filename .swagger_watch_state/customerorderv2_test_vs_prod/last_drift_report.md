# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-30T01:46:57Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f4d8f6c0ddefa4fe7fed83373acf334b127d8adf8d0ff0b82cc205e4650ee39d`
- PROD hash: `8ebd94b2ca3c0e80eb30eea1cd44496753253709bdced730dec61d1229468e8a`

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
