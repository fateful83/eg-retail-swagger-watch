# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-12T18:42:44Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6e0dfdb246f3a00bdfe4343a241f160e2d86c0aad7e444910d1dc67ad8abb716`
- PROD hash: `125f6cea40551f4bceec031d2323627b280f00420dd19af6ded93c7d7f1bea06`

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
