# TEST vs PROD drift detected: POS API

- Time: 2026-04-29T01:28:26Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c1738caf3b1c4027cecedd39fd382261cd5d4deca32da2c048d5f731de6274ee`
- PROD hash: `e2d6d61b5045ce37e48a31bbbdbbbc1fc89dced3c90bb6b0ac184bd8d2cb4ebf`

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
