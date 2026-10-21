# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-21T02:07:07Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `5c0a68e44c16ba6983f033060fcc3b1c26ba1813405236ee1a98fe0224952b82`
- PROD hash: `4b99b04ae65bf0a527b1b17e597f61987bcf1960e958a17b356c78754578e5e9`

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
