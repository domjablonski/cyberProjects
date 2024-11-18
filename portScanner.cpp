#include <iostream>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

void scan_port(const char* ip, int port) {
    int sock;
    struct sockaddr_in sa;

    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == -1) {
        std::cerr << "Socket creation failed." << std::endl;
        return;
    }

    sa.sin_family = AF_INET;
    sa.sin_addr.s_addr = inet_addr(ip);
    sa.sin_port = htons(port);

    int result = connect(sock, (struct sockaddr*)&sa, sizeof(sa));
    if (result == 0) {
        std::cout << "Port " << port << " is open." << std::endl;
    } else {
        std::cout << "Port " << port << " is closed." << std::endl;
    }

    close(sock);
}

int main() {
    const char* ip = "127.0.0.1"; // Replace with the IP you want to scan
    for (int port = 1; port <= 1024; ++port) {
        scan_port(ip, port);
    }
    return 0;
}
