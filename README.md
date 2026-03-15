# Projekt DevOps

## Opis projektu

Projekt prezentuje prosty **pipeline DevOps CI/CD** wykorzystujący GitHub, Docker oraz GitHub Actions.

Aplikacja jest niewielką usługą webową napisaną w **Python Flask**, która udostępnia kilka endpointów HTTP.
Głównym celem projektu jest pokazanie automatyzacji procesu budowania, publikacji oraz uruchamiania aplikacji przy użyciu narzędzi DevOps.

Po każdej zmianie w repozytorium kodu pipeline automatycznie buduje obraz Docker i publikuje go w Docker Hub.

---

# Architektura projektu

```
Developer
    │
    │ git push
    ▼
GitHub Repository
    │
    │ uruchomienie pipeline
    ▼
GitHub Actions (CI/CD)
    │
    │ docker build
    ▼
Docker Image
    │
    │ docker push
    ▼
Docker Hub (repozytorium artefaktów)
    │
    │ docker run
    ▼
Serwer (VM / Linux)
    │
    ▼
Kontener Docker
    │
    ▼
Aplikacja Flask
    │
    ▼
Użytkownik / przeglądarka
```

---

# Opis działania pipeline

Pipeline CI/CD działa w następujący sposób:

1. Programista wprowadza zmianę w kodzie aplikacji.
2. Zmiana jest wysyłana do repozytorium GitHub (`git push`).
3. GitHub Actions automatycznie uruchamia pipeline.
4. Pipeline buduje obraz Docker na podstawie pliku `Dockerfile`.
5. Zbudowany obraz zostaje opublikowany w repozytorium Docker Hub.
6. Obraz może zostać uruchomiony na serwerze jako kontener Docker.

---

# Aplikacja

Aplikacja jest prostą usługą webową napisaną w Python Flask.

Dostępne endpointy:

* `/` – wyświetla wersję aplikacji
* `/health` – endpoint monitorowania aplikacji
* `/version` – zwraca aktualną wersję aplikacji

Przykładowa odpowiedź:

```
DevOps Project - version 2.0
```

Endpoint zdrowia aplikacji:

```
OK
```

Endpoint `/health` może być używany przez systemy monitorujące do sprawdzania dostępności aplikacji.

---

# Pipeline CI/CD

Pipeline CI/CD jest zdefiniowany w pliku:

```
.github/workflows/pipeline.yml
```

Po każdym `git push` do gałęzi `main` wykonywane są następujące kroki:

1. Pobranie kodu z repozytorium
2. Budowanie obrazu Docker
3. Logowanie do Docker Hub
4. Publikacja obrazu Docker

---

# Repozytorium Docker

Obraz aplikacji publikowany jest w Docker Hub:

```
krzyniot/devops-project
```

Repozytorium:

```
https://hub.docker.com/r/krzyniot/devops-project
```

---

# Uruchomienie aplikacji

Aplikację można uruchomić przy użyciu Docker:

```
docker run -d -p 5000:5000 krzyniot/devops-project
```

Po uruchomieniu aplikacja dostępna jest pod adresem:

```
http://SERVER_IP:5000
```

Przykład:

```
http://192.168.1.108:5000
```

---

# Wykorzystane technologie

* Python (Flask)
* Docker
* Git
* GitHub
* GitHub Actions
* Docker Hub
* Linux

---

# Cel projektu

Celem projektu jest demonstracja podstawowych elementów środowiska DevOps:

* zarządzanie kodem źródłowym (Git)
* automatyczny pipeline CI/CD
* konteneryzacja aplikacji przy użyciu Docker
* publikacja artefaktów w Docker Hub
* wdrożenie aplikacji na serwerze
* podstawowy monitoring aplikacji poprzez endpoint `/health`

