#include <iostream> 
#include <string> 
#include <thread>

#include "logger.h"

const std::string SAVING_DIRECTORY {"/home/vhe/Desktop/log"} ;
const std::string CSV_DIR {"/home/vhe/Desktop/placeholder.csv"} ;


#define USE_CSV 

const std::vector<LEVELS> filtered_level_filter = {DEBUG, VISUALIZE,    CSV,
                                             INFO,  ROBOT_STATUS, PLOTJUGGLER};
const std::vector<LEVELS> text_level_filter = {VISUALIZE, CSV, ROBOT_STATUS, PLOTJUGGLER};
const std::string filter_suffix       = "_filtered";
const std::string text_suffix         = "_text";
const std::string log_name            = "thunderbots";

int main(){
    LoggerSingleton::initializeLogger(SAVING_DIRECTORY);

    // creating test data 
    std::string data = "*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*";
    std::cout << "Test data has size: " << data.size() * sizeof(char) << std::endl; 
     

    const int log_count = 1e6;
    for(int i = 0; i<log_count; ++i){
        LOG(INFO) << data;
    }

    std::cin.get();
    return 0; 
}
