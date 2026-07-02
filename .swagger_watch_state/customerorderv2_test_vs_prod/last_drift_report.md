# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-02T19:03:29Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a4aea0a50d943b39555572476fc9463d5a7a0a5c92795a9a8dcc0362dadc9f43`
- PROD hash: `a1dd7a42fca12177446d0af2c9894e4b9b3708b55609607da163299582647934`

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
