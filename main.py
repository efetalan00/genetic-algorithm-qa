from src.ga_engine import GeneticAlgorithm
from src.logger_config import logger
import cProfile
import pstats
import os


def run_simulation(pop_size, mut_rate, scenario_name):
    """Farklı parametrelerle simülasyonu çalıştıran yardımcı fonksiyon."""
    try:
        logger.info(f"--- {scenario_name}: Початок (Популяція={pop_size}) ---")
        ga = GeneticAlgorithm(pop_size=pop_size, mutation_rate=mut_rate)

        # Популяція (Popülasyonu oluştur)
        pop = ga.initialize_population(pop_size)

        # Мутація (Mutasyon testi)
        if pop:
            ga.mutate(pop[0])

        logger.info(f"--- {scenario_name}: Завершено ---")
    except Exception as e:
        print(f"\n[ПОВІДОМЛЕННЯ КОРИСТУВАЧА]: Помилка: {e}")


if __name__ == "__main__":
    # Rapor dosyasının klasörünü oluştur
    if not os.path.exists('docs'):
        os.makedirs('docs')

    # --- ПРОФІЛЮВАННЯ (PROFILLEME) ---
    profiler = cProfile.Profile()
    profiler.enable()

    # 1. Малий набір даних (Küçük veri seti)
    run_simulation(pop_size=5, mut_rate=0.1, scenario_name="Сценарій 1 (Малий)")

    # 2. Великий набір даних (Büyük veri seti - Lab bonus puanı için)
    run_simulation(pop_size=1000, mut_rate=0.05, scenario_name="Сценарій 2 (Великий)")

    profiler.disable()

    # --- РЕЗУЛЬТАТИ ТА ЗВІТНІСТЬ (SONUÇLAR VE RAPORLAMA) ---
    with open("docs/performance_results.txt", "w", encoding="utf-8") as f:
        stats = pstats.Stats(profiler, stream=f)
        stats.sort_stats(pstats.SortKey.TIME)

        # Konsola çıktı ver
        print("\n" + "=" * 60)
        print("      ЛАБОРАТОРНА РОБОТА 8: РЕЗУЛЬТАТИ ПРОФІЛЮВАННЯ")
        print("=" * 60)

        # Hem konsola hem dosyaya yazdır
        stats_console = pstats.Stats(profiler)
        stats_console.sort_stats(pstats.SortKey.TIME)
        stats_console.print_stats(15)  # İlk 15 fonksiyon

        # Dosyaya detaylı kaydet
        stats.print_stats()

    print(f"\n[OK]: Результати профілювання збережені в 'docs/performance_results.txt'")