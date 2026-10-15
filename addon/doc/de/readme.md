# KI Assistent pro Dokumentation

<!-- DOWNLOAD_COUNT_START --> Total Downloads: 75,451 <!-- DOWNLOAD_COUNT_END -->

**KI Assistent pro** ist ein fortschrittlicher, multimodaler KI-Assistent für NVDA. Er nutzt erstklassige KI-Engines, um intelligentes Screenreading, Übersetzungen, Sprachdiktate und Dokumentenanalysen zu ermöglichen.

_Dieses Add-on wurde zu Ehren des Internationalen Tages der Menschen mit Behinderungen für die Community veröffentlicht._

## 1. Einrichtung & Konfiguration

Gehen Sie zu **NVDA-Menü > Optionen > Einstellungen > KI Assistent pro**. Das Einstellungsfenster ist in 9 barrierefreie Reiter unterteilt: **Verbindung**, **Live-Assistent**, **KI-Verhalten**, **Übersetzungssprachen**, **Dokumentenleser**, **Video**, **CAPTCHA**, **Prompts** und **Erweitert**.

### 1.1 Verbindung Reiter

- **Anbieter:** Wählen Sie Ihren bevorzugten KI-Dienst. Unterstützte Anbieter sind **Google Gemini**, **OpenAI**, **Mistral**, **Groq**, **MiniMax** und **Benutzerdefiniert** (OpenAI-kompatible Server wie Ollama, LM Studio, Jan.ai oder KoboldCPP).
- **API-Schlüssel:** Geben Sie einzelne oder mehrere API-Schlüssel ein (getrennt durch Kommas oder neue Zeilen), um eine automatische Rotation zu ermöglichen.
- **Modelle abrufen:** Nachdem Sie Ihren API-Schlüssel eingegeben haben, drücken Sie diese Schaltfläche, um die aktuelle Liste der verfügbaren Modelle vom Anbieter herunterzuladen.
- **KI-Modell:** Wählen Sie das Hauptmodell aus, das für den allgemeinen Chat und die Analysen verwendet werden soll.
- **Erweitertes Modell-Routing (aufgabenspezifisch):** Wählen Sie optional über Auswahllisten eigene Modelle für OCR, STT, TTS, KI-Operator, Video und Live-Assistent. Bei Gemini werden die Modelle dynamisch und übersichtlich nach ihren Fähigkeiten sortiert.
- **Einstellungen für benutzerdefinierte Anbieter:** Konfigurieren Sie lokale oder benutzerdefinierte Endpunkte. Enthält **Lokale KI einrichten** (Ein-Klick-Konfiguration für Ollama, LM Studio, Jan.ai oder KoboldCPP) und die **Erweiterte Endpunkt-Konfiguration**.
- **Proxy-Konfiguration:** Volle Unterstützung für Tunneling und Endpunkt-Umleitung im gesamten Add-on (einschließlich Live-Assistent, Ambient Observer und TTS). Geben Sie Ihre **Proxy-URL** ein und wählen Sie Ihren **Proxy-Modus**:
  - **Automatisch erkennen:** Erkennt automatisch, ob es sich bei der URL um einen Forward-Proxy oder einen Reverse-Proxy handelt.
  - **SOCKS5-Proxy:** Erzwingt Forward-Tunneling über SOCKS5 mit Benutzername/Passwort-Authentifizierung nach RFC 1929 und Auflösung von Domainnamen.
  - **HTTP-Proxy:** Erzwingt Forward-Tunneling über einen HTTP-Proxy mit Basic-Authentifizierung.
  - **Reverse-Proxy:** Direkter Ersatz des Endpunkts für benutzerdefinierte KI-Gateways und selbst gehostete Spiegelserver (Anmeldedaten sind in diesem Modus deaktiviert).
- **Proxy-Verbindung testen:** Eine nicht blockierende Schaltfläche, die die Verbindung prüft und die Server-Latenz in Millisekunden misst (von NVDA angesagt).
- **Verbindungs- & Ausgabeoptionen:** Konfigurieren Sie Proxy-URL, Update-Prüfung beim Start, Bereinigtes Markdown im Chat, KI-Antworten in die Zwischenablage kopieren und Direkte Ausgabe (Kein Chat-Fenster).
- **Chats im Verlauf speichern:** Behalten Sie Ihre Chat-Gespräche in der Verlaufsliste.

### 1.2 Live-Assistent Reiter

- **Live-Assistent: Direkte Ausgabe (Kein Fenster):** Startet den Live-Assistenten ohne eigenes Konversationsfenster; öffnen Sie dieses später jederzeit über das Kürzel für das letzte Ergebnis (`Leertaste`).
- **Push-to-Talk:** Schaltet den Push-to-Talk-Modus um. Wenn aktiviert, überträgt das Mikrofon Audio nur, solange Sie die zugewiesene Taste gedrückt halten.
- **Push-to-Talk-Taste:** Drücken Sie die gewünschte Tastenkombination zur Aufzeichnung des Kürzels (z. B. `F12` oder `Strg+F12`) – selbst einzelne Modifikatortasten wie `Linke Strg-Taste` werden unterstützt. Halten Sie die Taste zum Sprechen gedrückt und lassen Sie sie los, um zu beenden; ein kurzer Signalton bestätigt jedes Drücken und Loslassen.

_Hinweis: Dieser Reiter wird nur angezeigt, wenn **Google Gemini** (oder ein Gemini-kompatibler benutzerdefinierter Anbieter) als aktiver Anbieter eingestellt ist._

### 1.3 AI Behavior Tab

- **Kreativität (Temperatur):** Steuert die Zufälligkeit und Kreativität der KI (von 0.0 bis 2.0). Niedrigere Werte liefern deterministischere und präzisere Übersetzungs- und OCR-Ergebnisse.

### 1.4 Übersetzungssprachen Reiter

- **Quellsprache:** Wählen Sie Ihre Standard-Eingabesprache.
- **Zielsprache:** Wählen Sie Ihre primäre Übersetzungssprache.
- **KI-Antwortsprache:** Wählen Sie die Sprache für allgemeine KI-Antworten.
- **Smart Swap (Intelligenter Tausch):** Tauscht Quell- und Zielsprache automatisch basierend auf der erkannten Eingabe.

### 1.5 Dokumentenleser Reiter

- **OCR-Engine:** Wählen Sie zwischen **Chrome (Schnell)** für schnelle Ergebnisse oder **KI (Erweitert)** für eine überlegene Beibehaltung des Layouts.
- **OCR-Stapelgröße:** Geben Sie die Seiten pro Anfrage an (auf 0 setzen für Einzelanfragen-Verarbeitung).
- **Bilder inline beschreiben:** Schaltet die Beschreibung von Bildern direkt im Textfluss während der Textextraktion ein oder aus.
- **Seitenzahlen exportieren:** Schaltet Seitenzahlen und Trennlinien bei mehrseitigen Dokumentausgaben ein oder aus.
- **TTS-Stimme:** Wählen Sie Ihren bevorzugten Stimmenstil für die Audioerzeugung.
- **Dokumente im Verlauf speichern:** Behalten Sie geöffnete Dokumente in der Verlaufsliste; zwischengespeicherte OCR-Texte und Wiederaufnahmedaten bleiben ohnehin gespeichert.

### 1.6 Video Reiter

- **Video-Segmentgröße:** Dauer der Abschnitte in Minuten für die Erstellung von Audiobeschreibungen (auf 0 setzen, um die gesamte Datei auf einmal zu verarbeiten).
- **Charakterliste hinzufügen:** Option, das Charakter-Wörterbuch als ersten Untertiteleintrag einzufügen.
- **KI-Haftungsausschluss hinzufügen:** Option, einen Hinweis auf KI-Generierung am Anfang von SRT-Untertiteln einzufügen.
- **Charakter-Wörterbuch & Serienverwaltung:** Erstellen, bearbeiten, importieren und verwalten Sie Charakternamen, physische Beschreibungen und Rollen pro Serie – die KI gleicht erkannte Charaktere automatisch mit Ihrem Wörterbuch ab und fügt im Laufe neuer Episoden weitere hinzu. Ihre manuellen Notizen genießen stets Vorrang vor KI-Aktualisierungen, während physische Beschreibungen über alle Episoden hinweg aktuell bleiben.

### 1.7 CAPTCHA Reiter

- **Visuellen CAPTCHA-Löser aktivieren:** Schaltet das automatische Lösen visueller Aufgaben (hCaptcha, reCAPTCHA) ein oder aus.
- **Text-CAPTCHA-Methode:** Wählen Sie zwischen der Erfassung des **Navigator-Objekts** oder des **Vollbilds**.

### 1.8 Prompts Reiter

- **System-Prompt für Direkten Chat:** Der Direkte Chat (`Umschalt+C`) besitzt nun einen eigenen editierbaren System-Prompt („Direct Chat Instruction“), um Persönlichkeit und Ausgabesprache festzulegen.
- **Eigene Prompt-Tastenkombinationen:** Weisen Sie jedem benutzerdefinierten Prompt direkt im Prompt-Manager ein eigenes Tastaturkürzel zu. Drücken Sie die Tasten zur Aufnahme – Einzeltasten funktionieren innerhalb der Befehlsebene (und global als `NVDA + Umschalt + Taste`), Tastenkombinationen wie `Strg + Umschalt + 1` funktionieren eigenständig global.
- **Ausgabeverhalten pro Prompt:** Legen Sie für jeden Prompt einzeln fest, wie sein Ergebnis ausgegeben wird (Globale Einstellung, In die Zwischenablage kopieren, Direkte Ausgabe / NVDA-Meldung, In die Zwischenablage kopieren + Direkte Ausgabe oder Chat-Fenster).

### 1.9 Erweitert Reiter & Globales Logging

Navigieren Sie zum Reiter **Erweitert**, um das globale Logging des Add-ons zu konfigurieren:

- **Dedizierte Log-Datei aktivieren:** Schaltet die Protokollierung aller betrieblichen Ereignisse, API-Anfragen und Fehler über alle Module hinweg in eine separate Datei (`vision_assistant.log`) ein.
- **Log-Level:** Wählen Sie die Detailtiefe zwischen **Debug (Alle Details)**, **Info (Allgemeine Informationen)**, **Warnung (Nur Warnungen)** und **Fehler (Nur Fehler)**.
- **Logs aufbewahren für:** Legen Sie automatische Aufbewahrungsfristen fest, um ältere Log-Einträge automatisch zu bereinigen (von 1 Stunde bis 90 Tage).
- **Log-Verwaltung:** Nutzen Sie **Log-Datei öffnen**, **Log-Ordner öffnen** oder **Log-Datei löschen**, um Protokolldaten direkt zu überprüfen oder zu bereinigen, ohne NVDA neu zu starten oder reguläre NVDA-Protokolle zu beeinträchtigen.
- **Einheitliches Datenverzeichnis:** Alle Datendateien des Add-ons (Verlauf, Serien, Beschriftungen, OCR-Fortschritte, Caches und Logs) werden in einem einzigen `VisionAssistant`-Ordner innerhalb Ihres NVDA-Konfigurationsverzeichnisses gespeichert – das hält Ordnung und macht manuelle Backups zum Kinderspiel.

### 1.10 Einstellungen sichern & wiederherstellen

Der Reiter **Erweitert** enthält zudem einen Bereich für **Sichern und Wiederherstellen**:

- **Sichern:** Speichert Ihre Konfiguration in einer einzelnen JSON-Datei. Beim Klick wählen Sie den Umfang: **Alles** (Einstellungen, benutzerdefinierte Beschriftungen, OCR-Fortschritte und Verlauf) oder **Nur Einstellungen**.
- **Wiederherstellen:** Lädt ein zuvor gespeichertes Backup, um Ihre Einstellungen und Daten jederzeit, auf jedem System oder nach einer NVDA-Neuinstallation wiederherzustellen. Sie werden vorab um Bestätigung gebeten, da das Wiederherstellen alle aktuellen Einstellungen und Daten ersetzt.

## 2. Gemini-API-Schlüsselmanager

Das Erstellen eines Gemini-API-Schlüssels auf **aistudio.google.com** war bisher der schwierigste Schritt des Add-ons. Mit einem Screenreader waren die Seiten unübersichtlich, und manche Menschen konnten schlicht gar keinen Schlüssel anlegen. Der **Gemini-API-Schlüsselmanager** löst dieses Problem. Drücken Sie **G** in der Befehlsebene oder öffnen Sie **NVDA-Menü > Optionen > Einstellungen > KI Assistent pro > Verbindung** und drücken Sie **Gemini-API-Schlüssel abrufen...**.

- **Anmelden:** Wenn Sie den Manager öffnen, startet Ihr Standardbrowser direkt mit der sicheren Anmeldeseite von Google. Melden Sie sich mit Ihrem Google-Konto an – externe Werkzeuge, SDKs oder Kommandozeilen-Einrichtungen sind nicht erforderlich. Das angemeldete Konto wird stets auf der Schaltfläche **Abmelden** angezeigt.
- **Schlüssel erstellen:** Nach der Anmeldung können Sie ohne jede Vorbereitung sofort mit **Neues Projekt und Schlüssel** einen Schlüssel erstellen. Haben Sie bereits Projekte, erscheinen diese in einer einfachen Liste, in der Sie eines auswählen und **Schlüssel für ausgewähltes Projekt erstellen** drücken können.
- **Was danach passiert:** Der neue Schlüssel wird sofort in die Zwischenablage kopiert, zur späteren Verwendung im Add-on gespeichert, und Sie werden einmalig gefragt, ob er zur Schlüsselliste des Add-ons hinzugefügt werden soll. Mehr ist nicht nötig – keine Webseiten, auf denen Sie suchen müssen.
- **Mit Ihren Schlüsseln arbeiten:** **Schlüssel des ausgewählten Projekts kopieren** kopiert den Schlüssel des gewählten Projekts, **Zuletzt erstellten Schlüssel kopieren** kopiert den Schlüssel, den Sie gerade erstellt haben, und **Gespeicherte Schlüssel als CSV exportieren...** speichert alle von Ihnen erstellten Schlüssel in einer Datei.
- **Schlüssel löschen:** **Schlüssel löschen...** zeigt die Schlüssel des ausgewählten Projekts an, fragt, welcher entfernt werden soll, und bittet vor dem Löschen um Bestätigung. Ein gelöschter Schlüssel wird auch aus der Schlüsselliste des Add-ons entfernt, sodass nie ein ungültiger Schlüssel in der Rotation zurückbleibt. Auch außerhalb des Add-ons erstellte Schlüssel können gelöscht werden, sofern Ihr Konto Berechtigungen für das jeweilige Projekt hat.
- **Abmelden:** **Abmelden** entfernt die gespeicherten Anmeldeinformationen von Ihrem Computer, sodass Sie jederzeit zu einem anderen Konto wechseln können.

## 3. Befehlsebene & Tastenkombinationen

Um Tastaturkonflikte zu vermeiden, verwendet dieses Add-on eine **Befehlsebene**.

1. Drücken Sie **NVDA + Umschalt + V** (Haupttaste), um die Ebene zu aktivieren (Sie hören einen Signalton).
2. Lassen Sie die Tasten los und drücken Sie dann eine der folgenden Einzeltasten:

| Key                | Funktion                                                   | Beschreibung                                                                                                                                                                                                                                                                                          |
| ------------------ | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Umschalt + A**   | **KI-Operator**                                            | **Autonome Steuerung:** Weisen Sie die KI an, eine Aufgabe auf Ihrem Bildschirm auszuführen. Erneutes Drücken bricht die Aktion sofort ab.                                                                                                            |
| **E**              | **UI-Explorer**                                            | **Interaktiver Klick:** Identifiziert und klickt auf UI-Elemente in jeder Anwendung.                                                                                                                                                                                  |
| **T**              | Intelligenter Übersetzer                                   | Übersetzt Text unter dem Navigator-Objekt oder der Markierung.                                                                                                                                                                                                                        |
| **Umschalt + T**   | Übersetzung                                                | Übersetzt den aktuellen Inhalt der Zwischenablage.                                                                                                                                                                                                                                    |
| **R**              | Text-Optimierer                                            | Zusammenfassen, Grammatik korrigieren, Erklären oder **Eigene Prompts** ausführen.                                                                                                                                                                                                    |
| **V**              | Objekt-Vision                                              | Beschreibt das aktuelle Navigator-Objekt.                                                                                                                                                                                                                                             |
| **O**              | Vollbild-Vision                                            | Analysiert das gesamte Bildschirmlayout und den Inhalt.                                                                                                                                                                                                                               |
| **Strg + V**       | Videoanalyse                                               | Analysiert lokale Videodateien oder Online-Videos von **YouTube**, **Instagram**, **TikTok** oder **Twitter (X)**.                                                                                                                                                 |
| **Umschalt + V**   | Lokale Videoaufnahme                                       | Nimmt ein lautloses Video Ihres Bildschirms auf und analysiert die Aktionen und das Layout.                                                                                                                                                                                           |
| **D**              | Dokumentenleser                                            | Fortgeschrittener Leser für PDF, Bilder und einfache Text-/HTML-Dateien mit Seitenbereichsauswahl.                                                                                                                                                                                    |
| **F**              | **Smarte Datei-Aktion**                                    | Kontextabhängige Erkennung aus ausgewählten Bild-, PDF- oder TIFF-Dateien.                                                                                                                                                                                                            |
| **M**              | Medien-Transkription & Synchronisation | Transkribiert oder synchronisiert Audio-/Videodateien (MP3, WAV, MP4 usw.) in Ihre Zielsprache.                                                                                                                                                    |
| **C**              | CAPTCHA-Löser                                              | Erfasst und löst CAPTCHAs.                                                                                                                                                                                                                                                            |
| **Umschalt + C**   | Direkter Chat                                              | Öffnet eine direkte, textbasierte Chat-Oberfläche mit der KI.                                                                                                                                                                                                                         |
| **S**              | Intelligentes Diktat                                       | Wandelt Sprache in Text um. Drücken zum Starten, erneut drücken zum Stoppen/Einfügen.                                                                                                                                                                                 |
| **Strg + T**       | Sprach-Übersetzung                                         | Transkribiert, übersetzt und tippt das Ergebnis basierend auf Ihren Spracheinstellungen.                                                                                                                                                                                              |
| **Strg + L**       | **Live-Assistent**                                         | **Echtzeit-Copilot (nur Gemini):** Startet oder beendet ein Live-Sprach- und Bildschirmgespräch mit dem KI-Assistenten.                                                                                                                            |
| **Strg + A**       | **Live-Operator**                                          | **Autonome Computersteuerung (nur Gemini):** Startet oder beendet eine Live-Operatorsitzung, um Bildschirm und Aktionen an die KI zu delegieren.                                                                                                   |
| **G**              | **Gemini-API-Schlüsselmanager**                            | **Erstellen Sie Ihren API-Schlüssel ohne Web (nur Gemini):** Öffnet den Manager, der die Anforderungen Ihres Computers einrichtet, den Browser zur Anmeldung öffnet und einen Schlüssel für das ausgewählte Projekt erstellt, kopiert oder löscht. |
| **I**              | Statusbericht                                              | Kündigt den aktuellen Fortschritt an (z. B. „Scannen...“, „Leerlauf“).                                                                                                             |
| **L**              | **Objekt beschriften**                                     | **Semantische KI-Beschriftung:** Beschriftet das aktuell fokussierte Navigator-Objekt oder Symbol dauerhaft.                                                                                                                                                          |
| **Umschalt + L**   | **Beschriftungen verwalten/scannen**                       | Öffnet den Beschriftungs-Manager (falls vorhanden) oder scannt die App nach unbeschrifteten Elementen.                                                                                                                                                             |
| **U**              | Nach Updates suchen                                        | Sucht auf GitHub manuell nach der neuesten Version des Add-ons.                                                                                                                                                                                                                       |
| **Leertaste**      | Letztes Ergebnis abrufen                                   | Zeigt die letzte KI-Antwort in einem Chat-Dialog zur Überprüfung oder Weiterverfolgung an.                                                                                                                                                                                            |
| **H**              | Befehlshilfe                                               | Zeigt eine Liste aller verfügbaren Tastenkombinationen an.                                                                                                                                                                                                                            |
| **Strg + H**       | **Verlauf**                                                | Öffnet das Verlaufsdialogfeld, in dem Ihre vergangenen Chats und Dokumente mit Typfiltern und Optionen zum Löschen aufgelistet sind.                                                                                                                                                  |
| **Alt + S**        | Einstellungen                                              | Öffnet das Dialogfeld „Einstellungen von KI Assistent pro“.                                                                                                                                                                                                                           |
| **Alt + Q**        | Bericht über Schlüssel mit erschöpftem Kontingent          | Meldet die Anzahl der Gemini-API-Schlüssel, die ihr Tageskontingent überschritten haben, welche Modelle betroffen sind und deren Zurücksetzungszeit.                                                                                                                                  |
| **Alt + M**        | Routing-Prüfung                                            | Meldet die KI-Modelle, die derzeit im erweiterten Routing für spezielle Aufgaben ausgewählt sind (überspringt Standardeinstellungen).                                                                                                                              |
| **Auf / Ab**       | Schnelleinstellungs-Navigation                             | Navigiert zwischen Schnelleinstellungs-Kategorien (Anbieter, Modell, Ausgabe)... in der Befehlsebene.                                                                                                              |
| **Links / Rechts** | Schnelleinstellung ändern                                  | Ändert den Wert der aktuell ausgewählten Schnelleinstellung.                                                                                                                                                                                                                          |

## 4. Chat & Verlauf

Chat-Fenster und der Verlaufsdialog greifen nahtlos über alle Funktionen hinweg ineinander, sodass Sie Konversationen nachlesen und jederzeit dort weitermachen können, wo Sie aufgehört haben.

### 4.1 Tastenkombinationen für das Chatfenster

Wenn ein Chat-Fenster geöffnet ist (Direkter Chat, Dokumenten-Chat, Text-Optimierer usw.), können Sie das Gespräch mit folgenden Tasten prüfen:

- **Alt + Pfeil runter:** Liest die nächste Nachricht vor.
- **Alt + Pfeil hoch:** Liest die vorherige Nachricht vor.
- **Alt + C:** Kopiert die aktuell ausgewählte Nachricht in die Zwischenablage.

### 4.2 Verlauf (Strg + H)

Drücken Sie **Strg + H** in der Befehlsebene, um den **Verlauf** Ihrer bisherigen Chats und Dokumente zu öffnen, filterbar nach Typ (Alle / Chats / Dokumente). Öffnen Sie einen Chat, um die Konversation fortzusetzen – einschließlich angehängter Dateien, die automatisch erneut verknüpft werden – oder öffnen Sie ein Dokument zum Weiterlesen. Drücken Sie **Entf** auf einem Eintrag, um ihn zu entfernen, oder **Alle löschen**, um die Liste zu leeren. Bei Dokumenten fragt das System beim Löschen, ob nur der Verlaufseintrag entfernt oder auch der zwischengespeicherte OCR-Text bereinigt werden soll, damit beim nächsten Öffnen komplett frisch gescannt wird – inklusive einer Option **Nicht mehr fragen**, um Ihre Wahl zu speichern.

You can also choose what the list remembers. Sie können auch festlegen, was die Liste speichert: **Chats im Verlauf speichern** (Reiter Verbindung) und **Dokumente im Verlauf speichern** (Reiter Dokumentenleser) sind standardmäßig aktiviert und können beide über die Schnelleinstellungen umgeschaltet werden. Die Dokumentenoption betrifft nur den Verlaufseintrag – zwischengespeicherte OCR-Texte und Wiederaufnahmedaten bleiben stets erhalten.

## 5. KI-Operator – Autonome Computersteuerung

Der **KI-Operator** macht aus KI Assistent pro von einem passiven Leser einen aktiven Assistenten, der in Ihrem Namen mit Ihrem Computer interagieren kann. Sie können ihn bitten, den Bildschirm zu beschreiben, Fragen zu dem zu beantworten, was er sieht, oder sogar die Kontrolle zu übernehmen – Knöpfe anklicken, Elemente ziehen, Text tippen und durch Anwendungen navigieren, indem Sie ganz normale Alltagssprache verwenden.

Der größte Vorteil? Es funktioniert perfekt in absolut unzugänglicher Software. Wenn Sie in einer benutzerdefinierten Anwendung, einer Remotedesktop-Verbindung oder auf einer Website feststecken, bei der Ihr Screenreader völlig stumm bleibt, stört das den Operator nicht. Da er den Bildschirm visuell „sieht“, kann er Elemente finden, lesen und mit ihnen interagieren, die keinerlei Barrierefreiheits-Labels besitzen.

### 5.1 So funktioniert es

1. Drücken Sie **NVDA + Umschalt + V** und dann **Umschalt + A** (oder nutzen Sie die direkte Tastenkombination), um den KI-Operator-Dialog zu öffnen.
2. Tippen Sie in verständlicher Sprache ein, was Sie tun möchten (z. B. „Klicke auf die Schaltfläche Speichern“, „Was sagt die Fehlermeldung?“ oder „Benenne die Datei in endgueltig.pdf um“).
3. Die KI analysiert Ihren Bildschirm, identifiziert die relevanten Elemente und führt die Aktion aus oder liefert die Antwort. Wenn eine Aufgabe mehrere Schritte erfordert, arbeitet der Operator so lange weiter, bis sie abgeschlossen ist.
4. Drücken Sie jederzeit erneut **Umschalt + A**, um eine laufende Aktion sofort abzubrechen.

### 5.2 Unterstützte Aktionen

Der Operator versteht eine Vielzahl von Befehlen:

- **Beschreiben & Antworten:** „Beschreibe das Bildschirmlayout“ oder „Was sagt die Fehlermeldung?“
- **Klicken:** „Klicke auf die Schaltfläche Speichern“
- **Rechtsklick:** „Mache einen Rechtsklick auf die Datei“
- **Doppelklick:** „Doppelklicke auf das Dokument“
- **Ziehen & Ablegen (Drag & Drop):** „Ziehe das Dokument in den Archiv-Ordner“
- **Tippen:** „Tippe 'Hallo Welt' in das Suchfeld“
- **Scrollen:** „Scrolle dreimal nach unten“
- **Tastendruck:** „Drücke Enter“, „Drücke Tab“, „Drücke Escape“
- **Mehrschrittige Aufgaben:** „Öffne den Datei-Explorer, suche den Bericht und benenne ihn in endgueltig.pdf um“

### 5.3 Wichtige Hinweise

- **⚠️ Warnung zur API-Nutzung:** Da der Operator genau „sehen“ muss, was auf dem Bildschirm passiert, um präzise zu sein, sendet er bei jedem Schritt einen hochauflösenden Screenshot. Eine häufige Nutzung verbraucht Ihr API-Kontingent viel schneller als standardmäßige textbasierte Aufgaben.
- **Administrator-Anwendungen:** Wenn NVDA nicht mit Administratorrechten ausgeführt wird, kann der Operator möglicherweise nicht mit Fenstern interagieren, die erhöhte Rechte erfordern. Dies ist eine Sicherheitsbeschränkung von Windows, kein Fehler im Add-on.
- **Best Practices:** Um die besten Ergebnisse zu erzielen, geben Sie klare und spezifische Befehle. „Klicke auf die blaue Senden-Schaltfläche unten im Formular“ funktioniert fast immer besser als nur „Klicke auf die Schaltfläche“.

### 5.4 Live-Operator (Strg+A)

Der Ambient Observer macht KI Assistent pro zu Ihren Augen im Hintergrund – ganz ohne Gespräch: Er hört und schaut weiter zu, während Sie arbeiten, meldet, was sich ändert, und bleibt still, wenn nichts passiert.
_(Hinweis: Diese Funktion ist exklusiv für Google Gemini und Gemini-kompatible benutzerdefinierte Anbieter verfügbar)._

- Drücken Sie **Strg + A** in der Befehlsebene, um eine Live-Operatorsitzung zu starten.
- **So funktioniert es:** Bitten Sie in Alltagssprache, zum Beispiel „Öffne Chrome und suche nach einer Website“ oder „Benenne diese Datei in endgueltig um“. Der Operator schaut auf den Bildschirm, führt die Schritte nacheinander aus und arbeitet mehrschrittige Anfragen ab, bis die Aufgabe erledigt ist.
- **Ansagen:** Jeder Schritt wird mit der eigenen Stimme des Live-Assistenten angesagt, und er teilt Ihnen mit, wenn die Aufgabe abgeschlossen ist – oder warum sie nicht ausgeführt werden konnte.
- **CAPTCHA:** Erscheint ein CAPTCHA, versucht der Operator zuerst Ihren integrierten **CAPTCHA-Löser**; kann dieser es nicht lösen, bittet er Sie, die barrierefreie Aufgabe selbst zu lösen.
- **Neugestaltung der Einstellungen:** Das Einstellungsfenster wurde auf ein modernes Layout mit Reitern umgestellt.
- **Einstellungen:** Die eigene Anweisung des Operators kann im Prompt-Manager bearbeitet werden (Abschnitt **Live**, **Anweisung für Live-Operator**). Der Schalter **Live: Direkte Ausgabe (Kein Fenster)** ist auch in den Schnelleinstellungen verfügbar.

## 6. Videoanalyse & Audiobeschreibung

> **Hinweis:** Die Funktionen zur Videoanalyse und Audiobeschreibung werden ausschließlich durch den Anbieter **Google Gemini** unterstützt. Stellen Sie sicher, dass Ihr aktiver Anbieter in den Add-on-Einstellungen auf Google Gemini eingestellt ist.

KI Assistent pro führt leistungsstarke Videoverarbeitungsfunktionen ein, die speziell für blinde und sehbehinderte Benutzer entwickelt wurden. Es kann sowohl Online-Videos als auch lokale Bildschirmaufnahmen analysieren, um hochdetaillierte visuelle Beschreibungen zu liefern und professionelle Audiobeschreibungs-Skripte (SRT) zu erstellen.

### 6.1 Lokale Bildschirmaufnahme (Strg + V)

Wenn Sie auf ein stummes Video, eine Animation oder eine Anleitung auf Ihrem Bildschirm stoßen, können Sie diese direkt aufnehmen:

1. Drücken Sie **NVDA + Umschalt + V**, um die Befehlsebene zu aktivieren, und drücken Sie dann **Strg + V**.
2. Das Add-on nimmt Ihren Bildschirm geräuschlos im Hintergrund auf.
3. Drücken Sie erneut **Strg + V**, um die Aufnahme zu stoppen.
4. Die KI analysiert den aufgenommenen Videoabschnitt und liefert eine hochdetaillierte Beschreibung der Szene, der Charaktere und der Aktionen.

### 6.2 Videoanalyse (Umschalt + V)

Sie können sowohl lokale Videodateien als auch Online-Videos analysieren. Wählen Sie einfach eine lokale Datei im Explorer aus oder kopieren Sie einen Videolink in Ihre Zwischenablage. Sie können auch überall **Umschalt + V** drücken (z. B. im Mediaplayer), um einen Dialog zum Auswählen einer Datei oder Einfügen einer URL aufzurufen.

- **Unterstützte Online-Plattformen:** YouTube, Instagram, TikTok und Twitter (X).
- Die KI erkennt die Datei bzw. URL automatisch, verarbeitet das Video und liefert eine umfassende visuelle Beschreibung und Audio-Zusammenfassung.
- **48-Stunden-Zwischenspeicherung von Videodateien:** Zu Gemini hochgeladene Videos werden 48 Stunden lang zwischengespeichert! Sie können SRT- oder MP3-Ausgaben für dasselbe Video ohne erneuten Upload neu generieren – selbst nach einem Neustart von NVDA. Der Cache erkennt den verwendeten API-Schlüssel und wird bei einem Schlüsselwechsel automatisch ungültig.

### 6.3 Erstellung von Audiobeschreibungen (SRT)

Für ein strukturierteres Erlebnis kann das Add-on professionelle Audiobeschreibungs-Skripte im Standard-SubRip-Format (SRT) generieren.

- **Smarte Pausen-Anpassung (Gap-Timing):** Die KI hört auf die Tonspur und verankert ihre Beschreibungen gezielt in natürlichen Sprechpausen, um Überschneidungen mit Dialogen intelligent zu minimieren.
- **Charakter-Verfolgung:** Die Engine führt vorab eine Analyse durch, um Personen anhand unveränderlicher Gesichtsmerkmale zu erfassen. Sie baut ein globales Wörterbuch auf, um Charaktere über Szenen hinweg fehlerfrei zu benennen. Zudem wird der **erste Auftritt** jedes Charakters verfolgt: Seine optische Erscheinung wird nur einmalig beim ersten Auftauchen beschrieben – spätere Szenen nutzen nur noch den etablierten Namen, was die Erzählung flüssig und natürlich hält.
- **Wortgetreues Text-OCR:** Jeder Text auf dem Bildschirm (Schilder, Telefone, Abspanne) wird strikt wortgetreu zitiert.
- **Nutzung:** Legen Sie die generierte `.srt`-Datei einfach in denselben Ordner wie Ihre Videodatei mit exakt demselben Dateinamen. Konfigurieren Sie dann Ihren Mediaplayer (z. B. VLC oder PotPlayer) so, dass der Untertiteltext während der Wiedergabe direkt an Ihren Screenreader oder Ihre TTS-Engine weitergeleitet wird.
- **Verbesserter Speicher-Workflow:** Beim Speichern von SRT- oder MP3-Dateien öffnet sich der Dateidialog nun standardmäßig direkt im Ordner des Quellvideos – unabhängig davon, ob das Video über den Auswahldialog oder per Umschalt+V aus dem Explorer geöffnet wurde.

### 6.4 Synchronisierte Audiosprachausgabe (MP3-Export)

Das Add-on geht über die Erstellung textbasierter SRT-Dateien hinaus und fungiert als vollständiges Werkzeug zur Erstellung von Audiobeschreibungen, indem es die Beschreibungen in Sprache synthetisiert und mit dem Video abmischt. Sie können nun **Gemini Live TTS** als Sprach-Engine wählen, um unbegrenzte und hochrealistische Beschreibungen über die Gemini Live API zu erzeugen. Beim Generieren einer MP3-Datei für lokale Videos stehen Ihnen mehrere Mischmodi zur Verfügung:

- **Standard-AD (Ton mischen):** Die Sprachbeschreibung wird direkt über den Originalton des Videos gelegt. Sie werden gefragt, ob Sie **Audio-Ducking** aktivieren möchten (wodurch die Hintergrundlautstärke während der Beschreibungen abgesenkt wird), um eine klare Verständlichkeit zu gewährleisten.
- **KI-gestützte Stille-Erkennung (Silero VAD):** Die erweiterte Audiobeschreibung (Extended AD) nutzt jetzt das neuronale Modell Silero VAD für eine hochpräzise Stille-Erkennung – und unterscheidet natürliche Dialogpausen zuverlässig von Musik und Hintergrundgeräuschen. Das Modell wird bei der ersten Nutzung automatisch heruntergeladen (mit Ihrer Zustimmung), genau wie ffmpeg und eSpeak.
- **YouTube-Videos:** Bei YouTube-Quellen (die nicht lokal heruntergeladen werden) enthält der MP3-Export ausschließlich die synchronisierte KI-Stimme ohne den Hintergrundton des Videos.

## 7. Medientranskription & Synchronisation (M)

Das Modul zur Audio-Transkription unterstützt sowohl Audio- als auch Videodateien (MP3, WAV, MP4, MKV usw.). Drücken Sie **M** in der Befehlsebene, um eine Mediendatei auszuwählen und eine von 3 Betriebsarten zu wählen:

1. **Transkribieren (Originalsprache):** Transkribiert die gesprochene Sprache präzise in ihrer Originalsprache.
2. **Transkribieren und Übersetzen (Zielsprache):** Transkribiert die Sprache und übersetzt sie in Ihre konfigurierte Zielsprache.
3. **Synchronisieren und Übersetzen (Zielsprache) _(nur Gemini)_:** Eine leistungsstarke Funktion, die Sprache transkribiert, übersetzt und mit der TTS-Engine des Add-ons eine neu eingesprochene Audio-Synchronfassung erzeugt.

## 8. Erweiterter Dokumenten- & Bildleser

Der **Dokumentenleser** verwandelt Dokumente in sauberen, lesbaren Text – damit Sie von eingescannten Büchern bis hin zu Fotostapeln alles lesen, übersetzen und anhören können. Er verarbeitet mehrseitige PDFs, komplexe Bilder, iPhone-HEIC-Formate und sogar reine Text- (`.txt`) sowie HTML-Dateien (`.html`, `.htm`), die ganz ohne OCR- oder KI-Verarbeitung sofort geöffnet werden. Wenn Sie mehrere Dateien auf einmal auswählen, werden diese in Seitenreihenfolge zu einem einzigen Dokument zusammengefügt. Drei OCR-Engines stehen bereit – **Chrome (Schnell)**, **KI (Erweitert)** für hervorragenden Layouterhalt und **Keine (Textschicht extrahieren)** für durchsuchbare PDFs – wählbar unter Einstellungen → Dokumentenleser.

### Wie es funktioniert

1. Drücken Sie **NVDA + Umschalt + V** und dann **D**, um den Dokumentenleser zu öffnen – oder markieren Sie vorher eine Datei im Explorer und drücken Sie **D** / **F**, um den Dateidialog direkt zu überspringen.
2. Wählen Sie eine oder mehrere PDFs bzw. Bilddateien. Das Add-on scannt sie und sagt die Gesamtseitenzahl an.
3. Im Dialog **Optionen** wählen Sie den Seitenbereich (Von/Bis). Sie können auch **Ausgabe übersetzen** aktivieren und die Zielsprache wählen, oder **Bilder inline während OCR beschreiben** zuschalten.
4. Die Textextraktion startet im Hintergrund in Stapeln. Sie können das Fenster jederzeit schließen und später fortfahren – es geht nichts verloren.
5. Sobald Seiten bereitstehen, lesen Sie diese im Viewer: blättern Sie zwischen Seiten, springen Sie zu bestimmten Seiten, stellen Sie der KI Fragen, speichern Sie den Text oder erzeugen Sie eine Audio-Sprachausgabe.

### 8.1 Stapelverarbeitung & Fortsetzen

Sie müssen ein riesiges Dokument nicht auf einmal lesen. Wählen Sie einen Seitenbereich (z. B. `1-20`) oder behalten Sie die Standardeinstellung bei, und die KI extrahiert alle Seiten im Hintergrund. Falls NVDA abstürzt oder der Scan unterbrochen wird, merkt sich das Add-on Ihren Fortschritt und bietet an, genau dort **fortzufahren**, wo Sie aufgehört haben – selbst über Neustarts hinweg! Vollständig gescannte Dokumente werden zudem zwischengespeichert, sodass ein erneutes Öffnen (aus den Zuletzt gelesenen Dokumenten oder über **D**) den Text sofort ohne erneutes OCR lädt, sofern sich die Quelldateien nicht geändert haben.

### 8.2 Intelligente Dateiaktion

Sie müssen das Dokument nicht immer zuerst über den Dialog öffnen. Markieren Sie im Explorer einfach eine PDF-, Bild- oder Text-/HTML-Datei und drücken Sie **D** (Dokumentenleser) – oder markieren Sie eine PDF- oder Bilddatei und drücken Sie **F** (Smarte Datei-Aktion) in der Befehlsebene. Das Add-on umgeht den Dateidialog sofort und verarbeitet die markierte Datei. Die Auswahl mehrerer Dateien verarbeitet diese gebündelt als ein Gesamtdokument.

### 8.3 Steuerelemente & Tastenkombinationen des Dokumentenbetrachters

Wenn das Fenster des Dokumentenlesers geöffnet ist, stehen folgende Optionen zur Verfügung:

#### Tastenkombinationen

- **Strg + BildAb / Strg + BildAuf:** Zur nächsten / vorherigen Seite wechseln.
- **Pfeil runter / hoch:** Erreicht Ihr Cursor die letzte Zeile einer Seite, springt **Pfeil runter** automatisch zur nächsten Seite; **Pfeil hoch** am oberen Seitenrand bringt Sie nahtlos zur vorherigen Seite zurück.
- **Alt + A:** Öffnet einen Chat-Dialog, um Fragen zum Dokument zu stellen.
- **Alt + R:** Erzwingt einen **erneuten Scan mit KI** über Ihren aktiven Anbieter.
- **Alt + G:** Erzeugt und speichert eine hochwertige Audiodatei (WAV/MP3). _Ausgeblendet, wenn der Anbieter kein TTS unterstützt._
- **Alt + S / Strg + S:** Speichert den extrahierten Text als TXT- oder HTML-Datei.

#### Schaltflächen & Steuerelemente

- **Gehe zu:** Wählen Sie eine beliebige Seite aus der Seitenauswahl.
- **Formatiert anzeigen:** Zeigt das gesamte Dokument zusammenhängend als formatierten Text an.
- **Fehlgeschlagene Seiten wiederholen:** Wiederholt nur die Stapel, die aufgrund eines vorübergehenden Serverfehlers (z. B. hohe Auslastung) fehlgeschlagen sind. Diese Schaltfläche erscheint bei Bedarf automatisch.
- **TTS-Stimme / TTS-Engine:** Wählen Sie die Stimme; bei Gemini können Sie zwischen **Standard TTS** und gestreamtem **Gemini Live** wählen.
- **Zurück / Weiter:** Zwischen Seiten blättern (entspricht Strg+BildAuf/BildAb).

### 8.4 Zuletzt geöffnete Dokumente (D)

**Zuletzt gelesene Dokumente im Reader:** Das Drücken von **D** in der Befehlsebene zeigt nun Ihre kürzlich gelesenen Dokumente an erster Stelle. Wählen Sie eines aus, um an der vorherigen Leseposition fortzufahren – selbst wenn das OCR bereits beendet war – oder drücken Sie **Datei öffnen...** (`Strg + O`), um wie gewohnt zu suchen.

## 9. Semantische KI-Beschriftung & UI Explorer

Stecken Sie in einer Anwendung fest, in der überall nur „unbenannte Schaltfläche“ angesagt wird? Die semantische KI-Beschriftungs-Engine löst dieses Problem dauerhaft.

### 9.1 Dauerhafte Objektbeschriftung (L)

Fokussieren Sie Ihren Screenreader auf eine unbenannte Grafik oder Schaltfläche und drücken Sie **L** in der Befehlsebene. Die KI schaut sich die Schaltfläche visuell an, ermittelt ihre Funktion und vergibt eine dauerhafte Beschriftung.
Im Gegensatz zu älteren Beschriftungswerkzeugen verwendet dieses Add-on ein fortschrittliches, hybrides „Objektsignatur-System“ (AutomationId/ControlID). Ihre benutzerdefinierten Beschriftungen überstehen das Ändern der Fenstergröße, Monitorwechsel und Anwendungs-Updates!

### 9.2 Vollständiger Anwendungs-Scan (Umschalt + L)

Drücken Sie **Umschalt + L**, um das gesamte aktive Fenster auf einmal zu scannen. Die KI findet alle unbeschrifteten Elemente und benennt sie intelligent in einem Rutsch. Sie können diese Beschriftungen später im integrierten Beschriftungs-Manager anzeigen, umbenennen oder im Stapel löschen.

### 9.3 UI Explorer (E)

Möchten Sie mit einem Element interagieren, ohne manuell dorthin zu navigieren? Drücken Sie **E**, um den UI-Explorer zu aktivieren. Die KI scannt den Bildschirm und generiert eine barrierefreie Liste aller anklickbaren Elemente (und ignoriert dabei System-Rauschen wie die Taskleiste). Wählen Sie ein Element aus der Liste, und das Add-on klickt es sofort für Sie an.

## 10. Live-Sprachassistent

Der Live-Assistent macht KI Assistent pro zu einem interaktiven Echtzeit-Copiloten.
_(Hinweis: Diese Funktion ist exklusiv für Google Gemini und Gemini-kompatible benutzerdefinierte Anbieter verfügbar)._

- **Aktivierung:** Drücken Sie **Strg + L** in der Befehlsebene, um den Live-Assistenten-Dialog zu öffnen.
- **Echtzeit-Interaktion:** Sprechen Sie ganz natürlich durch Ihr Mikrofon. Die KI hört gleichzeitig auf Ihre Stimme und schaut auf Ihren aktiven Bildschirm. Sie können Fragen stellen wie „Was sehe ich hier?“ oder „Lies mir den dritten Absatz vor.“
- **Push-to-Talk:** Aktivieren Sie **Push-to-Talk** im Reiter Live-Assistent (oder schalten Sie es direkt im Live-Assistenten-Fenster um), halten Sie die zugewiesene Taste zum Sprechen und lassen Sie sie los, um abzuschließen. Das hält das Mikrofon stumm, bis Sie drücken – ideal für laute Umgebungen.
- **Webcam-Eingabe:** Aktivieren Sie das Kontrollkästchen **&Webcam verwenden** im Live-Assistenten-Fenster, um anstelle des Bildschirms Ihren Kamerafeed an die KI zu senden – fragen Sie nach physischen Gegenständen, gedruckten Texten oder Ihrer Umgebung. Ist ffmpeg noch nicht installiert, lädt das Aktivieren der Option die Komponente einmalig mit Ihrer Zustimmung herunter; die Option ist deaktiviert, wenn keine Kamera erkannt wird oder Windows-Datenschutzeinstellungen den Zugriff blockieren.
- **Anpassung:** Direkt im Dialog können Sie den Sprachstil der KI ändern (z. B. Professionell, Freundlich, Aufgeweckt) und die „Denktiefe“ anpassen, um zu steuern, wie gründlich die KI vor einer Antwort nachdenkt.

## 11. Ambient Observer (Hintergrund-Assistent)

The Ambient Observer turns Vision Assistant Pro into your background eyes, without any conversation: it keeps listening and watching while you work, reports what changes, and stays silent when nothing happens.
_(Hinweis: Diese Funktion ist exklusiv für Google Gemini und Gemini-kompatible benutzerdefinierte Anbieter verfügbar)_.

- **Starten:** Drücken Sie **Umschalt + O** in der Befehlsebene, um den Observer zu starten, und drücken Sie es erneut, um ihn zu beenden.
- **Modi:** **Nur Audio-Übersetzung** übersetzt, was er hört, **Nur Bildschirm beobachten** meldet Änderungen auf dem Bildschirm, und **Nur Webcam beobachten** öffnet das Live-Assistenten-Fenster mit Ihrer Kamera und Push-to-Talk, sodass Sie Fragen zu dem stellen können, was die Kamera sieht.
- **Audioquelle:** Wählen Sie im Audiomodus, ob Ihr **Mikrofon** oder der **Systemton (Loopback)** übersetzt werden soll. Die kleine Loopback-Bibliothek wird bei der ersten Nutzung einmalig mit Ihrer Zustimmung heruntergeladen.
- **Kontext:** Für den Bildschirm- und den Webcam-Modus können Sie optional eine Angabe unter **Was ich gerade tue** wählen (zum Beispiel einen Film ansehen, einem Meeting oder Anruf folgen, ein Etikett lesen oder Ihr Aussehen überprüfen), um die Meldungen gezielter zu machen; Sie können auch einen eigenen Kontext eintippen.
- **Meldungen:** Das Add-on vergleicht jedes neue Bild mit dem vorherigen und sendet es nur dann an die KI, wenn sich das Bild tatsächlich verändert hat – ein unveränderter Bildschirm kostet Sie also keine Anfragen. Die KI meldet dann nur Neues und wiederholt sich nie.
- **Begrüßung:** Außer im Übersetzungsmodus begrüßt Sie der Observer beim Start kurz, damit Sie wissen, dass er zuhört.
- **Einstellungen:** Legen Sie unter **Einstellungen > Live-Assistent** den **Observer-Modus**, das **Bildintervall** (1 bis 10 Sekunden) und den **Meldestil** (kurz oder ausführlich) fest. Die Observer-Anweisung und jeder Kontexttext können im Prompt-Manager bearbeitet werden (Abschnitt **Ambient**).

## 12. Benutzerdefinierte Eingabeaufforderungen & Variablen

Sie können Prompts unter **Einstellungen > Prompts > Prompts verwalten...** verwalten.

- **Filter:** Der Reiter **Standard-Prompts** hat über der Prompt-Liste eine **Filter**-Liste, die **Alle** Prompts oder jeweils nur einen Abschnitt anzeigt (zum Beispiel **Ambient**), damit auch lange Listen übersichtlich bleiben.

### Eigene Prompt-Tastenkombinationen

Weisen Sie benutzerdefinierten Prompts direkt im Prompt-Manager ein eigenes Tastaturkürzel zu, um sie sofort mit der aktuellen Auswahl oder dem Kontext auszuführen:

- **Einzeltaste** (z. B. `1`, `p` oder `F3`): Funktioniert innerhalb der Befehlsebene und global als `NVDA + Umschalt + Taste`.
- **Tastenkombination** (z. B. `Strg + Umschalt + 1`, `Alt + P` oder `Einfügen + 1`): Funktioniert eigenständig global.

### Ausgabeverhalten pro Prompt

Jeder benutzerdefinierte Prompt kann individuell festlegen, wie sein Ergebnis ausgegeben wird:

- **Globale Einstellung:** Folgt der allgemeinen Ausgabeeinstellung im Reiter Verbindung (Direkte Ausgabe oder Chat-Fenster).
- **In die Zwischenablage kopieren:** Kopiert die Antwort ausschließlich in die Zwischenablage.
- **Direct Output (NVDA message):** Speaks/brailles the AI response directly via NVDA speech.
- **In die Zwischenablage kopieren und Direkte Ausgabe:** Kopiert die Antwort in die Zwischenablage und gibt sie direkt aus.
- **Chat-Fenster:** Öffnet das Ergebnis immer in einem interaktiven Konversationsfenster.

### Unterstützte Variablen

- `[selection]`: Aktuell markierter Text.
- `[text]`: Gesamter Textinhalt des aktuell fokussierten Eingabefelds (geschützte Passwortfelder werden automatisch ignoriert).
- `[currentURL]`: URL der Webseite oder des Dokuments aus unterstützten Webbrowsern (Chrome, Edge, Firefox).
- `[clipboard]`: Inhalt der Zwischenablage.
- `[clipboard_image]`: Aktuell in der Zwischenablage befindliches Bild.
- `[screen_obj]`: Screenshot des Navigator-Objekts.
- `[screen_fg_obj]`: Screenshot des aktiven Vordergrundfensters.
- `[screen_full]`: Vollbild-Screenshot.
- `[file_ocr]`: Bild-/PDF-Datei für Textextraktion auswählen.
- `[file_read]`: Dokument zum Lesen auswählen (TXT, Code, PDF).
- `[file_audio]`: Audiodatei zur Analyse auswählen (MP3, WAV, OGG).
- `[ambient_screen]`: Startet eine fortlaufende Bildschirmbeobachtung im Hintergrund.
- `[ambient_webcam]`: Startet eine fortlaufende Webcam-Beobachtung im Hintergrund (berücksichtigt die Push-to-Talk-Einstellung).
- `[ambient_audio]`: Startet eine Live-Übersetzungssitzung des Audio-Observers.
- `[loopback]`: Verwendet die Systemtonwiedergabe als Tonquelle (für `[ambient_audio]`).
- `[mic]`: Verwendet das Mikrofon als Tonquelle (für `[ambient_audio]` und `[ambient_webcam]`).
- `[brief]`: Setzt den Meldestil des Observers auf kurz (ein Satz).
- `[detailed]`: Setzt den Meldestil des Observers auf ausführlich (2–3 Sätze).
- `[lang:code]`: Legt den Sprachcode der Zielsprache für die Audio-Übersetzung fest (z. B. `[lang:fa]`, `[lang:en]`).
- `{target_lang}`: Aktuelle Zielsprache.
- `{source_lang}`: Aktuelle Quellsprache.
- `{response_lang}`: Aktuelle KI-Antwortsprache.
- `{swap_target}`: Ausweichsprache für die intelligente Übersetzung mit automatischem Tausch.
- `{swap_instruction}`: Anweisungsblock für die intelligente Übersetzung mit automatischem Tausch.

_Hinweis zu Ambient-Prompts:_ Prompts mit Ambient-Variablen funktionieren als Umschalter – wird das Kürzel bei laufender Sitzung gedrückt, endet diese sofort. Unverträgliche Kombinationen (etwa statische Screenshot-Variablen wie `[screen_full]` zusammen mit Ambient-Modi, mehrere Ambient-Modi gleichzeitig oder zusätzliche Prompt-Anweisungen bei `[ambient_audio]`) werden beim Speichern streng geprüft und verhindert.

## 13. Praktische Anwendungsfälle (Welche Funktion sollte ich verwenden?)

KI Assistent pro ist vollgepackt mit fortschrittlichen Werkzeugen. Hier sind einige häufige Szenarien, die Ihnen bei der Auswahl der richtigen Funktion helfen:

- _Lösung:_ Drücken Sie **O** (Vollbild-Vision). Die KI analysiert den gesamten Bildschirm und beschreibt genau, wo Elemente, Texte und Schaltflächen positioniert sind.

- _Lösung:_ Bewegen Sie Ihr Navigator-Objekt auf die Grafik und drücken Sie **V** (Objekt-Vision). Die KI beschreibt speziell, was dieses Bild enthält.

- _Lösung:_ Drücken Sie **Umschalt + V** auf Ihrem Video und wählen Sie **„Audiobeschreibung generieren (SRT-Datei)“**. Wenn der Vorgang abgeschlossen ist, klicken Sie auf **„Synchronisierte Sprachausgabe generieren (MP3)“** und wählen Sie **„Erweiterte AD“**. Das Add-on erstellt eine Tonspur, die den Filmdialog intelligent pausiert, um die visuellen Szenen zu beschreiben.

- _Lösung:_ Drücken Sie **L**, um die spezifische Schaltfläche mithilfe von KI dauerhaft zu beschriften. Oder drücken Sie **Umschalt + L**, um das gesamte Fenster auf einmal zu scannen und zu beschriften. Wenn Sie nur schnell auf etwas klicken möchten, drücken Sie **E** (UI-Explorer), um eine Liste aller anklickbaren Elemente zu erhalten.

- _Lösung:_ Drücken Sie **C** (CAPTCHA-Löser). Die KI erfasst das CAPTCHA automatisch, löst es und trägt die Antwort in das richtige Feld ein.

- _Lösung:_ Drücken Sie **D** (Dokumentenleser), stellen Sie Ihren Anbieter auf Google Gemini ein und geben Sie den Seitenbereich `1-50` ein. Das Add-on extrahiert den Text im Hintergrund fehlerfrei.

- _Lösung:_ Drücken Sie **Strg + V**, um die Aufnahme des Bildschirms zu starten. Lassen Sie die Anleitung laufen und drücken Sie dann erneut **Strg + V**. Die KI erklärt Ihnen genau, was gezeigt wurde.

- _Lösung:_ Gehen Sie zu **Einstellungen > Erweitert**, aktivieren Sie **"Dedizierte Log-Datei aktivieren"** und stellen Sie das **Log-Level** auf **"Debug"**. Führen Sie die Aktion erneut aus und klicken Sie auf **"Log-Datei öffnen"**, um technische Details einzusehen oder die Datei `vision_assistant.log` an ein Support-Ticket anzuhängen.

***

**Hinweis:** Für alle KI-Funktionen ist eine aktive Internetverbindung erforderlich. Mehrseitige Dokumente werden automatisch verarbeitet.

## 14. Support & Community

Bleiben Sie auf dem Laufenden über Neuigkeiten, Funktionen und Veröffentlichungen:

- **Telegram-Kanal:** [t.me/VisionAssistantPro](https://t.me/VisionAssistantPro?utm_source=gemini)
- **GitHub Issues:** Für Fehlermeldungen und Funktionsanfragen.

### Fehlerbehebung & Protokolle melden

Wenn Sie ein Issue auf GitHub erstellen oder Support anfragen, geben Sie bitte Details zu Ihrem aktiven KI-Anbieter, Modell und der NVDA-Version an. Wenn Sie Verbindungsprobleme oder unerwartete Abstürze haben, aktivieren Sie die dedizierte Log-Datei unter **Einstellungen > Erweitert**, stellen Sie das Problem nach und hängen Sie Ihre `vision_assistant.log`-Datei an, damit wir das Problem schneller lösen können.

## 15. Projekt-Unterstützer

Ein herzliches Dankeschön an unsere Community-Mitglieder, die die kontinuierliche Entwicklung und Pflege dieses Projekts durch ihre großzügigen finanziellen Beiträge unterstützen:

- **@Alyabani94**
- **Ali Alamri**
- **Ilya**
- **leonardo0216**
- **Sergei Fleytin**
- **Arne Siebert**
- **Schalkefan**
- **Rainer Brell**
- **[avalai.org](https://avalai.org?utm_source=gemini)**

_Wenn Sie das Projekt finanziell unterstützen und Ihren Namen hier sehen möchten, finden Sie die Option **Spenden** im NVDA-Werkzeuge-Menü (Untermenü KI-Assistent) oder während des Einrichtungsprozesses nach der Installation._

---

## Änderungen für 15.10.2026

- **Die meistgewünschte Verbesserung – Einen Gemini-API-Schlüssel zu erstellen ist endlich einfach:** Einen API-Schlüssel auf **aistudio.google.com** zu bekommen, war bisher der schwierigste Schritt überhaupt. Mit einem Screenreader waren die Seiten unübersichtlich, und manche Menschen konnten schlicht gar keinen Schlüssel anlegen. Dieses Problem ist nun direkt im Add-on gelöst. Drücken Sie **G** in der Befehlsebene (oder nutzen Sie **Gemini-API-Schlüssel abrufen...** in den Einstellungen), melden Sie sich ganz ohne externe Einrichtung über Ihren Standardbrowser an, und Ihr Schlüssel wird mit einer einzigen Bestätigung erstellt und eingerichtet – selbst wenn Sie noch nie ein Projekt hatten.
- **Ambient Observer:** Der Hintergrund-Assistent ist da. Drücken Sie **Umschalt+O** in der Befehlsebene, um ihn zu starten, und erneut, um ihn zu beenden. Er kann übersetzen, was er hört (Ihr Mikrofon oder den Systemton), den Bildschirm beobachten und Ihnen sagen, was sich geändert hat, oder den Live-Assistenten mit Ihrer Webcam und Push-to-Talk öffnen, damit Sie nach allem fragen können, was die Kamera sieht. Er sendet nur dann ein Bild, wenn sich wirklich etwas verändert hat – ein unveränderter Bildschirm kostet Sie also nichts –, und er bleibt still, wenn nichts passiert. Sie können den Observer auch direkt über eigene Prompts und eigene Tastenkürzel starten und umschalten, mit `[ambient_screen]`, `[ambient_webcam]` oder `[ambient_audio]` sowie den Zusätzen (`[loopback]`, `[mic]`, `[brief]`, `[detailed]`, `[lang:code]`); widersprüchliche Variablenkombinationen werden automatisch erkannt.
- **Live-Operator:** Der Live-Assistent kann nun das, worum Sie ihn bitten, auf Ihrem Computer ausführen, während Sie mit ihm sprechen. Drücken Sie **Strg+A** in der Befehlsebene, um eine Live-Operatorsitzung zu starten, und bitten Sie einfach in Alltagssprache. Er arbeitet mehrschrittige Anfragen ab, sagt jeden Schritt mit der eigenen Stimme des Live-Assistenten an, kümmert sich selbst um die nötigen Tastenkombinationen und entscheidet eigenständig, wann die Aufgabe erledigt ist. **Live: Direkte Ausgabe (Kein Fenster)** gibt es auch in den Schnelleinstellungen.
- **Charakter-Wörterbuch & Serienverwaltung:** Der Videoanalyse-Dialog enthält nun ein leistungsstarkes **Charakter-Wörterbuch**-System! Fügen Sie Charakternamen, optische Beschreibungen und Rollen pro Serie hinzu, bearbeiten, importieren oder verwalten Sie diese – die KI gleicht erkannte Personen automatisch mit dem Wörterbuch ab und fügt neue Charaktere beim Analysieren weiterer Episoden hinzu. Ihre manuellen Notizen behalten immer Vorrang vor KI-Aktualisierungen, während Beschreibungen über Episoden hinweg aktuell bleiben. Das Wörterbuch wird pro Serie gespeichert und für jedes Video der Serie wiederverwendet. Drücken Sie in der Liste **F2** zum Bearbeiten und **Entf** zum Löschen.
- **Unterstützung für SOCKS5-, HTTP- und Reverse-Proxys mit Latenztest:** Umgehen Sie Netzwerkbeschränkungen nahtlos mit vollständiger Proxy-Unterstützung im gesamten Add-on – einschließlich Live-Assistent, Ambient Observer und TTS-Erzeugung! Wählen Sie in den allgemeinen Einstellungen aus 4 Betriebsarten: **Automatisch erkennen**, **SOCKS5-Proxy**, **HTTP-Proxy** oder **Reverse-Proxy**. SOCKS5 unterstützt Benutzername/Passwort-Authentifizierung nach RFC 1929 und Domain-Tunneling; der HTTP-Proxy unterstützt Basic-Authentifizierung. Eine neue Schaltfläche **Proxy-Verbindung testen** läuft im Hintergrund und sagt Ihre Verbindungslatenz in Millisekunden an.
- **48-Stunden-Zwischenspeicherung von Videos:** Zu Gemini hochgeladene Videos werden nun für 48 Stunden zwischengespeichert! Sie können SRT- oder MP3-Dateien für dasselbe Video neu generieren, ohne es erneut hochzuladen – selbst nach einem Neustart von NVDA. Der Cache ist schlüsselabhängig und wird automatisch zurückgesetzt, wenn sich Ihr API-Schlüssel ändert.
- Die Stille-Erkennung nutzt nun das neuronale Modell **Silero VAD** (das bei Erstbenutzung genau wie ffmpeg und eSpeak mit Ihrer Zustimmung automatisch heruntergeladen wird) für hochpräzises Gap-Timing – wodurch echte Dialogpausen zuverlässig von Musik und Hintergrundgeräuschen unterschieden werden. The model is downloaded automatically on first use (with your permission), just like ffmpeg and eSpeak.
- **Webcam-Video für den Live-Assistenten:** Das Live-Assistenten-Fenster bietet nun die Option **&Webcam verwenden**, um Ihren Kamerafeed statt des Bildschirms an die KI zu senden – perfekt für Fragen zu realen Objekten, Dokumenten oder Ihrer Umgebung. Fehlt ffmpeg, wird es einmalig mit Ihrer Zustimmung heruntergeladen. Die Option ist deaktiviert, wenn keine Kamera erkannt wird oder Windows-Datenschutzeinstellungen blockieren. Liefert die aktivierte Kamera keine Bilder, wird dies im NVDA-Log protokolliert, statt geräuschlos zum Bildschirm zurückzukehren.
- **Auswahl des Audio-Ausgabegeräts:** Sie können nun ein eigenes Audio-Ausgabegerät für den Live-Assistenten und den Ambient Observer wählen. Wählen Sie zwischen der Standardausgabe von NVDA, dem Windows-Soundmapper oder jeder angeschlossenen physischen Soundkarte (etwa USB-Kopfhörer oder externe Lautsprecher) – im Reiter Live-Assistent, direkt im Live-Assistenten-Dialog oder spontan über die Schnelleinstellungen (NVDA+Umschalt+V, dann Pfeil hoch/runter/links/rechts).
- **Prompt-Manager:** Der Reiter Standard-Prompts hat nun eine **Filter**-Liste, sodass Sie alle Prompts oder nur einen Abschnitt (zum Beispiel **Ambient**) anzeigen können. Dort können Sie auch die Kontexttexte des Observers und die neue **Anweisung für Live-Operator** bearbeiten.
- **Intelligente Modellfilterung im erweiterten Routing:** Die Auswahllisten im erweiterten Modell-Routing sortieren Gemini-Modelle nun dynamisch und übersichtlich nach ihren Fähigkeiten. Der Live-Assistent zeigt nur echte bidirektionale Live- und Native-Audio-Modelle, TTS nur reine Sprachsynthese-Modelle, STT bevorzugt Transkriptions- und multimodale Modelle, und Videoanalyse, OCR sowie KI-Operator filtern Spezialmodelle für einzelne Zwecke (wie Bild- und Videogenerierung oder Embedding-Modelle) sauber heraus. Künftige Modelle werden anhand ihrer Fähigkeiten automatisch erkannt, ohne dass ein Versionsupdate nötig ist.
- **Erfassung des ersten Auftretens von Charakteren:** Die KI beschreibt das Aussehen jedes Charakters nun nur noch ein einziges Mal – beim ersten Auftauchen im Video. Nachfolgende Auftritte verwenden nur noch die Namen, was redundante Beschreibungen verhindert und die Erzählung lebendig und natürlich hält.
- **Einheitliches Datenverzeichnis:** Alle Datendateien des Add-ons (Verlauf, Serien, Beschriftungen, OCR-Fortschritte, Caches und Logs) wurden in einem einzigen `VisionAssistant`-Ordner innerhalb Ihres NVDA-Konfigurationsverzeichnisses zusammengeführt – was Ordnung schafft und manuelle Sicherungen vereinfacht.
- **Verbesserter Speicher-Workflow für Videos:** Beim Speichern von SRT- oder MP3-Dateien öffnet sich der Dateidialog nun standardmäßig im Quellordner des Videos, egal ob Sie das Video über den Dateidialog oder per Umschalt+V aus dem Explorer geöffnet haben.
- **Dokumente mit oder ohne Zwischenspeicher löschen:** Der Verlaufsdialog (`Strg + H`) bietet nun zwei Löschoptionen für Dokumente – drücken Sie Entf und wählen Sie **Nur aus Verlauf löschen** oder **Aus Verlauf und Cache löschen**. Die zweite Option leert den OCR-Cache des Dokuments, sodass es beim nächsten Öffnen von Grund auf neu gescannt wird – ideal nach einem fehlerhaften Scan. Ein Kontrollkästchen **Nicht mehr fragen** merkt sich Ihre Wahl. Wiederaufnahmedaten unterbrochener Vorgänge bleiben unangetastet.
- **Engine-abhängiger, zusammenführender OCR-Cache im Dokumentenleser:** Zwischengespeicherter OCR-Text wird nun pro OCR-Engine getrennt gespeichert; das Wechseln der Engine scannt somit stets mit der neuen Engine neu, anstatt alte Ergebnisse abzuspielen. Beim erneuten Öffnen eines Dokuments erscheint der Seitenbereichsdialog erneut (mit Ihrer letzten Auswahl vorausgewählt), bereits gescannte Seiten werden sofort wiederverwendet und nur fehlende Seiten nachgeladen – der Cache führt Seiten zusammen, statt überschrieben zu werden.
- **PDF-Komprimierung im Dokumentenleser:** Im Seitenbereichsdialog des Dokumentenlesers gibt es nun die optionale Einstellung **PDF-Seiten vor der Verarbeitung komprimieren**. Beim Hochladen großer oder hochauflösend gescannter PDF-Dokumente zu Gemini oder Mistral werden die Seiten automatisch verkleinert und neu komprimiert – das verringert die Upload-Größe drastisch, beschleunigt die Verarbeitung und verhindert Netzwerk-Zeitüberschreitungen. Die Option ist standardmäßig deaktiviert und wird bei Verwendung der Chrome-Engine oder bei Anbietern, die Bilder per Base64 übertragen, automatisch ausgeblendet.
- **Ausgabeverhalten pro Prompt anpassen:** Legen Sie für jeden eigenen Prompt einzeln fest, wie er sein Ergebnis ausgibt! Wählen Sie im Editor für eigene Prompts zwischen **Globale Einstellung**, **In die Zwischenablage kopieren**, **Direkte Ausgabe (NVDA-Meldung)**, **In die Zwischenablage kopieren und Direkte Ausgabe** oder **Chat-Fenster**. So können bestimmte Prompts ihre Antwort direkt sprechen, ohne ein Fenster zu öffnen, während andere einen vollständigen Chat öffnen.
- **Neue dynamische Prompt-Variablen (`[currentURL]` & `[text]`):** Eigene Prompts unterstützen nun `[currentURL]`, um die URL des aktiven Dokuments in Google Chrome, Mozilla Firefox und Microsoft Edge zu erfassen, sowie `[text]`, um den gesamten Textinhalt des aktuell fokussierten Eingabefelds dynamisch einzufügen (geschützte Passwortfelder werden ignoriert).
- **Überarbeitung des Twitter/X-Video-Downloaders:** Das Herunterladen und Analysieren von Twitter/X-Videos funktioniert nach Ausfällen der vorgelagerten Scraper wieder. Die Videoextraktion nutzt nun die robuste FixTweet-API, um MP4-Streams in höchster Qualität direkt vom CDN von Twitter abzurufen – mit automatischem Rückgriff auf TwitSave und Proxy-Unterstützung.
- **Korrektur des Instagram-Video-Downloaders:** Das Herunterladen und Analysieren von Instagram-Reels und Video-URLs funktioniert nach Änderungen am Formular des Downloader-Dienstes wieder.
- **Korrekturen & Leistung:** Push-to-Talk reagiert sofort beim Drücken der Taste, der Live-Assistent beginnt keine Antwort mehr mitten im Satz, der Observer meldet nicht mehr das vorherige Bild, und die Liste der Denktiefe bietet nur noch an, was Ihr Modell tatsächlich unterstützt. Der KI-Operator kann nun auch nach links und rechts scrollen. Ein `AttributeError` beim Analysieren von Online-Videos wurde behoben, und eigene Prompts ohne Textmarkierung fügen nicht mehr versehentlich Titel von Hintergrundfenstern in KI-Anfragen ein.

## Änderungen für 01.09.2026

- **Verlauf (Strg + H):** Die Befehlsebene enthält nun einen **Verlaufsdialog** (`Strg + H`), der vergangene Chats und Dokumente mit Filtern für Alle, Chats und Dokumente auflistet. Öffnen Sie jeden Chat mit dem gesamten Konversationsverlauf erneut – angehängte Dateien werden automatisch wieder verknüpft – oder setzen Sie das Lesen von Dokumenten fort. Drücken Sie **Entf**, um einzelne Einträge zu entfernen, oder leeren Sie alles auf einmal.
- Das Drücken von **D** in der Befehlsebene listet Ihre kürzlich geöffneten Dokumente zuerst auf. Wählen Sie eines aus, um direkt auf der Seite weiterzulesen, auf der Sie zuletzt waren – selbst wenn das OCR bereits komplett abgeschlossen ist – oder drücken Sie **Datei öffnen...** (`Strg + O`), um wie gewohnt nach einer Datei zu suchen.
- **Push-to-Talk für den Live-Assistenten:** Übernehmen Sie die volle Kontrolle über Live-Gespräche! Aktivieren Sie **Push-to-Talk** im neuen Reiter für den Live-Assistenten und weisen Sie eine beliebige Taste zu – selbst einzelne Sondertasten wie `Linke Strg-Taste`. Halten Sie die Taste zum Sprechen gedrückt und lassen Sie sie los, wenn Sie fertig sind, begleitet von einem kurzen Signalton. Ein Umschalter existiert auch direkt im Live-Fenster.
- **Gemini 2.5 Flash Native Audio:** Der Live-Assistent unterstützt nun das native Audiomodell von Gemini 2.5 Flash (`gemini-2.5-flash-native-audio-preview-12-2025`) für extrem latenzarme und natürliche Sprachgespräche. Wählbar unter **Einstellungen → Erweitertes Modell-Routing → Live-Assistenten-Modell (nur Gemini)** oder auf „Auto“ belassen.
- **Einstellungen sichern & wiederherstellen:** Umfangreiches Backup- und Wiederherstellungssystem im Reiter **Erweitert** hinzugefügt! Sichern Sie alle Add-on-Einstellungen – inklusive API-Schlüssel, Modelle, eigene Prompts und Präferenzen – in einer JSON-Datei. Beim Backup kann zwischen **Alles** (Einstellungen, eigene Beschriftungen, OCR-Fortschritte und Verlauf) oder **Nur Einstellungen** gewählt werden.
- **Direktes Lesen von Text & HTML:** Der Dokumentenleser kann nun reine Text- (`.txt`) und HTML-Dateien (`.html`, `.htm`) direkt öffnen! Kodierungen werden automatisch erkannt, störende Skripte und Formatierungen bereinigt und Inhalte intelligent in Seiten aufgeteilt – ganz ohne OCR oder KI-Aufwand!
- **Gemini Live TTS für den Dokumentenleser:** Die Schaltfläche „Audio generieren“ unterstützt jetzt Gemini Live – eine hochwertige, flüssige Streaming-Text-to-Speech-Engine! Ist Gemini aktiv, kann direkt im Reader zwischen Standard-TTS und Gemini Live gewählt werden.
- **Tastenkombinationen für eigene Prompts:** Sie können nun jedem Ihrer eigenen Prompts direkt im Prompt-Manager ein Tastaturkürzel zuweisen! Geben Sie jedem Prompt eine eigene Taste oder Tastenkombination, um ihn sofort auszuführen – Ihre aktuelle Markierung oder Ihr Kontext wird dabei ohne zusätzliche Schritte automatisch übernommen!
- **Navigation durch Chat-Nachrichten:** Navigieren Sie freihändig durch jedes Gespräch! Drücken Sie in Chat-Fenstern `Alt + Pfeil runter` für die nächste und `Alt + Pfeil hoch` für die vorherige Nachricht – mit klarer Ansage von „Sie“ / „KI“ sowie Randmeldungen („Erste Nachricht“ / „Letzte Nachricht“).
- **Chat-Nachricht kopieren (Alt + C):** Kopieren Sie die aktuell ausgewählte Nachricht beim Durchgehen mit `Alt + Pfeil hoch/runter` per `Alt + C` in die Zwischenablage – unter Beachtung der Markdown-Bereinigungseinstellung.
- **System-Prompt für den Direkten Chat:** Der Direkte Chat (`Umschalt+C`) hat nun einen eigenen, editierbaren System-Prompt – „Anweisung für Direkten Chat“ –, der Persönlichkeit und Antwortsprache des Assistenten für jedes Gespräch festlegt. Sie können ihn im Reiter Standard-Prompts des Prompt-Managers anpassen.
- **Cursor-Seitenwechsel im Dokumentenleser:** Das Lesen mehrseitiger Dokumente wird noch flüssiger! Erreicht Ihr Cursor beim Lesen die letzte Zeile einer Seite und Sie drücken `Pfeil runter`, springt das Dokument automatisch zur nächsten Seite. Drücken Sie am Anfang einer Seite `Pfeil hoch`, gelangen Sie nahtlos zur vorherigen zurück – kein manuelles Umblättern mehr beim Lesen!
- **Neue Schalter in den Schnelleinstellungen:** Die Optionen „KI-Antworten in die Zwischenablage kopieren“, „Direkte Ausgabe (Kein Chat-Fenster)“, „Bereinigtes Markdown im Chat“ und „Smart Swap“ können nun direkt über die Schnelleinstellungen der Befehlsebene ein- und ausgeschaltet werden.
- **Eigener Reiter für den Live-Assistenten:** Der Live-Assistent hat einen eigenen Einstellungsreiter erhalten. Die Option „Direkte Ausgabe (Kein Fenster)“ wurde hierhin verschoben. Der Reiter erscheint dynamisch nur, wenn Google Gemini (oder ein kompatibler benutzerdefinierter Anbieter) aktiv ist.

## Änderungen für 06.08.2026

- **Beschriftung im UI-Explorer:** Elemente können nun direkt innerhalb des UI-Explorers beschriftet werden! Eine neue Schaltfläche "Beschriftung hinzufügen" wurde ergänzt, und das Fenster bleibt geöffnet, damit mehrere Objekte nacheinander barrierefrei beschriftet werden können.
- **Erweiterte Schnelleinstellungs-Ebene:** Die Befehlsebene (`NVDA+Umschalt+V`) bleibt nun aktiv und interaktiv! Sie können `Pfeil hoch/runter` nutzen, um zwischen Schnelleinstellungen (Anbieter, Modell, KI-Antwortsprache, TTS-Modell) zu navigieren, und `Pfeil links/rechts`, um Werte sofort mit Sprachausgabe zu ändern. Ihre Auswahl wird sofort wirksam (einschließlich automatischer Aktivierung des erweiterten Routings, falls nötig), und die Ebene bleibt aktiv, während Sie Einstellungen vornehmen.
- **Direkter Chat (`Umschalt+C`):** Neuer Befehl in der Befehlsebene! Drücken Sie `Umschalt+C`, um sofort ein Fenster „Direkter Chat“ zu öffnen. Es bietet Ihnen direkt eine aufgeräumte, textbasierte Gesprächsoberfläche mit der KI, ohne dass ein Bild oder Dokument als Ausgangspunkt nötig ist.
- **Fehlerfreies Abrufen des Chatverlaufs:** Ein schwerwiegender Fehler wurde behoben, durch den beim Abrufen des letzten Ergebnisses mit der `Leertaste` der nachfolgende Chatverlauf verloren ging. Das Add-on verfolgt Ihr Gespräch nun global. Wenn Sie chatten, den Dialog schließen und mit der `Leertaste` erneut abrufen, wird Ihr gesamtes Hin und Her vollständig wiederhergestellt! Funktioniert für Direkten Chat, Vision-Analyse, Dokumenten-Chat und Übersetzung.
- **Inline-Bildbeschreibungen bei OCR:** Optionale Funktion zur Beschreibung von Bildern direkt im OCR-Textfluss hinzugefügt. Dies kann in den Einstellungen, vor der Extraktion im Dokumentenleser oder spontan über die Schnelleinstellungs-Ebene umgeschaltet werden.
- **Voice Translation (`Control+T`)**: Added a powerful new feature! Dictate speech and instantly translate and type it using AI based on your configured source and target languages.
- **Fehlerbehebungen & Stabilitätsverbesserungen:** Ein Hänger bei der MP3-Generierung beim Schließen des Fortschrittsdialogs wurde behoben, eine Race-Condition im Speicher des Charakter-Wörterbuchs beseitigt, eine saubere Fehlerberichterstattung bei MP3-Kodierungsfehlern ergänzt und die Warteschleife des Dokumentenlesers so angepasst, dass Benutzerabbrüche sofort beachtet werden.
- **Fortschrittsanzeige bei Updates & eSpeak-NG:** Der Download-Dialog für Add-on-Updates sowie eSpeak-NG zeigt nun den genauen Fortschritt in Prozent an.
- **Resilientes Stapel-OCR:** Behebt Unterbrechungen bei der Stapel-PDF-Verarbeitung; wenn ein API-Schlüssel sein Limit erreicht, wird automatisch zum nächsten Schlüssel gewechselt und der Scan fortgesetzt.
- **Visuelle CAPTCHA-Unterstützung:** Unterstützung für das automatische Lösen komplexer visueller Aufgaben wie hCaptcha und reCAPTCHA hinzugefügt – eine deutliche Verbesserung der Barrierefreiheit bei schwierigen Webformularen. It attempts to automatically solve complex image challenges like hCaptcha and reCAPTCHA, significantly enhancing accessibility on challenging web forms.
- **Überarbeitung der Audio-Transkription:** Das Modul wurde komplett neu aufgebaut, unterstützt nun Audio- und Videodateien und bietet 3 Modi: „Transkribieren (Originalsprache)“, „Transkribieren und Übersetzen (Zielsprache)“ sowie eine neue, leistungsstarke Option „Synchronisieren und Übersetzen (Zielsprache)“ (exklusiv für Gemini), die eine übersetzte Audio-Synchronfassung der Originalsprache erzeugt. It features 3 distinct operation modes: "Transcribe (Original Language)", "Transcribe and Translate (Target Language)", and a new powerful "Dub and Translate (Target Language)" option (exclusive to Gemini) that generates a translated audio dub of the original speech.
- **Optionale Seitenzahlen im Dokumentenleser:** Neue Einstellung zum Ein- oder Ausblenden von Seitenzahlen und Trennlinien in mehrseitigen Dokumentausgaben. Die Option lässt sich bequem in den Haupteinstellungen oder spontan über die Schnelleinstellungs-Ebene umschalten. Sie gilt sowohl für exportierte Text-/HTML-Dateien als auch für das Fenster „Formatiert anzeigen“, sodass Sie zusammengefügte Dokumente nahtlos lesen können.
- **Unbegrenztes Gemini Live TTS für Videobeschreibungen:** Gemini Live TTS kann nun als Sprach-Engine für synchronisierte Sprachausgaben (MP3) von Videos gewählt werden. Damit werden über die Gemini Live API hochwertige Audiobeschreibungen ganz ohne Zeichen- oder Längenbeschränkung erzeugt.
- **Codebase-Modularisierung:** Das Add-on wurde von einer einzelnen Datei in eine modulare Architektur mit mehreren Dateien aufgeteilt.
- **Neugestaltung der Einstellungen:** Das Einstellungsfenster wurde komplett auf ein modernes Layout mit Reitern statt gruppierter Bereiche umgestellt – für bessere Ordnung und einfachere Navigation bei Beibehaltung aller bisherigen Optionen.
- **Globales & dediziertes File-Logging:** Neues optionales, globales Protokollierungssystem im neuen Reiter „Erweitert“. Es zeichnet betriebliche Ereignisse, API-Verkehr und Fehler aller Module des Add-ons automatisch in einer eigenen Datei (`vision_assistant.log`) auf. Unterstützt werden einstellbare Log-Level (Debug, Info, Warnung, Fehler), automatische Aufbewahrungsfristen (1 Stunde bis 90 Tage) sowie das direkte Öffnen oder Leeren des Logs aus den Einstellungen – ohne Leistungseinbußen und ohne Beeinträchtigung des NVDA-Logs.
- **Gemini Upload-Fortschritt:** Echtzeit-Fortschrittsanzeigen in Prozent beim Hochladen großer Dateien (Video, Audio, Dokumente) zur Gemini API.

## Änderungen für 15.07.2026

- **Intelligente API-Modellfilterung:** Komplette Überarbeitung des Modellfilterungssystems hin zu einem reinen Blacklist-Ansatz anstelle von Whitelists. Es wurden stärkere Filter-Schlüsselwörter eingeführt (`embedding`, `bison`, `gecko`, `audio`, `realtime`, `babbage`, `moderation`, `deep`, `antigravity`, `computer`), um sicherzustellen, dass die Haupt-Chat-Modellauswahl sauber und zukunftssicher bleibt, während alle spezialisierten Modelle im erweiterten Routing-Bereich weiterhin verfügbar sind.
- **Durchsuchbares erweitertes Routing:** Alle Dropdown-Menüs im erweiterten Modell-Routing (OCR, STT, TTS, Operator, Video, Live) sowie die eSpeak-Variantenauswahl sind nun vollständig durchsuchbar. Sie können tippen, um das gewünschte Modell oder die Variante schnell zu filtern und zu finden.
- **Neue Tastenkombinationen in der Befehlsebene:**
  - **Einstellungen (`Alt + S`):** Öffnet direkt das Einstellungsfenster von KI Assistent pro.
  - **Bericht über erschöpfte Kontingente (`Alt + Q`):** Meldet die genaue Anzahl der Gemini-API-Schlüssel, die ihr tägliches Kontingent überschritten haben, identifiziert das betroffene Modell und sagt die genaue Zurücksetzungszeit an.
  - **Routing-Prüfung (`Alt + M`):** Überprüft und meldet Ihre aktuelle Konfiguration des erweiterten Modell-Routings und liest vor, welche Modelle aktiv für spezialisierte Aufgaben ausgewählt sind (Standardeinstellungen werden übersprungen).
- **Komplette Überarbeitung der Videoanalyse:** Die Videoanalyse wurde von Grund auf transformiert! Zuvor bot sie nur eine einfache Beschreibung von Online-Videos. Jetzt ist sie eine umfassende Videoverarbeitungssuite, die speziell für blinde Nutzer entwickelt wurde:
  - **Lokale Bildschirmaufnahme (`Strg+V`):** Sie können jetzt stumme Videos direkt von Ihrem Bildschirm aufnehmen. Die KI analysiert den aufgezeichneten Abschnitt und liefert eine hochdetaillierte Beschreibung der Szene, des Layouts und der Aktionen.
  - **Erstellung von Audiobeschreibungen (SRT):** Das Add-on kann nun hochdetaillierte Audiobeschreibungs-Skripte (im Standard-SRT-Format) für Videos generieren, komplett mit intelligentem Gap-Timing zur Pausenerkennung und wortgetreuem OCR für Bildschirmtexte.
  - **Synchronisierte Sprachausgabe (MP3-Export):** Neben textbasierten Untertiteln kann das Add-on die Audiobeschreibung in Sprache umwandeln, diese automatisch mit dem Originalton des Videos mischen, Audio-Ducking anwenden und das synchronisierte Ergebnis als MP3-Datei exportieren!
  - **Smarte Video-Datei-Aktion:** Wenn Sie eine lokale Videodatei fokussieren und die Video-Tastenkombination drücken, erkennt das Add-on diese automatisch und verarbeitet die Datei direkt.
  - **Fortgeschrittene Charakter-Verfolgung:** Die KI führt vorab eine Charakter-Erkennung durch. Sie erstellt ein globales Charakter-Wörterbuch und verfolgt Personen Abschnitt für Abschnitt fehlerfrei, ohne Identitäten zu verwechseln.
  - **Konfiguration der Videoanalyse:** Neue Einstellungen zur Steuerung von SRT-Blockgrößen, Charakter-Untertiteln und Haftungsausschlüssen wurden hinzugefügt.
  - **Erweitertes Modell-Routing:** Sie können nun explizit spezialisierte Videomodelle (`gemini_video_model`, `custom_video_model`) in den Einstellungen für das erweiterte Modell-Routing auswählen.
- **Smarte API-Kontingentverwaltung:** Verbesserte Handhabung von 429-Fehlern (Tägliches Limit) durch Modell-spezifische Erfassung. Wenn ein Schlüssel das Limit für ein bestimmtes Modell erreicht, wird er intelligent nur für dieses Modell gesperrt, bleibt aber für andere Modelle weiterhin einsatzbereit.

## Änderungen in 7.0.0

- **Fortsetzen nicht beendeter Scans:** Eine Fortsetzungsfunktion wurde sowohl für den Dokumentenleser als auch für die Smarten Datei-Aktionen hinzugefügt. Wenn ein Scan unterbrochen wird, können Sie nun an der Stelle weitermachen, an der er gestoppt wurde, anstatt von vorne beginnen zu müssen.
- **Neue Variable `[screen_fg_obj]`:** Eine neue Variable für eigene Prompts wurde hinzugefügt, um einen Screenshot ausschließlich des aktiven Vordergrundfensters anstelle des gesamten Bildschirms aufzunehmen.
- **Smarte Wiederholungen & Schlüsselrotation:** Das Add-on versucht nun bei temporären Serverüberlastungen (wie hoher Auslastung oder fehlerhaften Antworten) bis zu 5-mal unbemerkt eine Wiederholung mit demselben Schlüssel. Schlagen die Versuche fehl, wird automatisch zum nächsten API-Schlüssel in Ihrer Liste gewechselt.
- **Bildschirmvorhang-Erkennung:** Eine Prüfung wurde hinzugefügt, die verhindert, dass Screenshots aufgenommen werden, wenn der NVDA-Bildschirmvorhang aktiv ist (egal ob dauerhaft oder temporär über die Tastenkombination aktiviert). Das Add-on warnt Sie und bricht ab, um das Senden schwarzer Bilder und das Verschwenden von API-Tokens zu verhindern.
- **Verbesserungen im Dokumentenleser:** Der PDF-Seitenbereichsdialog wählt nun automatisch die in den Add-on-Einstellungen festgelegte Zielsprache vor. Zudem wurde die Thread-Verarbeitung optimiert, um sicherzustellen, dass Hintergrundaufgaben sauber beendet werden, wenn der Leser geschlossen wird.
- **Native Mistral OCR-Integration:** Die native Document OCR API von Mistral wurde integriert. Mehrseitige Dokumente werden automatisch zusammengeführt, hochgeladen und in Stapeln über den spezialisierten `/v1/ocr`-Endpunkt von Mistral verarbeitet, während einseitige Bilder ohne unnötige PDF-Konvertierung direkt verarbeitet werden.
- **Dynamische Handhabung benutzerdefinierter URLs:** Das Ändern der benutzerdefinierten API-URL löscht nun sofort die zwischengespeicherte Modellliste und stellt das manuelle Texteingabefeld für Modelle wieder her. Dies gewährleistet volle Kompatibilität mit benutzerdefinierten Endpunkten (wie Cloudflare AI Gateway), die den Standard-Endpunkt `/v1/models` nicht unterstützen.
- **Überarbeitete Eingabe-Engine für den KI-Operator:** Das zugrundeliegende Maus- und Tastatursimulationssystem für den KI-Operator wurde komplett neu geschrieben. Die veraltete `mouse_event`-API wurde durch die moderne Windows `SendInput`-API ersetzt, was eine deutlich höhere Kompatibilität mit modernen Anwendungen, benutzerkontengesteuerten Fenstern (UAC) und High-DPI-Displays mit sich bringt.
- **Stabile Drag & Drop-Aktionen:** Drag-and-Drop-Aktionen im KI-Operator laufen nun absolut stabil und zuverlässig. Die neue Engine nutzt natürliche Bewegungskurven, präzise Cursorpositionierung, optimiertes Timing und eine intelligente Anstups-Technik, um sicherzustellen, dass Windows und Anwendungen Drag-and-Drop-Gesten fehlerfrei erkennen.
- **Mehrere Monitore unterstützt:** Der KI-Operator unterstützt nun vollständig Setups mit mehreren Monitoren. Mausbewegungen und Klicks funktionieren über das `MOUSEEVENTF_VIRTUALDESK`-Flag korrekt auf allen Bildschirmen, was eine präzise Positionierung unabhängig vom Monitor der Zielanwendung garantiert.
- **Verbesserte Tastatursimulation:** Die Tastatureingabe wurde verbessert, um "Erweiterte Tasten" (wie Pfeiltasten, Pos1, Ende, BildAuf/Ab, Einfügen, Entf und F1-F12) vollständig zu unterstützen. Dies stellt sicher, dass Navigations- und Tastaturbefehle des KI-Operators in allen Anwendungen fehlerfrei funktionieren.
- **HEIC/HEIF-Bildunterstützung:** Native Unterstützung für iPhone-Fotoformate wurde hinzugefügt. Sie können nun `.heic`- und `.heif`-Dateien direkt für KI-Beschreibungen, OCR oder den Dokumentenleser auswählen, ohne sie vorher konvertieren zu müssen.

## Änderungen in 6.5.0

- **Live-Assistent:** Echtzeit-Sprach- und Bildschirmassistent hinzugefügt, der exklusiv für Google Gemini (oder Gemini-kompatible benutzerdefinierte Anbieter) verfügbar ist. Beinhaltet eine interaktive Anpassung von Stimme und Denktiefe direkt im Dialog, mit automatischer Wiederverbindung nach Einstellungsänderungen.
- **MiniMax KI-Anbieter:** MiniMax wurde als gleichwertiger Anbieter mit vollständiger multimodaler Unterstützung (Chat, Vision, OCR), benutzerdefiniertem TTS mit über 300+ dynamischen Stimmen und automatischem Entfernen von Denkblöcken (z. B. `<think>...</think>`) aus den Ausgaben integriert.
- **Übersetzung im Dokumentenleser:** Ein stiller Übersetzungsfehler für nicht-englische NVDA-Benutzer wurde behoben, indem sichergestellt wird, dass der standardmäßige zweistellige Sprachcode an Google Translate gesendet wird anstelle des lokalisierten Sprachnamens.
- **PDF-Stapelscan-Wiederholung:** Eine hochoptimierte, separate und stille Wiederholungslogik für das Scannen von PDF-Dokumentenstapeln wurde implementiert, um redundante Uploads zu vermeiden und störende Fehler-Popups während der Wiederholungen zu verhindern.
- **Status des Dokumentenlesers:** Ein Fehler wurde behoben, bei dem der Gesamtstatus des Plugins (überprüft mit `I`) während langer Dokumentenscans auf „Stapelverarbeitung gestartet“ hängen blieb.
- **Threading-Absturz behoben:** Ein schwerwiegender Thread-Assertion-Absturz (`IsMain() failed in wxTimerImpl`) beim Öffnen von Dokumenten aus einem Hintergrund-Thread wurde behoben, indem die GUI-Callback-Warteschlange auf `wx.CallAfter` umgestellt wurde.

## Änderungen in 6.1.2

- **Vorabprüfung auf doppelte Beschriftungen:** Ein Problem bei der Einzelbeschriftung wurde behoben, bei dem die Prüfung auf Duplikate alte Koordinatenschlüssel verwendete. Dies führte dazu, dass NVDA doppelte KI-Anfragen für bereits beschriftete Objekte stellte, anstatt die vorhandene Beschriftung anzusagen.
- **Dokumenten-Chat für Nicht-Gemini-Anbieter:** Eine strikte API-Schlüsselprüfung im Dokumenten-Chat (`on_ask`) wurde korrigiert, um sicherzustellen, dass Benutzer von OpenAI, Groq oder lokalen benutzerdefinierten Anbietern (wie Ollama) erfolgreich mit Dokumenten chatten können, ohne blockiert zu werden.
- **Schnelle Chrome-OCR-Übersetzung:** Die kostenlose, schlüssellose Übersetzungs-API für Chrome-OCR wurde wiederhergestellt. Das Übersetzen von extrahiertem Text umgeht nun Gemini-KI, was API-Kontingente spart und den Übersetzungsprozess beschleunigt.
- **Alphanumerischer Filter für CAPTCHAs:** Die Filterlogik im CAPTCHA-Löser wurde korrigiert, um sicherzustellen, dass nicht-alphanumerische Zeichen in allen Situationen ordnungsgemäß bereinigt werden.
- **Aktualisierung der Hilfe für die Befehlsebene:** Die Tastenkombination für die Statusansage im Hilfemenü wurde von `L` auf `I` korrigiert und beide Beschriftungsbefehle (`L` und `Umschalt+L`) wurden zur Liste hinzugefügt.

## Änderungen in 6.1.1

- **Korrektur der Denkausgabe bei Gemma 4:** Ein Problem mit Gemma 4-Modellen wurde behoben, bei dem der gesamte interne Denkprozess als endgültige Antwort angezeigt wurde oder das Deaktivieren des Denkens zu leeren Antworten führte. Das Add-on isoliert und extrahiert nun korrekt nur die finale, bereinigte Textantwort.
- **Stapel-OCR aus dem Datei-Explorer:** Sie können nun mehrere Fotos oder PDFs direkt im Windows Datei-Explorer auswählen und als Stapel Text extrahieren oder analysieren lassen. Das Add-on filtert und verarbeitet automatisch nur die unterstützten Dateiformate.

## Änderungen in 6.1.0

- **Universelle lokale KI-Integration (Lokale KI einrichten):** Eine neue Schaltfläche **"Lokale KI einrichten"** wurde in den Einstellungen für benutzerdefinierte Anbieter hinzugefügt. Benutzer können nun lokale KI-Engines wie **Ollama**, **LM Studio**, **Jan.ai** und **KoboldCPP** sofort automatisch konfigurieren.
- **Intelligenter lokaler Proxy-Bypass:** Die Verbindungslogik wurde mit einem fortschrittlichen Proxy-Bypass-Mechanismus neu aufgebaut. Das Add-on ist nun intelligent genug, um Windows-System-Proxys für lokale Loopback-Verbindungen vollständig zu umgehen, was stabile lokale KI-Verbindungen gewährleistet, selbst wenn Ihr VPN/TUN-Modus aktiv ist.
- **Ultra-stabile KI-Beschriftung (v2):** Absolute Bildschirmkoordinatenschlüssel wurden durch ein fortschrittliches, hybrides **Objektsignatur-System** ersetzt. Beschriftungen basieren nun auf programmgesteuerten Identifikatoren (UIA **AutomationId** oder Win32 **ControlID**) und fensterrelativen Koordinaten.
- **Nahtlose automatische Beschriftungsmigration:** Das Upgrade erfolgt völlig transparent. Das Add-on migriert Ihre älteren, auf Legacy-Koordinaten basierenden Beschriftungen beim ersten Fokussieren automatisch im Hintergrund in das neue, stabile Fingerabdruckformat – ganz ohne Datenverlust.

## Änderungen in 6.0

- **Einführung der semantischen KI-Beschriftung:** Benutzer können nun unbenannte Schaltflächen und Symbole mithilfe von KI dauerhaft beschriften. Drücken Sie **L**, um das aktuelle Navigator-Objekt zu beschriften (unterstützt sowohl den Tab-Fokus als auch die Objektnavigation), oder **Umschalt+L**, um die gesamte Anwendung auf einmal zu scannen und zu beschriften.
- **Intelligente Beschriftungsverwaltung:** Ein neuer, vollständig barrierefreier Beschriftungs-Manager-Dialog wurde hinzugefügt (erreichbar über **Umschalt+L**, falls Beschriftungen existieren), um benutzerdefinierte Beschriftungen anzuzeigen, umzubenennen oder im Stapel zu löschen.
- **Direkte Dateianalyse (Dateidialog umgehen):** Das Add-on ist nun intelligent genug, um zu erkennen, ob Sie gerade eine PDF- oder Bilddatei im Windows Datei-Explorer fokussieren. Das Drücken von **F (Smarte Datei-Aktion)** oder **D (Dokumentenleser)** auf einer markierten Datei verarbeitet diese sofort und umgeht den Standard-"Öffnen"-Dialog komplett.

## Änderungen in 5.6

- **OCR-Engine "Keine (Textschicht extrahieren)" hinzugefügt:** Benutzer können nun Text direkt aus durchsuchbaren PDFs extrahieren, ohne KI-Guthaben zu verbrauchen, was die Geschwindigkeit und den Datenschutz bei textbasierten Dokumenten erheblich verbessert.
- **Verfeinerte UI-Explorer-Genauigkeit:** Die UI-Explorer-Eingabeaufforderung wurde verbessert, um Elementtypen (wie Listeneinträge) besser zu identifizieren und Zustände wie „(Aktiviert)“, „(Ausgewählt)“ oder „(Erweitert)“ korrekt zu melden, während Windows-Systemkomponenten wie die Taskleiste und die Uhr ignoriert werden.
- **Installations-Einrichtungshinweis:** Nach der Installation wurde eine Benachrichtigung hinzugefügt, um Benutzer zum Einstellungsmenü zu führen, damit sie ihre API-Schlüssel und Präferenzen konfigurieren können.

## Änderungen in 5.5.2

- **Problem beim Tippen des KI-Operators behoben:** Ein Fehler wurde behoben, bei dem auf bestimmten Systemen der Buchstabe 'v' getippt wurde, anstatt Text einzufügen. Diese Korrektur behebt Timing-Konflikte, die bei hoher Systemlast auftraten.
- **Erhöhte Stabilität:** Es wurde eine robuste Fehlerbehandlung für Zwischenablage-Operationen hinzugefügt, um Abstürze des Add-ons zu verhindern, wenn die Systemzwischenablage vorübergehend durch andere Anwendungen gesperrt ist.
- **Timing-Optimierung:** Interne Verzögerungen für Tastaturereignisse wurden angepasst, um eine höhere Zuverlässigkeit bei unterschiedlichen Systemgeschwindigkeiten und eine bessere Kompatibilität mit Zwischenablage-Managern von Drittanbietern zu gewährleisten.

## Änderungen in 5.5 (Das Automatisierungs-Update)

- **KI-Operator (Autonome Steuerung - Umschalt+A):** Dies ist das Herzstück von v5.5. KI Assistent pro hat sich von einem passiven Assistenten zu Ihrem persönlichen **KI-Operator** weiterentwickelt. Er beschreibt nicht mehr nur den Bildschirm – er übernimmt das Kommando.
  - _Wie es funktioniert:_ Sie können jetzt sprachliche oder schriftliche Anweisungen geben, um Ihren PC zu steuern. In einer völlig unzugänglichen Anwendung, in der Ihr Screenreader stumm bleibt, können Sie beispielsweise **Umschalt+A** drücken und eingeben: _„Klicke auf die Schaltfläche Einstellungen“_ oder _„Suche das Suchfeld, tippe 'Aktuelle Nachrichten' ein und drücke Enter.“_ Die KI identifiziert die Elemente visuell, bewegt die Maus und führt die Aufgabe für Sie aus.
  - _Leistungshinweis:_ Diese Funktion ist für **Gemini 3.0 Flash (Preview)** optimiert und liefert unglaublich schnelle und intelligente Antworten, die selbst mit komplexesten UI-Layouts umgehen können.
  - **⚠️ Warnung zur API-Nutzung:** Da der KI-Operator genau „sehen“ muss, was passiert, um präzise zu sein, sendet er bei jedem Schritt einen hochauflösenden Screenshot. Bitte beachten Sie, dass eine häufige Nutzung Ihr API-Kontingent viel schneller verbraucht als standardmäßige textbasierte Aufgaben.
- **Visueller UI-Explorer (E):** Müde davon, durch „unbenannte Schaltflächen“ zu navigieren? Drücken Sie **E**, um den UI-Explorer zu aktivieren. Die KI scannt das gesamte Fenster und erstellt eine Liste aller anklickbaren Elemente, die sie sieht – einschließlich Symbolen, Grafiken und Menüs. Wählen Sie einfach ein Element aus der Liste aus, und der KI-Operator klickt es für Sie an. Es ist wie eine „barrierefreie Schicht“ über jeder App.
- **Kontextabhängige smarte Datei-Aktion (F):** Die Taste „F“ wurde komplett überarbeitet. Sie geht nicht mehr pauschal davon aus, dass Sie nur OCR möchten. Wenn Sie eine einzelne Bilddatei auswählen, fragt sie nun intelligent nach Ihrer Absicht: Sie können eine **Detaillierte visuelle Beschreibung** wählen, um die Szene zu verstehen, oder eine **Strukturierte Textextraktion (OCR)** zum Lesen. Das Menü passt sich dynamisch an den Dateityp und Ihre aktive KI-Engine an.
- **Kernoptimierung:** Wir haben die interne Logik des Add-ons gründlich bereinigt, ungenutzte Legacy-Funktionen und redundanten Code entfernt. Dies führt zu einer schlankeren, schnelleren und zuverlässigeren Benutzererfahrung für alle.

## Änderungen in 5.0

- **Multi-Anbieter-Architektur**: Volle Unterstützung für **OpenAI**, **Groq** und **Mistral** neben Google Gemini hinzugefügt. Benutzer können nun ihr bevorzugtes KI-Backend wählen.
- **Erweitertes Modell-Routing**: Benutzer nativer Anbieter (Gemini, OpenAI etc.) können nun spezifische Modelle für verschiedene Aufgaben (OCR, STT, TTS) aus einer Liste wählen.
- **Erweiterte Endpunkt-Konfiguration**: Benutzerdefinierte Anbieter können URLs und Modellnamen manuell eingeben, um die volle Kontrolle über lokale oder Drittanbieter-Server zu haben.
- **Intelligente Sichtbarkeit von Funktionen**: Das Einstellungsmenü und die Benutzeroberfläche des Dokumentenlesers blenden nicht unterstützte Funktionen (wie TTS) basierend auf dem gewählten Anbieter automatisch aus.
- **Dynamisches Abrufen von Modellen**: Das Add-on ruft die Liste der verfügbaren Modelle nun direkt über die API des Anbieters ab, um Kompatibilität mit neuen Modellen sofort nach deren Erscheinen sicherzustellen.
- **Hybrid-OCR & Übersetzung**: Die Logik wurde optimiert, um Google Translate für Geschwindigkeit bei Chrome-OCR zu nutzen und KI-basierte Übersetzung bei Gemini/Groq/OpenAI-Engines zu verwenden.
- **Universelles "Erneuter Scan mit KI"**: Die Re-Scan-Funktion des Dokumentenlesers ist nicht mehr auf Gemini beschränkt. Sie nutzt nun den jeweils aktiven KI-Anbieter zur Neuverarbeitung von Seiten.

## Änderungen in 4.6

- **Interaktives Abrufen von Ergebnissen:** Die **Leertaste** wurde zur Befehlsebene hinzugefügt, wodurch Benutzer die letzte KI-Antwort sofort in einem Chat-Fenster für Folgefragen öffnen können, auch wenn der Modus "Direkte Ausgabe" aktiv ist.
- **Telegram Community-Hub:** Link zum "Offiziellen Telegram-Kanal" im NVDA-Werkzeuge-Menü hinzugefügt.
- **Erhöhte Antwortstabilität:** Kernlogik für Übersetzung, OCR und Vision optimiert, um eine zuverlässigere Leistung bei direkter Sprachausgabe zu gewährleisten.
- **Verbesserte Benutzerführung:** Beschreibungen in den Einstellungen aktualisiert, um das neue Abrufsystem besser zu erklären.

## Änderungen in 4.5

- **Erweiterter Prompt-Manager:** Separater Verwaltungsdialog in den Einstellungen zum Anpassen von System-Prompts und Verwalten benutzerdefinierter Prompts (Hinzufügen, Bearbeiten, Sortieren, Vorschau).
- **Umfassende Proxy-Unterstützung:** Sichergestellt, dass Proxy-Einstellungen strikt auf alle API-Anfragen angewendet werden.
- **Automatisierte Datenmigration:** System zur automatischen Aktualisierung alter Prompt-Konfigurationen auf das v2 JSON-Format beim ersten Start.
- **Aktualisierte Kompatibilität (2025.1):** Erforderliche Mindestversion von NVDA auf 2025.1 gesetzt.
- **Optimierte Benutzeroberfläche:** Bereinigung der Einstellungen durch Auslagerung der Prompt-Verwaltung in einen eigenen Dialog.
- **Leitfaden für Prompt-Variablen:** Integrierter Leitfaden in den Prompt-Dialogen zur Verwendung von Variablen wie [selection], [clipboard] und [screen_obj].

## Änderungen in 4.0.3

- **Verbesserte Netzwerk-Resilienz:** Automatischer Wiederholungsmechanismus bei instabilen Verbindungen hinzugefügt.
- **Visueller Übersetzungsdialog:** Neues Fenster für Übersetzungsergebnisse. Lange Übersetzungen lassen sich nun – wie bei OCR-Ergebnissen – bequem Zeile für Zeile lesen und durchgehen.
- **Aggregierte formatierte Ansicht:** Die Funktion "Formatiert anzeigen" im Dokumentenleser zeigt nun alle verarbeiteten Seiten in einem einzigen, organisierten Fenster an.
- **Optimierter OCR-Workflow:** Überspringt die Seitenbereichsauswahl bei einseitigen Dokumenten automatisch.
- **Verbesserte API-Stabilität:** Umstellung auf Header-basierte Authentifizierung zur Vermeidung von Fehlern bei der Schlüsselrotation.
- **Fehlerbehebungen:** Mehrere mögliche Abstürze wurden behoben, darunter ein Problem beim Beenden des Add-ons und ein Fokusfehler im Chat-Dialog.

## Änderungen in 4.0.1

- **Fortgeschrittener Dokumentenleser:** Neuer Viewer für PDF und Bilder mit Seitenbereichsauswahl und Hintergrundverarbeitung.
- **Neues Werkzeuge-Untermenü:** Untermenü "KI Assistent" unter NVDA-Werkzeuge für schnelleren Zugriff hinzugefügt.
- **Flexible Anpassung:** OCR-Engine und TTS-Stimme direkt in den Einstellungen wählbar.
- **Unterstützung mehrerer API-Schlüssel:** Unterstützung für mehrere Gemini-Schlüssel (einer pro Zeile oder durch Komma getrennt). Sie können mehrere Schlüssel eingeben (getrennt durch Kommas oder neue Zeilen), um eine automatische Rotation zu ermöglichen.
- **Alternative OCR-Engine:** Neue Engine zur Texterkennung hinzugefügt, falls das Gemini-Kontingent erschöpft ist.
- **Unterstützung mehrerer API-Schlüssel:** Unterstützung für mehrere Gemini-Schlüssel (einer pro Zeile oder durch Komma getrennt).
- **Dokument zu MP3/WAV:** Fähigkeit zur Erzeugung hochwertiger Audiodateien direkt im Reader integriert.
- **Unterstützung für Instagram Stories & TikTok:** Analyse von Stories und TikTok-Videos über deren URLs hinzugefügt.
- **Gemini Live TTS für Videobeschreibungen:** Gemini Live TTS kann nun als Stimme für synchronisierte Sprachausgaben (MP3) gewählt werden, um unbegrenzte und hochwertige Beschreibungen ohne Längenbeschränkung zu generieren.
- **Neu gestalteter Update-Dialog:** Neue barrierefreie Oberfläche mit einem scrollbaren Textfeld, in dem sich die Versionsänderungen vor der Installation klar nachlesen lassen.
- **Einheitlicher Status & Bedienung:** Dateidialoge im gesamten Add-on vereinheitlicht und den Befehl 'L' so erweitert, dass er den Fortschritt in Echtzeit meldet.

## Änderungen in 3.6.0

- **Hilfesystem:** Hilfe-Befehl (`H`) innerhalb der Befehlsebene hinzugefügt.
- **Online-Videoanalyse:** Unterstützung für **Twitter (X)** Videos hinzugefügt sowie URL-Erkennung und Stabilität für ein zuverlässigeres Erlebnis verbessert. Also improved URL detection and stability for a more reliable experience.
- **Projektunterstützung:** Optionaler Spendendialog für Benutzer hinzugefügt, die künftige Updates und das kontinuierliche Wachstum des Projekts unterstützen möchten.

## Änderungen in 3.5.0

**Befehlsebene:** Einführung der Befehlsebene (Standard: `NVDA+Umschalt+V`), um Kürzel unter einer Haupttaste zu gruppieren. Statt beispielsweise `NVDA+Strg+Umschalt+T` für die Übersetzung zu drücken, drücken Sie nun `NVDA+Umschalt+V` gefolgt von `T`.
**Online-Videoanalyse:** Neue Funktion zur Analyse von YouTube- und Instagram-Videos direkt über eine URL hinzugefügt.

## Änderungen in 3.1.0

- **Direkter Ausgabemodus:** Option zum Überspringen des Chat-Dialogs, um KI-Antworten sofort per Sprache zu hören.
- **Zwischenablage-Integration:** Einstellung zum automatischen Kopieren von KI-Antworten in die Zwischenablage.

## Änderungen in 3.0

- **Neue Sprachen:** Persisch und Vietnamesisch hinzugefügt.
- **Erweiterte KI-Modelle:** Modellliste mit Präfixen (`[Free]`, `[Pro]`, `[Auto]`) neu organisiert. Unterstützung für **Gemini 3.0 Pro** und **Gemini 2.0 Flash Lite**.
- **Diktat-Stabilität:** Die Stabilität des Intelligenten Diktats wurde deutlich verbessert. Audioclips unter 1 Sekunde werden nun durch eine Sicherheitsprüfung ignoriert, um KI-Halluzinationen und leere Fehler zu vermeiden.
- **Dateihandhabung:** Fehler beim Hochladen von Dateien mit nicht-englischen Namen behoben.
- **Prompt-Optimierung:** Übersetzungslogik verbessert und Vision-Ergebnisse strukturierter aufbereitet.

## Änderungen in 2.9

- **Französische und türkische Übersetzungen hinzugefügt.**
- **Formatierte Ansicht:** Schaltfläche "Formatiert anzeigen" in Chat-Dialogen hinzugefügt (Überschriften, Fettdruck, Code).
- **Markdown-Einstellung:** Neue Option „Bereinigtes Markdown im Chat“ in den Einstellungen. Ist sie deaktiviert, sehen Benutzer die rohe Markdown-Syntax (z. B. `**`, `#`) im Chat-Fenster.
- **Dialogverwaltung:** Ein Problem wurde behoben, bei dem sich das Fenster „Text optimieren“ oder Chat-Fenster mehrfach öffneten oder den Fokus nicht korrekt erhielten.
- **Verbesserte Bedienung:** Titel von Dateidialogen einheitlich auf „Öffnen“ gesetzt und überflüssige Sprachansagen (z. B. „Menü wird geöffnet...“) für ein flüssigeres Erlebnis entfernt. for a smoother experience.

## Änderungen in 2.8

- Italienische Übersetzung hinzugefügt.
- **Statusbericht:** Neuer Befehl (NVDA+Strg+Umschalt+I) zum Ansagen des aktuellen Status.
- **HTML-Export:** Speichern-Schaltfläche exportiert nun als formatiertes HTML.
- **Einstellungsoberfläche:** Layout des Einstellungsbereichs durch barrierefreie Gruppierung verbessert.
- **Neue Modelle:** Unterstützung für gemini-flash-latest und gemini-flash-lite-latest hinzugefügt.
- **Sprachen:** Nepali hinzugefügt.
- **Logik des Optimierungsmenüs:** Ein kritischer Fehler wurde behoben, durch den Befehle von „Text optimieren“ fehlschlugen, wenn die NVDA-Oberflächensprache nicht Englisch war.
- **Diktat:** Stille-Erkennung verbessert, um fehlerhafte Textausgaben zu verhindern, wenn keine Sprache eingegeben wurde.
- **Update-Einstellungen:** „Beim Start nach Updates suchen“ ist nun standardmäßig deaktiviert, um den Richtlinien des Add-on-Stores zu entsprechen.
- Code-Bereinigung.

## Änderungen in 2.7

- Projektstruktur auf die offizielle NV Access Vorlage migriert.
- Automatisches Retry bei HTTP 429 (Rate Limit) Fehlern.
- Optimierte Übersetzungs-Prompts für höhere Genauigkeit und eine bessere Handhabung der „Smart Swap“-Logik.
- Optimierte Übersetzungs-Prompts.

## Änderungen in 2.6

- Russische Übersetzung hinzugefügt.
- Fehlermeldungen überarbeitet, um aussagekräftigere Rückmeldungen zu Verbindungsproblemen zu geben.
- Standard-Zielsprache auf Englisch geändert.

## Änderungen in 2.5

- Native Datei-OCR (NVDA+Strg+Umschalt+F) hinzugefügt.
- "Chat speichern" Schaltfläche hinzugefügt.
- Vollständige Unterstützung für Lokalisierung (i18n) implementiert.
- Akustische Rückmeldungen auf das native tones-Modul von NVDA umgestellt.
- Umstellung auf Gemini File API für bessere PDF- und Audio-Handhabung.
- Absturz beim Übersetzen von Text mit geschweiften Klammern behoben.

## Änderungen in 2.2

- Ein Problem wurde behoben, bei dem die Variable [file_ocr] in eigenen Prompts nicht korrekt funktionierte.

## Änderungen in 2.1

- Standardisierung aller Kürzel auf NVDA+Strg+Umschalt, um Konflikte mit dem Laptop-Layout zu vermeiden.

## Änderungen in 2.0

- Integriertes Auto-Update-System.
- Intelligenter Übersetzungscache hinzugefügt.
- Konversationsgedächtnis für Kontext im Chat hinzugefügt.
- Separater Befehl für Zwischenablage-Übersetzung (NVDA+Strg+Umschalt+Y).
- KI-Prompts optimiert, um die Ausgabe strikt in der Zielsprache zu erzwingen.
- Absturz durch Sonderzeichen im Eingabetext behoben.

## Änderungen in 1.5

- Unterstützung für über 20 neue Sprachen.
- Interaktiver Optimierungs-Dialog für Folgefragen.
- Native "Intelligentes Diktat" Funktion.
- Kategorie „KI Assistent“ im NVDA-Dialog „Eingabegesten“ hinzugefügt.
- COMError-Abstürze in bestimmten Anwendungen wie Firefox und Word behoben.
- Automatischer Wiederholungsmechanismus bei Serverfehlern hinzugefügt.

## Änderungen in 1.0

- Erstveröffentlichung.
