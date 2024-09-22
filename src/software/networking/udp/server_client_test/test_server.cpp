#include <iostream>
#include <string>
#include <thread>
#include "software/networking/udp/threaded_proto_udp_sender.hpp"
#include "proto/robot_log_msg.pb.h"

void sendMessage(ThreadedProtoUdpSender<TbotsProto::RobotLog>& sender, TbotsProto::RobotLog message, int count){
    for(int i = 0; i<count; ++i){
        sender.sendProto(message);
    }
}
int main(){
    std::cout << "Hello World" << std::endl; 
    
    std::string address = "ff02::c3d0:42d2:bb00"; 
    int port = 12345;
    bool multicast = true; 
    ThreadedProtoUdpSender<TbotsProto::RobotLog> sender (address, port, multicast);
    
    while(true){
        std::string message;
        int send_count = 0;

        std::cout << "What is the message you want to send (without space): "; 
        std::cin >> message; 
        std::cout << "number of times to send: "; 
        std::cin >> send_count;

        TbotsProto::RobotLog  some_log_message; 
        some_log_message.set_log_msg(message);

        sendMessage(sender, some_log_message, send_count);
        std::cout << "Sending message: " << message << " number of times: " << send_count << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1)); // Sleep for 1 second
    }

    return 0;
}