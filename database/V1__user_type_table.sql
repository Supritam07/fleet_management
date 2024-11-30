CREATE TABLE public.user_type
(
    id serial,
    user_type character varying(100) NOT NULL,
    created_date timestamp with time zone NOT NULL,
    modified_date time with time zone NOT NULL,
    created_by integer NOT NULL DEFAULT 1,
    modified_by integer NOT NULL DEFAULT 1,
    is_deleted boolean NOT NULL DEFAULT True,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.user_type
    OWNER to postgres;

GRANT SELECT ON public.user_type TO postgres;
GRANT INSERT, UPDATE ON public.user_type TO postgres;
GRANT INSERT, UPDATE, SELECT, DELETE ON ALL TABLES IN SCHEMA public TO postgres;
