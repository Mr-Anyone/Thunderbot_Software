#include <iostream> 
#include <g3log/g3log.hpp>
#include <g3log/logworker.hpp>

#include "logger.h"

static const std::string message = "this is just some dummy message for logging.this is just some dummy message for logging.this is just some dummy message for logging.this is just some dummy message for logging.this is just some dummy message for logging.this is just some dummy message for logging.";
static const int ITER_COUNT = 500000; 

int main() {
    // using thunderbot's logging system 
    //LoggerSingleton::initializeLogger("/tmp/tbots");
    
    // using the most basic barebone logging system
    auto worker = g3::LogWorker::createLogWorker();
    worker->addDefaultLogger(".log", "/tmp");
    g3::initializeLogging(worker.get());


    auto total_message_size = sizeof(char) * message.length() * ITER_COUNT;
    auto write_mb_size = static_cast<double> (total_message_size) / 1e6;
    std::cout << "writing a total of: " << write_mb_size << " mb" <<  std::endl; 
    for(int i = 0; i<ITER_COUNT; ++i){
        LOG(DEBUG) << message;
    }

    std::cout << "I've finished writing. Check your ram usage using whatever you want." << std::endl; 
    std::cout << "Press enter to exit program.";
    // block 
    //std::cin.get();
    return 0; 
}
