# TEST vs PROD drift detected: POS API

- Time: 2026-06-02T09:54:54Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b23b17a5e27052594544a8c8fd96b3f7511a0766361c7c723e7fc2c6c736d521`
- PROD hash: `4bbb4bc33683092902698364c713082a6c1181df758a342e32980e7893b0b5ef`

## Summary
- Only in TEST: 2
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- POST /api/Payment/BeginKlarnaPayment
- POST /api/Payment/EndKlarnaPayment

## Only in PROD
- None

## Different in TEST and PROD
- None
