#include <iostream>
#include <string>
#include <ctime>
#include <cmath> 

using namespace std;

bool brute_force_crack(const string& target, const string& guess) {
    return target == guess;
}

void brute_force(const string& target, int max_len) {
    const string charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    string guess(max_len, ' ');

    size_t charset_size = charset.size();
    size_t max_attempts = pow(charset_size, max_len);

    for (size_t attempt = 0; attempt < max_attempts; ++attempt) {
        size_t temp = attempt;
        for (int i = max_len - 1; i >= 0; --i) {
            guess[i] = charset[temp % charset_size];
            temp /= charset_size;
        }

        if (brute_force_crack(target, guess)) {
            cout << "Password found: " << guess << endl;
            return;
        }
    }

    cout << "Password not found." << endl;
}

int main() {
    string target = "abs123";
    int max_len = target.length();

    cout << "Starting brute force for password: " << target << endl;
    clock_t start_time = clock();

    brute_force(target, max_len);

    clock_t end_time = clock();
    double time_taken = double(end_time - start_time) / CLOCKS_PER_SEC;
    cout << "Time taken: " << time_taken << " seconds" << endl;

    return 0;
}
