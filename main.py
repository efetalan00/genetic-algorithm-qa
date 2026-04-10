from src.ga_engine import GeneticAlgorithm
from src.logger_config import logger


def run_simulation():
    try:
        # 1. Senaryo: Başarılı Çalışma
        logger.info("--- Senaryo 1: Normal Çalışma Başlıyor ---")
        ga = GeneticAlgorithm(pop_size=5, mutation_rate=0.1)

        # Popülasyonu başlat ve logları izle
        pop = ga.initialize_population(5)

        # Bir örnek üzerinde mutasyon dene
        sample = [0, 0, 0, 0, 0, 0, 0, 0]
        ga.mutate(sample)

        logger.info("--- Senaryo 1 Tamamlandı ---\n")

        # 2. Senaryo: Hata Durumu (Requirement %75)
        logger.info("--- Senaryo 2: Hata Testi Başlıyor ---")
        # Geçersiz mutasyon oranı veriyoruz (Hata fırlatmalı)
        bad_ga = GeneticAlgorithm(pop_size=5, mutation_rate=99.0)

    except Exception as e:
        # Hata yakalandığında kullanıcıya gösterilen dostane mesaj
        print(f"\n[KULLANICI MESAJI]: Üzgünüz, bir işlem hatası oluştu.")
        print(f"Lütfen destek ekibine şu hata kodunu iletin: {e}")


if __name__ == "__main__":
    run_simulation()