# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-18T01:40:22Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `488c81d2971b2c10daa18a6bf260337490d5860c69fd4ba2058eb08244f60e39`
- PROD hash: `31113c5b63086df762d111eebcb909cb76e35536c3126eecf94134c2e50cf143`

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
