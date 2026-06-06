# DEV vs TEST drift detected: ItemService

- Time: 2026-06-06T13:00:07Z
- Severity: breaking
- DEV Swagger URL: https://itemservice.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://itemservice.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `995ece27122a64af32ec2f8c256acb3cbf0fcbba47e02e917a12b162d0d9eb9a`
- TEST hash: `fec3fda5a7b555ad347d8adc9f61f8fba2b22451479557858867f77846784c5d`

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
