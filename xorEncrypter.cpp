#include <iostream>
#include <string>

std::string xor_encrypt_decrypt(const std::string& input, char key) {
    std::string output = input;
    for (size_t i = 0; i < input.length(); i++) {
        output[i] = input[i] ^ key;
    }
    return output;
}

int main() {
    std::string plaintext = "Hello, Cybersecurity!";
    char key = 'K';

    std::cout << "Original Text: " << plaintext << std::endl;
    
    std::string encrypted = xor_encrypt_decrypt(plaintext, key);
    std::cout << "Encrypted Text: " << encrypted << std::endl;

    std::string decrypted = xor_encrypt_decrypt(encrypted, key);
    std::cout << "Decrypted Text: " << decrypted << std::endl;

    return 0;
}
