
"""
Tugas 5 - Simulasi Node untuk Bully Algorithm

Infrastruktur jaringan (socket server/client) sudah disediakan.
Logika Bully Algorithm (bagian # TODO) harus kalian lengkapi sendiri.

Contoh menjalankan (5 terminal terpisah):
    python3 node.py --id 1 --port 5001 --peers 5002,5003,5004,5005
    python3 node.py --id 2 --port 5002 --peers 5001,5003,5004,5005
    ... dst untuk id 3, 4, 5
"""

import argparse
import socket
import threading
import time

ELECTION_TIMEOUT = 2.0  # detik menunggu balasan OK sebelum menyatakan diri leader


class Node:
    def __init__(self, node_id: int, port: int, peers: dict):
        self.node_id = node_id
        self.port = port
        # peers: dict {peer_id: peer_port} untuk semua node LAIN
        self.peers = peers
        self.leader_id = None
        self.lock = threading.Lock()
        self.ok_received = False

    # ---------- Infrastruktur jaringan (SUDAH LENGKAP, jangan diubah) ----------

    def start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("localhost", self.port))
        server.listen()
        print(f"[Node {self.node_id}] Listening di port {self.port}")
        while True:
            conn, _ = server.accept()
            threading.Thread(target=self.handle_connection, args=(conn,), daemon=True).start()

    def handle_connection(self, conn: socket.socket):
        with conn:
            data = conn.recv(1024).decode()
            if not data:
                return
            sender_id, msg_type = data.split(":")
            self.on_message(int(sender_id), msg_type)

    def send_message(self, target_port: int, msg_type: str) -> bool:
        """Kirim pesan ke node lain. Return False jika node target tidak merespons (dianggap mati)."""
        try:
            with socket.create_connection(("localhost", target_port), timeout=1.0) as s:
                s.sendall(f"{self.node_id}:{msg_type}".encode())
            return True
        except (ConnectionRefusedError, socket.timeout, OSError):
            return False

    # ---------- Logika Bully Algorithm (LENGKAPI BAGIAN INI) ----------

    def on_message(self, sender_id: int, msg_type: str):
        """Dipanggil setiap kali node ini menerima pesan dari node lain."""

        print(
            f"[Node {self.node_id}] Menerima pesan "
            f"'{msg_type}' dari node {sender_id}"
        )

        if msg_type == "ELECTION":
            if self.node_id > sender_id:
                # Balas OK kepada node yang ID-nya lebih rendah.
                sender_port = self.peers.get(sender_id)

                if sender_port is not None:
                    self.send_message(sender_port, "OK")

                # Mulai election sendiri.
                threading.Thread(
                    target=self.start_election,
                    daemon=True
                ).start()

        elif msg_type == "OK":
            # Tandai bahwa node dengan ID lebih tinggi masih aktif.
            if sender_id > self.node_id:
                self.ok_received = True

        elif msg_type == "COORDINATOR":
            with self.lock:
                self.leader_id = sender_id

            print(f"[Node {self.node_id}] " f"Leader saat ini: Node {sender_id}")

        elif msg_type == "PING":
            # Koneksi TCP yang berhasil menandakan node aktif.
            pass

    def start_election(self):
        """Dipanggil saat node mendeteksi leader tidak ada."""

        higher_peers = {
            pid: port
            for pid, port in self.peers.items()
            if pid > self.node_id
        }

        print(
            f"[Node {self.node_id}] Memulai election ke node "
            f"{list(higher_peers.keys())}"
        )

        self.ok_received = False

        # Kirim ELECTION ke semua peer dengan ID lebih tinggi.
        for peer_id, peer_port in higher_peers.items():
            success = self.send_message(peer_port, "ELECTION")

            if not success:
                print(
                    f"[Node {self.node_id}] "
                    f"Node {peer_id} tidak merespons."
                )

        # Tunggu balasan OK sampai timeout.
        start_time = time.time()

        while time.time() - start_time < ELECTION_TIMEOUT:
            if self.ok_received:
                print(f"[Node {self.node_id}] Menerima OK," "menunggu COORDINATOR.")
                return

            time.sleep(0.05)

        # Tidak ada peer dengan ID lebih tinggi yang merespons.
        if not self.ok_received:
            self.declare_leader()

    def declare_leader(self):
        """Node menyatakan dirinya leader dan memberi tahu semua node lain."""

        with self.lock:
            self.leader_id = self.node_id

        print(f"[Node {self.node_id}] " 
            "MENJADI LEADER! Broadcast COORDINATOR.")

        # Kirim COORDINATOR ke semua peer.
        for peer_id, peer_port in self.peers.items():
            success = self.send_message(
                peer_port, "COORDINATOR"
            )

            if success:
                print(
                    f"[Node {self.node_id}] "
                    f"COORDINATOR dikirim ke Node {peer_id}"
                )

    def monitor_leader(self):
        """Memantau leader dan memulai election jika leader mati."""

        while True:
            time.sleep(3)
            with self.lock:
                current_leader = self.leader_id
            # Jika leader belum diketahui atau node ini adalah leader,
            # tidak perlu melakukan pemeriksaan.
            if (
                current_leader is None
                or current_leader == self.node_id
            ):
                continue
            leader_port = self.peers.get(current_leader)
            if leader_port is None:
                continue
            # Periksa apakah leader masih bisa dihubungi.
            alive = self.send_message(leader_port, "PING")
            if not alive:
                print(
                    f"[Node {self.node_id}] "
                    f"Leader Node {current_leader} mati!"
                )
                with self.lock:
                    if self.leader_id == current_leader:
                        self.leader_id = None
                        leader_lost = True
                    else:
                        leader_lost = False

                if leader_lost:
                    self.start_election()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", type=int, required=True)
    parser.add_argument("--port", type=int, required=True)
    parser.add_argument("--peers", type=str, required=True,
                        help="daftar port peer dipisah koma, mis. 5002,5003,5004,5005")
    args = parser.parse_args()

    # Asumsi konvensi port: id N selalu di port 5000+N (lihat contoh perintah di README).
    peer_ports = [int(p) for p in args.peers.split(",")]
    peers = {port - 5000: port for port in peer_ports}

    node = Node(args.id, args.port, peers)

    threading.Thread(target=node.start_server, daemon=True).start()
    threading.Thread(target=node.monitor_leader, daemon=True).start()

    time.sleep(1)  # beri waktu semua node lain start dulu sebelum election awal
    node.start_election()

    while True:
        time.sleep(60)


if __name__ == "__main__":
    main()
