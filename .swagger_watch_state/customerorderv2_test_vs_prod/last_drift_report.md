# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-23T14:12:22Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6e02410cef967840b516ed982aa61f63e916c008f6375286414a040a601309f3`
- PROD hash: `5b88633a734bceccfb021c18c147e04f5361ff1bd213e0f4d3c3e5c5020a2576`

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
