--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.19
-- Dumped by pg_dump version 9.5.19

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- Name: seqIdBarrioMedellin; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."seqIdBarrioMedellin"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."seqIdBarrioMedellin" OWNER TO postgres;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: BarrioMedellin; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."BarrioMedellin" (
    "idBarrioMedellin" integer DEFAULT nextval('public."seqIdBarrioMedellin"'::regclass) NOT NULL,
    nombre character varying(50) NOT NULL
);


ALTER TABLE public."BarrioMedellin" OWNER TO postgres;

--
-- Name: seqIdMunicipio; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."seqIdMunicipio"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."seqIdMunicipio" OWNER TO postgres;

--
-- Name: Municipio; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Municipio" (
    "idMunicipio" integer DEFAULT nextval('public."seqIdMunicipio"'::regclass) NOT NULL,
    nombre character varying(50) NOT NULL
);


ALTER TABLE public."Municipio" OWNER TO postgres;

--
-- Name: seqIdTipoInmueble; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."seqIdTipoInmueble"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."seqIdTipoInmueble" OWNER TO postgres;

--
-- Name: TipoInmueble; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."TipoInmueble" (
    "idTipoInmueble" integer DEFAULT nextval('public."seqIdTipoInmueble"'::regclass) NOT NULL,
    nombre character varying(50) NOT NULL
);


ALTER TABLE public."TipoInmueble" OWNER TO postgres;

--
-- Name: seqIdScrapping; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."seqIdScrapping"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."seqIdScrapping" OWNER TO postgres;

--
-- Name: TipoScrapping; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."TipoScrapping" (
    "idScrapping" integer DEFAULT nextval('public."seqIdScrapping"'::regclass) NOT NULL,
    nombre_fuente character varying(2000) NOT NULL,
    nombre_publicacion character varying(2000) NOT NULL,
    url_fuente character varying(2000) NOT NULL,
    tipo_inmueble integer NOT NULL,
    valor_inmueble bigint NOT NULL,
    municipio integer NOT NULL,
    barrio integer,
    cantidad_habitaciones integer NOT NULL,
    area_total double precision NOT NULL,
    area_construida double precision,
    descripcion character varying(2000),
    vendedor character varying(2000),
    cantidad_banos integer NOT NULL,
    costo_administracion bigint,
    cantidad_parqueaderos integer,
    costo_servicios_publicos bigint,
    inmueble_nuevo boolean DEFAULT false NOT NULL,
    imagen_inmueble character varying(2000) NOT NULL,
    fecha_ultima_modificacion timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public."TipoScrapping" OWNER TO postgres;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO postgres;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: dot_restrict_scopes_restrictedapplication; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dot_restrict_scopes_restrictedapplication (
    id bigint NOT NULL,
    client_id character varying(100) NOT NULL,
    redirect_uris text NOT NULL,
    client_type character varying(32) NOT NULL,
    authorization_grant_type character varying(32) NOT NULL,
    client_secret character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    skip_authorization boolean NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    allowed_scope text NOT NULL,
    user_id integer,
    algorithm character varying(5) NOT NULL
);


ALTER TABLE public.dot_restrict_scopes_restrictedapplication OWNER TO postgres;

--
-- Name: dot_restrict_scopes_restrictedapplication_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dot_restrict_scopes_restrictedapplication_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dot_restrict_scopes_restrictedapplication_id_seq OWNER TO postgres;

--
-- Name: dot_restrict_scopes_restrictedapplication_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dot_restrict_scopes_restrictedapplication_id_seq OWNED BY public.dot_restrict_scopes_restrictedapplication.id;


--
-- Name: oauth2_provider_accesstoken; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.oauth2_provider_accesstoken (
    id bigint NOT NULL,
    token character varying(255) NOT NULL,
    expires timestamp with time zone NOT NULL,
    scope text NOT NULL,
    application_id bigint,
    user_id integer,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    source_refresh_token_id bigint,
    id_token_id bigint
);


ALTER TABLE public.oauth2_provider_accesstoken OWNER TO postgres;

--
-- Name: oauth2_provider_accesstoken_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.oauth2_provider_accesstoken_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.oauth2_provider_accesstoken_id_seq OWNER TO postgres;

--
-- Name: oauth2_provider_accesstoken_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.oauth2_provider_accesstoken_id_seq OWNED BY public.oauth2_provider_accesstoken.id;


--
-- Name: oauth2_provider_application; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.oauth2_provider_application (
    id bigint NOT NULL,
    client_id character varying(100) NOT NULL,
    redirect_uris text NOT NULL,
    client_type character varying(32) NOT NULL,
    authorization_grant_type character varying(32) NOT NULL,
    client_secret character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    user_id integer,
    skip_authorization boolean NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    algorithm character varying(5) NOT NULL
);


ALTER TABLE public.oauth2_provider_application OWNER TO postgres;

--
-- Name: oauth2_provider_application_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.oauth2_provider_application_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.oauth2_provider_application_id_seq OWNER TO postgres;

--
-- Name: oauth2_provider_application_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.oauth2_provider_application_id_seq OWNED BY public.oauth2_provider_application.id;


--
-- Name: oauth2_provider_grant; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.oauth2_provider_grant (
    id bigint NOT NULL,
    code character varying(255) NOT NULL,
    expires timestamp with time zone NOT NULL,
    redirect_uri text NOT NULL,
    scope text NOT NULL,
    application_id bigint NOT NULL,
    user_id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    code_challenge character varying(128) NOT NULL,
    code_challenge_method character varying(10) NOT NULL,
    nonce character varying(255) NOT NULL,
    claims text NOT NULL
);


ALTER TABLE public.oauth2_provider_grant OWNER TO postgres;

--
-- Name: oauth2_provider_grant_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.oauth2_provider_grant_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.oauth2_provider_grant_id_seq OWNER TO postgres;

--
-- Name: oauth2_provider_grant_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.oauth2_provider_grant_id_seq OWNED BY public.oauth2_provider_grant.id;


--
-- Name: oauth2_provider_idtoken; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.oauth2_provider_idtoken (
    id bigint NOT NULL,
    jti uuid NOT NULL,
    expires timestamp with time zone NOT NULL,
    scope text NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    application_id bigint,
    user_id integer
);


ALTER TABLE public.oauth2_provider_idtoken OWNER TO postgres;

--
-- Name: oauth2_provider_idtoken_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.oauth2_provider_idtoken_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.oauth2_provider_idtoken_id_seq OWNER TO postgres;

--
-- Name: oauth2_provider_idtoken_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.oauth2_provider_idtoken_id_seq OWNED BY public.oauth2_provider_idtoken.id;


--
-- Name: oauth2_provider_refreshtoken; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.oauth2_provider_refreshtoken (
    id bigint NOT NULL,
    token character varying(255) NOT NULL,
    access_token_id bigint,
    application_id bigint NOT NULL,
    user_id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    revoked timestamp with time zone
);


ALTER TABLE public.oauth2_provider_refreshtoken OWNER TO postgres;

--
-- Name: oauth2_provider_refreshtoken_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.oauth2_provider_refreshtoken_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.oauth2_provider_refreshtoken_id_seq OWNER TO postgres;

--
-- Name: oauth2_provider_refreshtoken_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.oauth2_provider_refreshtoken_id_seq OWNED BY public.oauth2_provider_refreshtoken.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dot_restrict_scopes_restrictedapplication ALTER COLUMN id SET DEFAULT nextval('public.dot_restrict_scopes_restrictedapplication_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_accesstoken ALTER COLUMN id SET DEFAULT nextval('public.oauth2_provider_accesstoken_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_application ALTER COLUMN id SET DEFAULT nextval('public.oauth2_provider_application_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_grant ALTER COLUMN id SET DEFAULT nextval('public.oauth2_provider_grant_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_idtoken ALTER COLUMN id SET DEFAULT nextval('public.oauth2_provider_idtoken_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_refreshtoken ALTER COLUMN id SET DEFAULT nextval('public.oauth2_provider_refreshtoken_id_seq'::regclass);


--
-- Data for Name: BarrioMedellin; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."BarrioMedellin" ("idBarrioMedellin", nombre) FROM stdin;
3978	El Chagualo
3979	Estación Villa
3980	Aranjuez
3981	Berlín
3982	La Piñuela
3983	San Isidro
3984	Palermo
3985	Bermejal
3986	San Pedro
3987	Sevilla
3988	Brasilia
3989	Manrique
3990	Campo Valdés 1
3991	Popular
3992	Santo Domingo Savio
3993	Moscú
3994	Granizal
3995	La Isla
3996	El Raizal
3997	El Playón de los Comuneros 1 
3998	Moravia
3999	El Jardín
4000	Las Nieves
4001	María Cano
4002	Carambolas
4003	Villa Roca
4004	La Esperanza
4005	La Avanzada
4006	El Compromiso
4007	Carpinelo
4008	Versalles
4009	San José la Cima
4010	Bello Horizonte
4011	Oriente
4012	La Cruz
4013	Villa Guadalupe
4014	San Pablo
4015	La Francia
4016	Andalucía
4017	La Rosa
4018	Santa Cruz
4019	La Salle
4020	Las Granjas
4021	El Pomar 
4022	Las Esmeraldas 
4023	Santa Inés 
4024	San Blas 
4025	Niza Norte (Villa Niza)
4026	Robledo
4027	Cerro El Volador
4028	El Cucaracho
4029	Palenque
4030	San Germán
4031	La Pilanca
4032	El Progreso
4033	Iguaná
4034	Lenin
4035	Aures
4036	Mirador del 12
4037	Picacho
4038	Picachito
4039	Salvador
4040	Allende
4041	Jorge Eliécer
4042	Gaitán
4043	La Torre
4044	Santa Teresa de Jesús
4045	Armero
4046	Búcaros
4047	El Paraíso
4048	El Bosque
4049	El Triunfo
4050	Brasil
4051	Los Arrayanes
4052	La Minita
4053	San Nicolás
4054	María Auxiliadora
4055	F.Gómez
4056	Castilla
4057	Caribe
4058	Belalcázar
4059	El Día
4060	San Martín
4061	Kennedy
4062	Castillita
4063	Miramar
4064	Santa Margarita
4065	Alfonso López
4066	Pedregal
4067	Florencia
4068	Boyacá
4069	Las Brisas
4070	Antonio Zea
4071	López de Mesa
4072	Córdoba
4073	Téjelo
4074	Santander
4075	12 de Octubre
4076	Tricentenario
4077	La Pola
4078	Monteverde
4079	Villaflora
4080	Vallejuelos
4081	Villa Sofía
4082	Romeral
4083	Doña María
4084	Nebraska
4085	El Cortijo
4086	Candelaria
4087	Guayaquil
4088	Colón
4089	Sucre
4090	La Ladera
4091	El Salvador
4092	Loreto
4093	Villa Hermosa
4094	Enciso
4095	La Milagrosa
4096	Alejandro
4097	Echavarría
4098	La Mansión
4099	Caicedo
4100	La Toma
4101	San Diego
4102	Las Palmas
4103	La Independencia
4104	Perpetuo Socorro
4105	Corazón de Jesús
4106	Barrio Nuevo
4107	Llanaditas
4108	Buenos Aires
4109	Boston
4110	Prado
4111	Villa Nueva
4112	San Benito
4113	Bomboná
4114	Los Ángeles
4115	San Miguel
4116	Villatina
4117	Lomas de
4118	Julio Rincón
4119	Manuel Morales
4120	Villa Turbay
4121	Juan Pablo II
4122	San Antonio
4123	Las Estancias
4124	Santa. Lucía
4125	8 de Marzo
4126	13 de Noviembre
4127	La Libertad
4128	La Primavera
4129	El Edén
4130	La Sierra
4131	Golondrinas
4132	Brisas de Oriente
4133	El Vergel
4134	Loyola
4135	Los Cerros
4136	Diego Echavarría
4137	La Colina
4138	Pinar del Cerro
4139	Caunces de Oriente
4140	Cataluña
4141	Colinas de La Candelaria
4142	Quintas de la Playa
4143	Urbanización Los Cerros
4144	Urbanización El Carmelo
4145	Urbanización La Palma
4146	Isaac Gaviria
4147	El Salado
4148	Betania
4149	La Puerta
4150	La Loma
4151	El Corazón
4152	Belencito
4153	El Coco
4154	El Socorro
4155	Campo Alegre
4156	La América
4157	San Javier
4158	Floresta
4159	El Danubio
4160	Barrio Cristóbal
4161	Lorena
4162	Laureles
4163	Miravalle
4164	Florida
4165	Ferrini
4166	Nuevos
4167	Conquistadores
4168	Fuente Clara
4169	Blanquizal
4170	La Quiebra
4171	Santa Rosa de Lima
4172	La Pradera
4173	Los Alcázares
4174	Antonio Nariño
4175	Metropolitano
4176	20 de Julio
4177	San Joaquín
4178	Carlos E. Restrepo
4179	Santa Mónica
4180	Santa Lucía
4181	Calasanz
4182	Velódromo
4183	Unidad Deportiva Florida Nueva
4184	Simón Bolívar
4185	Bolivariana
4186	Suramericana
4187	Loma de los Parra
4188	González
4189	El Garabato
4190	El Tesoro
4191	Loma de Los
4192	Mangos
4193	La Chacona
4194	El Poblado
4195	Aguacatala
4196	Castropol
4197	Patio Bonito
4198	LLeras
4199	Santa María de los
4200	Ángeles
4201	Villa Carlota
4202	Barrio Colombia
4203	Manila
4204	Astorga
4205	Provenza
4206	Alejandría
4207	Los Balsos
4208	Las Lomas
4209	Altos del Poblado
4210	San Lucas
4211	El Castillo
4212	El Diamante
4213	Los Naranjos
4214	El Remanso
4215	El Futuro
4216	Guadalajara
4217	Vegas del Poblado
4218	Cristo Rey
4219	Nutibara
4220	Barrio Antioquia
4221	El Rodeo
4222	Altavista
4223	El Rincón
4224	Las Mercedes
4225	Belén
4226	Guayabal
4227	Alpinos
4228	Trinidad
4229	San Bernardo
4230	Las Playas
4231	Granada
4232	Zafra
4233	Apolo
4234	Las Violetas
4235	Rafael Uribe Uribe
4236	Los Libertadores
4237	La Castellana
4238	Santa fe
4239	Colina del Sur
4240	Coimita
4241	Shellmar
4242	Noel
4243	Campo Amor
4244	Manzanares
4245	Mallorca
4246	Aliadas
4247	Rosales
4248	Fátima
4249	La Nubia
4250	Los Alpes
4251	La Palma
4252	La Mota
4253	El Enclave
4254	Kalamarí
4255	Loma de los Bernal
4256	Palmitas
4257	Santa Elena
4258	San Cristóbal
4259	San Antonio de Prado
\.


--
-- Data for Name: Municipio; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Municipio" ("idMunicipio", nombre) FROM stdin;
1	Barbosa
2	Bello
3	Caldas
4	Copacabana
5	Envigado
6	Girardota
7	Itagüí
8	La Estrella
9	Medellín
10	Sabaneta
11	Medellín Nororiental
12	Medellín Noroccidental
13	Medellín Centroriental
14	Medellín Centroccidental
15	Medellín Suroriental
16	Medellín Suroccidental
17	Medellín Rural
\.


--
-- Data for Name: TipoInmueble; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."TipoInmueble" ("idTipoInmueble", nombre) FROM stdin;
1	Apartamentos
2	Casas
3	Oficinas
4	Locales
5	Fincas
6	Lotes
7	Bodegas
8	Consultorios
\.


--
-- Data for Name: TipoScrapping; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."TipoScrapping" ("idScrapping", nombre_fuente, nombre_publicacion, url_fuente, tipo_inmueble, valor_inmueble, municipio, barrio, cantidad_habitaciones, area_total, area_construida, descripcion, vendedor, cantidad_banos, costo_administracion, cantidad_parqueaderos, costo_servicios_publicos, inmueble_nuevo, imagen_inmueble, fecha_ultima_modificacion) FROM stdin;
1	A	A	A	1	1	1	4176	1	1	1	TEST	TEST	1	1	1	1	t	TEST	2021-08-20 04:08:58
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 1, false);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$150000$XhkUGJ1HDLec$EPj7UOG3zyFvrccN6MG/Mdjng95F4bs41Euu5P1ReNg=	2021-08-20 03:54:50.214037+00	t	fp_scrapping			francapaisa@gmail.com	t	t	2021-08-20 03:19:57.724118+00
3	pbkdf2_sha256$150000$c4u2xTRLumnJ$y30FGjipOqHj6bUpxPycjXaTP1ppLwylhhobwjKcH1k=	\N	f	test1				f	t	2021-08-20 04:06:38.352517+00
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 3, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2021-08-20 03:59:46.385109+00	2	test1	1	[{"added": {}}]	1	1
2	2021-08-20 04:06:00.707127+00	2	test1	3		1	1
3	2021-08-20 04:06:38.473684+00	3	test1	1	[{"added": {}}]	1	1
4	2021-08-20 04:07:10.614842+00	1	Test1 Aplicacion	1	[{"added": {}}]	2	1
5	2021-08-20 04:11:30.834986+00	1	1 (A A A 1 (Apartamentos) 1 1 (Barbosa) 4176 (20 de Julio) 1 1.0 1.0 TEST TEST 1 1 1 1 True TEST 2021-08-20 04:08:58+00:00)	1	[{"added": {}}]	3	1
6	2021-08-20 04:11:54.03711+00	9	9 (Test1)	1	[{"added": {}}]	4	1
7	2021-08-20 04:12:05.360708+00	9	9 (Test1)	3		4	1
8	2021-08-20 04:12:19.329685+00	4260	4260 (Test1)	1	[{"added": {}}]	5	1
9	2021-08-20 04:12:43.852435+00	4260	4260 (Test1)	3		5	1
10	2021-08-20 04:12:55.424146+00	18	18 (Test1)	1	[{"added": {}}]	6	1
11	2021-08-20 04:13:05.860933+00	18	18 (Test1)	3		6	1
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 11, true);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	auth	user
2	dot_restrict_scopes	restrictedapplication
3	francapaisa_inmuebles	scrappingmodel
4	francapaisa_inmuebles	tipoinmueblemodel
5	francapaisa_zonas	barriomedellinmodel
6	francapaisa_zonas	municipiomodel
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 6, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
fqfxsuxpx9sjous51en7xetx22v7aao9	NjI5OWFjZjVjN2QxMzkxODA5MTQ4M2ZiOWZhOTVkYTYwYjYyM2ExNTp7Il9hdXRoX3VzZXJfaGFzaCI6IjIwMDA2NTdiNWU2OThhODQ1ZWVmMjdmZTkwYjJkOWVlODQ2MGY4M2IiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2021-09-03 03:54:50.223017+00
\.


--
-- Data for Name: dot_restrict_scopes_restrictedapplication; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dot_restrict_scopes_restrictedapplication (id, client_id, redirect_uris, client_type, authorization_grant_type, client_secret, name, skip_authorization, created, updated, allowed_scope, user_id, algorithm) FROM stdin;
1	fu44MIFEA3BcaMLcdLwzMrdF1pbE6RfW8p00wUqO		confidential	password	eFMjt6xAxPKCGiQUtEepS9ZVVoie5TGj07VxlL2G6rz3tQNnBT3wH2shXnffQhCz01oWPxXDzBAsyjH6wRV2mgxksMUMA1sYEvsYsTnoMCy4K35zqSmz4Aq4IGwPHZW2	Test1 Aplicacion	f	2021-08-20 04:07:10.612741+00	2021-08-20 04:07:10.61278+00	francapaisa_zonas_scope default francapaisa_inmuebles_scope francapaisa_users_scope	3	
\.


--
-- Name: dot_restrict_scopes_restrictedapplication_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dot_restrict_scopes_restrictedapplication_id_seq', 1, true);


--
-- Data for Name: oauth2_provider_accesstoken; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.oauth2_provider_accesstoken (id, token, expires, scope, application_id, user_id, created, updated, source_refresh_token_id, id_token_id) FROM stdin;
1	vq0bYSVEMOmbt5MkSbiNyJBEBw11Z0	2021-08-20 14:17:25.530915+00	default	1	3	2021-08-20 04:17:25.536691+00	2021-08-20 04:17:25.536708+00	\N	\N
\.


--
-- Name: oauth2_provider_accesstoken_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.oauth2_provider_accesstoken_id_seq', 1, true);


--
-- Data for Name: oauth2_provider_application; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.oauth2_provider_application (id, client_id, redirect_uris, client_type, authorization_grant_type, client_secret, name, user_id, skip_authorization, created, updated, algorithm) FROM stdin;
\.


--
-- Name: oauth2_provider_application_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.oauth2_provider_application_id_seq', 1, false);


--
-- Data for Name: oauth2_provider_grant; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.oauth2_provider_grant (id, code, expires, redirect_uri, scope, application_id, user_id, created, updated, code_challenge, code_challenge_method, nonce, claims) FROM stdin;
\.


--
-- Name: oauth2_provider_grant_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.oauth2_provider_grant_id_seq', 1, false);


--
-- Data for Name: oauth2_provider_idtoken; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.oauth2_provider_idtoken (id, jti, expires, scope, created, updated, application_id, user_id) FROM stdin;
\.


--
-- Name: oauth2_provider_idtoken_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.oauth2_provider_idtoken_id_seq', 1, false);


--
-- Data for Name: oauth2_provider_refreshtoken; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.oauth2_provider_refreshtoken (id, token, access_token_id, application_id, user_id, created, updated, revoked) FROM stdin;
1	qLpfFuvUj4E037ccBwXCKr7QNST5Yo	1	1	3	2021-08-20 04:17:25.547414+00	2021-08-20 04:17:25.547434+00	\N
\.


--
-- Name: oauth2_provider_refreshtoken_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.oauth2_provider_refreshtoken_id_seq', 1, true);


--
-- Name: seqIdBarrioMedellin; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."seqIdBarrioMedellin"', 4260, true);


--
-- Name: seqIdMunicipio; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."seqIdMunicipio"', 18, true);


--
-- Name: seqIdScrapping; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."seqIdScrapping"', 1, true);


--
-- Name: seqIdTipoInmueble; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."seqIdTipoInmueble"', 9, true);


--
-- Name: BarrioMedellin_nombre_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."BarrioMedellin"
    ADD CONSTRAINT "BarrioMedellin_nombre_key" UNIQUE (nombre);


--
-- Name: BarrioMedellin_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."BarrioMedellin"
    ADD CONSTRAINT "BarrioMedellin_pkey" PRIMARY KEY ("idBarrioMedellin");


--
-- Name: Municipio_nombre_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Municipio"
    ADD CONSTRAINT "Municipio_nombre_key" UNIQUE (nombre);


--
-- Name: Municipio_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Municipio"
    ADD CONSTRAINT "Municipio_pkey" PRIMARY KEY ("idMunicipio");


--
-- Name: TipoInmueble_nombre_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."TipoInmueble"
    ADD CONSTRAINT "TipoInmueble_nombre_key" UNIQUE (nombre);


--
-- Name: TipoInmueble_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."TipoInmueble"
    ADD CONSTRAINT "TipoInmueble_pkey" PRIMARY KEY ("idTipoInmueble");


--
-- Name: TipoScrapping_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."TipoScrapping"
    ADD CONSTRAINT "TipoScrapping_pkey" PRIMARY KEY ("idScrapping");


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: dot_restrict_scopes_restrictedapplication_client_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dot_restrict_scopes_restrictedapplication
    ADD CONSTRAINT dot_restrict_scopes_restrictedapplication_client_id_key UNIQUE (client_id);


--
-- Name: dot_restrict_scopes_restrictedapplication_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dot_restrict_scopes_restrictedapplication
    ADD CONSTRAINT dot_restrict_scopes_restrictedapplication_pkey PRIMARY KEY (id);


--
-- Name: oauth2_provider_accesstoken_id_token_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_accesstoken
    ADD CONSTRAINT oauth2_provider_accesstoken_id_token_id_key UNIQUE (id_token_id);


--
-- Name: oauth2_provider_accesstoken_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_accesstoken
    ADD CONSTRAINT oauth2_provider_accesstoken_pkey PRIMARY KEY (id);


--
-- Name: oauth2_provider_accesstoken_source_refresh_token_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_accesstoken
    ADD CONSTRAINT oauth2_provider_accesstoken_source_refresh_token_id_key UNIQUE (source_refresh_token_id);


--
-- Name: oauth2_provider_accesstoken_token_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_accesstoken
    ADD CONSTRAINT oauth2_provider_accesstoken_token_key UNIQUE (token);


--
-- Name: oauth2_provider_application_client_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_application
    ADD CONSTRAINT oauth2_provider_application_client_id_key UNIQUE (client_id);


--
-- Name: oauth2_provider_application_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_application
    ADD CONSTRAINT oauth2_provider_application_pkey PRIMARY KEY (id);


--
-- Name: oauth2_provider_grant_code_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_grant
    ADD CONSTRAINT oauth2_provider_grant_code_key UNIQUE (code);


--
-- Name: oauth2_provider_grant_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_grant
    ADD CONSTRAINT oauth2_provider_grant_pkey PRIMARY KEY (id);


--
-- Name: oauth2_provider_idtoken_jti_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_idtoken
    ADD CONSTRAINT oauth2_provider_idtoken_jti_key UNIQUE (jti);


--
-- Name: oauth2_provider_idtoken_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_idtoken
    ADD CONSTRAINT oauth2_provider_idtoken_pkey PRIMARY KEY (id);


--
-- Name: oauth2_provider_refreshtoken_access_token_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_refreshtoken
    ADD CONSTRAINT oauth2_provider_refreshtoken_access_token_id_key UNIQUE (access_token_id);


--
-- Name: oauth2_provider_refreshtoken_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_refreshtoken
    ADD CONSTRAINT oauth2_provider_refreshtoken_pkey PRIMARY KEY (id);


--
-- Name: oauth2_provider_refreshtoken_token_revoked_af8a5134_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_refreshtoken
    ADD CONSTRAINT oauth2_provider_refreshtoken_token_revoked_af8a5134_uniq UNIQUE (token, revoked);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: dot_restrict_scopes_rest_client_id_9234ae41_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX dot_restrict_scopes_rest_client_id_9234ae41_like ON public.dot_restrict_scopes_restrictedapplication USING btree (client_id varchar_pattern_ops);


--
-- Name: dot_restrict_scopes_rest_client_secret_f1af90ac_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX dot_restrict_scopes_rest_client_secret_f1af90ac_like ON public.dot_restrict_scopes_restrictedapplication USING btree (client_secret varchar_pattern_ops);


--
-- Name: dot_restrict_scopes_restri_client_secret_f1af90ac; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX dot_restrict_scopes_restri_client_secret_f1af90ac ON public.dot_restrict_scopes_restrictedapplication USING btree (client_secret);


--
-- Name: dot_restrict_scopes_restrictedapplication_user_id_4f5dea3d; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX dot_restrict_scopes_restrictedapplication_user_id_4f5dea3d ON public.dot_restrict_scopes_restrictedapplication USING btree (user_id);


--
-- Name: oauth2_provider_accesstoken_application_id_b22886e1; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_accesstoken_application_id_b22886e1 ON public.oauth2_provider_accesstoken USING btree (application_id);


--
-- Name: oauth2_provider_accesstoken_token_8af090f8_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_accesstoken_token_8af090f8_like ON public.oauth2_provider_accesstoken USING btree (token varchar_pattern_ops);


--
-- Name: oauth2_provider_accesstoken_user_id_6e4c9a65; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_accesstoken_user_id_6e4c9a65 ON public.oauth2_provider_accesstoken USING btree (user_id);


--
-- Name: oauth2_provider_application_client_id_03f0cc84_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_application_client_id_03f0cc84_like ON public.oauth2_provider_application USING btree (client_id varchar_pattern_ops);


--
-- Name: oauth2_provider_application_client_secret_53133678; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_application_client_secret_53133678 ON public.oauth2_provider_application USING btree (client_secret);


--
-- Name: oauth2_provider_application_client_secret_53133678_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_application_client_secret_53133678_like ON public.oauth2_provider_application USING btree (client_secret varchar_pattern_ops);


--
-- Name: oauth2_provider_application_user_id_79829054; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_application_user_id_79829054 ON public.oauth2_provider_application USING btree (user_id);


--
-- Name: oauth2_provider_grant_application_id_81923564; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_grant_application_id_81923564 ON public.oauth2_provider_grant USING btree (application_id);


--
-- Name: oauth2_provider_grant_code_49ab4ddf_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_grant_code_49ab4ddf_like ON public.oauth2_provider_grant USING btree (code varchar_pattern_ops);


--
-- Name: oauth2_provider_grant_user_id_e8f62af8; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_grant_user_id_e8f62af8 ON public.oauth2_provider_grant USING btree (user_id);


--
-- Name: oauth2_provider_idtoken_application_id_08c5ff4f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_idtoken_application_id_08c5ff4f ON public.oauth2_provider_idtoken USING btree (application_id);


--
-- Name: oauth2_provider_idtoken_user_id_dd512b59; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_idtoken_user_id_dd512b59 ON public.oauth2_provider_idtoken USING btree (user_id);


--
-- Name: oauth2_provider_refreshtoken_application_id_2d1c311b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_refreshtoken_application_id_2d1c311b ON public.oauth2_provider_refreshtoken USING btree (application_id);


--
-- Name: oauth2_provider_refreshtoken_user_id_da837fce; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_refreshtoken_user_id_da837fce ON public.oauth2_provider_refreshtoken USING btree (user_id);


--
-- Name: TipoScrapping_barrio_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."TipoScrapping"
    ADD CONSTRAINT "TipoScrapping_barrio_fkey" FOREIGN KEY (barrio) REFERENCES public."BarrioMedellin"("idBarrioMedellin");


--
-- Name: TipoScrapping_municipio_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."TipoScrapping"
    ADD CONSTRAINT "TipoScrapping_municipio_fkey" FOREIGN KEY (municipio) REFERENCES public."Municipio"("idMunicipio");


--
-- Name: TipoScrapping_tipo_inmueble_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."TipoScrapping"
    ADD CONSTRAINT "TipoScrapping_tipo_inmueble_fkey" FOREIGN KEY (tipo_inmueble) REFERENCES public."TipoInmueble"("idTipoInmueble");


--
-- Name: auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dot_restrict_scopes__user_id_4f5dea3d_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dot_restrict_scopes_restrictedapplication
    ADD CONSTRAINT dot_restrict_scopes__user_id_4f5dea3d_fk_auth_user FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: oauth2_provider_acce_application_id_b22886e1_fk_oauth2_pr; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_accesstoken
    ADD CONSTRAINT oauth2_provider_acce_application_id_b22886e1_fk_oauth2_pr FOREIGN KEY (application_id) REFERENCES public.dot_restrict_scopes_restrictedapplication(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: oauth2_provider_acce_id_token_id_85db651b_fk_oauth2_pr; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_accesstoken
    ADD CONSTRAINT oauth2_provider_acce_id_token_id_85db651b_fk_oauth2_pr FOREIGN KEY (id_token_id) REFERENCES public.oauth2_provider_idtoken(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: oauth2_provider_acce_source_refresh_token_e66fbc72_fk_oauth2_pr; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_accesstoken
    ADD CONSTRAINT oauth2_provider_acce_source_refresh_token_e66fbc72_fk_oauth2_pr FOREIGN KEY (source_refresh_token_id) REFERENCES public.oauth2_provider_refreshtoken(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: oauth2_provider_accesstoken_user_id_6e4c9a65_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_accesstoken
    ADD CONSTRAINT oauth2_provider_accesstoken_user_id_6e4c9a65_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: oauth2_provider_application_user_id_79829054_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_application
    ADD CONSTRAINT oauth2_provider_application_user_id_79829054_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: oauth2_provider_gran_application_id_81923564_fk_oauth2_pr; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_grant
    ADD CONSTRAINT oauth2_provider_gran_application_id_81923564_fk_oauth2_pr FOREIGN KEY (application_id) REFERENCES public.dot_restrict_scopes_restrictedapplication(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: oauth2_provider_grant_user_id_e8f62af8_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_grant
    ADD CONSTRAINT oauth2_provider_grant_user_id_e8f62af8_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: oauth2_provider_idto_application_id_08c5ff4f_fk_oauth2_pr; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_idtoken
    ADD CONSTRAINT oauth2_provider_idto_application_id_08c5ff4f_fk_oauth2_pr FOREIGN KEY (application_id) REFERENCES public.dot_restrict_scopes_restrictedapplication(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: oauth2_provider_idtoken_user_id_dd512b59_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_idtoken
    ADD CONSTRAINT oauth2_provider_idtoken_user_id_dd512b59_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: oauth2_provider_refr_access_token_id_775e84e8_fk_oauth2_pr; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_refreshtoken
    ADD CONSTRAINT oauth2_provider_refr_access_token_id_775e84e8_fk_oauth2_pr FOREIGN KEY (access_token_id) REFERENCES public.oauth2_provider_accesstoken(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: oauth2_provider_refr_application_id_2d1c311b_fk_oauth2_pr; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_refreshtoken
    ADD CONSTRAINT oauth2_provider_refr_application_id_2d1c311b_fk_oauth2_pr FOREIGN KEY (application_id) REFERENCES public.dot_restrict_scopes_restrictedapplication(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: oauth2_provider_refreshtoken_user_id_da837fce_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_refreshtoken
    ADD CONSTRAINT oauth2_provider_refreshtoken_user_id_da837fce_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- Name: SEQUENCE "seqIdBarrioMedellin"; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE public."seqIdBarrioMedellin" FROM PUBLIC;
REVOKE ALL ON SEQUENCE public."seqIdBarrioMedellin" FROM postgres;
GRANT ALL ON SEQUENCE public."seqIdBarrioMedellin" TO postgres;
GRANT ALL ON SEQUENCE public."seqIdBarrioMedellin" TO "FrancaPaisa";


--
-- Name: TABLE "BarrioMedellin"; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE public."BarrioMedellin" FROM PUBLIC;
REVOKE ALL ON TABLE public."BarrioMedellin" FROM postgres;
GRANT ALL ON TABLE public."BarrioMedellin" TO postgres;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public."BarrioMedellin" TO "FrancaPaisa";


--
-- Name: SEQUENCE "seqIdMunicipio"; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE public."seqIdMunicipio" FROM PUBLIC;
REVOKE ALL ON SEQUENCE public."seqIdMunicipio" FROM postgres;
GRANT ALL ON SEQUENCE public."seqIdMunicipio" TO postgres;
GRANT ALL ON SEQUENCE public."seqIdMunicipio" TO "FrancaPaisa";


--
-- Name: TABLE "Municipio"; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE public."Municipio" FROM PUBLIC;
REVOKE ALL ON TABLE public."Municipio" FROM postgres;
GRANT ALL ON TABLE public."Municipio" TO postgres;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public."Municipio" TO "FrancaPaisa";


--
-- Name: SEQUENCE "seqIdTipoInmueble"; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE public."seqIdTipoInmueble" FROM PUBLIC;
REVOKE ALL ON SEQUENCE public."seqIdTipoInmueble" FROM postgres;
GRANT ALL ON SEQUENCE public."seqIdTipoInmueble" TO postgres;
GRANT ALL ON SEQUENCE public."seqIdTipoInmueble" TO "FrancaPaisa";


--
-- Name: TABLE "TipoInmueble"; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE public."TipoInmueble" FROM PUBLIC;
REVOKE ALL ON TABLE public."TipoInmueble" FROM postgres;
GRANT ALL ON TABLE public."TipoInmueble" TO postgres;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public."TipoInmueble" TO "FrancaPaisa";


--
-- Name: SEQUENCE "seqIdScrapping"; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE public."seqIdScrapping" FROM PUBLIC;
REVOKE ALL ON SEQUENCE public."seqIdScrapping" FROM postgres;
GRANT ALL ON SEQUENCE public."seqIdScrapping" TO postgres;
GRANT ALL ON SEQUENCE public."seqIdScrapping" TO "FrancaPaisa";


--
-- Name: TABLE "TipoScrapping"; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE public."TipoScrapping" FROM PUBLIC;
REVOKE ALL ON TABLE public."TipoScrapping" FROM postgres;
GRANT ALL ON TABLE public."TipoScrapping" TO postgres;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public."TipoScrapping" TO "FrancaPaisa";


--
-- Name: TABLE auth_group; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE public.auth_group FROM PUBLIC;
REVOKE ALL ON TABLE public.auth_group FROM postgres;
GRANT ALL ON TABLE public.auth_group TO postgres;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.auth_group TO "FrancaPaisa";


--
-- Name: SEQUENCE auth_group_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE public.auth_group_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE public.auth_group_id_seq FROM postgres;
GRANT ALL ON SEQUENCE public.auth_group_id_seq TO postgres;
GRANT ALL ON SEQUENCE public.auth_group_id_seq TO "FrancaPaisa";


--
-- Name: TABLE auth_group_permissions; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE public.auth_group_permissions FROM PUBLIC;
REVOKE ALL ON TABLE public.auth_group_permissions FROM postgres;
GRANT ALL ON TABLE public.auth_group_permissions TO postgres;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.auth_group_permissions TO "FrancaPaisa";


--
-- Name: SEQUENCE auth_group_permissions_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE public.auth_group_permissions_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE public.auth_group_permissions_id_seq FROM postgres;
GRANT ALL ON SEQUENCE public.auth_group_permissions_id_seq TO postgres;
GRANT ALL ON SEQUENCE public.auth_group_permissions_id_seq TO "FrancaPaisa";


--
-- Name: TABLE auth_permission; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE public.auth_permission FROM PUBLIC;
REVOKE ALL ON TABLE public.auth_permission FROM postgres;
GRANT ALL ON TABLE public.auth_permission TO postgres;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.auth_permission TO "FrancaPaisa";


--
-- Name: SEQUENCE auth_permission_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE public.auth_permission_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE public.auth_permission_id_seq FROM postgres;
GRANT ALL ON SEQUENCE public.auth_permission_id_seq TO postgres;
GRANT ALL ON SEQUENCE public.auth_permission_id_seq TO "FrancaPaisa";


--
-- Name: TABLE auth_user; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE public.auth_user FROM PUBLIC;
REVOKE ALL ON TABLE public.auth_user FROM postgres;
GRANT ALL ON TABLE public.auth_user TO postgres;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.auth_user TO "FrancaPaisa";


--
-- Name: TABLE auth_user_groups; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE public.auth_user_groups FROM PUBLIC;
REVOKE ALL ON TABLE public.auth_user_groups FROM postgres;
GRANT ALL ON TABLE public.auth_user_groups TO postgres;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.auth_user_groups TO "FrancaPaisa";


--
-- Name: SEQUENCE auth_user_groups_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE public.auth_user_groups_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE public.auth_user_groups_id_seq FROM postgres;
GRANT ALL ON SEQUENCE public.auth_user_groups_id_seq TO postgres;
GRANT ALL ON SEQUENCE public.auth_user_groups_id_seq TO "FrancaPaisa";


--
-- Name: SEQUENCE auth_user_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE public.auth_user_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE public.auth_user_id_seq FROM postgres;
GRANT ALL ON SEQUENCE public.auth_user_id_seq TO postgres;
GRANT ALL ON SEQUENCE public.auth_user_id_seq TO "FrancaPaisa";


--
-- Name: TABLE auth_user_user_permissions; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE public.auth_user_user_permissions FROM PUBLIC;
REVOKE ALL ON TABLE public.auth_user_user_permissions FROM postgres;
GRANT ALL ON TABLE public.auth_user_user_permissions TO postgres;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.auth_user_user_permissions TO "FrancaPaisa";


--
-- Name: SEQUENCE auth_user_user_permissions_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE public.auth_user_user_permissions_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE public.auth_user_user_permissions_id_seq FROM postgres;
GRANT ALL ON SEQUENCE public.auth_user_user_permissions_id_seq TO postgres;
GRANT ALL ON SEQUENCE public.auth_user_user_permissions_id_seq TO "FrancaPaisa";


--
-- Name: TABLE django_admin_log; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE public.django_admin_log FROM PUBLIC;
REVOKE ALL ON TABLE public.django_admin_log FROM postgres;
GRANT ALL ON TABLE public.django_admin_log TO postgres;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.django_admin_log TO "FrancaPaisa";


--
-- Name: SEQUENCE django_admin_log_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE public.django_admin_log_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE public.django_admin_log_id_seq FROM postgres;
GRANT ALL ON SEQUENCE public.django_admin_log_id_seq TO postgres;
GRANT ALL ON SEQUENCE public.django_admin_log_id_seq TO "FrancaPaisa";


--
-- Name: TABLE django_content_type; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE public.django_content_type FROM PUBLIC;
REVOKE ALL ON TABLE public.django_content_type FROM postgres;
GRANT ALL ON TABLE public.django_content_type TO postgres;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.django_content_type TO "FrancaPaisa";


--
-- Name: SEQUENCE django_content_type_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE public.django_content_type_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE public.django_content_type_id_seq FROM postgres;
GRANT ALL ON SEQUENCE public.django_content_type_id_seq TO postgres;
GRANT ALL ON SEQUENCE public.django_content_type_id_seq TO "FrancaPaisa";


--
-- Name: TABLE django_session; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE public.django_session FROM PUBLIC;
REVOKE ALL ON TABLE public.django_session FROM postgres;
GRANT ALL ON TABLE public.django_session TO postgres;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.django_session TO "FrancaPaisa";


--
-- Name: TABLE dot_restrict_scopes_restrictedapplication; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE public.dot_restrict_scopes_restrictedapplication FROM PUBLIC;
REVOKE ALL ON TABLE public.dot_restrict_scopes_restrictedapplication FROM postgres;
GRANT ALL ON TABLE public.dot_restrict_scopes_restrictedapplication TO postgres;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.dot_restrict_scopes_restrictedapplication TO "FrancaPaisa";


--
-- Name: SEQUENCE dot_restrict_scopes_restrictedapplication_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE public.dot_restrict_scopes_restrictedapplication_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE public.dot_restrict_scopes_restrictedapplication_id_seq FROM postgres;
GRANT ALL ON SEQUENCE public.dot_restrict_scopes_restrictedapplication_id_seq TO postgres;
GRANT ALL ON SEQUENCE public.dot_restrict_scopes_restrictedapplication_id_seq TO "FrancaPaisa";


--
-- Name: TABLE oauth2_provider_accesstoken; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE public.oauth2_provider_accesstoken FROM PUBLIC;
REVOKE ALL ON TABLE public.oauth2_provider_accesstoken FROM postgres;
GRANT ALL ON TABLE public.oauth2_provider_accesstoken TO postgres;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.oauth2_provider_accesstoken TO "FrancaPaisa";


--
-- Name: SEQUENCE oauth2_provider_accesstoken_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE public.oauth2_provider_accesstoken_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE public.oauth2_provider_accesstoken_id_seq FROM postgres;
GRANT ALL ON SEQUENCE public.oauth2_provider_accesstoken_id_seq TO postgres;
GRANT ALL ON SEQUENCE public.oauth2_provider_accesstoken_id_seq TO "FrancaPaisa";


--
-- Name: TABLE oauth2_provider_application; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE public.oauth2_provider_application FROM PUBLIC;
REVOKE ALL ON TABLE public.oauth2_provider_application FROM postgres;
GRANT ALL ON TABLE public.oauth2_provider_application TO postgres;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.oauth2_provider_application TO "FrancaPaisa";


--
-- Name: SEQUENCE oauth2_provider_application_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE public.oauth2_provider_application_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE public.oauth2_provider_application_id_seq FROM postgres;
GRANT ALL ON SEQUENCE public.oauth2_provider_application_id_seq TO postgres;
GRANT ALL ON SEQUENCE public.oauth2_provider_application_id_seq TO "FrancaPaisa";


--
-- Name: TABLE oauth2_provider_grant; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE public.oauth2_provider_grant FROM PUBLIC;
REVOKE ALL ON TABLE public.oauth2_provider_grant FROM postgres;
GRANT ALL ON TABLE public.oauth2_provider_grant TO postgres;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.oauth2_provider_grant TO "FrancaPaisa";


--
-- Name: SEQUENCE oauth2_provider_grant_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE public.oauth2_provider_grant_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE public.oauth2_provider_grant_id_seq FROM postgres;
GRANT ALL ON SEQUENCE public.oauth2_provider_grant_id_seq TO postgres;
GRANT ALL ON SEQUENCE public.oauth2_provider_grant_id_seq TO "FrancaPaisa";


--
-- Name: TABLE oauth2_provider_idtoken; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE public.oauth2_provider_idtoken FROM PUBLIC;
REVOKE ALL ON TABLE public.oauth2_provider_idtoken FROM postgres;
GRANT ALL ON TABLE public.oauth2_provider_idtoken TO postgres;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.oauth2_provider_idtoken TO "FrancaPaisa";


--
-- Name: SEQUENCE oauth2_provider_idtoken_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE public.oauth2_provider_idtoken_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE public.oauth2_provider_idtoken_id_seq FROM postgres;
GRANT ALL ON SEQUENCE public.oauth2_provider_idtoken_id_seq TO postgres;
GRANT ALL ON SEQUENCE public.oauth2_provider_idtoken_id_seq TO "FrancaPaisa";


--
-- Name: TABLE oauth2_provider_refreshtoken; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE public.oauth2_provider_refreshtoken FROM PUBLIC;
REVOKE ALL ON TABLE public.oauth2_provider_refreshtoken FROM postgres;
GRANT ALL ON TABLE public.oauth2_provider_refreshtoken TO postgres;
GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.oauth2_provider_refreshtoken TO "FrancaPaisa";


--
-- Name: SEQUENCE oauth2_provider_refreshtoken_id_seq; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON SEQUENCE public.oauth2_provider_refreshtoken_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE public.oauth2_provider_refreshtoken_id_seq FROM postgres;
GRANT ALL ON SEQUENCE public.oauth2_provider_refreshtoken_id_seq TO postgres;
GRANT ALL ON SEQUENCE public.oauth2_provider_refreshtoken_id_seq TO "FrancaPaisa";


--
-- PostgreSQL database dump complete
--

