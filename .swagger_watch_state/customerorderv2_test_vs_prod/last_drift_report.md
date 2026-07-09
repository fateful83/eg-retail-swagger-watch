# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-09T01:23:53Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `5db0eafe9511899ed09515c5c39f10e037796fdb3af4111dfa9421e33ad903e7`
- PROD hash: `01615aee2859b0d3c4cd4b675f4f23f05856da835511537923a872cfe4704e40`

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
