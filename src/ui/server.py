import socketserver
from http.server import SimpleHTTPRequestHandler

from PyQt6.QtCore import QThread

PORT = 8000

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True  # evita "Address already in use"


class ServerThread(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.httpd = None

    def run(self):
        """
        Avvia il server HTTP in un thread separato.
        """
        handler = SimpleHTTPRequestHandler

        try:
            self.httpd = ReusableTCPServer(("", PORT), handler)
            print(f"[ServerThread] Server avviato su http://localhost:{PORT}")
            self.httpd.serve_forever()
        except Exception as e:
            print(f"[ServerThread] Errore nel server: {e}")

    def stop(self):
        """
        Arresta elegantemente il server.
        """
        if self.httpd:
            print("[ServerThread] Arresto del server...")
            self.httpd.shutdown()
            self.httpd.server_close()
            self.httpd = None

        self.quit()
        self.wait()
        print("[ServerThread] Server fermato.")
