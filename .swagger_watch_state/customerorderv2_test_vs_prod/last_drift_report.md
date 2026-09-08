# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-08T20:21:46Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `debaafdc36322b3da5763e3259866d0c3e9fb28cb4e7532c648d00aafe048b16`
- PROD hash: `a72b953422c2921551e6ec38e2aa79e03854bf742ab0ea3cbc635610a8ba2e7a`

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
