# TEST vs PROD drift detected: POS API

- Time: 2026-06-08T02:08:31Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `dab002b54a915a065f612688be2cd607e284f3844568dd67b34f7de0cacd676d`
- PROD hash: `e8e55e206fe73377c363f0eddf8faa94e06bc04394ee4eb75ca620668f46ac2e`

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
