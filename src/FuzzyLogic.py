from typing import Tuple, Dict


class FuzzyLogic:
    def __init__(self):
        self.kepuasan_range = {
            'rendah': [0, 0, 30, 50],
            'sedang': [30, 50, 50, 70],
            'tinggi': [70, 85, 90, 100],
        }
        
        self.anggaran_range = {
            'kritis': [-500, -200, 0, -100],
            'cukup': [0, 200, 500, 800],
            'aman': [500, 800, 1000, 1500],
        }
        
        self.infrastruktur_range = {
            'kurang': [0, 0, 10, 20],
            'memadai': [10, 20, 30, 40],
            'maju': [30, 40, 50, 60],
        }
        
    def _calculate_membership(self, x: float, range_vals: Tuple) -> float:
        a, b, c, d = range_vals
        
        if x <= a or x >= d:
            return 0
        elif b <= x <= c:
            return 1
        elif a < x < b:
            return (x - a) / (b - a)
        else:
            return (d - x) / (d - c)
    
    def evaluate_performance(self, resources: Dict) -> Tuple[str, float]:
        kepuasan = resources["kepuasan_masyarakat"]
        anggaran = resources["anggaran"]
        infrastruktur = resources["infrastruktur"]
        
        k_rendah = self._calculate_membership(kepuasan, self.kepuasan_range["rendah"])
        k_sedang = self._calculate_membership(kepuasan, self.kepuasan_range["sedang"])
        k_tinggi = self._calculate_membership(kepuasan, self.kepuasan_range["tinggi"])
        
        a_kritis = self._calculate_membership(anggaran, self.anggaran_range["kritis"])
        a_cukup = self._calculate_membership(anggaran, self.anggaran_range["cukup"])
        a_aman = self._calculate_membership(anggaran, self.anggaran_range["aman"])
        
        i_kurang = self._calculate_membership(infrastruktur, self.infrastruktur_range["kurang"])
        i_memadai = self._calculate_membership(infrastruktur, self.infrastruktur_range["memadai"])
        i_maju = self._calculate_membership(infrastruktur, self.infrastruktur_range["maju"])
        
        score = (k_tinggi * 0.4 + a_aman * 0.3 + i_maju * 0.3) * 100
        
        if score >= 80:
            return "Sangat Baik", score
        elif score >= 60:
            return "Baik", score
        elif score >= 40:
            return "Cukup", score
        else:
            return "Buruk", score
