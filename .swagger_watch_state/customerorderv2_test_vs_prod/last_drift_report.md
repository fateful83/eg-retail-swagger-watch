# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-11-02T02:51:02Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b06eef26f42e3df18095dc3df560186f02250d25d28bea2a46ce1043e09a6c13`
- PROD hash: `8a5673da04ebb70c9ab3169a6f35e22cea53ee59d6e3164f35c7296211b5a88c`

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
