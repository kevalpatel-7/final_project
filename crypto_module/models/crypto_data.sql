-- Table: public.crypto_data

-- DROP TABLE public.crypto_data;

CREATE TABLE public.crypto_data
(
    id integer NOT NULL DEFAULT nextval('crypto_data_id_seq'::regclass),
    name character varying COLLATE pg_catalog."default",
    price double precision,
    price_date timestamp without time zone,
    market_cap double precision,
    market_cap_dominance double precision,
    rank integer,
    create_uid integer,
    create_date timestamp without time zone,
    write_uid integer,
    write_date timestamp without time zone,
    CONSTRAINT crypto_data_pkey PRIMARY KEY (id),
    CONSTRAINT crypto_data_create_uid_fkey FOREIGN KEY (create_uid)
        REFERENCES public.res_users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE SET NULL,
    CONSTRAINT crypto_data_write_uid_fkey FOREIGN KEY (write_uid)
        REFERENCES public.res_users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE SET NULL
)

TABLESPACE pg_default;

ALTER TABLE public.crypto_data
    OWNER to openpg;

COMMENT ON TABLE public.crypto_data
    IS 'crypto.data';

COMMENT ON COLUMN public.crypto_data.name
    IS 'name';

COMMENT ON COLUMN public.crypto_data.price
    IS 'Price';

COMMENT ON COLUMN public.crypto_data.price_date
    IS 'Price Date';

COMMENT ON COLUMN public.crypto_data.market_cap
    IS 'Market Cap';

COMMENT ON COLUMN public.crypto_data.market_cap_dominance
    IS 'market cap Dominance';

COMMENT ON COLUMN public.crypto_data.rank
    IS 'Rank';

COMMENT ON COLUMN public.crypto_data.create_uid
    IS 'Created by';

COMMENT ON COLUMN public.crypto_data.create_date
    IS 'Created on';

COMMENT ON COLUMN public.crypto_data.write_uid
    IS 'Last Updated by';

COMMENT ON COLUMN public.crypto_data.write_date
    IS 'Last Updated on';