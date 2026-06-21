# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-21T13:28:21Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ec52cfbf9f6f0481b44fb4bf77759b7a13e975cd6a9e1daa2bfe45add77856af`
- PROD hash: `1643b0313d70ad6adcf511f25ac5dff2708235f38bf23958d46d5f46d98835c3`

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
