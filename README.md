# Genetic Algorithm Simulator (QA Project)

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)

Цей проєкт є програмним симулятором генетичного алгоритму, розробленим у межах курсу з акцентом на автоматизацію та якість коду.

## 📊 Візуалізація архітектури (Architecture Diagrams)

### 1. Логіка алгоритму (Activity Diagram)
```mermaid
graph TD
    A[Початок] --> B{Ініціалізація}
    B --> C[Оцінка фітнесу]
    C --> D{Умова зупинки?}
    D -- Ні --> E[Селекція]
    E --> F[Кросовер]
    F --> G[Мутація]
    G --> C
    D -- Так --> H[Найкраще рішення]




