# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-12T19:47:40Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `af0d4fb8f6d03a909c920a670ba507d4cad452b00d5d178cd1e15560892d8ee0`
- PROD hash: `bbca3868b8d0e0378562079d88996feeef571ebad14f6a8329a869584a8f36e1`

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
