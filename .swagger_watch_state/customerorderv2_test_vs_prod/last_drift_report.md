# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-20T01:57:33Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6bd015b41aaa697bbe869ebcd13120888113e9603a9a2cb08ef879f51ef87300`
- PROD hash: `dfd18d462f87f2959f05c970057b2fa52fb4e1fac6202ffde46e710ad2c608bd`

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
