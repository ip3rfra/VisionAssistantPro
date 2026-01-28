Profesyonel Görsel Asistan Dokümantasyonu

# Profesyonel Görsel Asistan

**Profesyonel Görsel Asistan**, NVDA için gelişmiş, çok modlu bir yapay zekâ asistanıdır. Google’ın Gemini modellerini kullanarak akıllı ekran okuma, çeviri, sesli dikte ve belge analiz yetenekleri sunar.

Bu eklenti, Engelliler Uluslararası Günü onuruna topluluğa sunulmuştur.

## 1. Kurulum ve Yapılandırma

**NVDA Menüsü > Tercihler > Ayarlar > Profesyonel Görsel Asistan** yolunu izleyin.

- **API Anahtarı:** Gereklidir. [Google AI Studio](https://aistudio.google.com/) üzerinden ücretsiz bir anahtar alabilirsiniz. Birden fazla anahtar girebilirsiniz (virgülle veya yeni satırlarla ayırarak). Kota sınırına ulaşıldığında asistan otomatik olarak bunlar arasında geçiş yapacaktır.
- **Yapay Zeka Modeli:** **Flash** (En Hızlı/Ücretsiz), **Lite** veya **Pro** (Yüksek Zeka) modelleri arasından seçim yapın.
- **Proxy Adresi:** İsteğe bağlı. Bölgenizde Google engellenmişse bunu kullanın. Gemini API'sine köprü görevi gören bir web adresi olmalıdır. İsteklerinizi alan ve Gemini API'sine ileten bir sunucu adresine (URL) ihtiyacınız vardır.
  > **Not:** Bu, standart VPN/SOCKS proxy'leri için **değildir** ('127.0.0.1:1080' gibi). Google'a köprü görevi gören bir web adresi (ör. "https://my-custom-proxy.com") olmalıdır.
- **OCR Motoru:** Hızlı sonuçlar için **Chrome (Hızlı)** veya üstün düzen koruması ve tablo tanıma için **Gemini (Biçimlendirilmiş)** arasında seçim yapın.
- **TTS Sesi:** Belge sayfalarından ses dosyaları oluşturmak için tercih edilen ses stilini seçin.
- **Diller:** Kaynak, Hedef ve Yapay Zekâ Yanıt dillerini ayarlayın.
- **Akıllı takas:** Kaynak metin hedef dille eşleşirse dilleri otomatik olarak değiştirir.
- **Doğrudan Çıktı:** Sohbet penceresini atlar ve yanıtı doğrudan konuşma yoluyla duyurur.
- **Pano Entegrasyonu:** Yapay zeka yanıtını otomatik olarak panoya kopyalar.

## 2. Komut Katmanı ve Kısayollar

Klavye kısayol çakışmalarını önlemek için bu eklenti bir **Komut Katmanı** kullanır.

1. Katmanı etkinleştirmek için **NVDA + Shift + V** (Ana Tuş) tuşlarına basın (bir bip sesi duyacaksınız).
2. Tuşları bırakın, ardından aşağıdaki tek tuşlardan birine basın:

| Tuş           | İşlev                   | Açıklama                                                                                    |
| ------------- | ----------------------- | ------------------------------------------------------------------------------------------- |
| **T**         | Akıllı Çeviri         | Dolaşım imleci altındaki veya seçili metni çevirir.                                         |
| **Shift + T** | Panodan Çeviri          | Panodaki mevcut içeriği çevirir.                                                            |
| **R**         | Metin İyileştirici      | Özetler, Dilbilgisini Düzeltir, Açıklar veya **Özel İstemler** çalıştırır.                  |
| **V**         | Görsel Nesne            | Mevcut dolaşım nesnesini betimler.                                                            |
| **O**         | Tam Ekran görseli        | Tüm ekran düzenini ve içeriğini analiz eder.                                                |
| **Shift + V** | Çevrimiçi Video Analizi | **YouTube** veya **Instagram** videolarını Bağlantı üzerinden analiz eder.                       |
| **D**         | Belge Analizi           | PDF/TXT/MD/PY dosyaları hakkında sohbet eder.                                                     |
| **F**         | Dosya OCR               | Görüntü/PDF/TIFF dosyalarından doğrudan OCR yapar (Çok sayfalı TIFF desteklenir).           |
| **A**         | Ses Transkripsiyonu     | MP3/WAV/OGG dosyalarını yazıya döker.                                                       |
| **C**         | CAPTCHA Çözücü          | CAPTCHA’yı otomatik olarak yakalar ve çözer.                                                |
| **S**         | Akıllı Dikte            | Konuşmayı metne dönüştürür. Kaydı başlatmak için basın, durdurmak/yazmak için tekrar basın. |
| **L**         | Durumu Seslendir         | Mevcut durumu seslendirir (örn. "Yükleniyor...", "Boşta").                                      |
| **U**         | Güncelleme Kontrolü     | GitHub üzerinden en son sürümü denetler.                                                |
| **H** | Komut Yardımı | Kullanılabilir tüm kısayol tuşlarının kapsamlı bir listesini ve bunların komut katmanındaki açıklamalarını görüntüler. |

### 2.1 Belge Okuyucu Kısayolları (İç Görüntüleyici)
**D** komutuyla bir belge açıldığında:
- **Ctrl + Sayfa Aşağı:** Sonraki sayfaya gider (sayfa numarasını duyurur).
- **Ctrl + Sayfa Yukarı:** Önceki sayfaya gider (sayfa numarasını duyurur).
- **Alt + A:** Belgeyle ilgili sorular sormak için bir sohbet iletişim kutusu açar.
- **Alt + R:** Gemini motorunu kullanarak geçerli sayfanın veya tüm sayfaların yeniden taranmasını zorlar.
- **Alt + G:** İçerikten yüksek kaliteli bir ses dosyası (WAV) oluşturur ve kaydeder.
- **Alt + S / Ctrl + S:** Çıkarılan metni TXT veya HTML dosyası olarak kaydeder.

## 3. Özel İstemler ve Değişkenler

Ayarlar bölümünde komutlar oluşturun: `Ad:İstem Metni` (`|` veya yeni satır ile ayırın).

### Kullanılabilir Değişkenler

| Değişken        | Açıklama                                        | Girdi Türü         |
| --------------- | ----------------------------------------------- | ------------------ |
| `[selection]`   | Seçili olan metin                               | Metin              |
| `[clipboard]`   | Pano içeriği                                    | Metin              |
| `[screen_obj]`  | Dolaşım nesnesinin ekran görüntüsü                 | Görüntü            |
| `[screen_full]` | Tam ekran görüntüsü                             | Görüntü            |
| `[file_ocr]`    | Görüntü/PDF/TIFF seç (varsayılan “Metni çıkar”) | Görüntü, PDF, TIFF |
| `[file_read]`   | Metin belgesi seç                               | TXT, Kod, PDF      |
| `[file_audio]`  | Ses dosyası seç                                 | MP3, WAV, OGG      |

### Örnek Özel İstemler

* **Hızlı OCR:** `My OCR:[file_ocr]`
* **Görüntü Çevir:** `Translate Img:Bu görüntüden metni çıkar ve Farsçaya çevir. [file_ocr]`
* **Ses Analizi:** `Summarize Audio:Bu kaydı dinle ve ana noktaları özetle. [file_audio]`
* **Kod Hata Ayıklayıcı:** `Debug:Bu koddaki hataları bul ve açıkla: [selection]`

**Not:** Tüm yapay zekâ özellikleri için aktif bir internet bağlantısı gereklidir. Çok sayfalı TIFF dosyaları otomatik olarak işlenir.

## 4.0.1 için değişiklikler
*   **Gelişmiş Belge Okuyucu:** Sayfa aralığı seçimi, arka planda işleme ve kesintisiz "Ctrl+Sayfa Yukarı/Aşağı" dolaşma özellikleriyle PDF ve görüntüler için yeni ve güçlü bir görüntüleyici.
*   **Yeni Araçlar Alt Menüsü:** Temel özelliklere, ayarlara ve belgelere daha hızlı erişim için NVDA'nın Araçlar menüsü altına özel bir "Görsel Asistan" alt menüsü eklendi.
*   **Esnek Özelleştirme:** Artık tercih ettiğiniz OCR motorunu ve TTS sesini doğrudan ayarlar panelinden seçebilirsiniz.
*   **Çoklu API Anahtarı Desteği:** Birden fazla Gemini API anahtarı için destek eklendi. Ayarlarda her satıra bir anahtar girebilir veya bunları virgülle ayırabilirsiniz.
*   **Alternatif OCR Motoru:** Gemini API kota sınırlarına ulaşıldığında bile güvenilir metin tanıma sağlamak için yeni bir OCR motoru kullanıma sunuldu.
*   **Akıllı API Anahtarı Döndürme:** Kota sınırlarını aşmak için otomatik olarak en hızlı çalışan API anahtarına geçiş yapar ve onu hatırlar.
*   **MP3/WAV'a belge Dönüştürme:** Hem MP3 (128kbps) hem de WAV formatlarında yüksek kaliteli ses dosyalarını doğrudan okuyucunun içinde oluşturma ve kaydetmeye yönelik entegre yetenek.
*   **Instagram Hikayeleri Desteği:** URL'lerini kullanarak Instagram Hikayelerini tanımlama ve analiz etme yeteneği eklendi.
*   **TikTok Desteği:** Kliplerin tam görsel betimlemesine ve sesli transkripsiyonuna olanak tanıyan TikTok videoları için destek eklendi.
*   **Yeniden Tasarlanan Güncelleme İletişim Kutusu:** Yüklemeden önce sürüm değişikliklerini net bir şekilde okumak için kaydırılabilir bir metin kutusu içeren yeni, erişilebilir bir arayüz içerir.
*   **Birleşik Durum ve UX:** Eklenti genelinde standartlaştırılmış dosya iletişim kutuları ve gerçek zamanlı ilerlemeyi bildirmek için 'L' komutu geliştirildi.

## 3.6.0 için değişiklikler
* **Yardım Sistemi:** Tüm kısayolların ve işlevlerinin kolay erişilebilen bir listesini sağlamak için Komut Katmanı içine bir yardım komutu (`H`) eklendi.
* **Çevrimiçi Video Analizi:** **Twitter (X)** videolarını içerecek şekilde genişletilmiş destek. Ayrıca daha güvenilir bir deneyim için iyileştirilmiş Bağlantı algılama ve kararlılık.
* **Proje Katkısı:** Projenin gelecekteki güncellemelerini ve sürekli büyümesini desteklemek isteyen kullanıcılar için isteğe bağlı bir bağış iletişim kutusu eklendi.

## 3.5.0 için değişiklikler
*   **Komut Katmanı:** Kısayolları tek bir ana tuş altında gruplamak için bir Komut Katmanı sistemi (varsayılan: `NVDA+Shift+V`) kullanıma sunuldu. Örneğin, çeviri için 'NVDA+Control+Shift+T' tuşlarına basmak yerine artık 'NVDA+Shift+V' ve ardından 'T' tuşlarına basıyorsunuz.
*   **Çevrimiçi Video Analizi:** YouTube ve Instagram videolarını bir Bağlantı sağlayarak doğrudan analiz etmek için yeni bir özellik eklendi.

## 3.1.0 için değişiklikler
* **Doğrudan Çıktı Modu:** Daha hızlı ve daha kusursuz bir deneyim için sohbet iletişim kutusunu atlayıp yapay zeka yanıtlarını doğrudan konuşma yoluyla duyma seçeneği eklendi.
* **Pano Entegrasyonu:** Yapay zeka yanıtlarını otomatik olarak panoya kopyalamak için yeni bir ayar eklendi.

## 3.0 için Değişiklikler

* **Yeni Diller:** **Farsça** ve **Vietnamca** çeviriler eklendi.
* **Genişletilmiş Yapay Zekâ Modelleri:** Model seçim listesi, ücretsiz ve hız sınırlı (ücretli) modelleri ayırt etmeye yardımcı olmak için (`[Free]`, `[Pro]`, `[Auto]`) önekleriyle yeniden düzenlendi. **Gemini 3.0 Pro** ve **Gemini 2.0 Flash Lite** desteği eklendi.
* **Dikte Kararlılığı:** Akıllı Dikte önemli ölçüde iyileştirildi. 1 saniyeden kısa ses kliplerini yok sayan bir güvenlik kontrolü eklendi; böylece yapay zekâ halüsinasyonları ve boş hatalar önlendi.
* **Dosya İşleme:** İngilizce olmayan isimlere sahip dosyaların yüklenememesine neden olan bir sorun düzeltildi.
* **İstem Optimizasyonu:** Çeviri mantığı geliştirildi ve Görüntü sonuçları daha yapılandırılmış hale getirildi.

## 2.9 için Değişiklikler

* **Fransızca ve Türkçe çeviriler eklendi.**
* **Biçimlendirilmiş Görünüm:** Sohbet diyaloglarında, konuşmayı başlıklar, kalın metinler ve kodlarla birlikte düzgün biçimde görüntülemek için “Biçimlendirilmiş Görünüm” düğmesi eklendi.
* **Markdown Ayarı:** Ayarlara “Sohbette Markdown Temizle” adlı yeni bir seçenek eklendi. Bu seçenek işaretlenmezse, kullanıcılar ham Markdown sözdizimini (`**`, `#` gibi) sohbet penceresinde görebilir.
* **Diyalog Yönetimi:** “Metni İyileştir” veya sohbet pencerelerinin birden fazla kez açılması ya da odağı doğru alamaması sorunu düzeltildi.
* **UX İyileştirmeleri:** Dosya iletişim kutusu başlıkları “Aç” olarak standartlaştırıldı ve daha akıcı bir deneyim için gereksiz sesli duyurular kaldırıldı (ör. “Menü açılıyor…”).

## 2.8 için Değişiklikler

* İtalyanca çeviri eklendi.
* **Durum Bildirimi:** Eklentinin mevcut durumunu (ör. “Yükleniyor…”, “Analiz ediliyor…”) duyurmak için yeni bir komut (NVDA+Control+Shift+I) eklendi.
* **HTML Dışa Aktarma:** Sonuç diyaloglarındaki “İçeriği Kaydet” düğmesi artık çıktıyı başlıklar ve kalın metinler gibi stilleri koruyarak biçimlendirilmiş bir HTML dosyası olarak kaydeder.
* **Ayarlar Arayüzü:** Ayarlar paneli, erişilebilir gruplamalarla iyileştirildi.
* **Yeni Modeller:** gemini-flash-latest ve gemini-flash-lite-latest desteği eklendi.
* **Diller:** Desteklenen dillere Nepalce eklendi.
* **İyileştirme Menüsü Mantığı:** NVDA arayüz dili İngilizce olmadığında “Metni İyileştir” komutlarının çalışmamasına neden olan kritik bir hata düzeltildi.
* **Dikte:** Konuşma girişi olmadığında yanlış metin üretimini önlemek için sessizlik algılama geliştirildi.
* **Güncelleme Ayarları:** “Başlangıçta güncellemeleri kontrol et” seçeneği, Eklenti Mağazası politikalarına uyum için varsayılan olarak devre dışı bırakıldı.
* Kod temizliği yapıldı.

## 2.7 için Değişiklikler

* Proje yapısı, daha iyi standart uyumluluğu için resmi NV Access Eklenti Şablonuna taşındı.
* Yüksek trafik sırasında güvenilirliği sağlamak için HTTP 429 (Hız Sınırı) hataları için otomatik yeniden deneme mantığı uygulandı.
* Daha yüksek doğruluk ve daha iyi “Akıllı Değiş Tokuş” mantığı için çeviri istemleri optimize edildi.
* Rusça çeviri güncellendi.

## 2.6 için Değişiklikler

* Rusça çeviri desteği eklendi (nvda-ru’ya teşekkürler).
* Bağlantı sorunlarıyla ilgili daha açıklayıcı geri bildirim sağlamak için hata mesajları güncellendi.
* Varsayılan hedef dil İngilizce olarak değiştirildi.

## 2.5 için Değişiklikler

* Yerel Dosya OCR Komutu eklendi (NVDA+Control+Shift+F).
* Sonuç diyaloglarına “Sohbeti Kaydet” düğmesi eklendi.
* Tam yerelleştirme desteği (i18n) uygulandı.
* Sesli geri bildirimler NVDA’nın yerel tonlar modülüne taşındı.
* PDF ve ses dosyalarının daha iyi işlenmesi için Gemini Dosya API’sine geçildi.
* Süslü parantez içeren metinler çevrilirken oluşan çökme düzeltildi.

## 2.1.1 için Değişiklikler

* `[file_ocr]` değişkeninin Özel İstemler içinde doğru çalışmamasına neden olan bir sorun düzeltildi.

## 2.1 için Değişiklikler

* NVDA’nın Dizüstü düzeni ve sistem kısayollarıyla çakışmaları önlemek için tüm kısayollar NVDA+Control+Shift olarak standartlaştırıldı.

## 2.0 için Değişiklikler

* Dahili Otomatik Güncelleme sistemi uygulandı.
* Önceden çevrilmiş metinlerin anında alınması için Akıllı Çeviri Önbelleği eklendi.
* Sohbet diyaloglarında sonuçları bağlamsal olarak iyileştirmek için Konuşma Hafızası eklendi.
* Ayrı Pano Çevirisi komutu eklendi (NVDA+Control+Shift+Y).
* Yapay zekâ istemleri, hedef dil çıktısını kesin olarak zorlayacak şekilde optimize edildi.
* Girdi metnindeki özel karakterlerin neden olduğu çökme düzeltildi.

## 1.5 için Değişiklikler

* 20’den fazla yeni dil desteği eklendi.
* Takip soruları için Etkileşimli İyileştirme Diyaloğu uygulandı.
* Yerel Akıllı Dikte özelliği eklendi.
* NVDA’nın Girdi Hareketleri diyaloguna “Vision Assistant” kategorisi eklendi.
* Firefox ve Word gibi belirli uygulamalarda oluşan COMError çökmeleri düzeltildi.
* Sunucu hataları için otomatik yeniden deneme mekanizması eklendi.

## 1.0 için Değişiklikler

* İlk sürüm.

