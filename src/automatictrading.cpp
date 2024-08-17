#include <iostream>
#include <string>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    std::string s;
    int q;

    std::cin >> s;
    
    std::cin >> q;
    
    for (int i = 0; i < q; i++) {
        int x, y;
        std::cin >> x >> y;
        int count = 0;

        while (s[x] == s[y]) {
            count++;
            x++;
            y++;
        }
        
        std::cout << count << "\n";
    }
    
    return 0;
}
