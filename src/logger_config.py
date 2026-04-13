import logging
import os

# %65 GEREKSİNİMİ: Uygulamayı değiştirmeden seviye kontrolü
# Varsayılan INFO. Terminalde 'set GA_LOG_LEVEL=DEBUG' yapılarak değiştirilebilir.
LOG_LEVEL = os.getenv("GA_LOG_LEVEL", "INFO").upper()

def setup_app_logger():
    logger = logging.getLogger("GeneticSimulator")
    logger.setLevel(LOG_LEVEL)

    # %60 GEREKSİNİMİ: Temel format (Zaman - Seviye - Modül - Mesaj)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - [%(name)s] - %(message)s')

    # Konsol Handler: Terminale yazdırır
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # %85 GEREKSİNİMİ: Dosya Handler (Log rotasyonu veya basit kayıt için)
    # Proje klasöründe 'simulation.log' dosyası oluşturur.
    file_handler = logging.FileHandler('simulation.log', encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

# Global kullanım için nesne
logger = setup_app_logger()