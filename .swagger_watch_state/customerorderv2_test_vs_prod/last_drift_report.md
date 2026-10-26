# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-26T21:57:21Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `16dae2a1aed1f30bcd87ed60ac0ffbecf6683bdbf5dc8a90d339e3f9d5330d31`
- PROD hash: `314182a61c69a53b0b78c4dd6292d637106f22cb7c28598986f7928a55ebdb97`

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
