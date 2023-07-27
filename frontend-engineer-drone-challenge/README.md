# Frontend Engineer Drone Challenge

## Intro


At regular recurring intervals, engineers at Axpo inspects their assets (power plants, substations, etc.) with drones to detect possible defects.

In the forefront of a flight, they must check whether drone restrictions apply to the area around the asset. Moreover, the population density at the location must be found out, as this affects the beyond visual line of sight drone operation.

To do that, we decided to engage you to develop a tool that will provide this information in an easy-to-use web application to the engineer.

**Please invest no more than 5 to 8 hours.**
If you cannot complete the task in this time frame, document where you got stuck, so we can use this as a basis for
discussion for your next interview.

## Your mission, should you choose to accept it:

### Initial position

* Data dump of assets with description and geocoordinates (located in this repo)
* Public API endpoints which return drone restriction and population density, respectively, for a given geocoordinate.
  * Population Density: ```GET https://api3.geo.admin.ch/rest/services/api/MapServer/identify?layers=all:ch.bfs.volkszaehlung-bevoelkerungsstatistik_einwohner&geometryType=esriGeometryPoint&sr=4326&lang=en&returnGeometry=false&tolerance=0&geometry={"x": <longitude>, "y": <latitude>}```
  * Drone Restriction: ```GET https://api3.geo.admin.ch/rest/services/api/MapServer/identify?layers=all:ch.bazl.einschraenkungen-drohnen&geometryType=esriGeometryPoint&sr=4326&lang=en&returnGeometry=false&tolerance=0&geometry={"x": <longitude>,"y": <latitude>}```

<details>
  <summary>Example request</summary>
  
  ### Request
  ```
 GET https://api3.geo.admin.ch/rest/services/api/MapServer/identify?layers=all:ch.bazl.einschraenkungen-drohnen&geometryType=esriGeometryPoint&sr=4326&lang=en&returnGeometry=false&tolerance=0&geometry={"x": 8.56383,"y": 47.45539}
  ```
  
  ### Response
  ```
{
	"results": [{
		"layerBodId": "ch.bazl.einschraenkungen-drohnen",
		"layerName": "Restrictions for drones",
		"featureId": 112667,
		"id": 112667,
		"attributes": {
			"zone_name_de": "LSZH Z\u00fcrich",
			"zone_name_fr": "LSZH Z\u00fcrich",
			"zone_name_it": "LSZH Z\u00fcrich",
			"zone_name_en": "LSZH Z\u00fcrich",
			"zone_restriction_id": "REQ_AUTHORISATION.MTOM_FROM",
			"zone_reason_id": "AIR_TRAFFIC",
			"zone_restriction_de": "Der Betrieb von unbemannten Luftfahrzeugen mit einem Gewicht von mehr als 250 g ist verboten.",
			"zone_restriction_fr": "L'exploitation d'a\u00e9ronefs sans occupants d'un poids sup\u00e9rieur \u00e0 250 g est interdite.",
			"zone_restriction_it": "L'esercizio di aeromobili senza occupanti di peso superiore a 250 g \u00e8 vietato.",
			"zone_restriction_en": "The operation of unmanned aircraft weighing more than 250 g is prohibited.",
			"zone_message_de": "Ausnahmebewilligungen k\u00f6nnen bei der zust\u00e4ndigen Stelle beantragt werden.",
			"zone_message_fr": "Des autorisations exceptionnelles peuvent \u00eatre demand\u00e9es \u00e0 l'autorit\u00e9 comp\u00e9tente.",
			"zone_message_it": "I permessi d'esenzione possono essere richieste all'autorit\u00e0 competente.",
			"zone_message_en": "Exemption permits may be applied for at the competent authority.",
			"auth_url_de": ["https://www.skyguide.ch/de/dienstleistungen/spezialfluge"],
			"auth_url_fr": ["https://www.skyguide.ch/fr/services/vols-speciaux"],
			"auth_url_it": ["https://www.skyguide.ch/fr/services/vols-speciaux"],
			"auth_url_en": ["https://www.skyguide.ch/services/special-flights"],
			"auth_name_de": ["Flughafen Z\u00fcrich AG / Skyguide"],
			"auth_name_fr": ["Flughafen Z\u00fcrich AG / Skyguide"],
			"auth_name_it": ["Flughafen Z\u00fcrich AG / Skyguide"],
			"auth_name_en": ["Flughafen Z\u00fcrich AG / Skyguide"],
			"auth_contact": [],
			"auth_service_de": ["Skyguide Special Flight Office"],
			"auth_service_fr": ["Skyguide Special Flight Office"],
			"auth_service_it": ["Skyguide Special Flight Office"],
			"auth_service_en": ["Skyguide Special Flight Office"],
			"auth_email": ["drones@zurich-airport.com"],
			"auth_phone": ["0041438162211"],
			"auth_intervalbefore": ["P10DT00H"],
			"air_vol_lower_vref": "AGL",
			"air_vol_lower_limit": null,
			"air_vol_upper_vref": "AGL",
			"air_vol_upper_limit": null,
			"time_permanent": "Yes",
			"time_start": null,
			"time_end": null,
			"period_day": null,
			"period_start": null,
			"period_end": null,
			"label": 112667
		}
	}, {
		"layerBodId": "ch.bazl.einschraenkungen-drohnen",
		"layerName": "Restrictions for drones",
		"featureId": 112752,
		"id": 112752,
		"attributes": {
			"zone_name_de": "LSZH Z\u00fcrich (Flugplatzperimeter)",
			"zone_name_fr": "LSZH Z\u00fcrich (P\u00e9rim\u00e8tre d'a\u00e9rodrome)",
			"zone_name_it": "LSZH Z\u00fcrich (Perimetro dell'aerodromo)",
			"zone_name_en": "LSZH Z\u00fcrich (Airport perimeter)",
			"zone_restriction_id": "REQ_AUTHORISATION.MTOM_ALL",
			"zone_reason_id": "AIR_TRAFFIC",
			"zone_restriction_de": "Der Betrieb von unbemannten Luftfahrzeugen ist verboten.",
			"zone_restriction_fr": "L'exploitation d'a\u00e9ronefs sans occupants est interdite.",
			"zone_restriction_it": "L'esercizio di aeromobili senza occupanti \u00e8 vietato.",
			"zone_restriction_en": "The operation of unmanned aircraft is prohibited.",
			"zone_message_de": "Ausnahmebewilligungen k\u00f6nnen bei der zust\u00e4ndigen Stelle beantragt werden.",
			"zone_message_fr": "Des autorisations exceptionnelles peuvent \u00eatre demand\u00e9es \u00e0 l'autorit\u00e9 comp\u00e9tente.",
			"zone_message_it": "I permessi d'esenzione possono essere richieste all'autorit\u00e0 competente.",
			"zone_message_en": "Exemption permits may be applied for at the competent authority.",
			"auth_url_de": ["https://www.skyguide.ch/de/dienstleistungen/spezialfluge"],
			"auth_url_fr": ["https://www.skyguide.ch/fr/services/vols-speciaux"],
			"auth_url_it": ["https://www.skyguide.ch/fr/services/vols-speciaux"],
			"auth_url_en": ["https://www.skyguide.ch/services/special-flights"],
			"auth_name_de": ["Flughafen Z\u00fcrich AG / Skyguide"],
			"auth_name_fr": ["Flughafen Z\u00fcrich AG / Skyguide"],
			"auth_name_it": ["Flughafen Z\u00fcrich AG / Skyguide"],
			"auth_name_en": ["Flughafen Z\u00fcrich AG / Skyguide"],
			"auth_contact": [],
			"auth_service_de": ["Skyguide Special Flight Office"],
			"auth_service_fr": ["Skyguide Special Flight Office"],
			"auth_service_it": ["Skyguide Special Flight Office"],
			"auth_service_en": ["Skyguide Special Flight Office"],
			"auth_email": ["drones@zurich-airport.com"],
			"auth_phone": ["0041438162211"],
			"auth_intervalbefore": ["P10DT00H"],
			"air_vol_lower_vref": "AGL",
			"air_vol_lower_limit": null,
			"air_vol_upper_vref": "AGL",
			"air_vol_upper_limit": null,
			"time_permanent": "Yes",
			"time_start": null,
			"time_end": null,
			"period_day": null,
			"period_start": null,
			"period_end": null,
			"label": 112752
		}
	}, {
		"layerBodId": "ch.bazl.einschraenkungen-drohnen",
		"layerName": "Restrictions for drones",
		"featureId": 112869,
		"id": 112869,
		"attributes": {
			"zone_name_de": "CTR ZURICH 1",
			"zone_name_fr": "CTR ZURICH 1",
			"zone_name_it": "CTR ZURICH 1",
			"zone_name_en": "CTR ZURICH 1",
			"zone_restriction_id": "REQ_AUTHORISATION.CTR",
			"zone_reason_id": "AIR_TRAFFIC",
			"zone_restriction_de": "Der Betrieb von unbemannten Luftfahrzeugen mit einem Gewicht von mehr als 250 g ist ab einer H\u00f6he von 120 m \u00fcber Grund verboten.",
			"zone_restriction_fr": "L'exploitation d'a\u00e9ronefs sans occupants d'un poids sup\u00e9rieur \u00e0 250 g est interdite \u00e0 partir d'une hauteur de 120 m au-dessus du sol.",
			"zone_restriction_it": "L'esercizio di aeromobili senza occupanti di peso superiore a 250 g \u00e8 vietato a partire da un'altezza di 120 m sopra il suolo.",
			"zone_restriction_en": "The operation of unmanned aircraft weighing more than 250 g is prohibited from an altitude of 120 m above ground.",
			"zone_message_de": "Ausnahmebewilligungen k\u00f6nnen bei der zust\u00e4ndigen Stelle beantragt werden.",
			"zone_message_fr": "Des autorisations exceptionnelles peuvent \u00eatre demand\u00e9es \u00e0 l'autorit\u00e9 comp\u00e9tente.",
			"zone_message_it": "I permessi d'esenzione possono essere richieste all'autorit\u00e0 competente.",
			"zone_message_en": "Exemption permits may be applied for at the competent authority.",
			"auth_url_de": ["https://skyguide.ch/de/dienstleistungen/spezialfluge"],
			"auth_url_fr": ["https://skyguide.ch/fr/services/vols-speciaux"],
			"auth_url_it": ["https://skyguide.ch/fr/services/vols-speciaux"],
			"auth_url_en": ["https://skyguide.ch/services/special-flights"],
			"auth_name_de": ["Skyguide"],
			"auth_name_fr": ["Skyguide"],
			"auth_name_it": ["Skyguide"],
			"auth_name_en": ["Skyguide"],
			"auth_contact": [],
			"auth_service_de": ["Skyguide Special Flight Office"],
			"auth_service_fr": ["Skyguide Special Flight Office"],
			"auth_service_it": ["Skyguide Special Flight Office"],
			"auth_service_en": ["Skyguide Special Flight Office"],
			"auth_email": [],
			"auth_phone": [],
			"auth_intervalbefore": ["P14DT00H"],
			"air_vol_lower_vref": "AGL",
			"air_vol_lower_limit": "120",
			"air_vol_upper_vref": "AGL",
			"air_vol_upper_limit": null,
			"time_permanent": "Yes",
			"time_start": null,
			"time_end": null,
			"period_day": null,
			"period_start": null,
			"period_end": null,
			"label": 112869
		}
	}]
}
   ```
</details>

### Your part

Using JavaScript or TypeScript and a framework/library of your choice, create a web application with the following features:

* On the start page, the user selects whether they want to retrieve information about drone restrictions or population density.
* In the next step, the user selects an asset from the provided data dump.
* Finally, the application does the API requests and shows the result to the user.

## Evaluation criteria

What we're looking for:

* Clean project setup
* Appealing UI
* Relevant tests for your code
* Scratch features when necessary, time is short!
* Document your approach, your decisions, and your general notes

## Preparations for interview

* open your IDE
* have a running version of your app ready
* prepare to present your approach for 5-10 min (no slides!)
* be prepared to answer a few questions after your presentation
