# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-28T09:37:39Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `39b742eea5c5895b49ed134cfea61397ee474939149479c43af504fa2b90fc3e`
- PROD hash: `bc4b88af6021de1f6cb34bb58aa37ad0cabef4d39e547a42bc9a5b1e874047cb`

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
