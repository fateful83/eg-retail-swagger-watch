# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-12T07:51:58Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0e2e257247181799c308bbe0ef7516d4492cfa6188e9549380b27e0c4bce670c`
- PROD hash: `00b6bd7487dce96b73e1ee2b5620777f429b4ebe771cf52c95f3f0ca3992bd20`

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
