# 📘 Component Name - Team X

## 🎯 Goal

Describe the purpose of this component in the observability stack.

---

## 📦 Helm Chart Used

```bash
helm repo add <repo-name> <repo-url>
helm install <release-name> <repo-name>/<chart-name> -f values.yaml
```

- **Helm Chart**: `<chart-name>`
- **Chart Version**: `<version>`
- **Deployed Namespace**: `<namespace>`

---

## ⚙️ Configuration Summary

| Setting                  | Value                                  |
|---------------------------|----------------------------------------|
| Resources                 | `<cpu and memory limits>`             |
| Endpoints exposed         | `<list of ports and APIs>`             |
| Important values changed  | `<key values changed in values.yaml>` |
| Dummy data setup (if any) | `<dummy data generators used>`        |

---

## 🧪 Testing Instructions

### Port Forward to Test Locally

```bash
kubectl port-forward svc/<service-name> <local-port>:<service-port>
```

Example:

```bash
kubectl port-forward svc/loki 3100:3100
```

### Basic Health Check

```bash
curl localhost:<local-port>/<health-endpoint>
```

Example:

```bash
curl localhost:3100/ready
```

### Example Query or Output

```bash
# Prometheus example
up{job="your-job-name"}

# Loki example
{job="your-job-name"} |= "some log message"

# Tempo example
service.name="your-service-name"
```

---

## 🔗 Dependencies

- **Input from**: `<source>`
- **Output to**: `<destination>`

---

## 🧹 Cleanup Commands

```bash
helm uninstall <release-name>
kubectl delete namespace <namespace> # Only if used exclusively
```

---

## 🚧 Problems You
