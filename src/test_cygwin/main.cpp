#include <boost/asio.hpp>
#include <cstdlib>
#include <iostream>

const std::string UNIX_PATH = "/tmp/testing.sock";

int main()
{
    try
    {
        boost::asio::io_service io_service;

        // Create a UNIX domain datagram socket endpoint
        boost::asio::local::datagram_protocol::endpoint endpoint(UNIX_PATH);

        // Create a UNIX domain datagram socket
        boost::asio::local::datagram_protocol::socket socket(io_service);
        socket.open(boost::asio::local::datagram_protocol());

        std::string send_data = "hello from the c++ world";
        socket.send_to(boost::asio::buffer(send_data, send_data.size()), endpoint);
        std::cout << "I've sent the full data" << std::endl;
    }
    catch (std::exception const& e)
    {
        std::cerr << "Exception: " << e.what() << std::endl;
        return -1;
    }
}
