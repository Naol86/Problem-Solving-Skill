#include <iostream>


class SoftwareEngineer {
public:
    void Life(unsigned int age) {
        while (true) {
            std::cout << "Code until u die! ";
            age++;
			if (age > 80){
				std::cout << "Oops, I've coded enough. Time to take a break!";
				break;
			}
        }
    }
};

SoftwareEngineer::SoftwareEngineer(/* args */)
{
}

SoftwareEngineer::~SoftwareEngineer()
{
}

int main() {
    int codingYears = 0;

    while (true) {
        std::cout << "Code until u die! ";
        codingYears++;

        if (codingYears >= 80) {
            std::cout << "Oops, I've coded enough. Time to take a break!";
            break;
        }
    }

    return 0;
}
