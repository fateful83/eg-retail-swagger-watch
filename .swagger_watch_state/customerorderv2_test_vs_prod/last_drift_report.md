# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-27T11:07:20Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `fcafb8792897613c62623d060522c1db7c406c7d399d9b2e181bc8e6b916c3b2`
- PROD hash: `23cff8ec14db943d73f974264ffaa3b2fd0c696b807f6c306d710cd138c7dc2f`

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
