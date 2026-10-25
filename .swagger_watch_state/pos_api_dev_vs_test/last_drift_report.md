# DEV vs TEST drift detected: POS API

- Time: 2026-10-25T20:03:25Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `6dd5e05541fbe30dc60baadf6774ed21046d7e3d122886936a9458c8c9995cdf`
- TEST hash: `f79bd2cd19d17fb00355ad1d12f5b2b97f2fc4df4210a0def8e400b4ce4d10d8`

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
