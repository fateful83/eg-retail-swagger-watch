# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-25T15:06:12Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0d7a7f37969f05970f72357ef49b9d587f9249823fd50f9f759a4cd079c1e871`
- PROD hash: `256d2dcf358e666a77b76091e37703baaa752143d1344ab7728220d299c8f3e8`

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
