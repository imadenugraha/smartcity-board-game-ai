import random

from typing import List, Tuple, Dict
from src.AILearning import AILearning
from src.FuzzyLogic import FuzzyLogic


class SmartCityGame:
    def __init__(self):
        self.board_size = 30
        self.player_position = 0
        self.resources = {
            "anggaran": 1000,
            "kepuasan_masyarakat": 50,
            "infrastruktur": 0,
        }
        self.turn = 1
        
        self.ai_learning = AILearning()
        self.fuzzy_logic = FuzzyLogic()
        
        self.services = [
            {
                "nama": "Membangun Universitas Internasional",
                "biaya": 100,
                "kepuasan": 30,
                "infrastruktur": 10,
            },
            {
                "nama": "Digitalisasi Pelayanan Publik",
                "biaya": 50,
                "kepuasan": 20,
                "infrastruktur": 5,
            },
            {
                "nama": "Membangun Rumah Sakit Umum",
                "biaya": 80,
                "kepuasan": 25,
                "infrastruktur": 10,
            },
            {
                "nama": "Membangun Jalan Tol",
                "biaya": 150,
                "kepuasan": 40,
                "infrastruktur": 20,
            },
            {
                "nama": "Membangun Infrastruktur Kereta Api",
                "biaya": 200,
                "kepuasan": 50,
                "infrastruktur": 30,
            }
        ]
        
        self.events = [
            {
                "nama": "Bencana Banjir",
                "efek": {
                    "anggaran": -10,
                    "kepuasan_masyarakat": -5,
                }
            },
            {
                "nama": "Serangan Hacker",
                "efek": {
                    "anggaran": -20,
                    "kepuasan_masyarakat": -10,
                    "infrastruktur": -5,
                }
            },
            {
                "nama": "Pandemi",
                "efek": {
                    "anggaran": -30,
                    "kepuasan_masyarakat": -15,
                }
            },
            {
                "nama": "Korupsi",
                "efek": {
                    "anggaran": -40,
                    "kepuasan_masyarakat": -30,
                    "infrastruktur": -30,
                }
            },
            {
                "nama": "Feedback Positif",
                "efek": {
                    "anggaran": 10,
                    "kepuasan_masyarakat": 5,
                }
            },
            {
                "nama": "Inovasi Teknologi",
                "efek": {
                    "anggaran": 200,
                    "kepuasan_masyarakat": 10,
                }
            }
        ]

        self.board = self._initialize_board()
        
    def _initialize_board(self) -> List[Dict]:
        board = [None] * self.board_size
        
        positions = random.sample(range(self.board_size), len(self.services) + len(self.events))
        
        for i, service in enumerate(self.services):
            board[positions[i]] = {
                "type": "service",
                "data": service
            }
        
        for i, event in enumerate(self.events):
            board[positions[i]] = {
                "type": "event",
                "data": event
            }

        return board
    
    def roll_dice(self) -> int:
        return random.randint(1, 6)
    
    def can_afford_service(self, service: Dict) -> bool:
        return self.resources["anggaran"] >= service["biaya"]
    
    def implement_service(self, service: Dict = None) -> str:
        print("\nLayanan E-Government yang tersedia:")
        for idx, service in enumerate(self.services, 1):
            print(f"{idx}. {service['nama']}")
            print(f"   Biaya: {service['biaya']}")
            print(f"   Efek Kepuasan: +{service['kepuasan']}")
            print(f"   Efek Infrastruktur: +{service['infrastruktur']}\n")
        
        while True:
            try:
                choice = input("Pilih nomor layanan yang ingin diimplementasikan (0 untuk skip): ")
                if choice == "0":
                    return "Anda memilih untuk tidak mengimplementasikan layanan."
                
                choice = int(choice) - 1
                if 0 <= choice < len(self.services):
                    selected_service = self.services[choice]
                    if not self.can_afford_service(selected_service):
                        print(f"\nAnggaran tidak mencukupi! Dibutuhkan: {selected_service['biaya']}")
                        continue
                        
                    self.resources['anggaran'] -= selected_service['biaya']
                    self.resources['kepuasan_masyarakat'] += selected_service['kepuasan']
                    self.resources['infrastruktur'] += selected_service['infrastruktur']
                    
                    return f"Berhasil mengimplementasikan {selected_service['nama']}!"
                else:
                    print("\nPilihan tidak valid! Silakan pilih nomor yang tersedia.")
            except ValueError:
                print("\nMasukkan nomor yang valid!")
    
    def handle_event(self, event: Dict) -> str:
        message = f"Event: {event['nama']}\n"
        
        for resource, value in event['efek'].items():
            self.resources[resource] += value
            if value > 0:
                message += f"+{value} {resource}\n"
            else:
                message += f"{value} {resource}\n"
                
        return message

    def play_turn(self) -> Tuple[str, bool, float]:
        dice_roll = self.roll_dice()
        old_position = self.player_position
        self.player_position = min(self.player_position + dice_roll, self.board_size - 1)
        
        message = f"Anda maju {dice_roll} langkah.\n"
        
        current_tile = self.board[self.player_position]
        if current_tile:
            if current_tile['type'] == 'service':
                print("\nAnda mendarat di kotak layanan!")
                service_result = self.implement_service()
                message += service_result
            else:
                print("\nAnda mendarat di kotak event!")
                event_result = self.handle_event(current_tile['data'])
                message += event_result
        else:
            print("\nAnda mendarat di kotak kosong.")
            if input("\nApakah Anda ingin mencoba mengimplementasikan layanan? (y/n): ").lower() == 'y':
                service_result = self.implement_service()
                message += "\n" + service_result
        
        self.resources['kepuasan_masyarakat'] = max(0, min(100, self.resources['kepuasan_masyarakat']))
        
        status, score = self.fuzzy_logic.evaluate_performance(self.resources)
        message += f"\nStatus Kota: {status} (Score: {score:.1f})"
        
        self.ai_learning.update_difficulty(score)
        
        game_over = self.player_position >= self.board_size - 1 or self.resources['anggaran'] < 0
        self.turn += 1
        
        return message, game_over, score
