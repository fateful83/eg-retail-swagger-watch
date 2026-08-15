# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-15T06:15:24Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d1260ece30c052b8144951efac043238e7bce0285d20d87183b9d1dc19b975a7`
- PROD hash: `906d06b2726d93a2f209eb3edafa5ef5f4b57127d6952ae9a0beb8a32419828d`

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
