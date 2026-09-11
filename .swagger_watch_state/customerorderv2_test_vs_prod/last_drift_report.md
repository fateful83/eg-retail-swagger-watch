# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-11T20:07:35Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a306fe5091d0bd10201559568ad7d4444a84410792c6611c820eaf8cdec11401`
- PROD hash: `ddd818dfa7fe8be67c1d17cbc0bb64721cc02c7918df22485b5f75ab6e620025`

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
