# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-25T01:57:15Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e0e3cee1fa7ad2418b95934384d2b90f2d59f4fd764b41a927b2d4244c87b768`
- PROD hash: `24fe736e5ab23d61868bf27f59938cd4e0274b93b3eb928355034624662de524`

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
