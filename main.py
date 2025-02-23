import numpy as np

from src.SmartCityGame import SmartCityGame


def main():
    print("=== Selamat Datang di Smart City E-Government Game ===")
    print("\nAnda adalah kepala dinas Smart City yang bertugas mengembangkan")
    print("layanan e-government untuk meningkatkan pelayanan publik.")
    print("\nFitur Baru:")
    print("- Sistem evaluasi berbasis Fuzzy Logic")
    print("- AI yang beradaptasi dengan gaya bermain Anda")
    print("\nTujuan:")
    print("1. Kembangkan layanan e-government")
    print("2. Tingkatkan kepuasan masyarakat")
    print("3. Bangun infrastruktur digital")
    print("4. Kelola anggaran dengan bijak")
    
    game = SmartCityGame()
    
    while True:
        print(f"\n=== Turn {game.turn} ===")
        print("\nStatus Kota:")
        print(f"Anggaran: {game.resources['anggaran']}")
        print(f"Kepuasan Masyarakat: {game.resources['kepuasan_masyarakat']}%")
        print(f"Level Infrastruktur: {game.resources['infrastruktur']}")
        print(f"Tingkat Kesulitan AI: {game.ai_learning.difficulty:.2f}")
        
        input("\nTekan Enter untuk melempar dadu...")
        
        message, game_over, score = game.play_turn()
        print("\n" + message)
        
        if game_over:
            print("\n=== Game Over! ===")
            print(f"Anda bertahan selama {game.turn} turn")
            
            status, final_score = game.fuzzy_logic.evaluate_performance(game.resources)
            print(f"\nEvaluasi Akhir: {status}")
            print(f"Skor Akhir: {final_score:.1f}")
            
            print("\nHasil Akhir:")
            print(f"Anggaran Akhir: {game.resources['anggaran']}")
            print(f"Kepuasan Masyarakat: {game.resources['kepuasan_masyarakat']}%")
            print(f"Level Infrastruktur: {game.resources['infrastruktur']}")
            print(f"Rata-rata Performa: {np.mean(game.ai_learning.history):.1f}")
            break
        

if __name__ == "__main__":
    main()
