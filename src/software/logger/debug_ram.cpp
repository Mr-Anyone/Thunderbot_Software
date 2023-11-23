#include <iostream> 
#include <g3log/g3log.hpp>
#include <g3log/logworker.hpp>
#include <string> 

int iter_count = 1e6; 

int main() {
    auto worker = g3::LogWorker::createLogWorker();
    auto handle= worker->addDefaultLogger(".log", "/home/vhe/Desktop/");
    g3::initializeLogging(worker.get());

    auto bytes = some_test_message.size() * sizeof(char) * static_cast<unsigned long> (iter_count);
    auto bytes_in_mb = static_cast<double> (bytes) / 1e6; 
    std::cout << bytes_in_mb << "MB" << std::endl; 



    for(int i = 0; i<iter_count; ++i){
        LOG(INFO) << some_test_message; 
    }

    std::cin.get(); 
    return 0; 
}
