# TEST vs PROD drift detected: POS API

- Time: 2026-04-23T18:50:13Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `41f73fb0e8cba40b73887d7150e731624b2892baa490499fe41f760e73016b1e`
- PROD hash: `b2fb9ec4d54f3f1816b978b33d5ebc6509df0e9739d422f33783279169ababfa`

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
