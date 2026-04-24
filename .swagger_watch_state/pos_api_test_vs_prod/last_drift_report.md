# TEST vs PROD drift detected: POS API

- Time: 2026-04-24T01:16:19Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `11b4da72048fe0ca2bf2a7572785ffd857357a0034455378054794fb3d4e8078`
- PROD hash: `27eff174d398a02fd11f906c7b57eba877d056867d7b40bb7727a8029fc28dca`

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
