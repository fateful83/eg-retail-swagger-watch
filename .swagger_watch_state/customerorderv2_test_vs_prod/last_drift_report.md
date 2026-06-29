# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-29T15:22:04Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6d08dba226b2accf789f34d3262513c4e229cd4e3318cbab515bdc1377073c7c`
- PROD hash: `0890f720597558c590f42cc3c82a4e11d4eb741130dcfb8f8dd8ace9292a89b1`

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
