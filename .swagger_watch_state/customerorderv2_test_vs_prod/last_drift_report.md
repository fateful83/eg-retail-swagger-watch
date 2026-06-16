# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-16T16:15:44Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2d7bd680bda22721eb005377716c929f5e554a22dee32600be00605fe127dabd`
- PROD hash: `b8046092e33863fce66a57fb5f13a52561f65cd42cc6cbdc62136c3154e82331`

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
