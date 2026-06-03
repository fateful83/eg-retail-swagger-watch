# DEV vs TEST drift detected: POS API

- Time: 2026-06-03T10:26:40Z
- Severity: breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `6784fc4f306d60ec2227ab934ef20dcf50adb5230a6405274000de2825578d40`
- TEST hash: `d46656561c7d4cbe58c9fd9aff43ceda52b1f558c2b1fed4043dd4603cb05b37`

## Summary
- Only in DEV: 0
- Only in TEST: 2
- Present in both but different: 0

## Only in DEV
- None

## Only in TEST
- POST /api/Payment/BeginKlarnaPayment
- POST /api/Payment/EndKlarnaPayment

## Different in DEV and TEST
- None
