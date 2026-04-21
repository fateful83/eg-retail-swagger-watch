# TEST vs PROD drift detected: POS API

- Time: 2026-04-21T12:52:51Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ed7f63b4fb435fd3db023b393aa922b66eda138192e3b34a4f30c2fbbaa6edb9`
- PROD hash: `5614e35f8e5f5a2b09f48558840da56d500485fc53eba5513f872f389ea9d8cb`

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
