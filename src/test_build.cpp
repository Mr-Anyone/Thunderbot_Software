#include <iostream> 
#include <fstream> 


int main(){
    std::cout << "Hello World" << std::endl; 

    // Create an ofstream object to handle file output
    std::ofstream outFile("/tmp/example.txt");

    // Check if the file was created/opened successfully
    if (!outFile) {
        std::cerr << "Error opening file for writing." << std::endl;
        return 1;
    }

    // Write data to the file
    outFile << "Hello, world!" << std::endl;
    outFile << "This is a line of text." << std::endl;
    outFile << "This is another line of text." << std::endl;

    // Close the file
    outFile.close();

    std::cout << "I've finished running!" << std::endl; 
    return 0;
}