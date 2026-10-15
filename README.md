# 2026 Baraj Krizi vs Gıda Enflasyonu
Kuraklık market fiyatlarını ne kadar sürede etkiliyor? Bu projede İstanbul baraj doluluk oranları ile gıda enflasyonunu aynı tabloda buluşturdum.
2026 Türkiye için sıradan bir yıl değil. Barajlar 10 yıllık ortalamanın neredeyse yarısına düştü ve aynı dönemde gıda fiyatları %60'ın üzerinde seyrediyor.
## Ne yaptım?
- İSKİ günlük baraj verilerini ve TCMB EVDS üzerinden gıda TÜFE serisini çektim.
- Günlük verileri aylığa çevirdim ve tek datasette birleştirdim.
- 1 ay gecikmeyle korelasyon -0.84 çıktı.
## Çalıştırma
pip install -r requirements.txt
python src/main.py
python src/analysis.py
