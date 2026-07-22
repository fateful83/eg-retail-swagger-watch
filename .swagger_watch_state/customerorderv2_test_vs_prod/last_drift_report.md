# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-22T01:14:47Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e0dfdf12223f9383188c8ab0f36a7f56f79be7ad9ccaa9c654c10554fcab567e`
- PROD hash: `6bcc0946c71fb7652e433f0f20c35744c3c4af862711977dec32088c4ca83369`

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
