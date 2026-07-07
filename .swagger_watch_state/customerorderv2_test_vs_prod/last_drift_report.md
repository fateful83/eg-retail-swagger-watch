# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-07T13:57:59Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `259d3b24d3cf8f5192389d93d22cb64d8ada51226df064c5adc6b7f7c130fbc5`
- PROD hash: `0e1d7b1d22e32108f8665f302407ff68f7a4b475ff1b3b98f993e3fa7acafdae`

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
