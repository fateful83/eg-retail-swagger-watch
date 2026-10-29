# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-29T22:03:58Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f57b218998ed8759311a80f56bf63ba50e2d7cc769a2dc7d1d5134ac835e14ea`
- PROD hash: `2004d63df454965943a269debf6295d4eff201c1859ea9213e1b00628b7f5f87`

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
