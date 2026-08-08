# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-08T06:28:10Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d828bdd59e75bab168e354520aeceab900aac5a44b8afe31b2f7ee4f4fc4e535`
- PROD hash: `fbd49d0e9729301db1c8cecd2f34d96a4dc8ac156b1b234727dff4035aa05298`

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
