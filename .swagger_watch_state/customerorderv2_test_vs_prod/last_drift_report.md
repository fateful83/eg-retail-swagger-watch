# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-25T00:27:04Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1e262cf1620a1985eab5c3998fb02f53e9a3b0d13912cd338bcb60e6e27a1596`
- PROD hash: `4aabbab8c7301cba1f6be4d7d96c66945b662756c6b223bf27358abb0d91017a`

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
