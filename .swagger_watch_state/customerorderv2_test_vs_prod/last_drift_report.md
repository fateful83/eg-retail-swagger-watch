# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-24T01:50:55Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `625581cf47bdd707d63a5930bbb34d04dd60ee818010dd4bc76a93174027f656`
- PROD hash: `753f327553f4a93e9606b2382d3e038819f3121591d3b61ce8a9783e95ca7fe1`

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
