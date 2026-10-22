# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-22T02:01:03Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `cd7d4b75fbb4186bcc9bb0a1373cb07b8a542ab739d0703872c9c430505ac3f0`
- PROD hash: `ea3135e7ff5e1168f43069aa745e1eeab72af3e2aba325a82de23d50ca330765`

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
