# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-26T01:49:22Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `91f643ce0c260f9ac0ef08d421b0571cb4f74944c29caaf2d6d42656b5171449`
- PROD hash: `4dbe71ad676bc927c5f11fcef8aeea10f3744a2553fea2f09538e38c7f3a1e8b`

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
