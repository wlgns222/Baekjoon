#include <iostream>
#include <string>

int main(int argc, const char * argv[]) {
    int num, count = 0;
    std::cin >> num;

    for (int i = 0; i < num; i++) {
        std::string str;
        std::cin >> str;

        bool seen[26] = {false};  // 알파벳 26개의 방문 여부를 기록하는 배열
        bool isGroupWord = true;

        for (size_t j = 0; j < str.length(); j++) {
            if (j > 0 && str[j] != str[j - 1] && seen[str[j] - 'a']) {
                isGroupWord = false;
                break;
            }
            seen[str[j] - 'a'] = true;
        }

        if (isGroupWord) {
            count++;
        }
    }

    std::cout << count;
}