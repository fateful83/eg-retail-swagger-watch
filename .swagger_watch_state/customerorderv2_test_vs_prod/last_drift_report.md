# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-11T18:41:54Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8c5c23440bcf5300efbff3c628979e03aa2040d4bece4896fb34da6135c236e7`
- PROD hash: `ddc4e3951ea935b55d19e991a9742b59d70abe99f19f80ac7e477d843d45ee4a`

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
