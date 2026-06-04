# TEST vs PROD drift detected: POS API

- Time: 2026-06-04T19:50:43Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `bbb83f670f43c860957814495e28c333856b704f9ea307608e5287a4925754cd`
- PROD hash: `083625f1ed7c673759ec6244077311a793d475e08122ec56e8557b140dbffd69`

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
