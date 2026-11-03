# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-11-03T00:05:42Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b35b50210cf1039134bf8a35becef8d522fc5bb02ab5aeff326bd008f36e9c80`
- PROD hash: `1ca101a633729dc38ddf650ce52b6cc138a91661e7e777ce15c0929bc711b952`

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
