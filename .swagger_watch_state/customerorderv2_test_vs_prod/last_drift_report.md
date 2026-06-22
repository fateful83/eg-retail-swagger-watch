# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-22T16:20:54Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f2a86f1524cad52936be9ea9999460d382ed4cbf32e27a0b14055bd26e95942e`
- PROD hash: `850b54f16fda4f573d53ef2b00c95a8ea5b8036cca6ae6339f4e4c6702a1cbf2`

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
