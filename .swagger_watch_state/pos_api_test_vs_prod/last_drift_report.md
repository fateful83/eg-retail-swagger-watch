# TEST vs PROD drift detected: POS API

- Time: 2026-06-08T15:19:42Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ca3fa3d38e3d4fad036aef15ec35366ad548307342cacea5f0965063f7a2546b`
- PROD hash: `12d08c69b085b4c7df8284a3e258892738a69f6806fbe57281a12359e45cf087`

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
