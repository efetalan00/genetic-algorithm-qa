import uuid

class GeneticAlgorithmError(Exception):
    """Genetik Algoritma simülatörüne özel hata sınıfı"""
    def __init__(self, message, context=None):
        # %75 GEREKSİNİMİ: Benzersiz Hata ID'si ve Bağlamsal Bilgi (Context)
        self.error_id = str(uuid.uuid4())[:8].upper()
        self.context = context
        self.message = message
        # Hata mesajına otomatik olarak ID ekler
        super().__init__(f"[{self.error_id}] {self.message}")

    def get_log_details(self):
        """Log dosyasına yazılacak detaylı hata bilgisi"""
        return f"ERROR_ID: {self.error_id} | Message: {self.message} | Context: {self.context}"