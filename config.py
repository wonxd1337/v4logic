# config.py - OPTIMIZED NETWORK & THREADS
import os
import tempfile

class Config:
    # Thread settings (Ditingkatkan untuk throughput maksimal)
    MAX_THREADS_REVERSE = 40  
    MAX_THREADS_SCAN = 120     
    
    # Proxy settings
    PREFER_SOCKS5 = True
    SOCKS5_PRIORITY = 0.7
    PROXY_REFRESH_INTERVAL = 1800  # 30 menit
    PROXY_URL = "https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/all/data.txt"
    
    # RNG settings
    MAX_VALID_RNG = 50
    MAX_VALID_RNG_LIMIT = 200
    
    # Cache settings
    MAX_CACHE_SIZE = 10000
    CACHE_CLEANUP_INTERVAL = 3600
    
    # Memory management
    TEMP_DIR = os.path.expanduser("~/.mt_scanner_cache/")
    MAX_MEMORY_ITEMS = 5000
    
    # File output
    OUTPUT_FILES = {
        'movable_type': 'mv.txt',
        'movable_type_v4': 'mv4.txt',
        'processed_ips': 'processed_ips.txt',
        'cache': 'cache.db'
    }
    
    # Retry settings (Fail-fast: lebih cepat berpindah jika gagal)
    MAX_RETRIES = 2
    RETRY_DELAY = 1
    
    # Timeout settings (Diperketat untuk menghindari thread tergantung lama)
    TIMEOUT_REVERSE = 12
    TIMEOUT_SCAN = 5
    
    # LEVEL 2 SMART SCAN SETTINGS
    SAMPLE_SIZE = 10
    MIN_DOMAINS_PER_IP = 20
    MIN_GOOD_SAMPLES = 1
    
    @staticmethod
    def ensure_temp_dir():
        if not os.path.exists(Config.TEMP_DIR):
            os.makedirs(Config.TEMP_DIR)
