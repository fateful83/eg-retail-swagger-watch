# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-22T06:16:33Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b8c2dc29bda7a576c76886a5c8c0db7f88bd5924360d2a7636922c2b28c6152a`
- PROD hash: `3c44c9411b4b357a36f6596ff8355f2a0fd9eb03a91191a8a3b7cb47d2ae483a`

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
