# Static Map Data

The goal is to host my full collection of information, geographic and otherwise. We can start with:

* Air Quality: OpenAQ: python API + Chile data + some plots.
* BIKES: bike data = bicilascondes (static+dynamic), bikesantiago (historic?), mobike, lime, scoot...
* Combustible: some data from apicne.cl/v3 (ojo con todo lo que ahí hay).
* PUBLIC: social public: censo, limites comunales, regionales
* TRANSIT: transit private: uber, isocronas, ciclovias
* PERSONAL: google locations, ??
* PLACES: quant.cl/places: CUBO ciudad x rubro
* TGR: datos de atención a público de la Tesorería General de la República
* SII: public data from the Chilean Tax Service, with some info about the ETL (.xlsb -> csv -> parquet).
* TV: data obtained from "television studies", multas del CNTV.

Adicionalmente sería bueno almacenar herramientas:

* NOTEBOOKS: folium/plot.ly/mapbox/kepler consumption, ETL + visualizations.
* CODE: s3_to_github.py

Para cada formato, debiéramos elegir (?) entre los formatos shapefile, geoJSON y CSV/Parquet.
