# Notas de curso PostgreSQL

### Creación de la tabla data

***Crear la tabla***
```
-- Crear tabla
CREATE TABLE data(
    gender varchar(10),
    height numeric,
    weight numeric
);
```
***Llenar la tabla***
```
--Poblarla (mediante un bloque anonimo de PL/pgSQL) 150 registros
DO $$DECLARE r record;
BEGIN 
  FOR i IN 1..150 LOOP
    INSERT INTO data 
    SELECT
      (SELECT CASE WHEN CEIL(RANDOM()*2) = 1 THEN 'Male' ELSE 'Female' END) as gender,
      (SELECT 72 - ROUND((RANDOM()*3)::numeric, 2)) as height,  -- esto genera valores entre 69 y 72
      (SELECT 100 - ROUND((RANDOM()*45)::numeric,2)) as weight
    ;
   END LOOP;
END$$
```
