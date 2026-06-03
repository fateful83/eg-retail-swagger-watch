# TEST vs PROD drift detected: POS API

- Time: 2026-06-03T10:26:40Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d46656561c7d4cbe58c9fd9aff43ceda52b1f558c2b1fed4043dd4603cb05b37`
- PROD hash: `6c5a9b3a84358b3e5d9553540f83a9b24ff93ccac4786df5a87e0fd307544718`

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
