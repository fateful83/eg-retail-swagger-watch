# TEST vs PROD drift detected: POS API

- Time: 2026-06-04T14:24:04Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `359e5fea50f8b1ff286afabf64fe2c13ce0846e1be9b690f8715648b5c86c7a3`
- PROD hash: `4a7d05fcc32a36861feb91d3971790143ebdfbbfd1f96835f4c45102bad0962d`

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
