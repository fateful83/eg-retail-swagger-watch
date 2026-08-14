# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-14T12:32:51Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `af18873f79f1ec8feb596b15735c2b955427d750d382c779e55453542da5aa14`
- PROD hash: `ebe0ddba26218ad10679744e219b53b5f77b23d1de14dffcd30b4c6cb3221e1a`

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
