# DevOps Project – Krzysztof Trojańczuk

## Opis projektu

Projekt przedstawia kompletny **pipeline DevOps CI/CD** dla aplikacji webowej napisanej w **Python Flask**.

System automatycznie:

* buduje obraz Dockera
* publikuje go w Docker Hub
* wdraża aplikację na serwerze po każdym `git push`

Dodatkowo projekt został rozszerzony o **monitoring (Prometheus + Grafana)**.

Aplikacja dostępna publicznie przez HTTPS:

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
Docker Hub
      ↓
SSH Deploy na serwer
      ↓
Docker Container (Flask)
      ↓
Nginx Reverse Proxy
      ↓
HTTPS (Let's Encrypt)
      ↓
User / Browser

Dodatkowo:

Flask (/metrics)
      ↓
Prometheus
      ↓
Grafana (dashboard)
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
* Prometheus
* Grafana
* Linux Ubuntu Server

---

# Funkcjonalność aplikacji

### Strona główna

```
/
```

Zwraca wersję aplikacji:

```
DevOps Project Krzysztof Trojańczuk - version 4.0
```

---

### Health check

```
/health
```

Odpowiedź:

```
OK
```

---

### Version

```
/version
```

---

### Metryki (Prometheus)

```
/metrics
```

Zawiera dane:

* liczba requestów
* metryki Pythona
* metryki procesu

---

# Konteneryzacja

```
docker run -d -p 5000:5000 krzyniot/devops-project
```

---

# CI/CD Pipeline

Plik:

```
.github/workflows/pipeline.yml
```

Pipeline:

1. checkout kodu
2. build Docker image
3. push do Docker Hub
4. SSH deploy
5. restart kontenera

---

# Automatyczny deploy

Po każdym:

```
git push
```

Wykonywane:

```
docker pull krzyniot/devops-project
docker stop devops
docker rm devops
docker run -d -p 5000:5000 --name devops --restart always krzyniot/devops-project
```

---

# Reverse Proxy i HTTPS

Nginx:

```
Nginx → Flask (port 5000)
```

SSL:

```
Let's Encrypt (certbot)
```

---

# Monitoring (Prometheus + Grafana)

## Prometheus

Zbiera metryki z:

* aplikacji Flask (`/metrics`)
* samego Prometheusa

Konfiguracja:

```yaml
scrape_configs:
  - job_name: 'devops-app'
    static_configs:
      - targets: ['devops:5000']
```

---

## Grafana

Dashboard zawiera:

###  CPU Usage (server)

* procentowe użycie CPU serwera

### RAM Usage (server)

* procent zajętej pamięci RAM

### Request total

* całkowita liczba requestów (od startu aplikacji)

### Traffic

* liczba requestów na sekundę (ruch w czasie)

---

## Przykładowe zapytania (PromQL)

### CPU usage

```
100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[1m])) * 100)
```

---

### RAM usage

```
(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100
```

---

### Request rate (ruch)

```
rate(app_requests_total[1m])
```

---

### Total requests

```
app_requests_total
```

---

# Wnioski

Projekt pokazuje pełny proces DevOps:

* CI/CD pipeline
* konteneryzacja
* automatyczny deploy
* monitoring aplikacji i infrastruktury

Rozdzielone zostały:

* metryki aplikacji (requesty)
* metryki serwera (CPU, RAM)

---

# Możliwe rozszerzenia

* alerty (email / Telegram / Slack)
* monitoring kontenerów (cAdvisor)
* Kubernetes
* autoskalowanie
* logowanie (ELK stack)

---

# Autor

Krzysztof Trojańczuk
