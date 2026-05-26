# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-26T09:00:09Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2479d21114c39983ee9a25933e971b18d6d0ed89f61844f290d515b3b24bc863`
- PROD hash: `9cba1ddcd2e004dfd1d6b93ffbf789a5fe660c6cfa4bc71d090dace74ccdd6db`

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
