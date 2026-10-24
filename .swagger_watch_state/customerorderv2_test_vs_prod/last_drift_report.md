# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-24T09:52:37Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `568453fe6e4411631f9e12a4189253183e05c4837bb1fb71f7bf658289315423`
- PROD hash: `6c37f53499511c18cff328c8be1b17c7f9852e8b976f0fffd3db1ec4da095868`

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
