# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-25T07:46:04Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `afe5dcd39e292f7f55c3d3d71cd5543dde459c98ae9669037c80160cb33b0f87`
- PROD hash: `8ea9962936f36e4faf104d58d927736ef18f3c70160e078a41f0ab0c0ff6dee9`

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
