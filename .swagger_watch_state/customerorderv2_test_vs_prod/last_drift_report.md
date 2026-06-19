# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-19T19:19:54Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d717a9e72899d004d7680a877924fa11b630d023eafffdcb474e21eb5fafa80d`
- PROD hash: `3db886a1e9c5af7188972d699dbbf70c6accff06060c6336fc020a17aab8fa12`

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
