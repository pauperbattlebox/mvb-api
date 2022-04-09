# Multiverse Bridge API
The Multiverse Bridge is a Cardsphere community-built project aimed to help translate Cardsphere card and set data to other platforms.

The project leverages existing tools MTGJSON and Scryfall to provide the data to enable consumers to translate their Cardsphere collection data to another platform that supports MTGJSON or Scryfall identifiers.

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/pauperbattlebox/mvb-api)

## Base URL
/api/v1

## APIs

<details>
  <summary>GET /cache</summary>
  
  Returns information about the current state of the cache. Card and pricing data is cached and refreshed once per day. 
  
  ```
  {
    "last_updated": "2022-01-22 12:34"
  }
  ```
</details>

<details>
  <summary>GET /cards</summary>
  
  Returns the IDs for all cards in the database as well as the current state of the cache.
  
  ```
  {
    "last_updated": "2022-01-22 12:34",
    "cards": [
      {
        "cs_id": 1,
        "mtgjson_id": 1,
        "scryfall_id": 1
      },
      ...
    ]
  }
  ```
</details>

<details>
  <summary>GET /cards/cs/{cs_id}</summary>

  Returns the Cardsphere card details specified by the cs_id.

  `includeRelatedPrintings` (bool, optional) - Query parameter to include the other printings of the specified card.

  ```
  {
    "cs_id": 1,
    "url": "/cards/1",
    "name": "Abundance",
    "edition": "10th Edition",
    "is_foil": true,
    "mtgjson_id": "1669af17-d287-5094-b005-4b143441442f",
    "scryfall_id": "46184f97-d5c9-4a98-9fd9-e19057ce9b7e",
    "collector_number": "249",
    "mtgjson_code": "10E",
    "prices": {
      "price": 120.9,
      "updated": "2022-01-17 02:05"
    },
    "related_printings": [
      {
        "cs_id": 2,
        "url": "/cards/2",
        "name": "Abundance",
        "edition": "10th Edition",
        "is_foil": false,
        "mtgjson_id": "1669af17-d287-5094-b005-4b143441442f",
        "scryfall_id": "46184f97-d5c9-4a98-9fd9-e19057ce9b7e",
        "collector_number": "249",
        "mtgjson_code": "10E",
        "prices": {
          "price": 5.53,
          "updated": "2022-01-17 02:05"
        }
      },
      {
        "cs_id": 50776,
        "url": "/cards/50776",
        "name": "Abundance",
        "edition": "Commander 2017",
        "is_foil": false,
        "mtgjson_id": "7e89befa-00f2-5326-a98d-70c5a54f0bea",
        "scryfall_id": "7f3fff7e-f34d-4a99-a805-bd66c4e9f0cb",
        "collector_number": "145",
        "mtgjson_code": "C17",
        "prices": {
          "price": 3.07,
          "updated": "2022-01-17 02:05"
        }
      },
      ...
    ]
  }
  ```
</details>

<details>
  <summary>GET /cards/mtgjson/{mtgjson_id}</summary>

  Returns the Cardsphere card details specified by the MTGJSON Id.

  ```
  {
    "cs_id": 2,
    "url": "/cards/2",
    "name": "Abundance",
    "edition": "10th Edition",
    "is_foil": false,
    "mtgjson_id": "1669af17-d287-5094-b005-4b143441442f",
    "scryfall_id": "46184f97-d5c9-4a98-9fd9-e19057ce9b7e",
    "collector_number": "249",
    "mtgjson_code": "10E",
    "prices": {
      "price": 5.53,
      "updated": "2022-01-17 02:05"
    }
  }
  ```
</details>

<details>
  <summary>GET /cards/scryfall/{scryfall_id}</summary>

  Returns the Cardsphere card details specified by the Scryfall Id.

  ```
  {
    "cs_id": 2,
    "url": "/cards/2",
    "name": "Abundance",
    "edition": "10th Edition",
    "is_foil": false,
    "mtgjson_id": "1669af17-d287-5094-b005-4b143441442f",
    "scryfall_id": "46184f97-d5c9-4a98-9fd9-e19057ce9b7e",
    "collector_number": "249",
    "mtgjson_code": "10E",
    "prices": {
      "price": 5.53,
      "updated": "2022-01-17 02:05"
    }
  }
  ```
</details>

<details>
  <summary>GET /cards/search</summary>

  Returns the Cardsphere card details of the cards that best match the provided query parameters.

  `name` (string, optional) - Query parameter to include search by card name. Allows partial matching.  
  `edition` (string, optional) - Query parameter to include search by card edition. Exact matching only.  
  `is_foil` (bool, optional) - Query parameter to include search by foil indicator. If true, only foil and etched foil results will be returned. If false, only nonfoil results will be returned. All finishes will be returned if the parameter is not provided.  
  `mtgjson_code` (string, optional) - Query parameter to include search by MTGJSON set code. Exact matching only.  
  `collector_number` (integer, optional) - Query parameter to include search by card collector number. Exact matching only.  

  At least one search query parameter must be provided.

  ```
  [
    {
      "cs_id": 75322,
      "url": "/cards/75322",
      "name": "Leyline of the Void",
      "edition": "Time Spiral Remastered",
      "is_foil": false,
      "mtgjson_id": "677a6e71-3038-5419-8503-dd2a58231cf4",
      "scryfall_id": "186eea73-46c5-4532-ac94-326db7d6f0cb",
      "collector_number": "326",
      "mtgjson_code": "TSR",
      "prices": {
        "price": 7.99,
        "updated": "2022-01-17 02:05"
      }
    },
    {
      "cs_id": 61482,
      "url": "/cards/61482",
      "name": "Leyline of Abundance",
      "edition": "Core 2020 - Promo Pack",
      "is_foil": false,
      "mtgjson_id": "5cb79b3b-cf8f-5485-84a9-7261a82c0e0b",
      "scryfall_id": "35ceac21-f2c6-4f48-8bf3-04a005ade645",
      "collector_number": "179p",
      "mtgjson_code": "PM20",
      "prices": {
        "price": 2.88,
        "updated": "2022-01-17 02:05"
      }
    },
    ...
  ]
  ```
</details>

<details>
  <summary>GET /sets</summary>

  Returns a list of all Cardsphere sets including that set's MTGJSON equivalent code value.

  ```
  [
    {
      "cs_id": 755,
      "cs_name": "10th Edition",
      "mtgjson_code": "10E"
    },
    {
      "cs_id": 756,
      "cs_name": "4th Edition",
      "mtgjson_code": "4ED"
    },
    ...
  ]
  ```
</details>

<details>
  <summary>GET /sets/cs/{cs_id}</summary>

  Returns the Cardsphere set specified by the cs_id and a list of the cards in the set.

  ```
  {
    "cs_id": 1290,
    "cs_name": "Zendikar Rising - Extended Art",
    "mtgjson_code": "ZNR",
    "related_mtgjson_codes": [
      {
        "mtgjson_code": "ZNC"
      }
    ],
    "cards": [
      {
        "cs_id": 71318,
        "url": "/cards/71318",
        "name": "Agadeem's Awakening // Agadeem, the Undercrypt",
        "edition": "Zendikar Rising - Extended Art",
        "is_foil": false,
        "mtgjson_id": "3e7731e8-ca30-50af-a6cb-a7ef60b3c137",
        "scryfall_id": "499c2b20-e83e-40ff-919e-1d134ad50c0a",
        "collector_number": "336",
        "mtgjson_code": "ZNR",
        "prices": {
            "price": 18.97,
            "updated": "2022-01-17 02:12"
        }
      },
    ...
    ]
  }
  ```
</details>

<details>
  <summary>GET /sets/mtgjson/{mtgjson_code}</summary>

  Returns the Cardsphere set specified by the MTGJSON set code and a list of the cards in the set.

  ```
  {
    "cs_id": 755,
    "cs_name": "10th Edition",
    "mtgjson_code": "10E",
    "cards": [
      {
        "cs_id": 2,
        "url": "/cards/2",
        "name": "Abundance",
        "edition": "10th Edition",
        "is_foil": false,
        "mtgjson_id": "1669af17-d287-5094-b005-4b143441442f",
        "scryfall_id": "46184f97-d5c9-4a98-9fd9-e19057ce9b7e",
        "collector_number": "249",
        "mtgjson_code": "10E",
        "prices": {
          "price": 5.53,
          "updated": "2022-01-17 02:12"
        }
      },
    ...
    ]
  }
  ```
</details>
