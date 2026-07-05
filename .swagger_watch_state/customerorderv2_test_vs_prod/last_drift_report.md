# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-05T08:34:19Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `995bfebae0db8dd608fad76a60b46f79aa55d3a13261b86ed4ad9ef3a0d2e4dd`
- PROD hash: `98a2d6b958ec043ee9870a388ed32dd368b17130dfb57794a36e1d50607bb34f`

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
