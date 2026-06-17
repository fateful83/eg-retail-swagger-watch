# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-17T19:53:07Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `96945f7501cce6b948a58b2584525a999e1fbf95978ea5bdc62edeb8f9cb7ac6`
- PROD hash: `94121773de4d48c7086e2cab607c1c56c6028b1a0bd52364371503e4209fe937`

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
