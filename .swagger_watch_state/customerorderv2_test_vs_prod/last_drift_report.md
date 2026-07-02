# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-02T13:22:59Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6ddc86d9dbe436969e8e00d7a4f32e2e34e0e665e655f370dab53637346613b8`
- PROD hash: `6e46d900f3f544b6c47e28e0fdce08bea55f44b850be4ebf26a06596fdc8c093`

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
