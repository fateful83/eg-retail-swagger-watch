# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-19T11:20:17Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ddfa6201b6bf372db19980cb85dc60bb57384fee164023063b487fab81e5feae`
- PROD hash: `7d60da241ae7b2c39915f28ce4596211569546da3e27a35bd2873ccde9026027`

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
