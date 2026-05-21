# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-21T14:31:27Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `54c3ca94225ee58fde6b9710a9111068cecdc85d947ecc56af3c72855784d398`
- PROD hash: `0ef828fa10f99f32308af96329bb45d19dada2f5baca00faf0897011bde5e80e`

## Summary
- Only in TEST: 1
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- GET /api/gateway/ServiceOrders/{storeNumber}

## Only in PROD
- None

## Different in TEST and PROD
- None
