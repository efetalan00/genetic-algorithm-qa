# Genetic Algorithm Simulator (QA Project)

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

Цей проєкт є програмним симулятором генетичного алгоритму, розробленим з акцентом на автоматизацію та якість коду. Проєкт демонструє роботу еволюційних процесів та інтеграцію сучасних інструментів розробки (CI/CD).

---

## 📊 Візуалізація архітектури (Architecture Diagrams)

### 1. Логіка генетичного алгоритму (Activity Diagram)
Ця діаграма відображає основний цикл роботи алгоритму: від ініціалізації популяції до знаходження оптимального рішення.

```mermaid
graph TD
    A[Початок] --> B{Ініціалізація}
    B --> C[Оцінка фітнесу осіб]
    C --> D{Умова зупинки?}
    D -- Ні --> E[Селекція батьків]
    E --> F[Кросовер / Схрещування]
    F --> G[Мутація генів]
    G --> C
    D -- Так --> H[Вивід найкращого рішення]
    H --> I([Кінець])
