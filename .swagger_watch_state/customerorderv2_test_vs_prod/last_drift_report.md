# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-25T02:00:27Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `fa1bdff24d41022d93f99c3b0918680cfb27fc7466ec6d1f9380cd9d1f4075c2`
- PROD hash: `ec7d52ce3ad2ca9c33942ed00f56ce1bea7726e42c5377aff3a4f20eeef6d8e7`

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
