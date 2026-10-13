# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-13T04:01:22Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `5313a86f39a874d49e19b3e081bd18d389a36c0b0f84ed66a91f3be164b809cc`
- PROD hash: `283cbc1dbfe25a77d172c6b7ed85a5e665a4c7c17115de5ce78b771e0dfd8815`

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
