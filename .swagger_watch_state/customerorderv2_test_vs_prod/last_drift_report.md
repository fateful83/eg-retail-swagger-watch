# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-08T13:20:10Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `cb2821cd54c17dc94557ed98e77a647df1cd03a60225f477a5326876db0885a8`
- PROD hash: `c73b8bf7edefeeaa0f93befa1c5e071d8e5fc8502ac80887b26f7b08ba94887b`

## Summary
- Only in TEST: 1
- Only in PROD: 0
- Present in both but different: 1

## Only in TEST
- PATCH /api/gateway/ServiceOrders/{orderNumber}/orderStatus

## Only in PROD
- None

## Different in TEST and PROD
- POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment
