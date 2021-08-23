CREATE DATABASE fp_scrapping;

CREATE USER "FrancaPaisa"
WITH PASSWORD 'FP#$tS'
NOSUPERUSER
NOCREATEDB
NOREPLICATION
NOCREATEROLE;

GRANT CONNECT ON DATABASE "fp_scrapping" TO "FrancaPaisa";

GRANT INSERT, SELECT, UPDATE, DELETE ON DATABASE "fp_scrapping" TO "FrancaPaisa";

CREATE SEQUENCE "seqIdTipoInmueble"
  MINVALUE      1
  NO MAXVALUE
  START WITH    1
  INCREMENT BY  1;

CREATE TABLE "TipoInmueble"
(
  "idTipoInmueble"              INTEGER         NOT NULL      DEFAULT NEXTVAL('"seqIdTipoInmueble"'),
  "nombre"                      VARCHAR(50)     NOT NULL,

  UNIQUE("nombre"),
  PRIMARY KEY ("idTipoInmueble")
);


CREATE SEQUENCE "seqIdMunicipio"
  MINVALUE      1
  NO MAXVALUE
  START WITH    1
  INCREMENT BY  1;

CREATE TABLE "Municipio"
(
  "idMunicipio"                 INTEGER         NOT NULL      DEFAULT NEXTVAL('"seqIdMunicipio"'),
  "nombre"                      VARCHAR(50)     NOT NULL,

  UNIQUE("nombre"),
  PRIMARY KEY ("idMunicipio")
);


CREATE SEQUENCE "seqIdZonaMedellin"
  MINVALUE      1
  NO MAXVALUE
  START WITH    1
  INCREMENT BY  1;

CREATE TABLE "ZonaMedellin"
(
  "idZonaMedellin"              INTEGER         NOT NULL      DEFAULT NEXTVAL('"seqIdZonaMedellin"'),
  "nombre"                      VARCHAR(50)     NOT NULL,

  UNIQUE("nombre"),
  PRIMARY KEY ("idZonaMedellin")
);



CREATE SEQUENCE "seqIdBarrioMedellin"
  MINVALUE      1
  NO MAXVALUE
  START WITH    1
  INCREMENT BY  1;

CREATE TABLE "BarrioMedellin"
(
  "idBarrioMedellin"            INTEGER         NOT NULL      DEFAULT NEXTVAL('"seqIdBarrioMedellin"'),
  "nombre"                      VARCHAR(50)     NOT NULL,
  "idZonaMedellin"              INTEGER         NOT NULL,

  UNIQUE("nombre"),
  PRIMARY KEY ("idBarrioMedellin"),
  FOREIGN KEY ("idZonaMedellin")      REFERENCES "ZonaMedellin" ("idZonaMedellin")
);

CREATE SEQUENCE "seqIdScrapping"
  MINVALUE      1
  NO MAXVALUE
  START WITH    1
  INCREMENT BY  1;

CREATE TABLE "TipoScrapping"
(
  "idScrapping"                       INTEGER         NOT NULL      DEFAULT NEXTVAL('"seqIdScrapping"'),

  "nombre_fuente"                     VARCHAR(2000)   NOT NULL,
  "nombre_publicacion"                VARCHAR(2000)   NOT NULL,
  "url_fuente"                        VARCHAR(2000)   NOT NULL,
  "tipo_inmueble"                     VARCHAR(2000)   NOT NULL,
  "valor_inmueble"                    BIGINT          NOT NULL,
  "municipio"                         VARCHAR(2000)   NOT NULL,
  "zona"                              VARCHAR(2000),
  "barrio"                            VARCHAR(2000),
  "cantidad_habitaciones"             INTEGER         NOT NULL,
  "area_total"                        FLOAT           NOT NULL,
  "area_construida"                   FLOAT,
  "descripcion"                       VARCHAR(2000),
  "vendedor"                          VARCHAR(2000),
  "cantidad_banos"                    INTEGER         NOT NULL,
  "costo_administracion"              BIGINT,
  "cantidad_parqueaderos"             INTEGER,
  "costo_servicios_publicos"          BIGINT,
  "inmueble_nuevo"                    BOOLEAN         NOT NULL      DEFAULT FALSE,
  "imagen_inmueble"                   VARCHAR(2000)   NOT NULL,
  "fecha_ultima_modificacion"         TIMESTAMP       NOT NULL      DEFAULT NOW(),

  PRIMARY KEY ("idScrapping"),
  FOREIGN KEY ("tipo_inmueble")      REFERENCES "TipoInmueble" ("idTipoInmueble"),
  FOREIGN KEY ("municipio")          REFERENCES "Municipio" ("idMunicipio"),
  FOREIGN KEY ("zona")               REFERENCES "ZonaMedellin" ("idZonaMedellin"),
  FOREIGN KEY ("barrio")             REFERENCES "BarrioMedellin" ("idBarrioMedellin"),
);


CREATE DATABASE fp_principal;
