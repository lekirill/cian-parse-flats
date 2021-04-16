-- reference for tasks:

CREATE SEQUENCE IF NOT EXISTS public.flats_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

CREATE TABLE IF NOT EXISTS public.flats (
	id                      bigint NOT NULL DEFAULT nextval('public.flats_seq'),
	flat_id                 bigint NOT NULL,
	cian_id                  bigint NOT NULL,
	raw_data                jsonb NOT NULL,
	added_timestamp          timestamp NOT NULL,
	total_area               numeric NULL,
	price_rur                bigint NULL,
	meter_price              float NULL,
	full_url                 text NULL,
	from_developer           bool NULL,
	is_premium           bool NULL,
	kitchen_area             float NULL,
	is_apartments            bool NULL,
	jk_url                   text NULL,
	floors_count             int NULL,
	build_year               int NULL,
	material_type            text NULL,
	coordinates_lat         float NULL,
	coordinates_lng         float NULL,
	distance_from_center     float NULL,
	nearest_underground      text NULL,
	nearest_underground_dist   int NULL,
    balconies_count          int NULL,
    floor_number             int NULL,
    is_by_homeowner            bool NULL,
    rooms_count              int NULL,
	created_at              timestamp NOT NULL DEFAULT now()::timestamp without time zone,
	updated_at              timestamp NULL,

	CONSTRAINT task_type_pk PRIMARY KEY (id),
	UNIQUE(flat_id, cian_id)

);

CREATE index "flats_id_idx" on public."flats"("id");
CREATE index "flats_created_at_idx" on public."flats"("created_at");
CREATE index "flats_price_rur_idx" on public."flats"("price_rur");

