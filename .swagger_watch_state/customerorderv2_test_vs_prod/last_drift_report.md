# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-25T19:41:38Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `fbb02ffad4c0c63e0f7b7b2102c23cf8f30c95d3bb180873f5c7fa7c1e2f3f9c`
- PROD hash: `ec53d239dd039e696e0b88eba92bed3e8a20f021ddafeba6fddf89323189092d`

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
