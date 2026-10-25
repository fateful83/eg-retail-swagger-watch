# DEV vs TEST drift detected: POS API

- Time: 2026-10-25T15:06:13Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `84a43dd961c7a8a39d4e1b371584084ecc91cae79ae66fe1e1a18107159e84a4`
- TEST hash: `c8fae534e99aabf6823c454346240b8533a0631c0af408be47b106c3e5611bf1`

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
