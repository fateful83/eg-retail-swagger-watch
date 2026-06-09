# TEST vs PROD drift detected: POS API

- Time: 2026-06-09T08:53:38Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `14b13f80fc33db093c552944d2cb909175216e788655bacb79a27a92d52d606f`
- PROD hash: `bb6003eb378f8849ddac87872af8105375156c4108ded5df2bb2462187df607c`

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
