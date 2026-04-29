# TEST vs PROD drift detected: POS API

- Time: 2026-04-29T19:03:00Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `babe253e64a875cdca1561b46f91ca61479431b258bc5caf8c520687c031cacf`
- PROD hash: `7d153cd03b1e5a9d9f1704fe385faa1daa5887f38171a01422f1eda802a61f09`

## Summary
- Only in TEST: 1
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- POST /api/Payment/AddBonusPaymentToCart

## Only in PROD
- None

## Different in TEST and PROD
- None
