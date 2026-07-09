# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-09T14:20:20Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f6ef1597e335b3c2af8ca02c75f0d1a227d4d673a3210a80aa7fc64a069eaf81`
- PROD hash: `26e4d9f6b6bbb1ac540ab886bc0813733e0579f30a561ff9c50e9155d984f847`

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
