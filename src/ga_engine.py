import random
from .logger_config import logger
from .exceptions import GeneticAlgorithmError


class GeneticAlgorithm:
    def __init__(self, pop_size=10, mutation_rate=0.1):
        # Önemli olay: Simülatörün başlatılması loglanıyor
        logger.info(f"Genetik Motor başlatıldı. Parametreler: Popülasyon={pop_size}, Mutasyon={mutation_rate}")

        # %75 GEREKSİNİMİ: Hata yakalama ve benzersiz ID ile raporlama
        if not (0.0 <= mutation_rate <= 1.0):
            err_msg = f"Geçersiz mutasyon oranı: {mutation_rate}. Değer 0 ile 1 arasında olmalıdır."
            err = GeneticAlgorithmError(err_msg, {"input_value": mutation_rate})

            # Hatayı ERROR seviyesinde kaydet
            logger.error(err.get_log_details())
            raise err

        self.pop_size = pop_size
        self.mutation_rate = mutation_rate
        self.genome_length = 8
        self.population = self.initialize_population(pop_size)

    def initialize_population(self, size):
        # DEBUG seviyesi: Sadece derinlemesine analizde görünür
        logger.debug(f"{size} boyutunda yeni popülasyon oluşturuluyor...")
        return [[random.randint(0, 1) for _ in range(8)] for _ in range(size)]

    def mutate(self, individual):
        try:
            # Kritik operasyon takibi
            original = individual.copy()
            mutated_ind = [1 - g if random.random() < self.mutation_rate else g for g in individual]

            if mutated_ind != original:
                logger.debug(f"Mutasyon gerçekleşti: {original} -> {mutated_ind}")

            return mutated_ind
        except Exception as e:
            # Kritik sistem hataları için
            logger.critical(f"Mutasyon sırasında sistem hatası! ID: {str(e)}", exc_info=True)
            raise

    def crossover(self, p1, p2):
        # İşlem kaydı
        logger.debug(f"Crossover yapılıyor: {p1} ve {p2}")
        point = random.randint(1, 7)
        return p1[:point] + p2[point:]
