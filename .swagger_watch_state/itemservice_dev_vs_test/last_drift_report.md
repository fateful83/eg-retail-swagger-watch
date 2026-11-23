# DEV vs TEST drift detected: ItemService

- Time: 2026-11-23T16:34:23Z
- Severity: breaking
- DEV Swagger URL: https://itemservice.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://itemservice.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `a9f195a304c758af5eab00fc12ec707696b8c9f1721ee2174ab1aeec76f18ffd`
- TEST hash: `63c266c9d9a6bdf40c95ba1c0416918b916cd49a122f73c1d8273f4aaf19a2ca`

## Summary
- Only in DEV: 0
- Only in TEST: 0
- Present in both but different: 30

## Only in DEV
- None

## Only in TEST
- None

## Different in DEV and TEST
- GET /api/Brands
- GET /api/Brands/{id}
- GET /api/ItemCategories
- GET /api/ItemCategories/{id}
- GET /api/ItemLists
- GET /api/NonsaleType
- GET /api/Nutritions
- GET /api/ProcurementRules
- GET /api/ProcurementRules/{id}
- GET /api/ReplenishmentCodes
- GET /api/ReplenishmentCodes/{id}
- GET /api/Sizes
- GET /api/Sizes/{id}
- POST /api/Brands
- POST /api/Colors/upsertByName
- POST /api/ItemCategories
- POST /api/ItemLists
- POST /api/NonsaleType
- POST /api/ProcurementRules
- POST /api/ReplenishmentCodes
- POST /api/Sizes
- POST /api/TradingUnits
- PUT /api/Brands/{id}
- PUT /api/ItemCategories/{id}
- PUT /api/ItemLists/{id}
- PUT /api/NonsaleType/{id}
- PUT /api/ProcurementRules/{id}
- PUT /api/ReplenishmentCodes/{id}
- PUT /api/Sizes/{id}
- PUT /api/TradingUnits/{id}
