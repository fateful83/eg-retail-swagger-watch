# DEV vs TEST drift detected: POS API

- Time: 2026-10-26T01:53:20Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `6d07a1dc6412ecaaf350f0cff42cefaf6323d72a37e651279d9c60576b6ceb88`
- TEST hash: `c486ec0808724d96fecc845329ad06fc46b97519e614f40adcb9497eb9faf9a9`

## Summary
- Only in DEV: 3
- Only in TEST: 0
- Present in both but different: 0

## Only in DEV
- GET /api/UserService/PingHealth
- POST /api/UserService/Authenticate
- POST /api/UserService/CheckUserExists

## Only in TEST
- None

## Different in DEV and TEST
- None
