CREATE TABLE raw_veri (
    tarih DATE,
    baraj_doluluk_yuzde DOUBLE PRECISION,
    yagis_mm DOUBLE PRECISION,
    gida_tufe_aylik_yuzde DOUBLE PRECISION,
    gida_tufe_yillik_yuzde DOUBLE PRECISION
);
COPY raw_veri FROM 'data/processed/dataset_final.csv' CSV HEADER;
CREATE VIEW aylik_ozet AS
SELECT date_trunc('month', tarih)::date AS ay,
       AVG(baraj_doluluk_yuzde) AS baraj_ort,
       AVG(yagis_mm) AS yagis_ort,
       MAX(gida_tufe_aylik_yuzde) AS gida_aylik,
       MAX(gida_tufe_yillik_yuzde) AS gida_yillik
FROM raw_veri GROUP BY 1 ORDER BY 1;
SELECT corr(baraj_doluluk_yuzde, gida_tufe_aylik_yuzde) AS r_lag0 FROM raw_veri;
