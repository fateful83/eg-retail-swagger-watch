# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-16T18:09:24Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e551cc3d411d473ddd486d8c9a4949806318955107f3c4a5b7a2a187780efef1`
- PROD hash: `e1dfe396380d3775a914143098960bcd49ce70de271a56adc15c65819106ab79`

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
