#include <iostream>
#include "proto/tbots_software_msgs.pb.h"
#include "proto/robot_status_msg.pb.h"
#include "software/networking/udp/threaded_proto_udp_sender.hpp"
#include "software/networking/udp/threaded_proto_udp_listener.hpp"

std::string address = "ff02::c3d0:42d2:bb00%wlp0s20f3";
const short unsigned int ROBOT_STATUS_PORT = 42071;

void sendOneRobotStatusMessage(ThreadedProtoUdpSender<TbotsProto::RobotStatus>& sender){
    TbotsProto::RobotStatus robot_status; 
    robot_status.set_robot_id(0); 


    sender.sendProto(robot_status);

}

void receiverCallback(TbotsProto::PrimitiveSet message){
    std::cout << "I've got a message!" << std::endl;
}

int main(){
    std::cout << "I've started the program" << std::endl; 
    ThreadedProtoUdpSender<TbotsProto::RobotStatus> sender (address, ROBOT_STATUS_PORT, true);

    auto primitive_set_callback = [](TbotsProto::PrimitiveSet message) {
        std::cout << "I've got a message: " << message << std::endl; 
    };

    ThreadedProtoUdpListener<TbotsProto::PrimitiveSet> listener (address, 42070, primitive_set_callback, true);

    while(true){
        char input; 
        std::cout << "input (y to send proto): " << std::endl; 
        std::cin >> input; 

        if(input == 'y'){
            sendOneRobotStatusMessage(sender);
        }else if (input == 'n'){
            break;
        }
    }

    std::cout << "I've sent a robot status" << std::endl; 

    return 0;
}
