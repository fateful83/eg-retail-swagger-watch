# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-21T00:28:51Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `565b61bbc280d5bf87d5dc08aab8abfdc811a467bf3449ddd0abd03ac5d829e0`
- PROD hash: `af6711d87e132edb6d2b78f3b47013afe967848c343b9ef9f0e0b45557489efc`

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
