# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-26T06:23:00Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1aab31bc737a893c5dc03a53af1cb43521477d892fe71c63db0f3409c3e94889`
- PROD hash: `ad6bd51893eedacf1827ec0671f3d0f3b0806c1c5ec7127a7a872842c56c8e35`

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
