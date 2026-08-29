# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-29T20:03:09Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6e6d8d939fea0a0dd0670278ef5c6e600290dc84b8d0a5c32424e1577fb1ac48`
- PROD hash: `152e8f854a844061355dbd0b0aef3fbffc946d76357a0858bc7a94a2627491e9`

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
