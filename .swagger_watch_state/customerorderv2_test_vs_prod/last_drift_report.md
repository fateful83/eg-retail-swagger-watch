# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-26T17:41:35Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6807b979dd3c27d6a97536b2419be797baea619807f7eef496e1c20e6a8e5d77`
- PROD hash: `5d18510948d8014c74099097ec400bcebaedbb676da9b7ba35a13235bd0f1ecd`

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
