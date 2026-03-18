# DevOps Project – Krzysztof Trojańczuk

## Opis projektu

Projekt przedstawia kompletny **pipeline DevOps CI/CD** dla aplikacji webowej napisanej w **Python Flask**.

System automatycznie:

* buduje obraz Dockera
* publikuje go w Docker Hub
* wdraża aplikację na serwerze po każdym `git push`
* aktualizuje działającą aplikację bez ręcznej ingerencji

Dodatkowo projekt zawiera **monitoring (Prometheus + Grafana)**.

---

## 🌍 Dostęp do projektu

### Aplikacja (live):

```
https://projektdyplomowy.ddns.net
```

### Repozytorium GitHub:

```
https://github.com/krzyniot/first-devops-project
```

### Docker Hub:

```
https://hub.docker.com/r/krzyniot/devops-project
```

---

# 🧠 Architektura systemu

```
                ┌────────────────────┐
                │     Developer      │
                │     (git push)     │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │   GitHub Repo      │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ GitHub Actions CI  │
                │  build + deploy    │
                └─────────┬──────────┘
                          │
        ┌─────────────────┴─────────────────┐
        ▼                                   ▼
┌───────────────┐                  ┌─────────────────┐
│ Docker Image  │                  │ SSH Deploy      │
│ build & push  │                  │ na serwer       │
└──────┬────────┘                  └────────┬────────┘
       │                                   │
       ▼                                   ▼
┌───────────────┐                  ┌─────────────────┐
│ Docker Hub    │                  │ Docker Container│
└───────────────┘                  │ Flask App       │
                                  └────────┬────────┘
                                           │
                                           ▼
                                  ┌─────────────────┐
                                  │ Nginx Reverse   │
                                  │ Proxy + HTTPS   │
                                  └────────┬────────┘
                                           │
                                           ▼
                                      ┌──────────┐
                                      │  User    │
                                      └──────────┘

Monitoring:

Flask (/metrics)
        ↓
Prometheus
        ↓
Grafana (dashboard)
```

---

# ⚙️ Technologie

* Python / Flask
* Docker
* Git / GitHub
* GitHub Actions (CI/CD)
* Docker Hub
* Nginx
* Let's Encrypt (SSL)
* Prometheus
* Grafana
* Linux Ubuntu Server

---

# 🚀 Funkcjonalność aplikacji

### `/`

Zwraca wersję aplikacji

```
DevOps Project Krzysztof Trojańczuk - version 5.0
```

---

### `/health`

```
OK
```

---

### `/version`

Zwraca wersję aplikacji

---

### `/metrics`

Metryki Prometheus:

* liczba requestów
* CPU procesu
* pamięć
* statystyki Pythona

---

# 🐳 Konteneryzacja

```
docker run -d -p 5000:5000 krzyniot/devops-project
```

---

# 🔄 CI/CD Pipeline

Plik:

```
.github/workflows/pipeline.yml
```

Pipeline:

1. checkout kodu
2. build obrazu Docker
3. push do Docker Hub
4. SSH deploy na serwer
5. restart kontenera

---

# ⚡ Automatyczny deploy – demonstracja

Proces działania:

1. Zmiana wersji:

```
VERSION = "5.0"
```

2. Commit i push:

```
git add .
git commit -m "release 5.0"
git push
```

3. GitHub Actions automatycznie:

* buduje obraz
* publikuje do Docker Hub
* wykonuje deploy

4. Aplikacja aktualizuje się automatycznie:

```
https://projektdyplomowy.ddns.net
```

---

# 🔐 Reverse Proxy i HTTPS

```
Nginx → Flask (port 5000)
```

Certyfikat:

```
Let's Encrypt (certbot)
```

---

# 📊 Monitoring

## Prometheus

Zbiera metryki z:

* aplikacji (`/metrics`)
* node-exporter (CPU, RAM)
* samego Prometheusa

---

## Grafana

Dashboard zawiera:

### CPU Usage (server)

* użycie CPU serwera

### RAM Usage (server)

* zużycie pamięci

### Request total

* liczba wszystkich requestów

### Traffic

* ruch w czasie (request/sec)

---

## 📈 Przykładowe zapytania

### CPU

```
100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[1m])) * 100)
```

### RAM

```
(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100
```

### Traffic

```
rate(app_requests_total[1m])
```

### Requests total

```
app_requests_total
```

---

# 🧩 Wnioski

Projekt pokazuje pełny proces DevOps:

* zarządzanie kodem (Git)
* automatyczny pipeline CI/CD
* konteneryzację (Docker)
* automatyczny deploy
* wystawienie aplikacji przez HTTPS
* monitoring aplikacji i serwera

---

# 👨‍💻 Autor

Krzysztof Trojańczuk
