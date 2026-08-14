# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-14T18:37:02Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `765db61cd5bdc11030b570912570eed7751be6b76436753338b5364e3881971d`
- PROD hash: `5ab9c54a3cb754086b2a3898c2d98a776c4528e5529783ae124a1eff1f5f33ce`

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
