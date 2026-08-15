# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-15T00:26:54Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8f46bdf44adf15186ae5d022ef404657d3ecee85a5e479716adff01b9275e556`
- PROD hash: `1f33b678fe9375cfd959bb1a4b1c08f59e461fae2ddb61946669eddf76b5c11d`

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
