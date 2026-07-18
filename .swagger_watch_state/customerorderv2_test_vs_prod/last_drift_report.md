# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-18T18:40:41Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `5eb00365ce02f39734bea029aa0464e71896d7e2607f389e7acea65bdc87ac77`
- PROD hash: `5ad36d1bf2bca229c12df069d2363a5655111209166874a12b15c8a33fa0b609`

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
