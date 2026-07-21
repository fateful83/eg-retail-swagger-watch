# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-21T01:14:27Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b89c9f340edbd6539a8360712e3150709e2f9585287f6f61463b0fd780026796`
- PROD hash: `c1bbfedf71d6f10668fd38deaf03db94965a7d07d37e0810b3cd2607928a1690`

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
