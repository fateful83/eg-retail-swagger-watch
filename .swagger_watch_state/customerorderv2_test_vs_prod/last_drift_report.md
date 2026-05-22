# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-22T08:43:55Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `838dfb5bb6746eca04379b2cf1c98d9bd1d0e2790f0bad62625c7d4a7ec0de03`
- PROD hash: `3a121fde1546df1acf99260e4b527419bc234bb0944082c273a18f3540bc11da`

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
