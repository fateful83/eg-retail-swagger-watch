# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-31T18:57:26Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7deaffad24e055154bd39d0a4a8e9149ec9733b822c5ad0268add1f8eed71b38`
- PROD hash: `30aa0bb01555af2e67c3c575f8be0014c8aaadfde3a591e810e880d0a79d275f`

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
