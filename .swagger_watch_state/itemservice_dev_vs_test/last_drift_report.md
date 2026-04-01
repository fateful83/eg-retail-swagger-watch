# DEV vs TEST drift detected: ItemService

- Time: 2026-04-01T12:45:41Z
- Severity: breaking
- DEV Swagger URL: https://itemservice.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://itemservice.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `535f35de4d7e6bbf770d58899926334488040affb37091390f2fc678f814b74f`
- TEST hash: `50bc90a5bcd1e2238d8b115b09ce00d8a4e249775434ae69c64db30c1316987f`

## Summary
- Only in DEV: 0
- Only in TEST: 0
- Present in both but different: 42

## Only in DEV
- None

## Only in TEST
- None

## Different in DEV and TEST
- GET /api/Brands
- GET /api/Brands/{id}
- GET /api/Collections
- GET /api/Collections/{id}
- GET /api/ItemCategories
- GET /api/ItemCategories/{id}
- GET /api/ItemLists
- GET /api/MarketingCodes
- GET /api/MarketingCodes/{id}
- GET /api/MarketingExclusivities
- GET /api/MarketingExclusivities/{id}
- GET /api/NonsaleType
- GET /api/Nutritions
- GET /api/ProcurementRules
- GET /api/ProcurementRules/{id}
- GET /api/ReplenishmentCodes
- GET /api/ReplenishmentCodes/{id}
- GET /api/Sizes
- GET /api/Sizes/{id}
- POST /api/Brands
- POST /api/Collections
- POST /api/Colors/upsertByName
- POST /api/ItemCategories
- POST /api/ItemLists
- POST /api/MarketingCodes
- POST /api/MarketingExclusivities
- POST /api/NonsaleType
- POST /api/ProcurementRules
- POST /api/ReplenishmentCodes
- POST /api/Sizes
- POST /api/TradingUnits
- PUT /api/Brands/{id}
- PUT /api/Collections/{id}
- PUT /api/ItemCategories/{id}
- PUT /api/ItemLists/{id}
- PUT /api/MarketingCodes/{id}
- PUT /api/MarketingExclusivities/{id}
- PUT /api/NonsaleType/{id}
- PUT /api/ProcurementRules/{id}
- PUT /api/ReplenishmentCodes/{id}
- PUT /api/Sizes/{id}
- PUT /api/TradingUnits/{id}
