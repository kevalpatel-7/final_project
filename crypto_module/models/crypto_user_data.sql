-- Table: public.user_data_crypto

-- DROP TABLE public.user_data_crypto;

CREATE TABLE public.user_data_crypto
(
    id integer NOT NULL DEFAULT nextval('user_data_crypto_id_seq'::regclass),
    experience character varying COLLATE pg_catalog."default",
    risk_amount double precision,
    start_date timestamp without time zone,
    end_date timestamp without time zone,
    code character varying COLLATE pg_catalog."default",
    create_uid integer,
    create_date timestamp without time zone,
    write_uid integer,
    write_date timestamp without time zone,
    CONSTRAINT user_data_crypto_pkey PRIMARY KEY (id),
    CONSTRAINT user_data_crypto_create_uid_fkey FOREIGN KEY (create_uid)
        REFERENCES public.res_users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE SET NULL,
    CONSTRAINT user_data_crypto_write_uid_fkey FOREIGN KEY (write_uid)
        REFERENCES public.res_users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE SET NULL
)

TABLESPACE pg_default;

ALTER TABLE public.user_data_crypto
    OWNER to openpg;

COMMENT ON TABLE public.user_data_crypto
    IS 'user.data.crypto';

COMMENT ON COLUMN public.user_data_crypto.experience
    IS 'Experience';

COMMENT ON COLUMN public.user_data_crypto.risk_amount
    IS 'Risk Amount';

COMMENT ON COLUMN public.user_data_crypto.start_date
    IS 'Start Date';

COMMENT ON COLUMN public.user_data_crypto.end_date
    IS 'End Date';

COMMENT ON COLUMN public.user_data_crypto.code
    IS 'Code';

COMMENT ON COLUMN public.user_data_crypto.create_uid
    IS 'Created by';

COMMENT ON COLUMN public.user_data_crypto.create_date
    IS 'Created on';

COMMENT ON COLUMN public.user_data_crypto.write_uid
    IS 'Last Updated by';

COMMENT ON COLUMN public.user_data_crypto.write_date
    IS 'Last Updated on';