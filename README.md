# DevOps Project – Krzysztof Trojańczuk

## Opis projektu

Projekt przedstawia kompletny **pipeline DevOps CI/CD** dla prostej aplikacji webowej napisanej w **Python Flask**.
System automatycznie buduje obraz Dockera, publikuje go w Docker Hub oraz wdraża aplikację na serwerze po każdym `git push`.

Aplikacja jest dostępna publicznie przez HTTPS.

Adres aplikacji:

```
https://projektdyplomowy.ddns.net
```

---

# Architektura systemu

```
Developer (Git)
      ↓
GitHub Repository
      ↓
GitHub Actions CI/CD
      ↓
Docker Image Build
      ↓
Docker Hub (image repository)
      ↓
SSH Deploy na serwer
      ↓
Docker Container
      ↓
Nginx Reverse Proxy
      ↓
HTTPS (Let's Encrypt)
      ↓
User / Browser
```

---

# Technologie użyte w projekcie

* Python
* Flask
* Docker
* Git
* GitHub
* GitHub Actions
* Docker Hub
* Nginx
* Let's Encrypt (SSL)
* Linux Ubuntu Server

---

# Funkcjonalność aplikacji

Aplikacja udostępnia kilka endpointów HTTP.

### Strona główna

```
/
```

Zwraca wersję aplikacji.

Przykład:

```
DevOps Project Krzysztof Trojańczuk - version 4.0
```

---

### Health check

```
/health
```

Sprawdza czy aplikacja działa poprawnie.

Odpowiedź:

```
OK
```

---

### Version endpoint

```
/version
```

Zwraca aktualną wersję aplikacji.

---

# Konteneryzacja

Aplikacja działa w kontenerze Docker.

Uruchomienie lokalne:

```
docker run -d -p 5000:5000 krzyniot/devops-project
```

Aplikacja dostępna wtedy pod:

```
http://localhost:5000
```

---

# CI/CD Pipeline

Pipeline jest realizowany przez **GitHub Actions**.

Plik pipeline:

```
.github/workflows/pipeline.yml
```

Pipeline wykonuje następujące kroki:

1. Pobranie kodu z repozytorium
2. Budowanie obrazu Docker
3. Publikacja obrazu do Docker Hub
4. Połączenie SSH z serwerem
5. Aktualizacja kontenera

---

# Automatyczny deploy

Po każdym `git push` na branch `main`:

```
git push
```

GitHub Actions automatycznie:

1. buduje obraz Dockera
2. wysyła obraz do Docker Hub
3. łączy się z serwerem przez SSH
4. wykonuje deploy

Komendy wykonywane na serwerze:

```
docker pull krzyniot/devops-project
docker stop devops
docker rm devops
docker run -d -p 5000:5000 --name devops --restart always krzyniot/devops-project
```

---

# Reverse Proxy i HTTPS

Aplikacja jest wystawiona przez **Nginx**.

Konfiguracja:

```
/etc/nginx/sites-available/devops
```

Nginx przekazuje ruch HTTPS na aplikację Flask:

```
Nginx → Flask (port 5000)
```

Certyfikat SSL został wygenerowany przez:

```
Let's Encrypt (certbot)
```

---

# Monitoring (planowane)

Projekt może zostać rozszerzony o monitoring:

* Prometheus
* Grafana
* endpoint `/metrics`

Pozwoli to monitorować:

* liczbę zapytań
* dostępność aplikacji
* metryki systemowe

---

# Demonstracja działania CI/CD

Proces demonstracji:

1. Zmiana wersji aplikacji w kodzie

```
VERSION = "4.0"
```

2. Commit i push

```
git add .
git commit -m "release 4.0"
git push
```

3. GitHub Actions uruchamia pipeline

4. Docker image jest budowany i publikowany

5. Serwer automatycznie aktualizuje kontener

6. Strona pokazuje nową wersję

```
https://projektdyplomowy.ddns.net
```

---

# Cel projektu

Celem projektu było pokazanie pełnego procesu DevOps:

* zarządzanie kodem w Git
* automatyczne budowanie aplikacji
* konteneryzacja
* publikacja artefaktów
* automatyczny deploy
* wystawienie aplikacji przez HTTPS

Projekt prezentuje kompletny **workflow CI/CD w środowisku DevOps**.

